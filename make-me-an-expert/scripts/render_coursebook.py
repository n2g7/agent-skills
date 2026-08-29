#!/usr/bin/env python3
"""Render a Markdown coursebook to a printable PDF.

Converts Markdown to HTML, then to a paginated coursebook PDF (A4 or US Letter),
not a 16:9 slide deck. Intended for make-me-an-expert packs:

    python3 scripts/render_coursebook.py course/book.md -o output/expert-course.pdf

PDF engines (first available wins unless --engine is set):

  1. WeasyPrint, if the ``weasyprint`` Python package imports
  2. pandoc on PATH, plus a PDF engine (weasyprint CLI, wkhtmltopdf, prince,
     or a TeX engine such as xelatex / lualatex / pdflatex)

Markdown-to-HTML uses the ``markdown`` package when installed (tables, fenced
code, TOC). Otherwise a stdlib converter covers headings, lists, links, images,
fenced code, blockquotes, and pipe tables.

Does not fetch http(s) resources at render time. Local images relative to the
Markdown file are allowed.

Exit status is 0 on success and non-zero on failure.
"""

from __future__ import annotations

import argparse
import html
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Callable, Dict, List, Optional, Sequence, Tuple
from urllib.parse import urlparse


class RenderError(Exception):
    """Fatal render failure; message is printed to stderr."""


# ---------------------------------------------------------------------------
# Availability
# ---------------------------------------------------------------------------


def weasyprint_importable() -> bool:
    try:
        import weasyprint  # noqa: F401
    except Exception:
        return False
    return True


def import_weasyprint():
    try:
        import weasyprint
    except Exception as exc:
        raise RenderError("WeasyPrint is not usable: %s" % exc) from exc
    return weasyprint


def pandoc_path() -> Optional[str]:
    return shutil.which("pandoc")


# ---------------------------------------------------------------------------
# Frontmatter
# ---------------------------------------------------------------------------

_FRONTMATTER_RE = re.compile(r"\A---[ \t]*\r?\n(.*?)\r?\n(?:---|\.\.\.)[ \t]*\r?\n", re.DOTALL)


def split_frontmatter(text: str) -> Tuple[str, Dict[str, str]]:
    """Strip YAML-ish frontmatter. Returns (body, simple string metadata)."""
    match = _FRONTMATTER_RE.match(text)
    if not match:
        return text, {}
    meta: Dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip().lower()
        value = value.strip().strip("\"'")
        if key and not key.startswith("#"):
            meta[key] = value
    return text[match.end() :], meta


def first_heading(text: str) -> Optional[str]:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            return stripped.lstrip("#").strip()
    return None


# ---------------------------------------------------------------------------
# Slugs / TOC
# ---------------------------------------------------------------------------


def slugify(text: str) -> str:
    plain = re.sub(r"<[^>]+>", "", text)
    plain = html.unescape(plain).strip().lower()
    plain = re.sub(r"[^\w\s-]", "", plain, flags=re.UNICODE)
    plain = re.sub(r"[-\s]+", "-", plain).strip("-")
    return plain or "section"


def unique_slug(text: str, used: Dict[str, int]) -> str:
    base = slugify(text)
    count = used.get(base, 0)
    used[base] = count + 1
    if count == 0:
        return base
    return "%s-%s" % (base, count)


def toc_from_html(body_html: str, min_level: int = 2, max_level: int = 3) -> str:
    """Build a nested TOC from heading ids already present in HTML."""
    heading_re = re.compile(
        r"<h([1-6])(\s[^>]*)?>(.*?)</h[1-6]>",
        re.IGNORECASE | re.DOTALL,
    )
    id_re = re.compile(r'\bid=["\']([^"\']+)["\']', re.IGNORECASE)
    entries: List[Tuple[int, str, str]] = []
    for match in heading_re.finditer(body_html):
        level = int(match.group(1))
        if level < min_level or level > max_level:
            continue
        attrs = match.group(2) or ""
        inner = re.sub(r"<[^>]+>", "", match.group(3)).strip()
        if not inner:
            continue
        id_match = id_re.search(attrs)
        hid = id_match.group(1) if id_match else slugify(inner)
        entries.append((level, hid, inner))
    if not entries:
        return ""
    return _toc_list_html(entries)


