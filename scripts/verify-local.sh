#!/usr/bin/env bash
# Verify skills library is ready for local Cursor and cloud agents.
set -euo pipefail

SKILLS_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$SKILLS_DIR"

echo "=== Skills library verification ==="
FAIL=0

check() {
  if eval "$2" >/dev/null 2>&1; then
    echo "OK  $1"
  else
    echo "FAIL $1"
    FAIL=1
  fi
}

check "Git repo initialized" "test -d .git"
check "skill-recommender exists" "test -f skill-recommender/SKILL.md"
check "Catalog JSON exists" "test -f _catalog/skills-index.json"
check "Catalog has skills" "python3 -c \"import json; d=json.load(open('_catalog/skills-index.json')); assert d['total']>1000\""

SKILL_COUNT=$(find . -name SKILL.md -not -path './.git/*' | wc -l | tr -d ' ')
echo "    SKILL.md count: $SKILL_COUNT"

echo ""
echo "=== skill-recommender search test ==="
python3 -c "
import json
data = json.load(open('_catalog/skills-index.json'))
matches = [s for s in data['skills'] if 'playwright' in f\"{s['id']} {s['description']}\".lower()]
print(f'playwright matches: {len(matches)}')
for s in matches[:3]:
    print(f'  - {s[\"id\"]}')
assert len(matches) > 0
"

echo ""
echo "=== Portable path check ==="
grep -q "Project submodule" skill-recommender/SKILL.md && echo "OK  skill-recommender has portable paths" || { echo "FAIL portable paths"; FAIL=1; }

if git remote get-url origin >/dev/null 2>&1; then
  echo ""
  echo "Remote: $(git remote get-url origin)"
  if git ls-remote origin main >/dev/null 2>&1; then
    echo "OK  GitHub remote reachable"
  else
    echo "WARN GitHub remote not reachable (run: gh auth login && ./scripts/push-to-github.sh)"
  fi
else
  echo ""
  echo "WARN No git remote — run: gh auth login && ./scripts/push-to-github.sh"
fi

echo ""
if [ "$FAIL" -eq 0 ]; then
  echo "All local checks passed."
else
  echo "Some checks failed."
  exit 1
fi
