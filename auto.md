# Cloud Agent: wire agent-skills into this project

Copy everything below the line into a **Cursor Cloud Agent** on any GitHub project repo. The agent should execute these steps in order, commit, and push.

---

## Goal

Add the public [n2g7/agent-skills](https://github.com/n2g7/agent-skills) library as a git submodule at `.agents/skills`, configure Cloud Agent install to init submodules, and verify `skill-recommender` works. Skills load **on demand only** (`disable-model-invocation: true` on every skill).

## Constants

- Skills repo (HTTPS): `https://github.com/n2g7/agent-skills.git`
- Submodule path: `.agents/skills`
- Catalog: `.agents/skills/_catalog/skills-index.json`
- Recommender: `.agents/skills/skill-recommender/SKILL.md`

## Steps

### 1. Init submodules if missing

```bash
git submodule update --init --recursive
```

### 2. Add or update the skills submodule

If `.agents/skills` does **not** exist:

```bash
mkdir -p .agents
git submodule add https://github.com/n2g7/agent-skills.git .agents/skills
```

If `.agents/skills` **already exists** (stale SSH URL or old commit):

```bash
# Fix remote to public HTTPS (Cloud Agents cannot use private SSH keys)
git config -f .gitmodules submodule..agents/skills.url https://github.com/n2g7/agent-skills.git
cd .agents/skills
git remote set-url origin https://github.com/n2g7/agent-skills.git
git fetch origin main
git checkout main
git pull origin main
cd ../..
git submodule sync --recursive
```

### 3. Configure `.cursor/environment.json`

Create `.cursor/` if needed. Merge with any existing `install` command — **submodule init must run first**.

If the file does not exist:

```json
{
  "install": "git submodule update --init --recursive"
}
```

If the file already has an `install` command, prepend submodule init:

```bash
python3 << 'PY'
import json, os
path = ".cursor/environment.json"
os.makedirs(".cursor", exist_ok=True)
data = {}
if os.path.isfile(path):
    data = json.load(open(path))
install = data.get("install", "").strip()
sub = "git submodule update --init --recursive"
if sub not in install:
    data["install"] = f"{sub} && {install}" if install else sub
    json.dump(data, open(path, "w"), indent=2)
    open(path, "a").write("\n")
    print("Updated environment.json")
else:
    print("environment.json already has submodule init")
PY
```

### 4. Add project note for agents (optional but recommended)

If the project has no `AGENTS.md`, create a short one or append:

```markdown
## Agent skills

Skills live in `.agents/skills/` (git submodule). Use `skill-recommender` to find skills.
Only read a skill's `SKILL.md` after the user explicitly asks to use that skill.
```

### 5. Verify

```bash
test -f .agents/skills/skill-recommender/SKILL.md && echo "OK recommender"
test -f .agents/skills/_catalog/skills-index.json && echo "OK catalog"
python3 -c "import json; d=json.load(open('.agents/skills/_catalog/skills-index.json')); assert d['total']>1000; print('OK', d['total'], 'skills')"
grep -q "submodule update" .cursor/environment.json && echo "OK environment.json"
```

### 6. Commit and push

```bash
git add .gitmodules .agents/skills .cursor/environment.json
# Include AGENTS.md only if you created or changed it
git status
git commit -m "Add agent-skills submodule for on-demand Cursor skills"
git push origin HEAD
```

### 7. Smoke test (after push)

Prompt the Cloud Agent:

```
Use skill-recommender: which skill should I use for [describe your actual task]?
```

**Expected:** Recommendations from `_catalog/` only. The agent must **not** bulk-read `SKILL.md` files unless you then say e.g. `Use the e2e-testing-patterns skill`.

## Updating skills later

```bash
cd .agents/skills && git pull origin main && cd ../..
git add .agents/skills
git commit -m "Bump agent-skills submodule"
git push
```

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `.agents/skills/` empty in Cloud Agent | Re-snapshot environment; confirm `install` runs `git submodule update --init --recursive` |
| Submodule URL is `git@github.com:...` | Switch to HTTPS URL (step 2) |
| Agent loads many skills at once | Remind it: recommend via `skill-recommender` first; load one `SKILL.md` only when asked |
| Repo not on GitHub | Push project to GitHub before using Cloud Agents |

## Reference repos

- Skills library: https://github.com/n2g7/agent-skills
- Example pilot project: https://github.com/n2g7/skills-pilot
