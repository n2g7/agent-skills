# Agent instructions for this skills library

## On-demand loading only

This repository contains **1,700+ skills**. Do **not** read skill files in bulk.

1. **Recommend first** — Use `skill-recommender` when the user asks which skill fits a task.
2. **Load one skill at a time** — Only open `<skill-id>/SKILL.md` after the user explicitly asks to use that skill (e.g. "use the `e2e-testing-patterns` skill" or `@e2e-testing-patterns`).
3. **Never preload** — Do not read multiple `SKILL.md` files "just in case." Search `_catalog/skills-index.json` or `_catalog/keyword-index.json` instead.
4. **Respect `disable-model-invocation`** — Every skill in this repo sets this flag. Skills are opt-in, not ambient context.

## Skill library paths

Resolve skills from the first path that exists:

| Layout | Skills root | Catalog |
|--------|-------------|---------|
| Standalone clone | `<repo>/` | `_catalog/` |
| Global install | `~/.agents/skills/` | `~/.agents/skills/_catalog/` |
| Project submodule | `.agents/skills/` | `.agents/skills/_catalog/` |

## Maintenance

```bash
bash scripts/sync-from-antigravity.sh    # pull new upstream skills
python3 scripts/ensure-lazy-load.py    # enforce on-demand loading
python3 _catalog/regenerate.py         # refresh catalog
```