def _toc_list_html(entries: Sequence[Tuple[int, str, str]]) -> str:
    min_level = min(e[0] for e in entries)
    parts: List[str] = ['<ul class="toc-list">']
    last_level: Optional[int] = None
    for level, hid, title in entries:
        level = level - min_level + 1
        link = '<a href="#%s">%s</a>' % (html.escape(hid, quote=True), title)
        if last_level is None:
            parts.append("<li>%s" % link)
        elif level > last_level:
            parts.append("<ul>" * (level - last_level))
            parts.append("<li>%s" % link)
        elif level == last_level:
            parts.append("</li><li>%s" % link)
        else:
            parts.append("</li>")
            parts.append("</ul></li>" * (last_level - level))
            parts.append("<li>%s" % link)
        last_level = level
    if last_level is not None:
        parts.append("</li>")
        parts.append("</ul></li>" * (last_level - 1))
        parts.append("</ul>")
    return "".join(parts)


def ensure_heading_ids(body_html: str) -> str:
    """Add id attributes to headings that lack them (for TOC links)."""
    used: Dict[str, int] = {}
    id_re = re.compile(r'\bid=["\']([^"\']+)["\']', re.IGNORECASE)

    def repl(match: re.Match) -> str:
        level, attrs, inner = match.group(1), match.group(2) or "", match.group(3)
        if id_re.search(attrs):
            existing = id_re.search(attrs)
            if existing:
                used[existing.group(1)] = used.get(existing.group(1), 0) + 1
            return match.group(0)
        plain = re.sub(r"<[^>]+>", "", inner).strip()
        hid = unique_slug(plain, used)
        return '<h%s%s id="%s">%s</h%s>' % (level, attrs, hid, inner, level)

    return re.sub(
        r"<h([1-6])(\s[^>]*)?>(.*?)</h[1-6]>",
        repl,
        body_html,
        flags=re.IGNORECASE | re.DOTALL,
    )


# ---------------------------------------------------------------------------
# Markdown -> HTML (markdown lib, then stdlib)
# ---------------------------------------------------------------------------


def markdown_library_html(text: str) -> Optional[Tuple[str, str]]:
    """Return (body_html, toc_html) or None if the markdown package is absent."""
    try:
        import markdown as mdlib
    except Exception:
        return None

    extensions = ["extra", "sane_lists", "toc", "smarty"]
    configs = {
        "toc": {
            "title": "",
            "permalink": False,
            "toc_depth": "2-3",
            "anchorlink": False,
        }
    }
    converter = mdlib.Markdown(
        extensions=extensions,
        extension_configs=configs,
        output_format="html5",
        tab_length=4,
    )
    body = converter.convert(text)
    toc = getattr(converter, "toc", "") or ""
    if toc and "<li>" not in toc:
        toc = ""
    return body, toc


_FENCE_RE = re.compile(r"^(`{3,}|~{3,})(.*)$")
_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
_HR_RE = re.compile(r"^(?:-{3,}|\*{3,}|_{3,})\s*$")
_UL_RE = re.compile(r"^(\s*)([-*+])\s+(.*)$")
_OL_RE = re.compile(r"^(\s*)(\d+)[.)]\s+(.*)$")
_BQ_RE = re.compile(r"^>\s?(.*)$")
_SETEXT_EQ_RE = re.compile(r"^=+\s*$")
_SETEXT_DASH_RE = re.compile(r"^-+\s*$")


