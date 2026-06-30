Wire this repo to my public skills library: https://github.com/n2g7/agent-skills.git

Add or refresh a git submodule at `.agents/skills` using that **HTTPS** URL on `main` (not SSH). Update `.cursor/environment.json` so `install` runs `git submodule update --init --recursive` first — prepend it if other install steps already exist.

Verify `.agents/skills/skill-recommender/SKILL.md` and `.agents/skills/_catalog/skills-index.json` exist. Commit and push `.gitmodules`, `.agents/skills`, and `.cursor/environment.json`.

Skills load on demand only (`disable-model-invocation: true` on every skill). Do not bulk-read SKILL.md files. Use `skill-recommender` to search `_catalog/` and recommend IDs; open a skill's SKILL.md only when I explicitly ask to use it.

Reply with submodule commit, skill count, and whether environment.json was created or updated.

Example pilot: https://github.com/n2g7/skills-pilot
