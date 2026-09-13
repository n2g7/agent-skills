---
description: Worked example of running spec-kit inside Cursor Plan Mode and stopping at CreatePlan.
metadata:
  tags: [spec-kit, example, plan-mode]
  source: community
---

# Example: Plan Mode run

User: "Use spec-kit in Plan Mode. Add saved dashboard views so a signed-in user can save the current filter set and reopen it later."

Assume a web app already using TypeScript, Postgres, and session auth. Plan Mode is active (read-only).

## 0. Research

Read existing dashboard filter code, auth session model, and schema. Note: no `.specify/` directory. Constitution absent.

## 1. Constitution

Skip. No principles file. User stated none.

## 2. Specify (excerpt)

**User Story 1 (P1):** Signed-in user saves the current dashboard filters as a named view.

- Independent test: save "Q3 closed-won" from the dashboard; list shows that name; selecting it restores filters.
- FR-001: System MUST let a signed-in user save the current filter set with a unique name they choose.
- FR-002: System MUST restore a saved view's filters onto the dashboard when the user selects it.
- SC-001: User can save and restore a view in under 30 seconds without re-entering filters.

No stack in the spec.

## 3. Clarify

One high-impact gap: are views private to the user or shared with the team?

AskQuestion: Private (A) vs team-shared (B) vs Custom.

User picks A. Record: views are per-user. Other defaults (max name length, overwrite on duplicate name) go under Assumptions.

## 4. Design (excerpt)

- Language: TypeScript (existing app)
- Storage: existing Postgres; new `saved_views` table keyed by `user_id`
- Files: `src/dashboard/filters.ts`, new `src/dashboard/saved-views.ts`, migration under `db/migrations/`
- Do not introduce a new framework.

## 5. Checklist

Content quality passes (no React/Postgres in spec). FRs testable. SC-001 measurable and technology-agnostic. Gate passes.

## 6. Tasks (excerpt)

- T001 Setup: confirm dashboard filter module paths
- T002 Foundational: add `saved_views` migration in `db/migrations/`
- T003 [US1] persist/list/restore helpers in `src/dashboard/saved-views.ts`
- T004 [US1] wire save/restore UI into `src/dashboard/filters.ts`
- T005 Polish: empty-state copy when the user has no views

## 7. Analyze

- FR-001 and FR-002 each have tasks
- No design/spec contradiction (privacy = per-user matches `user_id` key)
- T002 correctly sits in Foundational
- No Critical findings

## 8. CreatePlan — then STOP

Plan title: "Saved dashboard views". Body includes Spec, Clarifications, Design, Checklist, Tasks, Analysis, Implementation notes.

Todos: Foundational migration; US1 persist/restore; UI wire-up; empty state.

**Do not implement.** No files written (no `.specify/`, user did not ask to persist Spec Kit files).

## After approval (not this example)

Agent Mode implements T001–T005 from the approved plan. Persist `specs/` only if the user then asks for Spec Kit files or `.specify/` exists.
