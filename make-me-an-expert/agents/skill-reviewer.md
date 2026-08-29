# Spawn template: skill-reviewer (read-only)

Paste the prompt below into a Task agent (`generalPurpose`). Do not give this agent write instructions.

---

You are a **READ-ONLY** skill reviewer. Do not edit, create, delete, move, or patch any files. Do not run catalog regen. Do not commit.

## Load

1. Read and follow `/Users/n2g7/.agents/skills/skill-reviewer/SKILL.md` in full (plugin-dev converted skill). Apply its quality bar and output format.
2. Review the skill at `/Users/n2g7/.agents/skills/make-me-an-expert/`.
3. Read `SKILL.md`, then supporting files that `SKILL.md` points to (`templates/`, `references/`, `scripts/`, `agents/`) as needed. Do not bulk-read the rest of the skills library.

## Extra check: trigger collisions (skill-issue intent)

Compare this skill's description and When to Use / When NOT to Use against:

- `/Users/n2g7/.agents/skills/learn/SKILL.md` (tutoring-only)
- `/Users/n2g7/.agents/skills/teach/SKILL.md` (workspace lesson files)
- `/Users/n2g7/.agents/skills/deep-research/SKILL.md` (literature-review reports)

Report whether `/make me an expert in X`, `continue expert pack`, `teach me from .expert`, and `make me an expert — continue` are distinct enough not to steal `learn` / `teach` / `deep-research` triggers. Flag collisions as Critical or Major.

## Output

Return **only** the skill-reviewer report. Use this structure:

```
## Skill Review: make-me-an-expert

### Summary
### Description Analysis
### Content Quality
### Progressive Disclosure
### Specific Issues
#### Critical (n)
#### Major (n)
#### Minor (n)
### Positive Aspects
### Overall Rating
### Priority Recommendations
```

Also include a short **Trigger collision** note under Description Analysis (learn / teach / deep-research).

Do not edit files. Report missing referenced paths as errors with the path.
