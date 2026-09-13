---
description: Tasks phase — dependency-ordered, phased task list from spec and design.
metadata:
  tags: [spec-kit, tasks, breakdown]
  source: github-spec-kit
---

# Tasks

Generate an actionable task list from the spec and design. This is Spec Kit `/speckit.tasks`.

## Prerequisites

- Spec with prioritized user stories
- Design with stack and real file paths

Tests are optional. Include test tasks only when the spec or user requested tests.

## Format

`Tnnn [P?] [USn?] Description with exact file path`

- `[P]` — safe to run in parallel (different files, no dependency)
- `[USn]` — owning user story for traceability
- IDs sequential (`T001`, `T002`, …)
- Descriptions name the file to create or edit

## Phases (required order)

1. **Setup** — project/scaffold, tooling. No story work.
2. **Foundational** — blocking shared infrastructure (schema, auth, routing, shared models, logging). **Blocks all user stories.**
3. **User Story 1 (P1 / MVP)** — independently testable. Optional tests first if requested.
4. **User Story 2+** — one phase per remaining story, priority order.
5. **Polish** — docs, cleanup, cross-cutting hardening.

Within a story: tests (if any, and failing first) → models → services → endpoints/UI → integration.

## Independence

Each user story must be deliverable and testable without the later stories. Shared foundation stays in Phase 2, not duplicated per story.

## Parallel markers

Mark `[P]` only when:

- Different files
- No ordering dependency
- No write conflict on the same file

Do not mark `[P]` on a task that depends on another task's output.

## Map onto CreatePlan todos

Each phase or each P1 story should appear as a `CreatePlan` todo. Keep the full Tnnn list in the plan body's Tasks section. Do not collapse Foundational into a story todo.

## Done when

- Every FR maps to at least one task
- Foundational explicitly blocks stories
- File paths match the design
- P1 story is an MVP that can ship alone