def _looks_like_table_separator(line: str) -> bool:
    stripped = line.strip()
    if "|" not in stripped and not re.match(r"^\s*:?-+:?\s*$", stripped):
        return False
    cells = [c.strip() for c in stripped.strip("|").split("|")]
    if not cells:
        return False
    return all(re.match(r"^:?-{3,}:?$", c) for c in cells)


def markdown_to_html_stdlib(text: str) -> str:
    """Minimal CommonMark-ish converter using only the standard library."""
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    blocks: List[str] = []
    i = 0
    n = len(lines)
    used_slugs: Dict[str, int] = {}

    def flush_para(buf: List[str]) -> None:
        if not buf:
            return
        blocks.append("<p>%s</p>" % inline_format(" ".join(s.strip() for s in buf)))
        buf.clear()

    para: List[str] = []

    while i < n:
        line = lines[i]

        fence = _FENCE_RE.match(line)
        if fence:
            flush_para(para)
            marker, info = fence.group(1), fence.group(2).strip()
            lang = info.split()[0] if info else ""
            i += 1
            code_lines: List[str] = []
            while i < n and not lines[i].startswith(marker):
                code_lines.append(lines[i])
                i += 1
            if i < n:
                i += 1
            cls = ' class="language-%s"' % html.escape(lang, quote=True) if lang else ""
            blocks.append(
                "<pre><code%s>%s</code></pre>"
                % (cls, html.escape("\n".join(code_lines), quote=False))
            )
            continue

        if not line.strip():
            flush_para(para)
            i += 1
            continue

        heading = _HEADING_RE.match(line)
        if heading:
            flush_para(para)
            level = len(heading.group(1))
            title = heading.group(2).strip()
            hid = unique_slug(title, used_slugs)
            blocks.append(
                '<h%d id="%s">%s</h%d>' % (level, hid, inline_format(title), level)
            )
            i += 1
            continue

        if i + 1 < n and para == []:
            nxt = lines[i + 1]
            if line.strip() and _SETEXT_EQ_RE.match(nxt):
                hid = unique_slug(line.strip(), used_slugs)
                blocks.append('<h1 id="%s">%s</h1>' % (hid, inline_format(line.strip())))
                i += 2
                continue
            if line.strip() and _SETEXT_DASH_RE.match(nxt) and "|" not in nxt:
                hid = unique_slug(line.strip(), used_slugs)
                blocks.append('<h2 id="%s">%s</h2>' % (hid, inline_format(line.strip())))
                i += 2
                continue

        if _HR_RE.match(line.strip()) and not _UL_RE.match(line):
            flush_para(para)
            blocks.append("<hr>")
            i += 1
            continue

        if _BQ_RE.match(line):
            flush_para(para)
            quoted: List[str] = []
            while i < n and _BQ_RE.match(lines[i]):
                quoted.append(_BQ_RE.match(lines[i]).group(1))
                i += 1
            inner = markdown_to_html_stdlib("\n".join(quoted))
            blocks.append("<blockquote>%s</blockquote>" % inner)
            continue

        if _UL_RE.match(line) or _OL_RE.match(line):
            flush_para(para)
            list_html, i = _parse_list(lines, i, inline_format)
            blocks.append(list_html)
            continue

        if "|" in line and i + 1 < n and _looks_like_table_separator(lines[i + 1]):
            flush_para(para)
            table_html, i = _parse_table(lines, i, inline_format)
            blocks.append(table_html)
            continue

        para.append(line)
        i += 1

    flush_para(para)
    return "\n".join(blocks)


def _split_row(line: str) -> List[str]:
    row = line.strip()
    if row.startswith("|"):
        row = row[1:]
    if row.endswith("|"):
        row = row[:-1]
    return [c.strip() for c in row.split("|")]


