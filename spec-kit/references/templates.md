---
description: Distilled spec, design, and tasks outlines adapted from GitHub Spec Kit templates.
metadata:
  tags: [spec-kit, templates, outlines]
  source: github-spec-kit
---

# Templates

Fill these outlines in working memory during Plan Mode. After approval, optionally persist them under `specs/<n>-<short-name>/`.

Placeholders in `[brackets]` are to be replaced. Preserve heading order. Remove optional sections that do not apply; do not leave "N/A".

## Spec outline

```markdown
# Feature Specification: [FEATURE NAME]

**Status**: Draft
**Input**: [user description]

## User Scenarios & Testing *(mandatory)*

### User Story 1 - [Title] (Priority: P1)

[Plain-language journey]

**Why this priority**: [value]
**Independent Test**: [how to test this story alone]

**Acceptance Scenarios**:

1. **Given** [state], **When** [action], **Then** [outcome]
2. **Given** [state], **When** [action], **Then** [outcome]

### User Story 2 - [Title] (Priority: P2)

[Same shape as Story 1]

### Edge Cases

- [boundary]
- [error]

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST [capability]
- **FR-002**: System MUST [capability]

### Key Entities *(if data is involved)*

- **[Entity]**: [meaning and attributes, no schema]

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: [user-facing, measurable, technology-agnostic]
- **SC-002**: [user-facing, measurable, technology-agnostic]

## Assumptions

- [default taken]
- [scope boundary]
```

## Design outline

```markdown
# Implementation Plan: [FEATURE]

**Spec**: [feature name / link]

## Summary

[Primary requirement + technical approach]

## Technical Context

- **Language/Version**:
- **Primary Dependencies**:
- **Storage**:
- **Testing**:
- **Target Platform**:
- **Project Type**:
- **Performance Goals**:
- **Constraints**:
- **Scale/Scope**:

## Constitution Check

[Pass/fail against loaded principles, or "no constitution"]

## Project Structure

[Real directories from the repo]

**Structure Decision**: [why this layout]

## Files to change

- [path] — [why]

## Complexity Tracking

[Only if a principle is violated and justified]
```

## Tasks outline

```markdown
# Tasks: [FEATURE NAME]

## Phase 1: Setup

- [ ] T001 [description + path]
- [ ] T002 [P] [description + path]

## Phase 2: Foundational (blocks all stories)

- [ ] T003 [description + path]

**Checkpoint**: foundation ready

## Phase 3: User Story 1 - [Title] (P1 / MVP)

**Independent Test**: [from spec]

- [ ] T004 [US1] [description + path]
- [ ] T005 [P] [US1] [description + path]

**Checkpoint**: US1 independently testable

## Phase 4: User Story 2 - [Title] (P2)

- [ ] T00n [US2] [description + path]

## Phase N: Polish

- [ ] T00n [P] [docs/cleanup/hardening]
```
