---
description: Post-approval implementation and optional converge. Do not run this in Plan Mode.
metadata:
  tags: [spec-kit, implement, converge]
  source: github-spec-kit
---

# Implement (after approval)

Execute only after the user approves the plan. Plan Mode must not reach this file's write/code steps.

## Persist artifacts (optional)

Write `specs/<n>-<short-name>/` only when:

- `.specify/` already exists in the project, **or**
- The user asked for Spec Kit files

Never install `specify-cli` as a prerequisite. If persisting, write at least `spec.md`, `plan.md`, and `tasks.md` from the approved plan. Do not invent git branch hooks.

If neither condition holds, implement directly from the approved plan body.

## Checklist gate

Before coding, read checklist checkbox state.

- Unchecked built-in or custom items → ask before proceeding
- Do not silently mark items `[x]`
- Custom checklist `[x]` means requirements quality, not "code done"

## Execution

1. Walk tasks in phase order: Setup → Foundational → stories (P1 first) → Polish.
2. Respect `[P]` as "may parallelize", not "must spawn subagents".
3. Stop at story checkpoints and validate the independent test from the spec.
4. For large features, implement one phase per session rather than the entire list.
5. Do not change the spec to match sloppy code. Change code to match the spec, or go back to specify/clarify with the user.

## Converge (optional)

After implementation, compare the codebase to spec, design, and tasks.

- Append-only: add missing tasks under a Convergence section
- Do not delete code or rewrite the spec as a side effect
- Re-implement appended tasks, then converge again until no gaps remain

## Done when

- Approved P1 (or requested scope) is implemented and independently testable
- Checklist was honored as a gate
- Convergence either reports complete or has a remaining task list