def _parse_table(
    lines: Sequence[str], start: int, inline: Callable[[str], str]
) -> Tuple[str, int]:
    header = _split_row(lines[start])
    i = start + 2
    body_rows: List[List[str]] = []
    while i < len(lines) and lines[i].strip() and "|" in lines[i]:
        body_rows.append(_split_row(lines[i]))
        i += 1
    out = ["<table>", "<thead>", "<tr>"]
    for cell in header:
        out.append("<th>%s</th>" % inline(cell))
    out.extend(["</tr>", "</thead>", "<tbody>"])
    for row in body_rows:
        out.append("<tr>")
        for idx in range(len(header)):
            cell = row[idx] if idx < len(row) else ""
            out.append("<td>%s</td>" % inline(cell))
        out.append("</tr>")
    out.extend(["</tbody>", "</table>"])
    return "".join(out), i


def _parse_list(
    lines: Sequence[str], start: int, inline: Callable[[str], str]
) -> Tuple[str, int]:
    first = lines[start]
    ordered = bool(_OL_RE.match(first))
    tag = "ol" if ordered else "ul"
    items: List[str] = []
    i = start
    n = len(lines)

    def match_item(line: str):
        return _OL_RE.match(line) if ordered else _UL_RE.match(line)

    while i < n:
        matched = match_item(lines[i])
        if not matched:
            break
        indent, content = len(matched.group(1)), matched.group(3)
        i += 1
        extra: List[str] = []
        while i < n:
            nxt = lines[i]
            if match_item(nxt):
                break
            if not nxt.strip():
                nxt_item = lines[i + 1] if i + 1 < n else ""
                if match_item(nxt_item) or nxt_item.startswith(" " * (indent + 2)):
                    i += 1
                    continue
                break
            if nxt.startswith(" " * (indent + 2)):
                extra.append(nxt[indent + 2 :])
                i += 1
                continue
            break
        extra_text = "\n".join(extra).strip()
        if extra_text:
            extra_html = markdown_to_html_stdlib(extra_text)
            items.append("<li><p>%s</p>%s</li>" % (inline(content), extra_html))
        else:
            items.append("<li>%s</li>" % inline(content))

    return "<%s>%s</%s>" % (tag, "".join(items), tag), i


_INLINE_CODE_RE = re.compile(r"`([^`]+)`")
_IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)(?:\s+\"([^\"]*)\")?\)")
_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)\s]+)(?:\s+\"([^\"]*)\")?\)")
_BOLD_RE = re.compile(r"(\*\*|__)(.+?)\1")
_ITALIC_RE = re.compile(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)|(?<!_)_(?!_)(.+?)(?<!_)_(?!_)")
_AUTOLINK_RE = re.compile(r"<(https?://[^>\s]+)>")


def inline_format(text: str) -> str:
    """Escape HTML and apply inline Markdown (code, images, links, emphasis)."""
    placeholders: List[str] = []

    def stash(fragment: str) -> str:
        placeholders.append(fragment)
        return "\x00PH%d\x00" % (len(placeholders) - 1)

    def code_sub(match: re.Match) -> str:
        return stash("<code>%s</code>" % html.escape(match.group(1), quote=False))

    work = _INLINE_CODE_RE.sub(code_sub, text)
    work = _AUTOLINK_RE.sub(
        lambda m: stash(
            '<a href="%s">%s</a>'
            % (html.escape(m.group(1), quote=True), html.escape(m.group(1), quote=False))
        ),
        work,
    )

    def image_sub(match: re.Match) -> str:
        alt, src = match.group(1), match.group(2)
        title = match.group(3)
        attrs = 'src="%s" alt="%s"' % (
            html.escape(src, quote=True),
            html.escape(alt, quote=True),
        )
        if title:
            attrs += ' title="%s"' % html.escape(title, quote=True)
        return stash("<img %s>" % attrs)

    work = _IMAGE_RE.sub(image_sub, work)

    def link_sub(match: re.Match) -> str:
        label, href = match.group(1), match.group(2)
        title = match.group(3)
        attrs = 'href="%s"' % html.escape(href, quote=True)
        if title:
            attrs += ' title="%s"' % html.escape(title, quote=True)
        return stash("<a %s>%s</a>" % (attrs, html.escape(label, quote=False)))

    work = _LINK_RE.sub(link_sub, work)
    work = html.escape(work, quote=False)
    work = _BOLD_RE.sub(r"<strong>\2</strong>", work)
    work = _ITALIC_RE.sub(lambda m: "<em>%s</em>" % (m.group(1) or m.group(2)), work)

    def unstash(match: re.Match) -> str:
        return placeholders[int(match.group(1))]

    return re.sub(r"\x00PH(\d+)\x00", unstash, work)


