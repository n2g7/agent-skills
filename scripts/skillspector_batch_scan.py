#!/usr/bin/env python3
"""Parallel static SkillSpector scan across this skills library.

SkillSpector's --recursive mode caps multi-skill detection at 1024 directories,
so this library (~1600+ skills) must be scanned per-skill.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

SKIP_DIR_NAMES = {
    ".git",
    ".cursor",
    ".github",
    "_catalog",
    "_security",
    "scripts",
    "node_modules",
    "__pycache__",
    ".venv",
    "venv",
}

SEVERITY_RANK = {
    "CRITICAL": 5,
    "HIGH": 4,
    "MEDIUM": 3,
    "LOW": 2,
    "INFO": 1,
    "NONE": 0,
}


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def discover_skills(root: Path) -> list[Path]:
    skills: list[Path] = []
    for child in sorted(root.iterdir()):
        if not child.is_dir() or child.name in SKIP_DIR_NAMES or child.name.startswith("."):
            continue
        if (child / "SKILL.md").is_file():
            skills.append(child)
    return skills


def find_skillspector() -> str:
    env = os.environ.get("SKILLSPECTOR_BIN")
    if env and Path(env).is_file():
        return env
    from shutil import which

    found = which("skillspector")
    if found:
        return found
    candidate = Path.home() / ".local" / "bin" / "skillspector"
    if candidate.is_file():
        return str(candidate)
    raise SystemExit("skillspector not found on PATH (install: uv tool install git+https://github.com/NVIDIA/skillspector.git)")


def scan_one(
    skillspector: str,
    skill_dir: Path,
    out_dir: Path,
    offline: bool,
) -> dict:
    skill_id = skill_dir.name
    out_path = out_dir / f"{skill_id}.json"
    cmd = [
        skillspector,
        "scan",
        str(skill_dir),
        "--no-llm",
        "--format",
        "json",
        "--output",
        str(out_path),
    ]
    env = os.environ.copy()
    env.setdefault("SKILLSPECTOR_LOG_LEVEL", "ERROR")
    if offline:
        env["SKILLSPECTOR_OFFLINE"] = "1"

    started = time.time()
    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            env=env,
            timeout=600,
        )
        elapsed = time.time() - started
        report = None
        if out_path.is_file():
            try:
                report = json.loads(out_path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                report = None

        ra = (report or {}).get("risk_assessment") or {}
        issues = (report or {}).get("issues") or []
        # SkillSpector may exit non-zero on high risk; a parsed report counts as success.
        return {
            "skill_id": skill_id,
            "path": skill_id,
            "ok": report is not None,
            "returncode": proc.returncode,
            "elapsed_sec": round(elapsed, 3),
            "score": ra.get("score"),
            "severity": ra.get("severity"),
            "recommendation": ra.get("recommendation"),
            "max_issue_severity": ra.get("max_issue_severity"),
            "issue_count": len(issues),
            "top_rules": _top_rules(issues),
            "stderr_tail": (proc.stderr or "")[-500:],
            "report_file": str(out_path.relative_to(repo_root())) if out_path.is_file() else None,
        }
    except subprocess.TimeoutExpired:
        return {
            "skill_id": skill_id,
            "path": skill_id,
            "ok": False,
            "returncode": -1,
            "elapsed_sec": 600,
            "score": None,
            "severity": None,
            "recommendation": None,
            "max_issue_severity": None,
            "issue_count": 0,
            "top_rules": [],
            "stderr_tail": "timeout after 600s",
            "report_file": None,
        }


def _top_rules(issues: list[dict], limit: int = 5) -> list[str]:
    counts: dict[str, int] = {}
    for issue in issues:
        rid = issue.get("id") or "UNKNOWN"
        counts[rid] = counts.get(rid, 0) + 1
    ranked = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    return [f"{rid}×{n}" if n > 1 else rid for rid, n in ranked[:limit]]


def write_outputs(out_root: Path, results: list[dict], meta: dict) -> None:
    out_root.mkdir(parents=True, exist_ok=True)

    combined = {
        "meta": meta,
        "results": results,
    }
    (out_root / "static-report.json").write_text(
        json.dumps(combined, indent=2, sort_keys=False) + "\n",
        encoding="utf-8",
    )

    ranked = sorted(
        results,
        key=lambda r: (
            -(r.get("score") if isinstance(r.get("score"), (int, float)) else -1),
            -SEVERITY_RANK.get(str(r.get("severity") or "NONE").upper(), 0),
            r.get("skill_id") or "",
        ),
    )

    high_critical = [
        r
        for r in ranked
        if str(r.get("severity") or "").upper() in {"HIGH", "CRITICAL"}
    ]

    lines = [
        "# SkillSpector static scan summary",
        "",
        f"- Scanned at: `{meta['scanned_at']}`",
        f"- Skillspector: `{meta.get('skillspector_version', 'unknown')}`",
        f"- Mode: static (`--no-llm`)",
        f"- Skills discovered: **{meta['discovered']}**",
        f"- Scanned OK: **{meta['ok']}** / failed: **{meta['failed']}**",
        f"- Workers: **{meta['workers']}**",
        f"- Duration: **{meta['duration_sec']}s**",
        f"- High/Critical (by SkillSpector severity): **{len(high_critical)}**",
        "",
        "## Severity counts",
        "",
    ]
    sev_counts: dict[str, int] = {}
    for r in results:
        sev = str(r.get("severity") or "UNKNOWN").upper()
        sev_counts[sev] = sev_counts.get(sev, 0) + 1
    for sev in ("CRITICAL", "HIGH", "MEDIUM", "LOW", "INFO", "NONE", "UNKNOWN"):
        if sev in sev_counts:
            lines.append(f"- {sev}: {sev_counts[sev]}")
    for sev, n in sorted(sev_counts.items()):
        if sev not in {"CRITICAL", "HIGH", "MEDIUM", "LOW", "INFO", "NONE", "UNKNOWN"}:
            lines.append(f"- {sev}: {n}")

    lines += [
        "",
        "## Ranked skills (highest risk first)",
        "",
        "| Score | Severity | Rec | Issues | Skill | Top rules |",
        "|------:|----------|-----|-------:|-------|-----------|",
    ]
    for r in ranked:
        score = r.get("score")
        score_s = str(score) if score is not None else "—"
        sev = r.get("severity") or "—"
        rec = r.get("recommendation") or "—"
        issues = r.get("issue_count") or 0
        skill = r.get("skill_id") or "?"
        rules = ", ".join(r.get("top_rules") or []) or "—"
        flag = "" if r.get("ok") else " *(scan failed)*"
        lines.append(
            f"| {score_s} | {sev} | {rec} | {issues} | `{skill}`{flag} | {rules} |"
        )

    if high_critical:
        lines += ["", "## High / Critical skills", ""]
        for r in high_critical:
            lines.append(
                f"- `{r['skill_id']}` — score={r.get('score')}, "
                f"severity={r.get('severity')}, max_issue={r.get('max_issue_severity')}, "
                f"rules={', '.join(r.get('top_rules') or []) or '—'}"
            )

    failed = [r for r in results if not r.get("ok")]
    if failed:
        lines += ["", "## Failed scans", ""]
        for r in failed:
            lines.append(f"- `{r['skill_id']}` rc={r.get('returncode')}: {r.get('stderr_tail')}")

    (out_root / "static-summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    (out_root / "high-critical.txt").write_text(
        "\n".join(r["path"] for r in high_critical) + ("\n" if high_critical else ""),
        encoding="utf-8",
    )


def skillspector_version(skillspector: str) -> str:
    try:
        proc = subprocess.run(
            [skillspector, "--version"],
            capture_output=True,
            text=True,
            timeout=30,
        )
        for line in (proc.stdout or proc.stderr or "").splitlines():
            if "SkillSpector" in line or line.strip().startswith("v"):
                return line.strip()
        return (proc.stdout or "").strip() or "unknown"
    except Exception:
        return "unknown"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=repo_root(),
        help="Skills library root (default: repo root)",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Output directory (default: <root>/_security/skillspector)",
    )
    parser.add_argument("--workers", type=int, default=12)
    parser.add_argument("--offline", action="store_true", help="Hint offline/static mode to SkillSpector")
    parser.add_argument("--limit", type=int, default=0, help="Scan only first N skills (debug)")
    args = parser.parse_args()

    root = args.root.resolve()
    out_root = (args.out or (root / "_security" / "skillspector")).resolve()
    per_skill = out_root / "per-skill"
    per_skill.mkdir(parents=True, exist_ok=True)

    skillspector = find_skillspector()
    skills = discover_skills(root)
    if args.limit and args.limit > 0:
        skills = skills[: args.limit]

    if not skills:
        print("No skills discovered.", file=sys.stderr)
        return 1

    print(f"Scanning {len(skills)} skills with {args.workers} workers via {skillspector}")
    started = time.time()
    results: list[dict] = []

    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        futures = {
            pool.submit(scan_one, skillspector, skill, per_skill, args.offline): skill
            for skill in skills
        }
        done = 0
        for fut in as_completed(futures):
            result = fut.result()
            results.append(result)
            done += 1
            if done % 50 == 0 or done == len(skills):
                print(f"  progress {done}/{len(skills)}", flush=True)

    duration = round(time.time() - started, 1)
    ok = sum(1 for r in results if r.get("ok"))
    meta = {
        "scanned_at": datetime.now(timezone.utc).isoformat(),
        "root": str(root),
        "discovered": len(skills),
        "ok": ok,
        "failed": len(skills) - ok,
        "workers": args.workers,
        "duration_sec": duration,
        "mode": "static --no-llm",
        "skillspector_bin": skillspector,
        "skillspector_version": skillspector_version(skillspector),
        "offline": bool(args.offline),
    }
    write_outputs(out_root, results, meta)
    print(f"Done in {duration}s — ok={ok} failed={len(skills)-ok}")
    print(f"Wrote {out_root / 'static-report.json'}")
    print(f"Wrote {out_root / 'static-summary.md'}")
    print(f"Wrote {out_root / 'high-critical.txt'}")
    return 0 if ok == len(skills) else 2


if __name__ == "__main__":
    raise SystemExit(main())
