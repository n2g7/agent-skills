#!/usr/bin/env python3
"""Regenerate the skills catalog from all SKILL.md files in ~/.agents/skills/."""

import os
import re
import json
import sys
from collections import defaultdict

SKILLS_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATALOG_DIR = os.path.join(SKILLS_ROOT, "_catalog")


def parse_frontmatter(content):
    m = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not m:
        return None, None
    fm = m.group(1)
    name = desc = None
    desc_lines, in_desc = [], False
    for line in fm.split("\n"):
        if line.startswith("name:"):
            name = line.split(":", 1)[1].strip().strip('"').strip("'")
            in_desc = False
        elif line.startswith("description:"):
            val = line.split(":", 1)[1].strip()
            if val in (">", "|"):
                in_desc, desc_lines = True, []
            elif val:
                desc, in_desc = val.strip('"').strip("'"), False
            else:
                in_desc, desc_lines = True, []
        elif in_desc:
            if line and not line[0].isspace() and ":" in line:
                in_desc = False
            else:
                desc_lines.append(line.strip())
    if desc_lines and not desc:
        desc = " ".join(desc_lines)
    return name, desc


def categorize(skill_id, name, desc):
    text = f"{skill_id} {name or ''} {desc or ''}".lower()
    rules = [
        ("Azure", [r"\bazure[-_]"]),
        ("AWS", [r"\baws[-_]", r"\bamazon\b"]),
        ("Google Cloud", [r"\bgcp\b", r"\bgoogle[-_]cloud", r"\bfirebase\b"]),
        ("Cloudflare", [r"\bcloudflare\b", r"\bwrangler\b", r"\bdurable[-_]object"]),
        ("DevOps & CI/CD", [r"\bdevops\b", r"\bci[-_/]cd\b", r"\bterraform\b", r"\bkubernetes\b", r"\bdocker\b", r"\bdeploy\b"]),
        ("Security & Pentesting", [r"\bsecurity\b", r"\bpenetration\b", r"\bpentest\b", r"\bxss\b", r"\bburp\b", r"\bowasp\b", r"\bpci\b"]),
        ("SEO & Marketing", [r"\bseo\b", r"\bmarketing\b", r"\bemail[-_]sequence\b", r"\bbrand\b", r"\bcopywriting\b"]),
        ("Automation & Integrations", [r"\bautomation\b", r"\bn8n\b", r"\bmcp\b", r"\bintegration\b"]),
        ("Database", [r"\bdatabase\b", r"\bpostgres\b", r"\bmysql\b", r"\bsupabase\b", r"\bmigration\b", r"\bsql\b"]),
        ("Frontend & UI", [r"\breact\b", r"\bvue\b", r"\btailwind\b", r"\bfrontend\b", r"\bthreejs\b", r"\bshader\b"]),
        ("Mobile", [r"\bexpo\b", r"\bflutter\b", r"\bios\b", r"\bswiftui\b", r"\bmobile\b"]),
        ("Backend & API", [r"\bbackend\b", r"\bapi\b", r"\bgraphql\b", r"\bgrpc\b", r"\bdjango\b", r"\blaravel\b"]),
        ("Languages: Python", [r"\bpython\b", r"[-_]py\b"]),
        ("Languages: TypeScript/JavaScript", [r"\btypescript\b", r"\bjavascript\b", r"[-_]ts\b", r"[-_]js\b"]),
        ("Languages: Go", [r"\bgolang\b", r"[-_]go\b"]),
        ("Languages: Rust", [r"\brust\b", r"[-_]rs\b"]),
        ("Languages: C#/.NET", [r"\bdotnet\b", r"[-_]dotnet\b"]),
        ("Languages: Java/Kotlin", [r"\bjava\b", r"\bkotlin\b"]),
        ("AI & LLM", [r"\bllm\b", r"\blangchain\b", r"\bagent\b", r"\brag\b", r"\bhugging[-_]face\b"]),
        ("Testing & QA", [r"\btest\b", r"\btdd\b", r"\be2e\b", r"\bplaywright\b"]),
        ("Git & Version Control", [r"\bgit\b", r"\bcommit\b", r"\bpull[-_]request\b"]),
        ("Observability & Monitoring", [r"\bobservability\b", r"\bmonitoring\b", r"\bopentelemetry\b", r"\bslo\b"]),
        ("Architecture & Design Patterns", [r"\barchitecture\b", r"\bcqrs\b", r"\bddd\b"]),
        ("Business & Startup", [r"\bstartup\b", r"\bsaas\b", r"\bmvp\b", r"\bkpi\b"]),
        ("Productivity & Workflow", [r"\bworkflow\b", r"\bplanning\b", r"\bskill\b"]),
        ("Apple HIG & Design", [r"\bhig[-_]"]),
        ("Odoo & ERP", [r"\bodoo\b"]),
        ("Blockchain & Web3", [r"\bweb3\b", r"\bsolidity\b", r"\bdefi\b"]),
        ("Data & Analytics", [r"\banalytics\b", r"\bdashboard\b"]),
        ("Game Development", [r"\bgame\b", r"\bminecraft\b"]),
        ("Media & Creative", [r"\bvideo\b", r"\baudio\b", r"\bremotion\b"]),
        ("Legal & Compliance", [r"\bcompliance\b", r"\bgdpr\b", r"\bprivacy\b"]),
        ("Cursor & IDE", [r"\bcursor\b", r"\bdevcontainer\b"]),
    ]
    for cat, patterns in rules:
        if any(re.search(p, text) for p in patterns):
            return cat
    return "General & Miscellaneous"


def main():
    skills = []
    for root, _, files in os.walk(SKILLS_ROOT):
        if "_catalog" in root.split(os.sep) or "skill-recommender" in root.split(os.sep):
            continue
        if "SKILL.md" not in files:
            continue
        rel = os.path.relpath(root, SKILLS_ROOT)
        skill_id = rel if rel != "." else os.path.basename(root)
        with open(os.path.join(root, "SKILL.md"), encoding="utf-8", errors="replace") as f:
            name, desc = parse_frontmatter(f.read(8000))
        skills.append({
            "id": skill_id,
            "name": name or skill_id.split("/")[-1],
            "description": (desc or "").strip(),
            "category": categorize(skill_id, name, desc),
        })

    skills.sort(key=lambda s: (s["category"], s["id"]))
    cats = defaultdict(list)
    for s in skills:
        cats[s["category"]].append(s)

    os.makedirs(CATALOG_DIR, exist_ok=True)
    with open(os.path.join(CATALOG_DIR, "skills-index.json"), "w") as f:
        json.dump({"total": len(skills), "categories": {k: len(v) for k, v in sorted(cats.items(), key=lambda x: -len(x[1]))}, "skills": skills}, f, indent=2)

    print(f"Regenerated catalog: {len(skills)} skills, {len(cats)} categories")
    print(f"Run the full doc generator separately or ask the agent to refresh all _catalog/ files.")


if __name__ == "__main__":
    main()
