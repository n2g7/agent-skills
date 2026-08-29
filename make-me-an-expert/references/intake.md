# Intake

Run intake once for a new pack. Ask, wait, then proceed. Do not research or compose until answers are in.

Write artifacts only under `.expert/<topic-slug>/` in the **user workspace** (current project). Never write packs into the skills library.

## 1. Scope (hybrid — user chooses)

Ask: this **repo**, the **named topic**, or **both**?

- **Repo only** — curriculum and examples come from this codebase.
- **Topic only** — ignore the repo except as the write target for `.expert/`.
- **Both** — research the topic; bind worked examples to this repo.

If the workspace is this skills library (~1,700 skills): do not bulk-read it. Catalog and structure first; then targeted reads only.

Derive `<topic-slug>` (lowercase, hyphenated). Confirm if ambiguous.

## 2. Prior knowledge

Ask for a self-rating: **none** / **some** / **practitioner**.

Then ask 3–5 probes that fail if the rating is inflated. Cover:

- a term they should define if the rating is true
- a concrete decision or tradeoff
- a failure mode or common bug
- (if repo-scoped) a file, API, or pattern in this codebase

Do **not** treat the self-rating as fact. Record claimed knowledge as hypotheses in `STATE.md`. Curriculum and teaching must verify before skipping foundations.

## 3. Goal

Ask which outcome they need:

- ship something in this repo
- interview / hiring bar
- academic (papers, proofs, citations)
- operational fluency (run, debug, decide)

## 4. Constraints

Ask: time budget, languages, topics to skip, depth ceiling. Honor skips. Do not expand past the ceiling.

## 5. Teaching style

Default: explainer from the pack (this skill).

Offer, do not clone:

- `learn` — adaptive tutoring, retrieval checks, study guides
- `explain-like-socrates` — Socratic questioning

Record the choice. Load the sibling later only if chosen (see `compose.md`).

## 6. Resume hook

This library uses `disable-model-invocation: true`. Later chats will not auto-load this skill.

Tell the user the resume line: *make me an expert — continue*.

Offer a small **project rule** in the user repo so Ask mode notices `.expert/`. Do not add the rule unless they accept. See `teaching.md`.

## After answers

Write `MISSION.md` (why they are learning) and start `STATE.md` (`known` / `unknown`, mode, open gaps, claimed-vs-probed notes). Then route the catalog (`compose.md`).
