---
disable-model-invocation: true
name: spec-kit
description: This skill should be used when the user asks to "use Spec Kit", "spec-driven development", "/speckit", "specify then plan", "run speckit in Plan Mode", or to do more work in Plan Mode before coding. Distills GitHub Spec Kit's specify → clarify → plan → tasks → analyze loop into a richer CreatePlan; implementation waits for approval.
category: planning
risk: safe
source: community
date_added: "2026-09-13"
---

# Spec Kit (Plan Mode)

Run GitHub Spec Kit's Spec-Driven Development loop **inside Cursor Plan Mode**. Produce a richer `CreatePlan`. Do not write code until the user approves the plan.

This skill is a Plan Mode dispatcher. It does **not** install `specify-cli`, does **not** run `specify init`, and does **not** replace per-project `.cursor/skills/speckit-*` skills.

## Naming collisions

| Term | Meaning |
|------|---------|
| Cursor **Plan Mode** | Read-only research + clarifying questions + `CreatePlan`, then wait for approval |
| Spec Kit **plan** (`/speckit.plan`) | The "how" phase: stack, architecture, constraints |
| Official **cursor-agent** integration | Per-project `specify init --integration cursor-agent` that writes `.cursor/skills/speckit-*/SKILL.md` and `.specify/` |

Treat Cursor Plan Mode as the **container**. Treat Spec Kit specify/clarify/plan/tasks/analyze as **work that happens before `CreatePlan`**.

## When to Use

- User asks to "use Spec Kit", "spec-driven development", `/speckit`, or "specify then plan"
- User wants more work done in Plan Mode before coding
- Feature work with meaningful ambiguity: user stories, acceptance criteria, architecture, task breakdown
- Planning a non-trivial change where iterating on spec/design is cheaper than iterating on code

## When NOT to Use

- One-line or obvious fixes with no spec value
- Updating an existing Spec Kit install or templates — use `speckit-updater`
- User explicitly asked to run official `specify init` / project-local `/speckit-*` skills
- Already in Agent Mode with an approved plan and the task is "just implement"

## Mode detection

**Plan Mode (read-only):** Research, specify, clarify, design, checklist, tasks, analyze, then `CreatePlan`. Do not write files. Do not implement.

**Agent Mode after plan approval:** Optional persist of `specs/` artifacts, then implement from the approved task list. See [references/implement.md](references/implement.md).

If mode is unclear, assume Plan Mode whenever the session is planning, designing, or producing a plan artifact.

## Plan Mode workflow

Copy and track:

```
- [ ] 0. Research (read-only)
- [ ] 1. Constitution (load if present)
- [ ] 2. Specify (what/why)
- [ ] 3. Clarify (AskQuestion, max 3–5)
- [ ] 4. Design (how: stack/architecture)
- [ ] 5. Checklist (spec quality gate)
- [ ] 6. Tasks (phased, dependency-ordered)
- [ ] 7. Analyze (cross-artifact consistency)
- [ ] 8. CreatePlan (all artifacts as sections)
- [ ] STOP — wait for approval
```

Load the matching reference **before** executing that phase. Do not skip 2, 4, 6, or 8. Skip 3 only when no high-impact gaps remain. Skip 1 when no constitution exists and the user stated no principles.

### 0. Research

Read the repo, existing specs, AGENTS.md, and constraints. Do not write files.

Detect optional Spec Kit layout:

- `.specify/` present → later persistence is allowed after approval; still do not write during Plan Mode
- `specs/` or `.specify/memory/constitution.md` → load as input
- No `.specify/` → proceed without the CLI; artifacts live in `CreatePlan` only until approval

### 1. Constitution

If `.specify/memory/constitution.md` (or similar project principles) exists, load it and evaluate later phases against it.

If none exists and the user stated principles, encode a short Constitution section in the plan. Do not invent a constitution ceremony.

### 2. Specify — what and why

Follow [references/specify.md](references/specify.md). Fill [references/templates.md](references/templates.md) spec outline.

Focus on user-facing behavior and goals. No tech stack, APIs, frameworks, or file paths in this phase.

### 3. Clarify