def convert_markdown(text: str) -> Tuple[str, str, str]:
    """Return (body_html, toc_html, converter_name)."""
    lib = markdown_library_html(text)
    if lib is not None:
        body, toc = lib
        body = ensure_heading_ids(body)
        if not toc:
            toc = toc_from_html(body)
        return body, toc, "markdown"
    body = markdown_to_html_stdlib(text)
    body = ensure_heading_ids(body)
    return body, toc_from_html(body), "stdlib"


# ---------------------------------------------------------------------------
# HTML document + print CSS
# ---------------------------------------------------------------------------


def print_css(paper: str) -> str:
    size = "A4" if paper == "a4" else "letter"
    return """
@page {
  size: %s;
  margin: 22mm 18mm 24mm 18mm;
  @top-center {
    content: string(chapter);
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    font-size: 8.5pt;
    color: #555;
  }
  @bottom-center {
    content: counter(page);
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    font-size: 9pt;
    color: #333;
  }
}
@page :first {
  @top-center { content: none; }
}
html { font-size: 11pt; }
body {
  font-family: Palatino, "Palatino Linotype", "Book Antiqua", Georgia, "Times New Roman", serif;
  line-height: 1.55;
  color: #1a1a1a;
  hyphens: auto;
}
h1, h2, h3, h4, h5, h6 {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-weight: 650;
  line-height: 1.25;
  color: #111;
  page-break-after: avoid;
}
h1 { font-size: 1.7rem; margin: 1.6em 0 0.55em; string-set: chapter content(); }
h2 { font-size: 1.28rem; margin: 1.35em 0 0.45em; }
h3 { font-size: 1.08rem; margin: 1.15em 0 0.4em; }
h4, h5, h6 { font-size: 1rem; margin: 1em 0 0.35em; }
p { margin: 0.65em 0; orphans: 3; widows: 3; }
a { color: #063a8a; text-decoration: none; }
a:hover { text-decoration: underline; }
ul, ol { margin: 0.5em 0 0.5em 1.3em; padding: 0; }
li { margin: 0.2em 0; }
li > p { margin: 0.25em 0; }
blockquote {
  margin: 1em 0;
  padding: 0.15em 0 0.15em 1em;
  border-left: 3px solid #888;
  color: #333;
}
pre, code {
  font-family: Menlo, Consolas, "Liberation Mono", "Courier New", monospace;
  font-size: 0.86em;
}
pre {
  background: #f4f4f4;
  border: 1px solid #ddd;
  padding: 0.75em 0.9em;
  overflow-x: auto;
  white-space: pre-wrap;
  word-wrap: break-word;
  page-break-inside: avoid;
}
code { background: #f4f4f4; padding: 0.05em 0.25em; }
pre code { background: transparent; padding: 0; }
table {
  border-collapse: collapse;
  width: 100%%;
  margin: 1em 0;
  font-size: 0.92em;
  page-break-inside: avoid;
}
th, td {
  border: 1px solid #bbb;
  padding: 0.35em 0.55em;
  text-align: left;
  vertical-align: top;
}
th { background: #eee; font-weight: 650; }
img { max-width: 100%%; height: auto; }
hr { border: 0; border-top: 1px solid #ccc; margin: 1.4em 0; }
nav.toc {
  page-break-after: always;
}
nav.toc > h1 {
  string-set: chapter "Contents";
  page-break-before: avoid;
  margin-top: 0;
}
nav.toc ul { list-style: none; margin-left: 0; padding-left: 0; }
nav.toc ul ul { padding-left: 1.1em; }
nav.toc li { margin: 0.28em 0; }
nav.toc a { color: #111; }
article.book > h1:first-child { margin-top: 0; }
""".strip() % size


