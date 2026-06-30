# Agent Skills — cloud-ready Antigravity snapshot

My curated, **cloud-ready**, **recommendation-enhanced** snapshot of the [Antigravity Awesome Skills](https://github.com/sickn33/antigravity-awesome-skills) library.

**Huge thanks** to [sickn33](https://github.com/sickn33) and everyone behind Antigravity Awesome Skills — this repo would not exist without that project. I sync from upstream periodically and add my own catalog, recommender, and Cloud Agent wiring on top.

| | |
|---|---|
| **Skills** | 1,700+ `SKILL.md` playbooks |
| **Upstream** | [antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) (MIT) |
| **License** | [MIT](LICENSE) (includes upstream attribution) |
| **On-demand loading** | Every skill uses `disable-model-invocation: true` — loaded only when you explicitly invoke one |

## Why this repo exists

- **Cloud Agents** — Public repo so Cursor Cloud Agents can clone it (private repos are often out of scope).
- **Submodule-friendly** — Drop into any project at `.agents/skills/`.
- **Find skills without loading 1,700 files** — `skill-recommender` + `_catalog/` index search by keyword/category.
- **Lazy by design** — Agents should recommend first, then read a single `SKILL.md` only after you ask.

See [AGENTS.md](AGENTS.md) for agent behavior in this repo.

## Install

### Global (local Cursor)

```bash
git clone https://github.com/n2g7/agent-skills.git ~/.agents/skills
```

### Project submodule (local + Cloud Agents)

```bash
cd /path/to/your-project
git submodule add https://github.com/n2g7/agent-skills.git .agents/skills
```

Add to `.cursor/environment.json` (merge with your existing `install` if needed):

```json
{
  "install": "git submodule update --init --recursive"
}
```

## Usage

### New project setup (Cloud Agent)

Paste [auto.md](auto.md) into a Cursor Cloud Agent on any project (~200 words).

### Find a skill (does not load skill content)

```
Use skill-recommender: which skill should I use for [your task]?
```

Or attach `@skill-recommender`.

### Use a specific skill (loads that skill only)

```
Use the `e2e-testing-patterns` skill to ...
```

## Catalog

| File | Purpose |
|------|---------|
| `_catalog/README.md` | Category overview |
| `_catalog/skills-index.json` | Machine-readable index |
| `_catalog/keyword-index.json` | Keyword → skill ID |
| `skill-recommender/SKILL.md` | Recommends skills without executing them |

Regenerate after adding skills:

```bash
python3 _catalog/regenerate.py
```

## Sync from upstream Antigravity

```bash
bash scripts/sync-from-antigravity.sh
python3 scripts/ensure-lazy-load.py
python3 _catalog/regenerate.py
```

## Credits

- **[Antigravity Awesome Skills](https://github.com/sickn33/antigravity-awesome-skills)** — source library (MIT). Install upstream directly with `npx antigravity-awesome-skills` if you want their npm installer and plugin bundles.
- **This repo** — snapshot + `_catalog/`, `skill-recommender`, lazy-load enforcement, Cloud Agent submodule docs.

Thank you to the Antigravity community for building and maintaining an incredible open skill library.
