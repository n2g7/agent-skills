---
name: skill-recommender
description: >-
  Recommends which agent skills to use from the user's skill library (1,700+
  skills). Works from ~/.agents/skills/, project .agents/skills/ submodule,
  or when this repo is the workspace root. Use when the user asks which skill
  to use, wants skill suggestions for a task, or says "what skill should I
  use for X". Does NOT load or execute other skills — only recommends skill
  IDs and explains why. Never read other SKILL.md files unless the user
  explicitly asks to use a recommended skill afterward.
disable-model-invocation: true
---

# Skill Recommender

Help the user pick the right skill(s) from their library. **Never load or invoke recommended skills** unless the user explicitly asks you to use one afterward.

## Skill library location

Resolve the skills root in this order:

1. **Project submodule:** `.agents/skills/<skill-id>/SKILL.md` (when embedded in a code repo)
2. **This repo as workspace:** `<skill-id>/SKILL.md` at repo root (standalone skills repo)
3. **Global install (local only):** `~/.agents/skills/<skill-id>/SKILL.md`

Resolve the catalog directory the same way:

- Submodule: `.agents/skills/_catalog/`
- Standalone repo: `_catalog/` (relative to repo root)
- Global: `~/.agents/skills/_catalog/`

Catalog (generated index of all skills):

| File | Use for |
|------|---------|
| [_catalog/README.md](../_catalog/README.md) | Category overview + decision guide |
| [_catalog/top-skills.md](../_catalog/top-skills.md) | Best-documented skills per category |
| [_catalog/categories.md](../_catalog/categories.md) | Full list grouped by category |
| [_catalog/general-subcategories.md](../_catalog/general-subcategories.md) | 270+ uncategorized skills, sub-grouped |
| [_catalog/full-index.md](../_catalog/full-index.md) | Alphabetical lookup of all 1,432 skills |
| [_catalog/skills-index.json](../_catalog/skills-index.json) | Machine search by keyword |
| [_catalog/keyword-index.json](../_catalog/keyword-index.json) | Keyword → skill ID mapping |

**Total:** 1,700+ skills across 34+ primary categories.

## On-demand loading policy

Every skill in this library sets `disable-model-invocation: true`. When recommending:

1. Search `_catalog/` only — do not open skill folders during recommendation.
2. Return skill IDs and rationale.
3. Tell the user how to invoke the chosen skill explicitly.
4. Read `<skill-id>/SKILL.md` **only after** the user confirms they want to use it.

## Recommendation workflow

When the user describes what they're working on:

### 1. Parse intent

Extract from their message:
- **Domain** (e.g. React, Azure, SEO, mobile, security)
- **Action** (build, debug, deploy, audit, automate, review, plan)
- **Tools/platforms** mentioned (Expo, n8n, Playwright, Odoo, etc.)
- **Language** if relevant (Python, TypeScript, Rust, etc.)

### 2. Search the catalog

Use this priority order (read only what you need):

1. **Quick match** — Check the decision guide in [_catalog/README.md](../_catalog/README.md)
2. **Category browse** — Open the matching section in [_catalog/top-skills.md](../_catalog/top-skills.md) for curated picks
3. **Keyword search** — Grep `_catalog/skills-index.json` or `_catalog/keyword-index.json` for domain terms
4. **Broad category** — Fall back to [_catalog/categories.md](../_catalog/categories.md)
5. **Obscure/general** — Check [_catalog/general-subcategories.md](../_catalog/general-subcategories.md)

Search command examples (use the catalog path that matches your layout):

```bash
# Standalone skills repo or cwd at skills root
CATALOG="_catalog/skills-index.json"
# Submodule in a project:
# CATALOG=".agents/skills/_catalog/skills-index.json"
# Global install:
# CATALOG="$HOME/.agents/skills/_catalog/skills-index.json"

python3 -c "
import json, os
catalog = os.environ.get('CATALOG', '_catalog/skills-index.json')
data = json.load(open(catalog))
for s in data['skills']:
    t = f\"{s['id']} {s['description']}\".lower()
    if 'playwright' in t:
        print(s['id'], '-', s['category'])
"

# Or ripgrep the catalog folder
rg -i "playwright" _catalog/
```

### 3. Rank candidates

Prefer skills that:
1. Match the **specific tool/platform** mentioned (e.g. `azure-storage-blob-py` over generic `cloud-architect`)
2. Match the **action** (e.g. `e2e-testing-patterns` for tests, not `react-patterns`)
3. Have a **substantive description** (not placeholder "Describe what this skill does...")
4. Are **more specific** over more general when both fit

Return **1 primary skill** and **1–3 alternates** when useful.

### 4. Respond in this format

