---
disable-model-invocation: true
name: make-me-an-expert
description: >
  This skill should be used when the user says "make me an expert in",
  "/make me an expert in", "continue expert pack", "teach me from .expert",
  or "make me an expert — continue", or is stuck on a chapter in an existing
  `.expert/<topic>/` pack. It builds a sourced `.expert/<topic>/` pack and one
  Markdown coursebook PDF (repo, named topic, or both): intake, catalog-routed
  web/paper/YouTube-transcript research, cited kb, then teach-from-pack and
  gap-fill. Not tutoring-only (learn), workspace lessons (teach), or
  lit-review reports (deep-research).
source: original
date_added: "2026-08-29"
---

# Make Me An Expert

Build a sourced path from novice to competent practitioner with a map of the frontier. Write a local expert pack plus one coursebook PDF, then teach from that pack. This is not a certificate, a slide deck, or a dump of copyrighted books.

## When to Use

- User says "make me an expert in …", "/make me an expert in …", "continue expert pack", "teach me from .expert", or "make me an expert — continue"
- User wants a sourced `.expert/<topic>/` pack and one Markdown coursebook PDF (repo, named topic, or both), then teaching from that pack
- User is stuck on a chapter in an existing `.expert/<topic>/` pack and needs gap-fill

## When NOT to Use

- Tutoring-only, drills, study guides, or "help me understand X" with no pack — use `learn`
- Multi-file teaching workspace (MISSION, HTML lessons, learning-records) as the primary artifact — use `teach`
- Literature-review or research report with no coursebook and no teaching loop — use `deep-research`
- Slide decks — do not compose `2slides-ppt-generator` or `frontend-slides`
- User has started coding or other work — pause teaching; leave `STATE.md`; do not hijack Agent mode

## Constraints

- **Pack path:** always `<user-project>/.expert/<topic-slug>/`. Never write packs inside `~/.agents/skills/` or this skills repo. If the current workspace is the skills library, ask for a target project path first.
- **PDF:** paginated coursebook generated from Markdown, not 16:9 slides.
- **Compose cap:** at most 4 sibling skills this run. Catalog-first; load one `SKILL.md` at a time. Never bulk-read the library.
- **YouTube:** transcripts + `watchlist.md`. Cannot watch video.
- **Copyright:** distill and cite. Never paste full books, papers, or transcripts into `kb/` or the PDF. Link out.
- **Safety:** educational material, not professional advice (especially medical, legal, financial). Put this line in the PDF too.
- **Expertise ceiling:** fluency plus a map of open debates, not mastery.

## Resume

This skill does not auto-load (`disable-model-invocation: true`).

1. Write `.expert/<topic-slug>/STATE.md` in the user project (copy [templates/STATE.md](templates/STATE.md)).
2. During intake, offer an optional Cursor project rule in that repo so Ask mode notices `.expert/` and resumes. If accepted, add a short rule: when `.expert/` exists, load `STATE.md` and continue teaching from the current chapter.
3. Tell the user the resume line: **make me an expert — continue**
4. Later chats: load `STATE.md` first. Reuse `composed_skills`. Do not redo the research pass unless sources are stale or the user asks.

## Pack layout

```
.expert/<topic-slug>/
  STATE.md
  MISSION.md
  SOURCES.md
  kb/                      # distilled, cited notes
  course/book.md           # coursebook source (also the PDF source)
  output/expert-course.pdf
  watchlist.md
  supplements/             # gap-fill addenda
```

[templates/chapter.md](templates/chapter.md) is the **section shape inside** `course/book.md`, not a second file tree. Do not create `course/ch-*.md`. The PDF script reads a single `course/book.md`.

## Phases

Run in order. Stop if the user switches to other work.

### 1. Intake

Ask once, then proceed. Details: [references/intake.md](references/intake.md).

