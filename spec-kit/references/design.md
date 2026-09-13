---
description: Design phase — Spec Kit plan (how). Stack, architecture, constraints, and files to change.
metadata:
  tags: [spec-kit, plan, architecture, design]
  source: github-spec-kit
---

# Design (Spec Kit plan)

This is Spec Kit `/speckit.plan`. Implementation detail belongs here. It is **not** Cursor Plan Mode.

## Inputs

- Completed spec (what/why)
- Clarification answers
- Constitution / principles
- Actual repo layout and existing stack

## Output

A design matching the design outline in [templates.md](templates.md):

- Summary (primary requirement + technical approach)
- Technical context (language, dependencies, storage, testing, platform, constraints)
- Constitution check (gates from principles, if any)
- Project structure (real directories, not a generic scaffold)
- Files likely to change
- Complexity tracking only when a principle is violated and justified

## Rules

1. Prefer the repo's existing stack. Do not propose a greenfield stack unless the user asked or the repo is empty.
2. Put stack, APIs, schemas, and file paths here — never back in the spec.
3. Name concrete files and modules that will change.
4. If constitution gates fail, either change the design or record a justified exception in Complexity Tracking. Do not ignore gates.
5. Keep research notes short. Link to existing docs instead of restating them.
6. Do not generate `tasks.md` in this phase.

## Technical context fields

Fill from evidence. Mark unknown only when the repo and user both omit it and it blocks design:

- Language/version
- Primary dependencies
- Storage
- Testing
- Target platform
- Project type
- Performance goals
- Constraints
- Scale/scope

## Done when

- Design is consistent with the spec
- Stack matches the repo or an explicit user choice
- Structure decision cites real directories
- Ready for checklist + tasks
