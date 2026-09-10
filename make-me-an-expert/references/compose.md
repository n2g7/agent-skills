# Compose

Do not clone research or teaching skills. After intake, run the skill-recommender protocol in this process. Then load matching siblings one at a time.

This skill owns sourced research, a local pack, one coursebook PDF, and teach-from-pack. Tutoring-only requests stay with `learn`. Pure literature-review reports stay with `deep-research`.

Always run `ste-writing` and `unslop` after you write pack Markdown. See `ste-pass.md`. Those two skills do not count toward the cap of 4.

## Catalog protocol (in this process)

Search `_catalog/` only. Never bulk-read the library.

Resolve catalog path in order: `.agents/skills/_catalog/` (project submodule), then `_catalog/` (this repo as workspace), then `~/.agents/skills/_catalog/` (global).

1. **Parse intent** from intake: domain, action, tools or platforms, language, academic vs applied, repo-scoped or not.
2. **Search the catalog** (read only what you need):
   - Keyword grep on `_catalog/keyword-index.json` or `_catalog/skills-index.json`
   - Then `_catalog/categories.md` / `_catalog/top-skills.md` if the keyword miss
3. **Rank:** specific tool or platform over generic. Action match. Substantive description. More specific over more general.
4. **Return** 1 primary and 1 to 3 supporting skill IDs (topic or domain experts plus pipeline siblings that this run needs).
5. **Load** those `SKILL.md` files one at a time, only if they match this run. Follow the sibling. Do not copy it into this skill.
6. **Cap 4** loaded sibling skills. If teaching later needs `learn` or `explain-like-socrates` and the slot is full, drop a research-ingest sibling and update the list.
7. **Record** chosen IDs in `.expert/<topic-slug>/STATE.md` under `composed_skills:`. Later chats reuse that set. Do not re-scan 1,700 skills.

Skip placeholders whose catalog description is still "Describe what this skill does…".

## Pipeline siblings (composition graph)

Name these as candidates. Load only those that match the run, inside the cap of 4.

### Research / ingest

- `efficient-web-research`: default fetch policy. Token-efficient URL and search. Prefer this over raw full-page dumps.
- `defuddle`: clean markdown from web pages. Use this instead of dumping WebFetch HTML.
- `papers-skill`: Semantic Scholar and arXiv PDF text when the topic is academic.
- `hugging-face-papers`: arXiv or HF paper pages when ML papers dominate.
- `youtube-full`: search and transcripts (preferred over `ingest-youtube` on cloud IPs). Fallback: `youtube-summarizer` / `youtube-notetaker`.
- `wiki-builder`: optional provenance habits for `kb/`. Do not replace the `.expert/` layout.
- `deep-research`: only if the topic is huge and intake asked for a full literature pass. This skill still owns the coursebook and teaching loop.
- `context7-auto-research`: when scope includes a specific library or framework in the current repo.
- `citation-management`: keep `SOURCES.md` consistent.

### Codebase / domain

- `wiki-researcher` and `wiki-onboarding`: when scope is this repo (trace code. Onboarding-grade maps).
- **Topic expert from catalog**: for example `postgres-best-practices`, `rust-pro`, `langchain-architecture`. The recommender picks these from the topic string. They are **curriculum sources**. They are not a second teacher.

### Teaching (after the pack exists)

- `learn`: primary tutoring sibling. Prefer this over inventing a tutor.
- `teach`: only if the user wants that skill's multi-file workspace (MISSION, lessons, learning-records) in addition to `.expert/`.
- `explain-like-socrates`: only if intake chose Socratic style.
- `tutorial-engineer`: when the pack needs hands-on tutorials from this codebase.

## Do not compose

- `2slides-ppt-generator` / `frontend-slides`: decks. Not the expert coursebook.
- `pdf-official`: PDF processing. Not Markdown to PDF generation.
- `tavily-web` / `exa-search` / `firecrawl-scraper`: API-key tools. Use only if the user already has those keys. Default stack: Cursor WebSearch or WebFetch plus `efficient-web-research` plus `defuddle`.

## Collision notes

- `learn`: tutoring only. No expert pack. Hand off to `learn` when the user wants a tutor, not a pack.
- `teach`: multi-file teaching workspace. Compose only if the user asked for that workspace and `.expert/`.
- `deep-research`: literature-review report. Compose only for a huge topic and an explicit literature pass. We still write the pack, PDF, and teaching loop.

If a user asks only to be tutored, or only for a literature-review memo, do not take the job. Point them at `learn` or `deep-research`.
