---
description: Clarify phase — ask at most 3–5 high-impact questions and fold answers back into the spec.
metadata:
  tags: [spec-kit, clarify, questions]
  source: github-spec-kit
---

# Clarify

Resolve underspecified areas **before** design. Planning on top of ambiguity wastes the rest of the loop.

## When to run

Run after specify, before design. Re-run only when analyze later reports requirement gaps.

Skip when the spec has no high-impact gaps and Assumptions cover the rest.

## Question budget

Ask **at most 3–5** questions per pass. Prefer 3.

Keep a question only when:

- The choice significantly changes scope or user experience
- Multiple reasonable interpretations have different implications
- No reasonable default exists

Drop technical-detail questions. Those belong in design, using repo conventions.

## AskQuestion mapping (Plan Mode)

Map each kept question to Cursor `AskQuestion` when that tool is available. Otherwise present the same structured questions in the conversation and wait.

Per question include:

- Topic and quoted spec context
- What must be known
- 2–4 concrete options plus Custom
- Implications of each option

Present all questions together. Wait for answers before design. Do not proceed with placeholders.

## After answers

1. Replace each `[NEEDS CLARIFICATION]` marker with the chosen answer.
2. Record unanswered low-impact items as Assumptions (stated defaults).
3. Re-check the spec quality checklist in [checklist.md](checklist.md).

## Built-in vs custom checklists

Spec Kit distinguishes:

- Built-in `checklists/requirements.md` — specify/clarify may update evaluated state
- Custom checklists from the checklist phase — reviewer-owned; do not silently mark `[x]`

In Plan Mode, keep the requirements checklist inside the plan document. Do not self-approve custom quality items.

## Done when

- High-impact gaps resolved or explicitly defaulted
- Spec updated in working memory (Plan Mode: not written to disk)
- Design can start without blocking questions
