---
description: Analyze phase — read-only consistency check across spec, design, and tasks.
metadata:
  tags: [spec-kit, analyze, consistency]
  source: github-spec-kit
---

# Analyze

Read-only cross-artifact check. This is Spec Kit `/speckit.analyze`. Do not rewrite artifacts here — report, then fix at the owning phase.

## Inputs

- Spec (what/why)
- Design (how)
- Tasks (Tnnn list)
- Constitution, if any

## Report

Grade findings:

| Severity | Meaning | Action |
|----------|---------|--------|
| Critical | Conflict that would implement the wrong thing | Fix before `CreatePlan` |
| Major | Gap (task with no FR, FR with no task, design contradicts spec) | Fix at owner, then re-check |
| Minor | Wording, extra polish, optional coverage | Record; do not block |

## Checks

- Every `FR-nnn` has at least one task
- Every task traces to a story or to Setup/Foundational/Polish
- Design stack/files do not contradict spec behavior
- Success criteria remain technology-agnostic in the spec
- Foundational really blocks stories (no story task that belongs in foundation)
- `[P]` tasks do not share a file
- Constitution gates still hold, or exceptions are in Complexity Tracking
- No leftover `[NEEDS CLARIFICATION]` that blocks implementation

## Fix at the source

| Problem | Owner |
|---------|-------|
| Wrong/missing requirement | specify or clarify |
| Wrong stack/structure | design |
| Missing/misordered work | tasks |

Re-run the check after fixes. Do not call `CreatePlan` while Critical findings remain. Major findings should be gone or explicitly accepted by the user.

## Plan Mode

Keep the report in the plan's `## Analysis` section. Do not write a separate analyze file.

## Done when

- No Critical findings
- Major findings fixed or user-accepted
- Spec, design, and tasks tell one story
