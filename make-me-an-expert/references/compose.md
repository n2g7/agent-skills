# Compose

Do **not** clone research or teaching skills. After intake, run the skill-recommender protocol **in-process**, then load matching siblings one at a time.

This skill owns: sourced research → local pack → one coursebook PDF → teach-from-pack. Tutoring-only requests stay with `learn`. Pure literature-review reports stay with `deep-research`.

## Catalog protocol (in-process)

Search `_catalog/` only. Never bulk-read the library.

Resolve catalog path in order: `.agents/skills/_catalog/` (project submodule) → `_catalog/` (this repo as workspace) → `~/.agents/skills/_catalog/` (global).

1. **Parse intent** from intake: domain, action, tools/platforms, language, academic vs applied, repo-scoped or not.
2. **Search the catalog** (read only what you need):
   - keyword grep on `_catalog/keyword-index.json` or `_catalog/skills-index.json`
   - then `_catalog/categories.md` / `_catalog/top-skills.md` if the keyword miss
3. **Rank:** specific tool/platform over generic; action match; substantive description; more specific over more general.
4. **Return** 1 primary + 1–3 supporting skill IDs (topic/domain experts plus pipeline siblings that this run actually needs).
5. **Load** those `SKILL.md` files **one at a time**, only if they match this run. Follow the sibling; do not copy it into this skill.
6. **Cap 4** loaded sibling skills. If teaching later needs `learn` or `explain-like-socrates` and the slot is full, drop a research-ingest sibling and update the list.
7. **Record** chosen IDs in `.expert/<topic-slug>/STATE.md` under `composed_skills:`. Later chats reuse that set — do not re-scan 1,700 skills.

Skip placeholders whose catalog description is still “Describe what this skill does…”.

## Pipeline siblings (composition graph)

Name these as candidates. Load only those that match the run, inside the cap of 4.

### Research / ingest

- `efficient-web-research` — default fetch policy; token-efficient URL/search. Prefer this over raw full-page dumps.
- `defuddle` — clean markdown from web pages. Use instead of dumping WebFetch HTML.
- `papers-skill` — Semantic Scholar + arXiv PDF text when the topic is academic.
- `hugging-face-papers` — arXiv/HF paper pages when ML papers dominate.
- `youtube-full` — search + transcripts (preferred over `ingest-youtube` on cloud IPs). Fallback: `youtube-summarizer` / `youtube-notetaker`.
- `wiki-builder` — optional provenance habits for `kb/`. Do not replace the `.expert/` layout.
- `deep-research` — only if the topic is huge **and** intake asked for a full literature pass. This skill still owns the coursebook and teaching loop.
- `context7-auto-research` — when scope includes a specific library/framework in the current repo.
- `citation-management` — keep `SOURCES.md` consistent.

### Codebase / domain

- `wiki-researcher` + `wiki-onboarding` — when scope is this repo (trace code; onboarding-grade maps).
- **Topic expert from catalog** — e.g. `postgres-best-practices`, `rust-pro`, `langchain-architecture`. Recommender picks these from the topic string. They are **curriculum sources**, not a second teacher.

### Teaching (after the pack exists)

- `learn` — primary tutoring sibling. Prefer this over inventing a tutor.
- `teach` — only if the user wants that skill’s multi-file workspace (MISSION, lessons, learning-records) *in addition to* `.expert/`.
- `explain-like-socrates` — only if intake chose Socratic style.
- `tutorial-engineer` — when the pack needs hands-on tutorials from *this* codebase.

## Do not compose

- `2slides-ppt-generator` / `frontend-slides` — decks, not the expert coursebook.
- `pdf-official` — PDF *processing*, not Markdown→PDF generation.
- `tavily-web` / `exa-search` / `firecrawl-scraper` — API-key tools. Use only if the user already has those keys. Default stack: Cursor WebSearch/WebFetch + `efficient-web-research` + `defuddle`.

## Collision notes

| Skill | Their job | Ours |
|-------|-----------|------|
| `learn` | Tutoring-only, no expert pack | Pack + coursebook + teach-from-pack. Hand off to `learn` when the user wants a tutor, not a pack. |
| `teach` | Multi-file teaching workspace | Compose only if the user asked for that workspace *plus* `.expert/`. |
| `deep-research` | Literature-review report | Compose only for a huge topic + explicit lit-pass. We still write the pack, PDF, and teaching loop. |

If a user asks only to be tutored, or only for a lit-review memo, do not take the job — point them at `learn` or `deep-research`.
