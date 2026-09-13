---
description: Spec quality gate — unit tests for requirements before task breakdown.
metadata:
  tags: [spec-kit, checklist, quality]
  source: github-spec-kit
---

# Checklist

Validate the spec before breaking work into tasks. This is Spec Kit `/speckit.checklist` distilled to a requirements-quality gate.

## Purpose

Confirm the spec is complete, clear, unambiguous, and consistent. Checked items mean **requirements quality**, not implementation complete.

## Built-in requirements checklist

Evaluate every item. Fix the spec on failure (except remaining `[NEEDS CLARIFICATION]` items, which go back to clarify).

### Content quality

- [ ] No implementation details (languages, frameworks, APIs)
- [ ] Focused on user value and business needs
- [ ] Written for non-technical stakeholders
- [ ] All mandatory sections completed

### Requirement completeness

- [ ] No `[NEEDS CLARIFICATION]` markers remain (or they are queued for clarify)
- [ ] Requirements are testable and unambiguous
- [ ] Success criteria are measurable
- [ ] Success criteria are technology-agnostic
- [ ] All acceptance scenarios are defined
- [ ] Edge cases are identified
- [ ] Scope is clearly bounded
- [ ] Dependencies and assumptions identified

### Feature readiness

- [ ] All functional requirements have clear acceptance criteria
- [ ] User scenarios cover primary flows
- [ ] Feature meets measurable outcomes in Success Criteria
- [ ] No implementation details leak into the specification

## Handling results

- All pass → continue to tasks.
- Failures (not clarifications) → patch the spec, re-evaluate, max 3 iterations. Remaining fails go in Analysis notes.
- Clarification markers → return to [clarify.md](clarify.md) before tasks.

## Custom checklists

A broader "unit tests for requirements" pass is optional (e.g. "Are drag-and-drop rules defined for every column?"). Custom items are reviewer-owned. Do not mark `[x]` unless the user/reviewer confirmed the criterion.

## Plan Mode

Keep checklist state inside the plan document (`## Requirements checklist`). Do not write `checklists/requirements.md` until after approval, and only if persisting Spec Kit files.

## Done when

- Gate passed or residual issues are documented and non-blocking
- Spec is stable enough for task generation
