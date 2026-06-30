# Agent Skills Library

Personal Cursor Agent Skills library — 1,400+ skills with catalog and skill recommender.

## Local install

```bash
git clone git@github.com:n2g7/agent-skills.git ~/.agents/skills
```

## Cloud Agents

### Run recommendations on this repo

Start a Cloud Agent on this repository and prompt:

```
Use skill-recommender: which skill should I use for [your task]?
```

### Use skills in other projects (submodule)

```bash
cd /path/to/your-project
git submodule add git@github.com:n2g7/agent-skills.git .agents/skills
```

Add to `.cursor/environment.json`:

```json
{
  "install": "git submodule update --init --recursive"
}
```

Merge with your project's existing `install` steps if needed.

## Catalog

| File | Purpose |
|------|---------|
| `_catalog/README.md` | Category overview and decision guide |
| `_catalog/top-skills.md` | Best-documented skills per category |
| `_catalog/skills-index.json` | Machine-readable index |
| `skill-recommender/SKILL.md` | Recommends skills without executing them |

## Maintenance

Regenerate catalog after adding skills:

```bash
python3 _catalog/regenerate.py
```

Then commit and push.

## Invoke recommender

Attach `@skill-recommender` or type:

```
Use skill-recommender: which skill for [task]?
```
