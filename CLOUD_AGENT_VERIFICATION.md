# Cloud Agent Verification

Use these prompts after connecting repos in [Cursor dashboard](https://cursor.com/dashboard).

## Repos

| Repo | URL | Purpose |
|------|-----|---------|
| agent-skills | https://github.com/n2g7/agent-skills | Full skills library + skill-recommender |
| skills-pilot | https://github.com/n2g7/skills-pilot | Example project with skills submodule |

## Mode A — Cloud agent on skills repo

1. Open Cursor → agent input → **Cloud**
2. Select repo: `n2g7/agent-skills`
3. Prompt:

```
Use skill-recommender: I'm building a Next.js API with Postgres. Which skills should I use?
```

**Expected:** Recommendations from `_catalog/` without executing other skills.

**Local simulation passed:** Fresh clone contains 1,432 skills, `skill-recommender`, and portable catalog paths.

## Mode B — Cloud agent on pilot project (submodule)

1. Connect `n2g7/skills-pilot` in Cursor dashboard
2. Ensure environment runs: `git submodule update --init --recursive` (see `.cursor/environment.json`)
3. Re-snapshot cloud environment after first submodule add
4. Prompt:

```
List skills under .agents/skills/ and use skill-recommender: which skill should I use for a Python CLI tool?
```

**Expected:** Agent sees submodule contents; empty `.agents/skills/` means submodule init failed.

**Local verification passed:** Pilot has `.gitmodules`, `environment.json`, and populated `.agents/skills/`.

## Adding skills to your own projects

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

Merge with existing install steps if your project has dependencies.

## Sync workflow

```bash
# Update skills library
cd ~/.agents/skills && git pull

# Bump submodule in a project
cd /path/to/project/.agents/skills && git pull origin main
cd ../.. && git add .agents/skills && git commit -m "Bump agent-skills" && git push
```
