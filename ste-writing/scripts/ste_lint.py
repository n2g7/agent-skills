#!/usr/bin/env python3
"""Mechanical STE / anti-slop lint for ste-writing drafts.

Checks sentence and paragraph length, semicolons, em/en dashes, contractions,
passive voice heuristics, -ing main verbs, nominalizations, phrasal verbs,
banned words, marketing adjectives, and modal hedges.

Does not claim full ASD-STE100 compliance.

Usage:
  python3 ste_lint.py [--mode strict|flavored] [--json] [file ...]
  cat draft.txt | python3 ste_lint.py --mode strict
  python3 ste_lint.py --json docs/*.md

Exit code 0 if clean, 1 if any finding, 2 on usage/IO error.
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys
from pathlib import Path

MARKETING = [
    "seamless",
    "seamlessly",
    "robust",
    "powerful",
    "cutting-edge",
    "effortless",
    "effortlessly",
    "world-class",
    "next-generation",
    "revolutionary",
    "blazing",
    "lightning-fast",
    "elegant",
    "delightful",
    "turnkey",
    "best-in-class",
    "state-of-the-art",
    "game-changing",
    "first-class",
    "battle-tested",
    "enterprise-grade",
    "supercharge",
    "unlock",
    "unleash",
    "empower",
    "empowers",
]

BANNED = [
    "begin",
    "begins",
    "commence",
    "commences",
    "initiate",
    "initiates",
    "originate",
    "utilize",
    "utilizes",
    "utilizing",
    "leverage",
    "leverages",
    "leveraging",
    "facilitate",
    "facilitates",
    "ensure",
    "ensures",
    "ensuring",
    "prior to",
    "subsequent to",
    "obtain",
    "obtains",
    "acquire",
    "acquires",
    "demonstrate",
    "demonstrates",
    "additionally",
    "furthermore",
    "moreover",
    "comprehensive",
    "comprehensively",
    "utilization",
    "aforementioned",
    "henceforth",
    "therein",
    "whilst",
    "amongst",
    "numerous",
    "myriad",
    "plethora",
    "in order to",
    "a variety of",
    "in the event that",
    "due to the fact that",
    "it is important to note",
]

PHRASAL = [
    "spin up",
    "spin down",
    "reach out",
    "dive into",
    "dives into",
    "diving into",
    "kick off",
    "kicks off",
    "roll out",
    "rolls out",
    "tear down",
    "ramp up",
    "circle back",
    "drill down",
    "spun up",
    "reaching out",
]

MODAL_HEDGE = [
    "it is important to note",
    "it should be noted",
    "it is worth noting",
    "please note that",
    "as mentioned",
    "as noted above",
]

BE = r"(?:am|is|are|was|were|be|been|being)"
PP_IRREG = (
    r"(?:done|made|sent|read|built|kept|held|set|put|run|written|shown|"
    r"given|taken|found|got|gotten|seen|known|thrown|drawn)"
)


def strip_code(t: str) -> str:
    t = re.sub(r"```.*?```", " ", t, flags=re.S)
    t = re.sub(r"`[^`]*`", " ", t)
    return t


def sentences(text: str) -> list[str]:
    out: list[str] = []
    for line in text.split("\n"):
        s = line.strip()
        if not s:
            continue
        s = re.sub(r"^\s*#{1,6}\s*", "", s)
        s = re.sub(r"^\s*(?:[-*+]|\d+[.)])\s+", "", s)
        if not s:
            continue
        parts = re.split(r"(?<=[.!?:])\s+(?=[A-Z0-9\"'\-])", s)
        for p in parts:
            p = p.strip()
            if p:
                out.append(p)
    return out


def wc(s: str) -> int:
    return len([w for w in re.findall(r"[A-Za-z0-9][A-Za-z0-9'\-/]*", s)])


def count_ci(text: str, phrases: list[str]) -> tuple[int, list[str]]:
    n = 0
    hits: list[str] = []
    low = text.lower()
    # Longer phrases first so "it is important to note" wins over shorter overlaps
    for ph in sorted(phrases, key=len, reverse=True):
        for m in re.finditer(r"(?<![a-z])" + re.escape(ph) + r"(?![a-z])", low):
            n += 1
            hits.append(ph)
    return n, hits


def lint(text: str, mode: str = "flavored") -> dict:
    raw = text
    prose = strip_code(text)
    sents = sentences(prose)
    words = sum(wc(s) for s in sents) or 1
    max_words = 20 if mode == "strict" else 25

    v: dict[str, int] = {}
    longs = [(wc(s), s) for s in sents if wc(s) > max_words]
    v[f"long_sentence(>{max_words}w)"] = len(longs)
    v["semicolon"] = prose.count(";")
    v["contraction"] = len(re.findall(r"\b\w+['’](?:t|re|ve|ll|d|s|m)\b", prose))
    v["passive_voice"] = len(
        re.findall(rf"\b{BE}\s+(?:\w+ed|{PP_IRREG})\b", prose, re.I)
    )
    v["ing_main_verb"] = len(re.findall(rf"\b{BE}\s+\w+ing\b", prose, re.I))
    v["nominalization"] = len(
        re.findall(
            r"\b(?:perform(?:s|ed)?|conduct(?:s|ed)?|provide(?:s|d)?|"
            r"carry out|carries out|make use of|makes use of)\b",
            prose,
            re.I,
        )
    ) + len(re.findall(r"\b\w{4,}(?:tion|ment|ance|ence)\s+of\b", prose, re.I))
    v["phrasal_verb"], _ = count_ci(prose, PHRASAL)
    v["banned_word"], bh = count_ci(prose, BANNED)
    v["marketing_adjective"], mh = count_ci(prose, MARKETING)
    v["modal_hedge"], _ = count_ci(prose, MODAL_HEDGE)
    paras = [p for p in re.split(r"\n\s*\n", raw) if p.strip()]
    v["long_paragraph(>6s)"] = sum(
        1 for p in paras if len(sentences(strip_code(p))) > 6
    )
    em = raw.count("—") + raw.count("–")
    total = sum(v.values()) + em
    per100 = {k: round(x * 100.0 / words, 2) for k, x in v.items()}

    findings: list[str] = []
    if v["semicolon"]:
        findings.append(f"semicolon: {v['semicolon']} (replace with a period)")
    if em:
        findings.append(f"em/en dash: {em} (replace with a period or rephrase)")
    if v["contraction"]:
        findings.append(f"contraction: {v['contraction']}")
    if v["passive_voice"]:
        findings.append(f"passive_voice (heuristic): {v['passive_voice']}")
    if v["ing_main_verb"]:
        findings.append(f"ing_main_verb (be + -ing): {v['ing_main_verb']}")
    if v["nominalization"]:
        findings.append(f"nominalization: {v['nominalization']}")
    if v["phrasal_verb"]:
        findings.append(f"phrasal_verb: {v['phrasal_verb']}")
    if v["banned_word"]:
        samples = ", ".join(list(dict.fromkeys(bh))[:6])
        findings.append(f"banned_word: {v['banned_word']} ({samples})")
    if v["marketing_adjective"]:
        samples = ", ".join(list(dict.fromkeys(mh))[:6])
        findings.append(f"marketing_adjective: {v['marketing_adjective']} ({samples})")
    if v["modal_hedge"]:
        findings.append(f"modal_hedge: {v['modal_hedge']}")
    if v["long_paragraph(>6s)"]:
        findings.append(f"long_paragraph(>6s): {v['long_paragraph(>6s)']}")
    for n, s in sorted(longs, key=lambda x: -x[0])[:8]:
        snippet = s if len(s) <= 80 else s[:80] + "…"
        findings.append(f"long_sentence: {n}w (max {max_words}) — {snippet}")

    return {
        "mode": mode,
        "words": words,
        "sentences": len(sents),
        "violations": v,
        "total": total,
        "total_per100w": round(total * 100.0 / words, 2),
        "em_dash(slop-marker)": em,
        "longest_sentence_words": (
            max(longs)[0] if longs else max((wc(s) for s in sents), default=0)
        ),
        "sample_marketing": list(dict.fromkeys(mh))[:6],
        "sample_banned": list(dict.fromkeys(bh))[:6],
        "findings": findings,
        "ok": total == 0,
    }


def expand_files(patterns: list[str]) -> list[str]:
    out: list[str] = []
    for f in patterns:
        if any(c in f for c in "*?["):
            out.extend(sorted(glob.glob(f)))
        else:
            out.append(f)
    return out


def print_human(path: str | None, result: dict) -> None:
    label = os.path.basename(path) if path else "stdin"
    status = "OK" if result["ok"] else "FAIL"
    print(
        f"{status} ({result['mode']}) {label:32} "
        f"words={result['words']:4d} total={result['total']:3d} "
        f"per100w={result['total_per100w']:6.2f} "
        f"em_dash={result['em_dash(slop-marker)']:2d}"
    )
    for f in result["findings"]:
        print(f"  - {f}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Mechanical STE lint for ste-writing")
    parser.add_argument(
        "files",
        nargs="*",
        help="Files or globs to lint (default: stdin)",
    )
    parser.add_argument(
        "--mode",
        choices=("strict", "flavored"),
        default="flavored",
        help="strict: 20-word cap; flavored: 25-word cap (default)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print full JSON report",
    )
    args = parser.parse_args()

    paths = expand_files(args.files) if args.files else []
    results: list[tuple[str | None, dict]] = []

    try:
        if not paths:
            text = sys.stdin.read()
            if not text.strip():
                print("error: empty input", file=sys.stderr)
                return 2
            results.append((None, lint(text, args.mode)))
        else:
            for path in paths:
                text = Path(path).read_text(encoding="utf-8")
                results.append((path, lint(text, args.mode)))
    except OSError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2

    if args.json:
        if len(results) == 1:
            print(json.dumps(results[0][1], indent=2))
        else:
            payload = {path or "stdin": r for path, r in results}
            print(json.dumps(payload, indent=2))
    else:
        for path, r in results:
            print_human(path, r)

    return 0 if all(r["ok"] for _, r in results) else 1


if __name__ == "__main__":
    sys.exit(main())
