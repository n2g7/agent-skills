#!/usr/bin/env bash
# Verify pilot project submodule setup for cloud agents.
set -euo pipefail

PILOT_DIR="${1:-$HOME/.agents/skills-pilot}"

if [ ! -d "$PILOT_DIR" ]; then
  echo "Pilot dir not found: $PILOT_DIR"
  exit 1
fi

cd "$PILOT_DIR"
echo "=== Pilot project verification: $PILOT_DIR ==="
FAIL=0

check() {
  if eval "$2" >/dev/null 2>&1; then
    echo "OK  $1"
  else
    echo "FAIL $1"
    FAIL=1
  fi
}

check "Git repo" "test -d .git"
check ".gitmodules exists" "test -f .gitmodules"
check "environment.json exists" "test -f .cursor/environment.json"
check "submodule skill-recommender" "test -f .agents/skills/skill-recommender/SKILL.md"
check "submodule catalog" "test -f .agents/skills/_catalog/skills-index.json"
check "submodule HTTPS URL" "grep -q 'https://github.com/n2g7/agent-skills.git' .gitmodules"

echo ""
echo "environment.json install command:"
python3 -c "import json; print(json.load(open('.cursor/environment.json')).get('install',''))"

echo ""
grep "submodule update" .cursor/environment.json >/dev/null && echo "OK  submodule init in environment.json" || { echo "FAIL missing submodule init"; FAIL=1; }

if [ "$FAIL" -eq 0 ]; then
  echo ""
  echo "Pilot ready for Cloud Agents (public HTTPS submodule)."
else
  exit 1
fi
