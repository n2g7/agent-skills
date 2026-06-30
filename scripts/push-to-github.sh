#!/usr/bin/env bash
# Create private GitHub repo and push agent-skills library.
# Prerequisite: gh auth login (run once)

set -euo pipefail

REPO_NAME="${1:-agent-skills}"
SKILLS_DIR="$(cd "$(dirname "$0")/.." && pwd)"

cd "$SKILLS_DIR"

if ! command -v gh >/dev/null 2>&1; then
  echo "Install GitHub CLI: brew install gh"
  exit 1
fi

if ! gh auth status >/dev/null 2>&1; then
  echo "Not logged in. Run: gh auth login"
  exit 1
fi

GITHUB_USER="$(gh api user -q .login)"
echo "GitHub user: $GITHUB_USER"

if git remote get-url origin >/dev/null 2>&1; then
  echo "Remote origin already set: $(git remote get-url origin)"
else
  gh repo create "$REPO_NAME" --public --source=. --remote=origin --push
  echo "Created and pushed: https://github.com/$GITHUB_USER/$REPO_NAME"
  exit 0
fi

git push -u origin main
echo "Pushed to: https://github.com/$GITHUB_USER/$REPO_NAME"
