---
description: Specify phase — write a technology-agnostic feature spec (what and why) before design.
metadata:
  tags: [spec-kit, specify, requirements]
  source: github-spec-kit
---

# Specify

Create or update the feature specification from the user's natural-language request. Focus on **what** and **why**. Leave stack, APIs, and file layout to [design.md](design.md).

## Inputs

- User's feature description
- Repo context from research (existing behavior, constraints, similar features)
- Constitution / project principles, if loaded

## Output

A spec matching the spec outline in [templates.md](templates.md):

- User scenarios & testing (mandatory)
- Functional requirements (mandatory)
- Success criteria (mandatory, technology-agnostic)
- Key entities (when data is involved)
- Assumptions
- Edge cases

## Rules

1. Parse the feature description. Empty description → stop and ask for one.
2. Extract actors, actions, data, and constraints.
3. Fill user stories with priority (P1, P2, …), independent test, and Given/When/Then acceptance scenarios. At least one P1 story is required.
4. Write testable functional requirements (`FR-001`, `FR-002`, …). Each MUST statement must be checkable.
5. Write measurable success criteria (`SC-001`, …) from the user/business view. No frameworks, languages, databases, or tools.
6. Cap `[NEEDS CLARIFICATION: …]` markers at **3**. Prefer informed defaults; record them under Assumptions.
7. Prioritize remaining clarifications: scope > security/privacy > user experience > technical details.
8. Keep implementation out of the spec. Languages, libraries, endpoints, and folder trees belong in design.

## Reasonable defaults (do not ask)

- Industry-standard data retention for the domain
- Typical web/mobile performance unless the user set a target
- User-friendly errors with a safe fallback
- Reuse the repo's existing auth/session pattern when one exists
- Integration style that already matches the project (REST, GraphQL, in-process, CLI)

## Success criteria quality

Good: "Users complete checkout in under 3 minutes"; "95% of searches return results in under 1 second".

Bad: "API p95 under 200ms"; "React components render efficiently"; "Redis hit rate above 80%".

## Done when

- Spec has mandatory sections filled
- No more than 3 unresolved `[NEEDS CLARIFICATION]` markers
- Spec is ready for clarify (if markers remain) or design (if none remain)