def build_html_document(
    body_html: str,
    toc_html: str,
    title: str,
    paper: str,
    include_toc: bool,
) -> str:
    toc_block = ""
    if include_toc and toc_html:
        toc_inner = toc_html
        if "<ul" not in toc_inner:
            toc_inner = "<ul>%s</ul>" % toc_inner
        toc_block = (
            '<nav class="toc">\n<h1>Contents</h1>\n%s\n</nav>\n' % toc_inner
        )
    return (
        "<!DOCTYPE html>\n"
        '<html lang="en">\n'
        "<head>\n"
        '<meta charset="utf-8">\n'
        "<title>%s</title>\n"
        "<style>\n%s\n</style>\n"
        "</head>\n"
        "<body>\n"
        "%s"
        '<article class="book">\n%s\n</article>\n'
        "</body>\n"
        "</html>\n"
        % (
            html.escape(title, quote=False),
            print_css(paper),
            toc_block,
            body_html,
        )
    )


# ---------------------------------------------------------------------------
# PDF engines
# ---------------------------------------------------------------------------


def offline_url_fetcher(url: str, timeout: int = 10, ssl_context=None):
    """WeasyPrint fetcher that refuses http(s) and protocol-relative URLs."""
    raw = (url or "").strip()
    if raw.startswith("//"):
        raise OSError("Network URLs are disabled at render time: %s" % url)
    parsed = urlparse(raw)
    scheme = (parsed.scheme or "").lower()
    if scheme in ("http", "https", "ftp"):
        raise OSError("Network URLs are disabled at render time: %s" % url)
    weasyprint = import_weasyprint()
    fetcher = weasyprint.default_url_fetcher
    try:
        return fetcher(url, timeout=timeout, ssl_context=ssl_context)
    except TypeError:
        return fetcher(url)


def render_weasyprint(html_doc: str, output: Path, base_dir: Path) -> str:
    weasyprint = import_weasyprint()
    base_url = base_dir.resolve().as_uri()
    if not base_url.endswith("/"):
        base_url += "/"
    weasyprint.HTML(
        string=html_doc,
        base_url=base_url,
        url_fetcher=offline_url_fetcher,
    ).write_pdf(str(output))
    return "weasyprint"


_HTML_PDF_ENGINES = ("weasyprint", "wkhtmltopdf", "prince")
_TEX_PDF_ENGINES = ("xelatex", "lualatex", "pdflatex", "context")


