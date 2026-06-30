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
    cat_counts = {k: len(v) for k, v in sorted(cats.items(), key=lambda x: -len(x[1]))}
    with open(os.path.join(CATALOG_DIR, "skills-index.json"), "w") as f:
        json.dump({"total": len(skills), "categories": cat_counts, "skills": skills}, f, indent=2)

    # Keyword index
    kw_index = defaultdict(set)
    stop = {"the", "a", "an", "and", "or", "for", "to", "in", "on", "with", "when", "use", "this", "that", "from", "is", "are", "be", "by", "of", "as", "at", "it", "you", "your", "not", "do", "does"}
    for s in skills:
        tokens = re.findall(r"[a-z0-9][a-z0-9_-]{1,}", f"{s['id']} {s['description']}".lower())
        for t in tokens:
            if len(t) >= 3 and t not in stop:
                kw_index[t].add(s["id"])
    with open(os.path.join(CATALOG_DIR, "keyword-index.json"), "w") as f:
        json.dump({k: sorted(v) for k, v in sorted(kw_index.items())}, f, indent=2)

    # categories.md
    lines = [f"# Skills by Category\n\nTotal: {len(skills)} skills across {len(cats)} categories.\n"]
    for cat in sorted(cats, key=lambda c: (-len(cats[c]), c)):
        lines.append(f"\n## {cat} ({len(cats[cat])})\n")
        for s in cats[cat]:
            desc = (s["description"] or "").replace("\n", " ")
            if len(desc) > 120:
                desc = desc[:117] + "..."
            lines.append(f"- **`{s['id']}`** — {desc}")
    with open(os.path.join(CATALOG_DIR, "categories.md"), "w") as f:
        f.write("\n".join(lines) + "\n")

    # full-index.md
    alpha = sorted(skills, key=lambda s: s["id"].lower())
    flines = [
        "# Full Skills Index (Alphabetical)\n",
        f"{len(skills)} skills.\n",
        "| Skill ID | Category | Description (truncated) |",
        "|----------|----------|-------------------------|",
    ]
    for s in alpha:
        desc = (s["description"] or "").replace("|", "\\|").replace("\n", " ")
        if len(desc) > 120:
            desc = desc[:117] + " "
        flines.append(f"| `{s['id']}` | {s['category']} | {desc} |")
    with open(os.path.join(CATALOG_DIR, "full-index.md"), "w") as f:
        f.write("\n".join(flines) + "\n")

    # _catalog/README.md category table
    readme = [
        "# Skills Catalog Overview\n",
        f"**Total skills:** {len(skills)}  ",
        "**Location:** repo root, `~/.agents/skills/`, or `.agents/skills/` submodule\n",
        "## How to use this catalog\n",
        "1. **Ask for recommendations** — Use `skill-recommender`: *\"Which skill should I use for X?\"*",
        "2. **Browse by category** — [categories.md](categories.md)",
        "3. **Curated picks** — [top-skills.md](top-skills.md)",
        "4. **Full index** — [full-index.md](full-index.md)",
        "5. **Machine-readable** — [skills-index.json](skills-index.json)",
        "6. **Uncategorized skills** — [general-subcategories.md](general-subcategories.md)\n",
        "Refresh: `python3 _catalog/regenerate.py`\n",
        "## Category summary\n",
        "| Category | Count | Top examples |",
        "|----------|------:|--------------|",
    ]
    for cat, count in sorted(cat_counts.items(), key=lambda x: -x[1]):
        examples = ", ".join(f"`{s['id']}`" for s in cats[cat][:3])
        readme.append(f"| {cat} | {count} | {examples} |")
    with open(os.path.join(CATALOG_DIR, "README.md"), "w") as f:
        f.write("\n".join(readme) + "\n")

    print(f"Regenerated catalog: {len(skills)} skills, {len(cats)} categories")


if __name__ == "__main__":
    main()
