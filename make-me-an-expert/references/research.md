# Research

Run research in sequence in this agent. Do not spawn a research swarm.

Write the pack under `.expert/<topic-slug>/` in the user workspace:

```
.expert/<topic-slug>/
  STATE.md
  MISSION.md
  SOURCES.md
  kb/
  watchlist.md
```

## Source ranking

Prefer, in order:

1. Official docs and primary papers
2. Textbooks and survey papers
3. High-signal talks (transcripts of conference or university talks)
4. Reputable practitioner blogs

Skip SEO junk, listicles, affiliate roundups, and uncited "ultimate guides."

## Search

Build a short query set from intake (topic, goal, language, skips). Cover: canonical intro, official docs, one survey or textbook-level source, known controversies, and (if repo-scoped) the stack used here.

If the codebase is in scope: map structure first. Then targeted reads. Do not bulk-read a large repo.

## Ingest caps (per run)

- About 8 to 15 core text sources
- About 3 to 5 transcripts

Quality over a giant unread pile. Record every candidate in `SOURCES.md` with rank, URL, and ingest status (`fetched` / `distilled` / `skipped` / `watchlist`).

## How to fetch

Load siblings one at a time (see `compose.md`). Follow them. Do not clone.

- **Web:** `efficient-web-research` and `defuddle`. Do not dump raw WebFetch HTML into `kb/` or the coursebook.
- **Papers:** `papers-skill` when the topic is academic. `hugging-face-papers` when ML papers dominate.
- **YouTube:** search. Pick a small set of conference or university talks. Ingest transcripts via `youtube-full` (preferred). Fallback: `youtube-summarizer` / `youtube-notetaker`. Put the rest on `watchlist.md`.
- **Citations:** keep `SOURCES.md` consistent (`citation-management` if composed).

This agent cannot watch video pixels. Videos become transcripts and a watch list. This agent cannot ingest whole books into context. Distill.

## Distill

For each accepted source: fetch. Distill into `kb/` with citations. Link out.

- One note per concept or source cluster. Cite title, authors or org, URL, date.
- Quote sparingly (a sentence, not a page).
- Do not paste full copyrighted works into `kb/` or the PDF. No textbook dumps. No paper-body dumps. No full transcripts in the coursebook.
- Long-form media not fully ingested goes on `watchlist.md` (title, URL, why it matters, what was not read).

After distill, run the STE and unslop pass on pack Markdown (`ste-pass.md`) before you write or render the coursebook.

## Done when

`SOURCES.md` lists the ranked set. `kb/` covers foundations through frontier at the intake depth ceiling. `watchlist.md` exists (even if short). Then build the coursebook (`curriculum.md`).