```markdown
## Recommended skills for: [user's task summary]

### Primary
- **`skill-id`** — One sentence on what it does and why it fits.

### Also consider
- **`other-skill-id`** — When/why you'd pick this instead.

### Category context
Brief note on which category these come from and related categories to explore.

### How to use
Tell the agent: "Use the `skill-id` skill" or "@skill-id" — do not auto-load unless asked.
```

## Category quick-reference

| User says... | Category | Start here |
|--------------|----------|------------|
| React, Next.js, Tailwind, UI, CSS, Three.js | Frontend & UI | `react-patterns`, `tailwind-design-system` |
| Azure, blob storage, Key Vault, Cosmos | Azure | `azure-identity-ts`, `azure-storage-blob-py` |
| AWS, Lambda, S3, cost optimization | AWS | `aws-cost-optimizer` |
| Tests, E2E, TDD, Playwright | Testing & QA | `e2e-testing-patterns`, `playwright-skill` |
| CI/CD, Docker, K8s, deploy | DevOps & CI/CD | `devops-troubleshooter` |
| AI agent, LLM, RAG, LangChain, MCP | AI & LLM | `langchain-architecture`, `mcp-builder-ms` |
| Automate Slack/Notion/Linear/n8n | Automation & Integrations | `n8n-mcp-tools-expert`, `*-automation` skills |
| Security, pentest, OWASP, Burp | Security & Pentesting | `burp-suite-testing`, `pci-compliance` |
| SEO, marketing, content | SEO & Marketing | `seo-fundamentals`, `seo-content-auditor` |
| Expo, Flutter, iOS, SwiftUI, mobile | Mobile | `expo-tailwind-setup`, `flutter-expert` |
| Postgres, migrations, SQL, Supabase | Database | `database-migrations-sql-migrations`, `neon-postgres` |
| API, backend, GraphQL, gRPC | Backend & API | `api-design-principles`, `nodejs-backend-patterns` |
| Git, PR, commit, worktree | Git & Version Control | `iterate-pr`, `git-advanced-workflows` |
| Monitoring, SLO, OpenTelemetry | Observability & Monitoring | `observability-monitoring-slo-implement` |
| Startup, MVP, SaaS, pricing | Business & Startup | `saas-mvp-launcher`, `startup-business-analyst-business-case` |
| Write a new skill | Productivity & Workflow | `skill-writer`, `10-andruia-skill-smith` |
| Apple HIG, SwiftUI, macOS | Apple HIG & Design | `hig-foundations`, `swiftui-view-refactor` |
| Odoo, ERP | Odoo & ERP | `odoo-module-developer` |
| Cloudflare Workers, Wrangler | Cloudflare | `cloudflare-workers-expert`, `hono` |
| Python / TypeScript / Go / Rust patterns | Languages: * | `python-patterns`, `rust-pro`, `golang-pro` |
| Architecture, CQRS, DDD | Architecture & Design Patterns | `cqrs-implementation`, `ddd-strategic-design` |
| Code review, refactor, simplify | Code Quality (see general-subcategories) | `code-simplifier`, `vibers-code-review` |
| Debug errors, trace failures | Debugging (see general-subcategories) | `error-diagnostics-error-trace`, `devops-troubleshooter` |

## Special cases

### Cursor built-in skills
Skills in `~/.cursor/skills-cursor/` are Cursor-managed (create-skill, create-rule, babysit, canvas, etc.). Recommend those for Cursor-specific tasks (hooks, rules, automations, PR babysitting).

### Plugin cache skills
Figma, Cloudflare, etc. may also appear under `~/.cursor/plugins/cache/`. Mention both if relevant.

### Placeholder skills
Many skills still have template descriptions ("Describe what this skill does..."). Warn the user and suggest better-documented alternatives from `top-skills.md`.

### Multiple skills in sequence
Some tasks need a chain, e.g.:
- New feature: `concise-planning` → implement → `e2e-testing-patterns` → `iterate-pr`
- New Azure service: `cloud-architect` → `azure-identity-ts` → `observability-monitoring-slo-implement`

## Examples

**User:** "I'm building an Expo app with Tailwind and need CI"
→ Primary: `expo-tailwind-setup`, Also: `expo-cicd-workflows`, `upgrading-expo`

**User:** "Security audit on our Laravel API"
→ Primary: `laravel-security-audit`, Also: `api-design-principles`, `pci-compliance`

**User:** "Which skill for SEO content?"
→ Primary: `seo-content-auditor`, Also: `seo-fundamentals`, `seo-dataforseo`

**User:** "I don't know what skills I even have"
→ Summarize categories from README.md, point to `top-skills.md`, offer to drill into any area.

## Maintenance

The catalog in `_catalog/` was auto-generated from all SKILL.md frontmatter. To refresh after adding skills:

```bash
python3 _catalog/regenerate.py
# Or: ls */SKILL.md | wc -l
```
