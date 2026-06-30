# Cloud Agent Verification

Use these prompts after connecting repos in [Cursor dashboard](https://cursor.com/dashboard).

**New projects:** paste [auto.md](auto.md) into a Cloud Agent (~200 words).

## Repos

| Repo | URL | Purpose |
|------|-----|---------|
| agent-skills | https://github.com/n2g7/agent-skills | Public skills library + skill-recommender |
| skills-pilot | https://github.com/n2g7/skills-pilot | Example project with skills submodule |

## Mode A — Cloud agent on skills repo

1. Open Cursor → agent input → **Cloud**
2. Select repo: `n2g7/agent-skills`
3. Prompt:

```
Use skill-recommender: I'm building a Next.js API with Postgres. Which skills should I use?
```

**Expected:** Recommendations from `_catalog/` without executing other skills.

## Mode B — Cloud agent on pilot project (submodule)

1. Connect `n2g7/skills-pilot` in Cursor dashboard
2. Ensure environment runs: `git submodule update --init --recursive` (see `.cursor/environment.json`)
3. Re-snapshot cloud environment after submodule URL or commit changes
4. Prompt:

```
Use skill-recommender: which skill should I use for a Python CLI tool?
```

**Expected:** Agent searches catalog; empty `.agents/skills/` means submodule init failed.

## Adding skills to any project

**Cloud Agent (recommended):** paste contents of [auto.md](auto.md).

**Local script:**

```bash
bash https://raw.githubusercontent.com/n2g7/agent-skills/main/scripts/setup-project-submodule.sh /path/to/your-project
# Or from a clone:
bash ~/.agents/skills/scripts/setup-project-submodule.sh /path/to/your-project
```

**Manual:**

```bash
git submodule add https://github.com/n2g7/agent-skills.git .agents/skills
```

Add to `.cursor/environment.json`:

```json
{
  "install": "git submodule update --init --recursive"
}
```

Use **HTTPS** URLs so Cloud Agents can clone without your SSH keys.

## Sync workflow

```bash
# Update skills library
cd ~/.agents/skills && git pull

# Bump submodule in a project
cd /path/to/project/.agents/skills && git pull origin main
cd ../.. && git add .agents/skills && git commit -m "Bump agent-skills" && git push
```
