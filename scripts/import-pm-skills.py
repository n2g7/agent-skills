#!/usr/bin/env python3
"""Vendor phuryn/pm-skills into this library as on-demand skills.

Copies upstream skill folders and command workflows, stamps this repo's
frontmatter, and adds missing trigger sections. Upstream procedure text is
left in place. Refuses to overwrite an existing skill folder.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPSTREAM_URL = "https://github.com/phuryn/pm-skills.git"
UPSTREAM_WEB = "https://github.com/phuryn/pm-skills"
LICENSE_URL = "https://github.com/phuryn/pm-skills/blob/main/LICENSE"

SKILL_RENAMES = {
    "competitor-analysis": "pm-competitor-analysis",
    "marketing-ideas": "pm-marketing-ideas",
    "pricing-strategy": "pm-pricing-strategy",
}
COMMAND_RENAMES = {
    "pricing": "pm-pricing",
}
FOLD_COMMANDS = {
    "business-model",
    "draft-nda",
    "pre-mortem",
    "privacy-policy",
    "review-resume",
    "stakeholder-map",
    "test-scenarios",
    "value-proposition",
}
SAFE_RISK = {
    "code-review",
    "security-audit-static",
    "performance-audit-static",
    "ship-check",
}
TOKEN_RENAMES = (
    ("pricing-strategy", "pm-pricing-strategy"),
    ("competitor-analysis", "pm-competitor-analysis"),
    ("marketing-ideas", "pm-marketing-ideas"),
)
NEIGHBORS = {
    "pm-competitor-analysis": "Use `competitor-analysis` for Browserbase discovery, screenshots, and HTML reports.",
    "pm-marketing-ideas": "Use `marketing-ideas` for the 140-idea feasibility library.",
    "pm-pricing-strategy": "Use `pricing-strategy` or `pricing` for the other packaging workflows already in this library.",
    "pm-pricing": "Use `pricing` or `pricing-strategy` for the other packaging workflows already in this library.",
    "market-sizing": "Use `market-sizing-analysis` for the longer TAM/SAM/SOM methodology playbook.",
    "create-prd": "Use `to-prd` to turn the current conversation into an issue-tracker ticket.",
    "write-prd": "Use `to-prd` to turn the current conversation into an issue-tracker ticket.",
    "review-resume": "Use `resume-ats-review` to score an attached resume PDF without rewriting it.",
    "tailor-resume": "Use `resume-ats-review` to score an attached resume PDF without rewriting it.",
    "code-review": "Use `code-reviewer` for a general code review that is not tied to documented product intent.",
    "security-audit-static": "Use `security-audit` for a pentest-style security workflow. This skill is a static review of existing code and does not write exploits.",
    "monetization-strategy": "Use `monetization` for Stripe implementation, subscriptions, and billing mechanics.",
    "lean-canvas": "Use `osterwalder-canvas-architect` for an iterative 9-block Business Model Canvas.",
    "business-model": "Use `osterwalder-canvas-architect` for an iterative 9-block Business Model Canvas.",
    "plan-launch": "Use `launch-strategy` for SaaS launch announcements and momentum planning.",
    "brainstorm": "Use `brainstorming` to turn a vague idea into a validated design before implementation.",
    "ab-test-analysis": "Use `ab-test-setup` to design a test before analyzing results.",
}
LEGAL_IDS = {"draft-nda", "privacy-policy"}

WHEN_USE_RE = re.compile(
    r"(?im)^#{2,3}\s+(when to use(?: this skill)?|use this skill when)\s*$"
)
WHEN_NOT_RE = re.compile(r"(?im)^#{2,3}\s+when not to use\s*$")
LIMIT_RE = re.compile(r"(?im)^#{2,3}\s+limitations\s*$")
REF_RE = re.compile(r"references/[A-Za-z0-9_./-]+\.[A-Za-z0-9]+")
SECOND_PERSON_RE = re.compile(r"\b[Yy]ou (?:should|need to|can|must)\b")


def skill_local_id(name: str) -> str:
    return SKILL_RENAMES.get(name, name)


def command_local_id(name: str) -> str:
    if name in FOLD_COMMANDS:
        return skill_local_id(name)
    return COMMAND_RENAMES.get(name, name)


def split_frontmatter(text: str) -> tuple[dict[str, str], str]:
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n?", text, re.S)
    if not match:
        return {}, text
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line or line[0].isspace() or ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"').strip("'")
    return fields, text[match.end() :]


def clip_words(text: str, limit: int) -> str:
    if len(text) <= limit:
        cut = text
    else:
        cut = text[:limit]
        if " " in cut:
            cut = cut.rsplit(" ", 1)[0]
    cut = re.sub(r"(?i)(?:\s+(?:and|or|with|including|covering|for|to|the|a|an))+$", "", cut)
    return cut.rstrip(" ,;:-—–")


def fit_description(raw: str, skill_id: str) -> tuple[str, bool]:
    """Keep a description that already has a when-clause and fits in 200 chars."""
    text = raw.strip().strip('"').strip("'")
    has_when = bool(re.search(r"\bwhen\b", text, re.I))
    if text and len(text) <= 200 and has_when:
        return text, False
    phrase = skill_id.replace("-", " ")
    what = re.split(r"\s+[—–]\s+|\.\s+|\s+-\s+", text or phrase)[0].strip().rstrip(".")
    prefix = f'This skill should be used when the user asks to "{phrase}". '
    if 200 - len(prefix) < 24:
        phrase = " ".join(phrase.split()[:4])
        prefix = f'This skill should be used when the user asks to "{phrase}". '
    what = clip_words(what, 200 - len(prefix) - 1)
    description = f"{prefix}{what}."
    while len(description) > 200 and what:
        what = clip_words(what, len(what) - 1)
        description = f"{prefix}{what}."
    return description, True


def retarget(text: str, slash_map: dict[str, str]) -> str:
    text = text.replace("$ARGUMENTS", "the user's request")

    def plugin(match: re.Match[str]) -> str:
        name = match.group(1)
        return slash_map.get(name, name)

    text = re.sub(r"/pm-[a-z0-9-]+:([a-z0-9-]+)", plugin, text)

    def slash(match: re.Match[str]) -> str:
        name = match.group(1)
        if name in slash_map:
            return slash_map[name]
        return match.group(0)

    text = re.sub(r"(?<![\w/])/([a-z][a-z0-9-]*)\b", slash, text)
    for old, new in TOKEN_RENAMES:
        text = re.sub(rf"(?<![\w-]){re.escape(old)}(?![\w-])", new, text)
    return text


def when_not_lines(skill_id: str) -> list[str]:
    lines: list[str] = []
    if skill_id in LEGAL_IDS:
        lines.append(
            "Do not treat the draft as legal advice. Have a licensed attorney in the relevant jurisdiction review it before anyone signs or publishes it."
        )
    if skill_id in NEIGHBORS:
        lines.append(NEIGHBORS[skill_id])
    if skill_id not in LEGAL_IDS:
        lines.append(
            "Do not use this skill for implementation work, legal advice, or exploit development."
        )
    lines.append("Stop if the user's inputs are missing.")
    return lines


def insert_after_title(body: str, block: str) -> str:
    match = re.match(r"(\s*# [^\n]+\n+)", body)
    if match:
        return body[: match.end()] + block + body[match.end() :]
    return block + body


def ensure_sections(body: str, skill_id: str, description: str) -> tuple[str, list[str]]:
    added: list[str] = []
    blocks: list[str] = []
    if not WHEN_USE_RE.search(body):
        phrase = skill_id.replace("-", " ")
        blocks.append(
            f'## When to Use\n\nThis skill should be used when the user asks to "{phrase}".\n'
        )
        added.append("When to Use")
    if not WHEN_NOT_RE.search(body):
        bullets = "\n".join(f"- {line}" for line in when_not_lines(skill_id))
        blocks.append(f"## When NOT to Use\n\n{bullets}\n")
        added.append("When NOT to Use")
    if blocks:
        body = insert_after_title(body, "\n".join(blocks) + "\n")
    if not LIMIT_RE.search(body):
        body = body.rstrip() + (
            "\n\n## Limitations\n\n"
            "- This skill does not replace environment-specific validation, testing, or expert review.\n"
            "- Stop and ask for clarification if required inputs are missing.\n"
        )
        added.append("Limitations")
    if description and not description.strip():
        raise ValueError(skill_id)
    return body, added


def render_frontmatter(skill_id: str, description: str) -> str:
    risk = "safe" if skill_id in SAFE_RISK else "none"
    lines = [
        "---",
        "disable-model-invocation: true",
        f"name: {skill_id}",
        f"description: {json.dumps(description, ensure_ascii=False)}",
        f"risk: {risk}",
        "source: community",
        "source_repo: phuryn/pm-skills",
        "source_type: community",
        "license: MIT",
        f"license_source: {json.dumps(LICENSE_URL)}",
        'author: "Pawel Huryn"',
        'date_added: "2026-09-29"',
        'catalog_category: "Product Management"',
        "---",
        "",
    ]
    return "\n".join(lines)


def render_source(upstream_paths: list[str], skill_id: str, renamed_from: str | None) -> str:
    paths = ", ".join(f"`{path}`" for path in upstream_paths)
    lines = [
        "# Source",
        "",
        f"Imported from [phuryn/pm-skills]({UPSTREAM_WEB}) ({paths}).",
        "",
        "- Author: Pawel Huryn",
        "- License: MIT",
        f"- License file: {LICENSE_URL}",
        f"- Local id: `{skill_id}`",
    ]
    if renamed_from:
        lines.append(f"- Upstream id: `{renamed_from}` (renamed so it does not overwrite a different local skill)")
    if skill_id in NEIGHBORS:
        neighbor = NEIGHBORS[skill_id]
        lines.append(f"- Not a copy of the local neighbor named in this sentence: {neighbor}")
    lines.append("")
    return "\n".join(lines)


def discover(upstream: str) -> tuple[list[tuple[str, str, str]], list[tuple[str, str, str]]]:
    skills: list[tuple[str, str, str]] = []
    commands: list[tuple[str, str, str]] = []
    for plugin in sorted(os.listdir(upstream)):
        plugin_dir = os.path.join(upstream, plugin)
        if not plugin.startswith("pm-") or not os.path.isdir(plugin_dir):
            continue
        skill_root = os.path.join(plugin_dir, "skills")
        if os.path.isdir(skill_root):
            for name in sorted(os.listdir(skill_root)):
                skill_md = os.path.join(skill_root, name, "SKILL.md")
                if os.path.isfile(skill_md):
                    skills.append((plugin, name, os.path.join(skill_root, name)))
        command_root = os.path.join(plugin_dir, "commands")
        if os.path.isdir(command_root):
            for filename in sorted(os.listdir(command_root)):
                if filename.endswith(".md"):
                    name = filename[:-3]
                    commands.append((plugin, name, os.path.join(command_root, filename)))
    return skills, commands


def clone_upstream() -> str:
    dest = tempfile.mkdtemp(prefix="pm-skills-")
    subprocess.check_call(
        ["git", "clone", "--depth", "1", UPSTREAM_URL, dest],
        stdout=subprocess.DEVNULL,
    )
    return dest


def validate(skill_id: str, skill_dir: str, text: str, critical: list[str], suggestions: list[str]) -> None:
    fields, body = split_frontmatter(text)
    if fields.get("name") != skill_id:
        critical.append(f"{skill_id}: name {fields.get('name')!r} != folder")
    description = fields.get("description", "")
    if not description:
        critical.append(f"{skill_id}: missing description")
    elif not re.search(r"\bwhen\b", description, re.I):
        critical.append(f"{skill_id}: description has no when-clause")
    if not WHEN_USE_RE.search(body):
        critical.append(f"{skill_id}: missing When to Use")
    if not WHEN_NOT_RE.search(body):
        critical.append(f"{skill_id}: missing When NOT to Use")
    if "disable-model-invocation: true" not in text:
        critical.append(f"{skill_id}: missing disable-model-invocation")
    if "source_repo: phuryn/pm-skills" not in text:
        critical.append(f"{skill_id}: missing source_repo")
    for ref in sorted(set(REF_RE.findall(text))):
        if not os.path.isfile(os.path.join(skill_dir, ref)):
            critical.append(f"{skill_id}: missing referenced file {ref}")
    if "-" not in skill_id:
        suggestions.append(f"{skill_id}: single-word id kept")
    if SECOND_PERSON_RE.search(body):
        suggestions.append(f"{skill_id}: second-person upstream prose kept")
    line_count = text.count("\n") + 1
    if line_count > 500:
        suggestions.append(f"{skill_id}: {line_count} lines, not split")


def main() -> int:
    upstream = clone_upstream()
    try:
        skills, commands = discover(upstream)
        skill_by_name = {name: (plugin, path) for plugin, name, path in skills}
        missing_fold = sorted(name for name in FOLD_COMMANDS if name not in skill_by_name)
        if missing_fold:
            print("Fold targets missing:", ", ".join(missing_fold), file=sys.stderr)
            return 1

        slash_map: dict[str, str] = {}
        for _plugin, name, _path in skills:
            slash_map[name] = skill_local_id(name)
        for _plugin, name, _path in commands:
            slash_map[name] = command_local_id(name)

        planned: dict[str, str] = {}
        for _plugin, name, _path in skills:
            planned[skill_local_id(name)] = "skill"
        for _plugin, name, _path in commands:
            if name in FOLD_COMMANDS:
                continue
            local_id = command_local_id(name)
            if local_id in planned:
                print(f"Duplicate local id {local_id}", file=sys.stderr)
                return 1
            planned[local_id] = "command"

        blocked = [skill_id for skill_id in planned if os.path.exists(os.path.join(REPO_ROOT, skill_id))]
        if blocked:
            print("Refusing to overwrite:", ", ".join(sorted(blocked)), file=sys.stderr)
            return 1

        rewritten = 0
        sections_added: list[str] = []
        written: list[str] = []

        for plugin, name, src in skills:
            local_id = skill_local_id(name)
            dest = os.path.join(REPO_ROOT, local_id)
            shutil.copytree(src, dest)
            skill_md = os.path.join(src, "SKILL.md")
            fields, body = split_frontmatter(open(skill_md, encoding="utf-8").read())
            description, changed = fit_description(fields.get("description", ""), local_id)
            if changed:
                rewritten += 1
            body = retarget(body, slash_map)
            body, added = ensure_sections(body, local_id, description)
            if added:
                sections_added.append(f"{local_id}: {', '.join(added)}")
            workflows: list[str] = []
            upstream_paths = [f"{plugin}/skills/{name}"]
            for command_plugin, command_name, command_path in commands:
                if command_name in FOLD_COMMANDS and command_name == name:
                    _cfields, command_body = split_frontmatter(
                        open(command_path, encoding="utf-8").read()
                    )
                    command_body = retarget(command_body, slash_map).strip()
                    workflows.append(command_body)
                    upstream_paths.append(f"{command_plugin}/commands/{command_name}.md")
            if workflows:
                body = body.rstrip() + "\n\n## Workflow\n\n" + "\n\n".join(workflows) + "\n"
            renamed_from = name if name != local_id else None
            text = render_frontmatter(local_id, description) + body.lstrip("\n")
            if not text.endswith("\n"):
                text += "\n"
            with open(os.path.join(dest, "SKILL.md"), "w", encoding="utf-8") as handle:
                handle.write(text)
            with open(os.path.join(dest, "SOURCE.md"), "w", encoding="utf-8") as handle:
                handle.write(render_source(upstream_paths, local_id, renamed_from))
            written.append(local_id)

        for plugin, name, path in commands:
            if name in FOLD_COMMANDS:
                continue
            local_id = command_local_id(name)
            dest = os.path.join(REPO_ROOT, local_id)
            os.makedirs(dest)
            fields, body = split_frontmatter(open(path, encoding="utf-8").read())
            description, changed = fit_description(fields.get("description", ""), local_id)
            if changed:
                rewritten += 1
            body = retarget(body, slash_map)
            body, added = ensure_sections(body, local_id, description)
            if added:
                sections_added.append(f"{local_id}: {', '.join(added)}")
            renamed_from = name if name != local_id else None
            text = render_frontmatter(local_id, description) + body.lstrip("\n")
            if not text.endswith("\n"):
                text += "\n"
            with open(os.path.join(dest, "SKILL.md"), "w", encoding="utf-8") as handle:
                handle.write(text)
            with open(os.path.join(dest, "SOURCE.md"), "w", encoding="utf-8") as handle:
                handle.write(
                    render_source([f"{plugin}/commands/{name}.md"], local_id, renamed_from)
                )
            written.append(local_id)

        critical: list[str] = []
        suggestions: list[str] = []
        for skill_id in written:
            skill_dir = os.path.join(REPO_ROOT, skill_id)
            text = open(os.path.join(skill_dir, "SKILL.md"), encoding="utf-8").read()
            validate(skill_id, skill_dir, text, critical, suggestions)

        print(f"Wrote {len(written)} skills ({len(skills)} upstream skills, {len(commands) - len(FOLD_COMMANDS)} command skills, {len(FOLD_COMMANDS)} folded)")
        print(f"Descriptions rewritten: {rewritten}")
        print(f"Sections added on {len(sections_added)} skills")
        print(f"Suggestions ({len(suggestions)}):")
        for item in suggestions:
            print(f"  - {item}")
        if critical:
            print(f"Critical ({len(critical)}):", file=sys.stderr)
            for item in critical:
                print(f"  - {item}", file=sys.stderr)
            return 1
        print("Critical: 0")
        return 0
    finally:
        shutil.rmtree(upstream, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
