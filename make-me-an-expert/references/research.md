# Research

Run research **sequentially** in this agent. Do not spawn a research swarm.

Write the pack under `.expert/<topic-slug>/` in the **user workspace**:

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
3. High-signal talks (transcripts of conference / university talks)
4. Reputable practitioner blogs

Skip SEO junk, listicles, affiliate roundups, and uncited “ultimate guides.”

## Search

Build a short query set from intake (topic, goal, language, skips). Cover: canonical intro, official docs, one survey or textbook-level source, known controversies, and (if repo-scoped) the stack actually used here.

If codebase is in scope: map structure first, then targeted reads. Do not bulk-read a large repo.

## Ingest caps (per run)

- ~8–15 core text sources
- ~3–5 transcripts

Quality over a giant unread pile. Record every candidate in `SOURCES.md` with rank, URL, and ingest status (`fetched` / `distilled` / `skipped` / `watchlist`).

## How to fetch

Load siblings one at a time (see `compose.md`); follow them; do not clone.

- **Web:** `efficient-web-research` + `defuddle`. Do not dump raw WebFetch HTML into `kb/` or the coursebook.
- **Papers:** `papers-skill` when the topic is academic. `hugging-face-papers` when ML papers dominate.
- **YouTube:** search, pick a small set of conference/university talks, ingest transcripts via `youtube-full` (preferred). Fallback: `youtube-summarizer` / `youtube-notetaker`. Put the rest on `watchlist.md`.
- **Citations:** keep `SOURCES.md` consistent (`citation-management` if composed).

This agent cannot watch video pixels. Videos become transcripts + a watch list. This agent cannot ingest whole books into context — distill.

## Distill

For each accepted source: fetch → distill into `kb/` with citations → link out.

- One note per concept or source cluster; cite title, authors/org, URL, date.
- Quote sparingly (a sentence, not a page).
- **Do not paste full copyrighted works** into `kb/` or the PDF. No textbook dumps, no paper-body dumps, no full transcripts in the coursebook.
- Long-form media not fully ingested goes on `watchlist.md` (title, URL, why it matters, what was not read).

## Done when

`SOURCES.md` lists the ranked set, `kb/` covers foundations through frontier at the intake depth ceiling, and `watchlist.md` exists (even if short). Then build the coursebook (`curriculum.md`).
