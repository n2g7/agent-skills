#!/usr/bin/env bash
# Static SkillSpector scan of this skills library (per-skill; --no-llm).
#
# Usage:
#   scripts/scan-skillspector.sh              # same as: static
#   scripts/scan-skillspector.sh static
#   scripts/scan-skillspector.sh static --workers 16
#   scripts/scan-skillspector.sh static --offline
#   scripts/scan-skillspector.sh static --limit 20   # debug
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

export PATH="${HOME}/.local/bin:${PATH}"

cmd="${1:-static}"
if [[ $# -gt 0 ]]; then
  shift
fi

case "$cmd" in
  static|"")
    exec python3 "$ROOT/scripts/skillspector_batch_scan.py" --root "$ROOT" "$@"
    ;;
  -h|--help|help)
    sed -n '1,12p' "$0"
    exit 0
    ;;
  *)
    echo "Unknown command: $cmd (expected: static)" >&2
    exit 1
    ;;
esac
