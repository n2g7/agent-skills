#!/usr/bin/env bash
# Sync missing skills from antigravity-awesome-skills into this repo.
set -euo pipefail

SKILLS_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TAG="${1:-main}"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

echo "Cloning antigravity-awesome-skills (tag/branch: $TAG)..."
git clone --depth 1 --branch "$TAG" https://github.com/sickn33/antigravity-awesome-skills.git "$TMP" 2>/dev/null \
  || git clone --depth 1 https://github.com/sickn33/antigravity-awesome-skills.git "$TMP"

AG_SKILLS="$TMP/skills"
added=0
skipped=0

for skill_dir in "$AG_SKILLS"/*/; do
  name="$(basename "$skill_dir")"
  [[ -f "$skill_dir/SKILL.md" ]] || continue
  dest="$SKILLS_ROOT/$name"
  if [[ -d "$dest" ]]; then
    ((skipped++)) || true
    continue
  fi
  cp -R "$skill_dir" "$dest"
  ((added++)) || true
  echo "  + $name"
done

echo ""
echo "Added: $added | Already present: $skipped"
echo "Run: python3 _catalog/regenerate.py"
echo "Run: python3 scripts/ensure-lazy-load.py"
