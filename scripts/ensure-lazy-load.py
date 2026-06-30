#!/usr/bin/env python3
"""Ensure every SKILL.md has disable-model-invocation: true (on-demand loading only)."""

import os
import re
import sys

SKILLS_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".git", "_catalog", "scripts", "node_modules", ".venv", "venv"}

LAZY_FLAG = "disable-model-invocation: true"
META_DIRS = {"_catalog", "scripts"}


def ensure_lazy(path: str) -> bool:
    with open(path, encoding="utf-8") as f:
        content = f.read()
    if LAZY_FLAG in content:
        return False
    m = re.match(r"^---\s*\n", content)
    if not m:
        new = f"---\n{LAZY_FLAG}\n---\n\n{content}"
        with open(path, "w", encoding="utf-8") as f:
            f.write(new)
        return True
    # Insert after opening ---
    new = re.sub(r"^(---\s*\n)", rf"\1{LAZY_FLAG}\n", content, count=1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new)
    return True


def main() -> int:
    updated = 0
    for root, dirs, files in os.walk(SKILLS_ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
        if "SKILL.md" in files:
            rel = os.path.relpath(root, SKILLS_ROOT).split(os.sep)[0]
            if rel in META_DIRS:
                continue
            if ensure_lazy(os.path.join(root, "SKILL.md")):
                updated += 1
                print(f"  + {os.path.relpath(root, SKILLS_ROOT)}")
    print(f"\nUpdated {updated} skill(s) with {LAZY_FLAG}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