Follow [references/clarify.md](references/clarify.md). Ask at most 3–5 high-impact questions (scope > security/privacy > UX). Record remaining defaults under Assumptions. Wait for answers before design.

### 4. Design — how

Follow [references/design.md](references/design.md). This is Spec Kit `/speckit.plan`: stack, architecture, files to change, constraints. Derive from the spec plus the repo. Do not invent a parallel stack when the repo already has one.

### 5. Checklist

Follow [references/checklist.md](references/checklist.md). Fail the gate if the spec leaks implementation, FRs are untestable, or success criteria are not measurable. Fix the spec, then continue.

### 6. Tasks

Follow [references/tasks.md](references/tasks.md). Phases: Setup → Foundational (blocks stories) → one phase per user story in priority order → Polish. Mark `[P]` only when tasks touch different files and have no ordering dependency.

### 7. Analyze

Follow [references/analyze.md](references/analyze.md). Read-only consistency across spec, design, and tasks. Fix at the owning phase. Do not call `CreatePlan` while critical conflicts remain.

### 8. CreatePlan — then stop

Emit **one** `CreatePlan` whose body contains every artifact as sections. Map Spec Kit tasks onto `CreatePlan` todos.

Required plan sections:

```markdown
# [Feature Name]

## Spec (what / why)
[User stories, FRs, success criteria, assumptions — technology-agnostic]

## Clarifications resolved
[Questions asked, answers, remaining defaults]

## Design (how)
[Stack, architecture, files to change, constraints]

## Requirements checklist
[Pass/fail items from the spec quality gate]

## Tasks
[Phased task list with IDs, [P] markers, story labels, file paths]

## Analysis
[Conflicts/gaps found and how they were resolved]

## Implementation notes
Do this only after plan approval. Do not implement in Plan Mode.
Optional persist to specs/ only if .specify/ exists or the user asked for Spec Kit files.
```

**Hard stop.** Do not implement. Do not create files. Do not start todos.

## After approval (Agent Mode)

1. Persist `specs/<n>-<short-name>/` **only if** `.specify/` already exists **or** the user asked for Spec Kit files. Never require `specify-cli`.
2. Implement from the approved task list. Follow [references/implement.md](references/implement.md).
3. Converge is optional: compare code to spec/design/tasks; append missing tasks; do not silently rewrite the spec.

## Common mistakes

| Mistake | Fix |
|---------|-----|
| Treating `/speckit.plan` as Cursor Plan Mode | Design is one phase inside Plan Mode. `CreatePlan` is the stop point. |
| Putting stack in the spec | Move languages, APIs, and paths to Design. |
| Asking more than 5 clarifications | Cap at 3–5. Default the rest. Record Assumptions. |
| Calling `CreatePlan` then starting code | Hard stop after `CreatePlan`. Implement only after approval. |
| Running `specify init` unasked | This skill does not need the CLI. Scaffold only when the user asked. |
| Marking custom checklist items complete during implement | Unchecked items are a gate. Ask. Do not self-approve. |
| Writing `specs/` during Plan Mode | Plan Mode is read-only. Persist after approval, and only if `.specify/` exists or the user asked. |

## Official CLI (out of scope)

Official install remains:

```bash
uv tool install specify-cli
specify init . --integration cursor-agent
```

That path is per-project scaffolding. Use it only when the user asked to initialize Spec Kit in the repo. This skill covers Plan Mode methodology without that install.

## Additional resources

- [references/specify.md](references/specify.md) — what/why spec rules
- [references/clarify.md](references/clarify.md) — question budget and AskQuestion mapping
- [references/design.md](references/design.md) — stack and architecture
- [references/checklist.md](references/checklist.md) — spec quality gate
- [references/tasks.md](references/tasks.md) — phased task breakdown
- [references/analyze.md](references/analyze.md) — cross-artifact consistency
- [references/implement.md](references/implement.md) — post-approval execution
- [references/templates.md](references/templates.md) — spec / design / tasks outlines
- [examples/plan-mode-run.md](examples/plan-mode-run.md) — worked Plan Mode example
- [SOURCE.md](SOURCE.md) — attribution to github/spec-kit
