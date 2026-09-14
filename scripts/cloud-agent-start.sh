#!/usr/bin/env bash
# Per-boot refresh for Cloud Agents: fast-forward this clone to origin.
#
# Cursor already checks out a revision before `install`. Environment builds do
# not re-run `install`, so this `start` hook keeps a booted pod from sitting
# on a stale SHA. Never clobber a dirty tree or an unmerged feature branch.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if [[ ! -d .git ]]; then
  echo "cloud-agent-start: not a git checkout; skip"
  exit 0
fi

if [[ -n "$(git status --porcelain)" ]]; then
  echo "cloud-agent-start: dirty working tree; skip pull"
  git status --short | head
  exit 0
fi

echo "cloud-agent-start: fetching origin..."
git fetch origin --prune

before="$(git rev-parse HEAD)"
branch="$(git rev-parse --abbrev-ref HEAD)"

if [[ "$branch" != "HEAD" ]]; then
  if git rev-parse --abbrev-ref --symbolic-full-name '@{u}' >/dev/null 2>&1; then
    echo "cloud-agent-start: fast-forward $branch from upstream"
    git pull --ff-only
  elif git rev-parse "refs/remotes/origin/$branch" >/dev/null 2>&1; then
    echo "cloud-agent-start: fast-forward $branch from origin/$branch"
    git merge --ff-only "origin/$branch"
  else
    echo "cloud-agent-start: no origin/$branch; skip pull"
  fi
elif git rev-parse refs/remotes/origin/main >/dev/null 2>&1 \
  && git merge-base --is-ancestor HEAD origin/main; then
  # Detached SHA that is already on main's history (typical boot from main).
  echo "cloud-agent-start: detached HEAD is behind origin/main; check out latest main"
  git checkout --detach origin/main
else
  echo "cloud-agent-start: detached HEAD at $(git rev-parse --short HEAD); not on origin/main; skip"
fi

after="$(git rev-parse HEAD)"
if [[ "$before" == "$after" ]]; then
  echo "cloud-agent-start: already up to date at $(git rev-parse --short HEAD)"
else
  echo "cloud-agent-start: $(git rev-parse --short "$before") -> $(git rev-parse --short "$after")"
fi
