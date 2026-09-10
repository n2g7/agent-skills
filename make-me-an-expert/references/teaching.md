# Teaching

Teach from the pack. Do not lecture from memory. Do not reopen the full research pass.

Write each reply in STE. Then run `unslop --stdin --deterministic` on the reply. Send only the cleaned text. See `ste-pass.md`.

## Mode

Prefer **Ask mode**. Teach from `.expert/<topic-slug>/kb/` plus the current chapter in `course/book.md`. One idea at a time. Check understanding before the next idea.

If `learn` is in `composed_skills`, follow that skill's retrieval-check pattern. Do not invent a second tutor.

If intake chose Socratic style and `explain-like-socrates` is composed, follow that skill. Otherwise explain. Then question.

## Session start (later chats)

This skill does not auto-load. On *make me an expert — continue*, *teach me from .expert*, or *I do not understand this chapter*:

1. Load `.expert/<topic-slug>/STATE.md` first (`composed_skills`, last chapter, known or unknown, open gaps, mode).
2. Load only the current chapter and the `kb/` notes it needs.
3. Do not redo research unless sources are stale or the user asks.

If several packs exist, ask which `<topic-slug>`.

## Gap-fill loop

If the user is stuck, or a probe shows the pack assumed too much:

1. Name the missing prerequisite.
2. Research that gap (same ingest rules as `research.md`. Stay inside the compose cap).
3. Append distilled notes to `kb/` and a short addendum under `supplements/`.
4. Run the STE and unslop pass on the new Markdown.
5. Re-render the coursebook PDF (or a short supplement PDF).
6. Say this clearly: you said you knew X. The gap is Y. I added that.
7. Explain again from the new notes. Update `STATE.md` (open gaps, last chapter).

Do not only rephrase the same chapter from memory.

## Stop conditions

If the user starts coding or other work, stop teaching. Do not take over Agent mode. Leave `STATE.md` current. Tell them the resume line: *make me an expert — continue*.

## Handoff

- Tutoring only (no pack work): point to `learn`.
- Socratic only: point to `explain-like-socrates`.
- They want `teach`'s multi-file workspace in addition to `.expert/`: compose `teach` (cap 4) and keep this pack as the source of truth.

Do not clone those skills.

## Optional project rule

If the user accepted at intake, add a small project rule in the user repo (not the skills library) so Ask mode notices `.expert/`. Keep it short: pack path, resume phrase (*make me an expert — continue*), load `STATE.md` first, stop if they start other work. Do not add the rule unless they agreed.