def _run(cmd: Sequence[str], timeout: int = 180) -> Tuple[bool, str]:
    try:
        proc = subprocess.run(
            list(cmd),
            capture_output=True,
            text=True,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        return False, "command timed out after %ss: %s" % (timeout, " ".join(cmd))
    except OSError as exc:
        return False, str(exc)
    if proc.returncode == 0:
        return True, ""
    err = (proc.stderr or proc.stdout or "exit %s" % proc.returncode).strip()
    return False, err


def render_pandoc(
    html_doc: str,
    markdown_text: str,
    source: Path,
    output: Path,
    paper: str,
    css_text: str,
    include_toc: bool,
) -> str:
    exe = pandoc_path()
    if not exe:
        raise RenderError("pandoc is not on PATH")

    errors: List[str] = []
    resource = str(source.parent.resolve())

    with tempfile.TemporaryDirectory(prefix="coursebook-") as tmp:
        tmp_path = Path(tmp)
        html_file = tmp_path / "book.html"
        css_file = tmp_path / "print.css"
        md_file = tmp_path / "book.md"
        html_file.write_text(html_doc, encoding="utf-8")
        css_file.write_text(css_text, encoding="utf-8")
        md_file.write_text(markdown_text, encoding="utf-8")

        for engine in _HTML_PDF_ENGINES:
            if not shutil.which(engine):
                continue
            ok, err = _run(
                [
                    exe,
                    str(html_file),
                    "--from=html",
                    "-o",
                    str(output),
                    "--pdf-engine=%s" % engine,
                    "--css=%s" % css_file,
                    "--resource-path=%s" % resource,
                ]
            )
            if ok and output.is_file() and output.stat().st_size > 0:
                return "pandoc+%s" % engine
            errors.append("%s (html): %s" % (engine, err or "no output"))

        geometry = (
            "margin=1in,a4paper" if paper == "a4" else "margin=1in,letterpaper"
        )
        toc_args = ["--toc", "--toc-depth=3"] if include_toc else []
        for engine in _TEX_PDF_ENGINES:
            if not shutil.which(engine):
                continue
            ok, err = _run(
                [
                    exe,
                    str(md_file),
                    "--from=gfm",
                    "-o",
                    str(output),
                    "--standalone",
                    "--pdf-engine=%s" % engine,
                    "-V",
                    "geometry:%s" % geometry,
                    "-V",
                    "fontsize=11pt",
                    "--resource-path=%s" % resource,
                ]
                + toc_args
            )
            if ok and output.is_file() and output.stat().st_size > 0:
                return "pandoc+%s" % engine
            errors.append("%s (markdown): %s" % (engine, err or "no output"))

        ok, err = _run(
            [
                exe,
                str(html_file),
                "--from=html",
                "-o",
                str(output),
                "--css=%s" % css_file,
                "--resource-path=%s" % resource,
            ]
        )
        if ok and output.is_file() and output.stat().st_size > 0:
            return "pandoc"
        if err:
            errors.append("pandoc default: %s" % err)

    detail = "\n".join("  - %s" % e for e in errors) if errors else "  - no PDF engine found"
    raise RenderError(
        "pandoc is installed but could not produce a PDF.\n"
        "Tried html engines %s and TeX engines %s.\n"
        "Install WeasyPrint (`pip install weasyprint` plus Pango/Cairo) or a TeX\n"
        "distribution (xelatex/pdflatex), then retry.\n"
        "Details:\n%s"
        % (", ".join(_HTML_PDF_ENGINES), ", ".join(_TEX_PDF_ENGINES), detail)
    )


def neither_engine_message() -> str:
    return (
        "cannot render PDF: neither WeasyPrint nor pandoc is available.\n"
        "\n"
        "Install one of:\n"
        "  pip install weasyprint\n"
        "    (also needs Pango/Cairo; on macOS: brew install pango cairo)\n"
        "  pandoc  (https://pandoc.org) plus a PDF engine such as\n"
        "    weasyprint, wkhtmltopdf, or a TeX distribution (xelatex/pdflatex)\n"
        "\n"
        "Then retry:\n"
        "  python3 scripts/render_coursebook.py course/book.md "
        "-o output/expert-course.pdf"
    )


def render_pdf(
    html_doc: str,
    markdown_text: str,
    source: Path,
    output: Path,
    paper: str,
    engine: str,
    include_toc: bool,
) -> str:
    """Write PDF to output. Returns the engine label used."""
    output.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(suffix=".pdf", dir=str(output.parent))
    os.close(fd)
    tmp_path = Path(tmp_name)
    try:
        used = _render_to_path(
            html_doc,
            markdown_text,
            source,
            tmp_path,
            paper,
            engine,
            include_toc,
        )
        if not tmp_path.is_file() or tmp_path.stat().st_size == 0:
            raise RenderError("PDF engine produced an empty file (%s)" % used)
        os.replace(str(tmp_path), str(output))
        return used
    except Exception:
        try:
            tmp_path.unlink()
        except OSError:
            pass
        raise


def _render_to_path(
    html_doc: str,
    markdown_text: str,
    source: Path,
    dest: Path,
    paper: str,
    engine: str,
    include_toc: bool,
) -> str:
    if engine == "weasyprint":
        return render_weasyprint(html_doc, dest, source.parent)
    if engine == "pandoc":
        return render_pandoc(
            html_doc,
            markdown_text,
            source,
            dest,
            paper,
            print_css(paper),
            include_toc,
        )

    if weasyprint_importable():
        try:
            return render_weasyprint(html_doc, dest, source.parent)
        except RenderError:
            raise
        except Exception as exc:
            if not pandoc_path():
                raise RenderError("WeasyPrint failed: %s" % exc) from exc
            sys.stderr.write(
                "warning: WeasyPrint failed (%s); falling back to pandoc\n" % exc
            )

    if pandoc_path():
        return render_pandoc(
            html_doc,
            markdown_text,
            source,
            dest,
            paper,
            print_css(paper),
            include_toc,
        )

    raise RenderError(neither_engine_message())


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def read_markdown(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        raise RenderError("cannot read %s: %s" % (path, exc)) from exc


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="render_coursebook.py",
        description=(
            "Convert a Markdown coursebook to a printable PDF "
            "(paginated A4/Letter pages, not 16:9 slides)."
        ),
        epilog=(
            "Engines: WeasyPrint (Python package) first, then pandoc on PATH. "
            "Example: python3 scripts/render_coursebook.py course/book.md "
            "-o output/expert-course.pdf"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "input",
        help="Path to the Markdown coursebook (e.g. course/book.md)",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Output PDF path (default: <input-stem>.pdf next to the Markdown file)",
    )
    parser.add_argument(
        "--paper",
        choices=("a4", "letter"),
        default="a4",
        help="Page size for the coursebook (default: a4)",
    )
    parser.add_argument(
        "--engine",
        choices=("auto", "weasyprint", "pandoc"),
        default="auto",
        help="PDF engine (default: auto = WeasyPrint if importable, else pandoc)",
    )
    parser.add_argument(
        "--no-toc",
        action="store_true",
        help="Do not insert a generated table of contents",
    )
    return parser.parse_args(argv)


def run(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    source = Path(args.input).expanduser()
    if not source.is_file():
        raise RenderError("input Markdown not found: %s" % source)

    if args.output:
        output = Path(args.output).expanduser()
    else:
        output = source.with_suffix(".pdf")
    if output.suffix.lower() != ".pdf":
        output = output.with_suffix(output.suffix + ".pdf") if output.suffix else output.with_suffix(".pdf")

    raw = read_markdown(source)
    body_text, meta = split_frontmatter(raw)
    if not body_text.strip():
        raise RenderError("input Markdown is empty: %s" % source)

    title = meta.get("title") or first_heading(body_text) or source.stem.replace("-", " ")
    has_toc_marker = bool(re.search(r"(?m)^\[TOC\]\s*$", body_text))
    body_html, toc_html, _converter = convert_markdown(body_text)
    include_toc = not args.no_toc
    if has_toc_marker:
        toc_html = ""
    html_doc = build_html_document(
        body_html,
        toc_html,
        title,
        args.paper,
        include_toc,
    )

    used = render_pdf(
        html_doc,
        body_text,
        source,
        output.resolve(),
        args.paper,
        args.engine,
        include_toc,
    )
    written = output.resolve()
    sys.stdout.write("Wrote %s (engine: %s)\n" % (written, used))
    return 0


def main(argv: Optional[Sequence[str]] = None) -> int:
    try:
        return run(argv)
    except RenderError as exc:
        sys.stderr.write("error: %s\n" % exc)
        return 1
    except KeyboardInterrupt:
        sys.stderr.write("error: interrupted\n")
        return 130


if __name__ == "__main__":
    sys.exit(main())
