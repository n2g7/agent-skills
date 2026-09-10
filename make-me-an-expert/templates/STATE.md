# Expert pack state

Fill this file at `.expert/<topic-slug>/STATE.md` in the user project. Never write it inside the skills repo.

Do not run `unslop` on the YAML keys below. You may run STE on the `notes` lines.

```yaml
topic: ""
topic_slug: ""
scope: topic          # repo | topic | both
goal: operational     # ship | interview | academic | operational
mode: intake          # intake | research | kb | pdf | teaching | gap-fill | paused
teaching_style: explainer   # explainer | learn | socratic
resume_line: "make me an expert — continue"
```

## composed_skills

Catalog IDs loaded this pack (cap 4). Later chats reuse this list. Do not re-scan the library.

- Primary:
- Supporting: []

## known

What the user actually showed (not only what they claimed).

-

## unknown

What is still untested or missing.

-

## last_chapter

- Id:
- Title:
- Status: not-started   # not-started | in-progress | stuck | done

## open_gaps

Prerequisite holes found during teaching or diagnostics. Each gap should point at a `kb/` note or `supplements/` addendum after fill.

| Gap | Claimed as known? | Added to pack? | Notes |
|-----|-------------------|----------------|-------|
|     |                   |                |       |

## notes

- Pack path: `.expert/<topic-slug>/`
- If the user starts other work, set `mode: paused` and stop teaching.
