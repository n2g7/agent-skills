# Curriculum

Build one linear coursebook from the pack. Not a slide deck. Not a certificate.

Write `.expert/<topic-slug>/course/book.md` in the **user workspace**. Teach from the same Markdown the PDF is built from.

## Expertise ceiling

Aim for **competent practitioner with a map of the frontier**. Say so in the book. The pack does not certify expertise and must not claim the user is now an expert.

## `course/book.md` outline

Write these sections in order:

1. **Map of the territory** — short orientation: what the field is, how pieces connect, what this book covers vs skips.
2. **Diagnostic** — “you said you know X — 1-page check.” Probes from intake, not a recap of the self-rating. Mark what the pack will still teach.
3. **Foundations → core → advanced → frontier** — one chapter per idea cluster. Match depth to intake goal and ceiling. Do not skip foundations because they claimed knowledge.
4. **Repo examples** — when scope includes this repo, work examples against real paths and APIs here. When scope is topic-only, use canonical public examples.
5. **Active recall** — questions at the end of each chapter (define, decide, debug).
6. **Deliberate practice** — tasks per chapter; prefer repo work when in scope.
7. **Annotated bibliography** — from `SOURCES.md`; why each source matters; what was not ingested.
8. **What experts still argue about** — open debates so fluency is not mistaken for mastery.

Each chapter: claim → explanation → example → recall → practice. Keep chapters teachable in one sitting. `templates/chapter.md` is the section shape inside `course/book.md`; do not create `course/ch-*.md`.

## PDF

Render from the user-project cwd (packs live there; the script lives in the skills repo):

`python3 <skills-root>/make-me-an-expert/scripts/render_coursebook.py .expert/<topic-slug>/course/book.md -o .expert/<topic-slug>/output/expert-course.pdf`

Resolve `<skills-root>` as: project `.agents/skills`, else this repo root, else `~/.agents/skills/`. Markdown → HTML → PDF; WeasyPrint, Pandoc fallback.

Output: `.expert/<topic-slug>/output/expert-course.pdf`.

Requirements: printable, TOC, page numbers. **Not** 16:9 slides. Do not use `2slides-ppt-generator` or `frontend-slides`.

After gap-fill, re-render this PDF (or a short supplement PDF under `supplements/`).

## Safety line

Put this in the coursebook **and** the PDF front matter:

> Educational material only. Not professional advice. Especially not medical, legal, or financial advice. Verify against primary sources and qualified practitioners before acting.

## Honest limits

This agent cannot watch YouTube or ingest whole books. Point at `watchlist.md` and citations. Distilled notes in `kb/` are the teaching source; the PDF is the human-readable coursebook, not a copyrighted dump.