1. **Scope:** this repo, the named topic, or both
2. **Prior knowledge:** none / some / practitioner, plus 3–5 probing questions. Do not assume they know what they claimed.
3. **Goal:** ship in this repo, interview, academic, or operational fluency
4. **Constraints:** time, languages, topics to skip, depth ceiling
5. **Teaching style:** default explainer. Offer `learn` (adaptive tutoring) or `explain-like-socrates` if they ask — do not copy those skills.
6. Offer the optional project rule and give the resume line.

If the codebase is in scope: catalog and structure first, then targeted reads. Do not bulk-read this skills library.

### 2. Catalog route

Follow [references/compose.md](references/compose.md). Run the skill-recommender protocol in-process: search `_catalog/` only; pick 1 primary + up to 3 supporting skill IDs; write them to `STATE.md` under `composed_skills:`. Load each matching `SKILL.md` **one at a time**, only if it matches this run. Cap **4** siblings.

Do not compose: `2slides-ppt-generator`, `frontend-slides`, `pdf-official`. Skip API-key search tools (`tavily-web`, `exa-search`, `firecrawl-scraper`) unless the user already has keys.

### 3. Research

Follow [references/research.md](references/research.md). Rank: official docs and primary papers > textbooks/surveys > high-signal talk transcripts > reputable blogs. Skip SEO junk.

Cap ingest per run: ~8–15 core text sources, ~3–5 transcripts. Default fetch: composed `efficient-web-research` + `defuddle`. Academic topics: `papers-skill`. YouTube: `youtube-full` transcripts; put the rest on `watchlist.md`.

### 4. Knowledge base

Write distilled notes into `kb/` with citations. Record ingest status in `SOURCES.md`. If `wiki-builder` is composed, borrow provenance habits; do not replace the `.expert/` layout.

### 5. Coursebook PDF

Follow [references/curriculum.md](references/curriculum.md). Write one linear `course/book.md` (do not create `course/ch-*.md`; use [templates/chapter.md](templates/chapter.md) as the section shape inside that file):

- Map of the territory
- Diagnostic: "you said you know X — 1-page check"
- Foundations → core → advanced → frontier
- Worked examples tied to this repo when scope includes it
- Active-recall questions and deliberate-practice tasks per chapter
- Annotated bibliography
- "What experts still argue about"

Render with this skill's `scripts/render_coursebook.py` (Markdown → HTML → PDF; WeasyPrint, Pandoc fallback). Packs live in the user project; the script lives in the skills repo. From the user-project cwd:

`python3 <skills-root>/make-me-an-expert/scripts/render_coursebook.py .expert/<topic-slug>/course/book.md -o .expert/<topic-slug>/output/expert-course.pdf`

Resolve `<skills-root>` as: project `.agents/skills`, else this repo root, else `~/.agents/skills/`. Write `output/expert-course.pdf`. Printable TOC and page numbers. Not slides.

### 6. Teach

Follow [references/teaching.md](references/teaching.md). Teach from `kb/` + the current chapter. One idea at a time. Check understanding. If `learn` is composed, use that skill's retrieval-check pattern. If the user asked for Socratic style, load `explain-like-socrates`.

### 7. Gap-fill

When the user is stuck or a diagnostic fails: research the missing prerequisite, append `kb/` + `supplements/`, re-render the PDF (or a short supplement PDF), then re-explain. Say plainly: they claimed X; the gap is Y; it was added. Update `STATE.md` (`known` / `unknown` / `open_gaps` / `last_chapter`).

## Mode

- **Ask mode:** teach from the pack.
- **Agent mode:** research, write files, render PDF. If the user starts other work, pause.

## References

- [references/intake.md](references/intake.md) — scope and diagnostic questions
- [references/compose.md](references/compose.md) — catalog routing, sibling table, do-not-compose
- [references/research.md](references/research.md) — queries, source ranking, YouTube/transcript rules
- [references/curriculum.md](references/curriculum.md) — coursebook outline, expertise ceiling
- [references/teaching.md](references/teaching.md) — Ask-mode teaching, gap-fill, handoff to `learn` / Socratic
