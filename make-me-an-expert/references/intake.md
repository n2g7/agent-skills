# Intake

Run intake once for a new pack. Ask. Wait. Then proceed. Do not research or compose until you have answers.

Write artifacts only under `.expert/<topic-slug>/` in the user workspace (current project). Never write packs into the skills library.

## 1. Scope (hybrid. The user chooses)

Ask: this **repo**, the **named topic**, or **both**?

- **Repo only**: curriculum and examples come from this codebase.
- **Topic only**: ignore the repo except as the write target for `.expert/`.
- **Both**: research the topic. Bind worked examples to this repo.

If the workspace is this skills library (about 1,700 skills): do not bulk-read it. Catalog and structure first. Then targeted reads only.

Derive `<topic-slug>` (lowercase, hyphenated). Confirm if it is ambiguous.

## 2. Prior knowledge

Ask for a self-rating: **none** / **some** / **practitioner**.

Then ask 3 to 5 probes that fail if the rating is inflated. Cover:

- A term they should define if the rating is true
- A concrete decision or tradeoff
- A failure mode or common bug
- (if repo-scoped) a file, API, or pattern in this codebase

Do not treat the self-rating as fact. Record claimed knowledge as hypotheses in `STATE.md`. Curriculum and teaching must check before they skip foundations.

## 3. Goal

Ask which outcome they need:

- Ship something in this repo
- Interview / hiring bar
- Academic (papers, proofs, citations)
- Operational fluency (run, debug, decide)

## 4. Limits

Ask: time budget, languages, topics to skip, depth ceiling. Honor skips. Do not expand past the ceiling.

## 5. Teaching style

Default: explainer from the pack (this skill).

Offer. Do not clone:

- `learn`: adaptive tutoring, retrieval checks, study guides
- `explain-like-socrates`: Socratic questions

Record the choice. Load the sibling later only if chosen (see `compose.md`).

## 6. Resume hook

This library uses `disable-model-invocation: true`. Later chats will not auto-load this skill.

Tell the user the resume line: *make me an expert — continue*.

Offer a small **project rule** in the user repo so Ask mode notices `.expert/`. Do not add the rule unless they accept. See `teaching.md`.

## After answers

Write `MISSION.md` (why they are learning). Start `STATE.md` (`known` / `unknown`, mode, open gaps, claimed-vs-probed notes). Then route the catalog (`compose.md`).
