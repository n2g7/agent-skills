#!/usr/bin/env bash
# Wire agent-skills submodule into a project (local or Cloud Agent).
# Usage: bash /path/to/agent-skills/scripts/setup-project-submodule.sh [PROJECT_DIR]
set -euo pipefail

SKILLS_REPO_HTTPS="${SKILLS_REPO_HTTPS:-https://github.com/n2g7/agent-skills.git}"
PROJECT_DIR="${1:-.}"
PROJECT_DIR="$(cd "$PROJECT_DIR" && pwd)"
SUB_PATH=".agents/skills"

cd "$PROJECT_DIR"
echo "=== Setup agent-skills in: $PROJECT_DIR ==="

git rev-parse --git-dir >/dev/null 2>&1 || { echo "Not a git repo: $PROJECT_DIR"; exit 1; }

mkdir -p .agents .cursor

if [ ! -d "$SUB_PATH/.git" ] && [ ! -f "$SUB_PATH/.git" ]; then
  git submodule add "$SKILLS_REPO_HTTPS" "$SUB_PATH"
else
  echo "Submodule exists — updating remote and pulling main"
  git config -f .gitmodules "submodule.$SUB_PATH.url" "$SKILLS_REPO_HTTPS"
  git submodule sync --recursive
  git -C "$SUB_PATH" remote set-url origin "$SKILLS_REPO_HTTPS"
  git submodule update --init --recursive
  git -C "$SUB_PATH" fetch origin main
  git -C "$SUB_PATH" checkout main
  git -C "$SUB_PATH" pull origin main
fi

python3 << 'PY'
import json, os
path = ".cursor/environment.json"
data = {}
if os.path.isfile(path):
    data = json.load(open(path))
install = data.get("install", "").strip()
sub = "git submodule update --init --recursive"
if sub not in install:
    data["install"] = f"{sub} && {install}" if install else sub
json.dump(data, open(path, "w"), indent=2)
open(path, "a").write("\n")
print("environment.json:", data.get("install"))
PY

test -f "$SUB_PATH/skill-recommender/SKILL.md"
test -f "$SUB_PATH/_catalog/skills-index.json"
python3 -c "import json; d=json.load(open('$SUB_PATH/_catalog/skills-index.json')); print(f\"Catalog: {d['total']} skills\")"

echo ""
echo "Done. Stage and commit:"
echo "  git add .gitmodules $SUB_PATH .cursor/environment.json"
echo "  git commit -m 'Add agent-skills submodule for on-demand Cursor skills'"
