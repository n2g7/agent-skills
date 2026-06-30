# Skills Catalog Overview

**Total skills:** 1432  
**Location:** `~/.agents/skills/`

## How to use this catalog

1. **Ask for recommendations** — Use the `skill-recommender` skill: *"Which skill should I use for X?"*
2. **Browse by category** — See [categories.md](categories.md) for grouped listings.
3. **Curated picks** — See [top-skills.md](top-skills.md) for the best-documented skills per category.
4. **Full index** — See [full-index.md](full-index.md) for every skill alphabetically.
5. **Machine-readable** — See [skills-index.json](skills-index.json) for programmatic search.
6. **Uncategorized skills** — See [general-subcategories.md](general-subcategories.md) for the 270+ general skills.

To refresh after adding skills: `python3 ~/.agents/skills/_catalog/regenerate.py`

## Category summary

| Category | Count | Top examples |
|----------|------:|--------------|
| General & Miscellaneous | 271 | `00-andruia-consultant`, `20-andruia-niche-intelligence`, `advogado-criminal` |
| Automation & Integrations | 144 | `activecampaign-automation`, `agent-memory-mcp`, `ai-dev-jobs-mcp` |
| AI & LLM | 134 | `adhx`, `advanced-evaluation`, `agent-evaluation` |
| Azure | 118 | `agent-framework-azure-ai-py`, `azure-ai-agents-persistent-dotnet`, `azure-ai-agents-persistent-java` |
| Security & Pentesting | 86 | `007`, `active-directory-attacks`, `ai-engineering-toolkit` |
| SEO & Marketing | 83 | `ai-seo`, `angular-migration`, `apify-brand-reputation-monitoring` |
| Frontend & UI | 75 | `3d-web-experience`, `angular`, `angular-best-practices` |
| Backend & API | 66 | `agentmail`, `agentphone`, `api-design-principles` |
| Productivity & Workflow | 65 | `10-andruia-skill-smith`, `acceptance-orchestrator`, `agentfolio` |
| Database | 42 | `backend-dev-guidelines`, `biopython`, `bullmq-specialist` |
| DevOps & CI/CD | 41 | `aegisops-ai`, `agentic-actions-auditor`, `apify-actorization` |
| Testing & QA | 35 | `ab-test-setup`, `ad-creative`, `airflow-dag-patterns` |
| Business & Startup | 31 | `alpha-vantage`, `apify-competitor-intelligence`, `apify-market-research` |
| Languages: Python | 29 | `agents-v2-py`, `astropy`, `async-python-patterns` |
| Architecture & Design Patterns | 27 | `architect-review`, `architecture`, `architecture-decision-records` |
| Mobile | 26 | `android-jetpack-compose-expert`, `android_ui_verification`, `app-store-optimization` |
| Observability & Monitoring | 20 | `blog-writing-guide`, `create-pr`, `distributed-debugging-debug-trace` |
| Languages: TypeScript/JavaScript | 17 | `animejs-animation`, `bun-development`, `dbos-typescript` |
| Git & Version Control | 15 | `address-github-comments`, `app-store-changelog`, `commit` |
| AWS | 13 | `amazon-alexa`, `aws-cost-cleanup`, `aws-cost-optimizer` |
| Legal & Compliance | 13 | `accessibility-compliance-accessibility-audit`, `akf-trust-metadata`, `beautiful-prose` |
| Game Development | 11 | `game-development`, `2d-games`, `3d-games` |
| Odoo & ERP | 11 | `odoo-accounting-setup`, `odoo-hr-payroll-setup`, `odoo-inventory-optimizer` |
| Apple HIG & Design | 10 | `hig-components-content`, `hig-components-dialogs`, `hig-components-layout` |
| Media & Creative | 10 | `daily-gift`, `fal-audio`, `fal-upscale` |
| Google Cloud | 9 | `cloud-architect`, `cloud-devops`, `cost-optimization` |
| Data & Analytics | 7 | `analytics-product`, `analytics-tracking`, `apify-content-analytics` |
| Languages: Rust | 5 | `makepad-skills`, `rust-async-patterns`, `rust-pro` |
| Languages: Go | 4 | `dbos-golang`, `go-concurrency-patterns`, `golang-pro` |
| Languages: Other | 4 | `elixir-pro`, `haskell-pro`, `php-pro` |
| Blockchain & Web3 | 3 | `blockchain-developer`, `defi-protocol-templates`, `spec-to-code-compliance` |
| Cloudflare | 2 | `cloudflare-workers-expert`, `hono` |
| Languages: C#/.NET | 2 | `csharp-pro`, `m365-agents-dotnet` |
| Languages: Java/Kotlin | 2 | `java-pro`, `playwright-java` |
| Cursor & IDE | 1 | `vscode-extension-guide-en` |

## Decision guide — "What skill do I need?"

| If you are... | Start with category | Example skills |
|---------------|--------------------|-----------------|
| Building a React/Next.js UI | Frontend & UI | `react-patterns`, `tailwind-design-system`, `nextjs-app-router` |
| Deploying to Azure | Azure | `azure-identity-ts`, `azure-storage-blob-py` |
| Writing tests | Testing & QA | `e2e-testing-patterns`, `playwright-skill`, `tdd-workflows-tdd-red` |
| Setting up CI/CD | DevOps & CI/CD | `devops-troubleshooter`, `expo-cicd-workflows` |
| Building an AI agent | AI & LLM | `langchain-architecture`, `mcp-builder-ms`, `agent-evaluation` |
| Automating a SaaS tool | Automation & Integrations | `n8n-mcp-tools-expert`, `linear-claude-skill`, `slack-automation` |
| Security audit / pentest | Security & Pentesting | `burp-suite-testing`, `aws-penetration-testing`, `pci-compliance` |
| SEO work | SEO & Marketing | `seo-fundamentals`, `seo-content-auditor`, `seo-dataforseo` |
| Mobile app (Expo/React Native) | Mobile | `expo-tailwind-setup`, `upgrading-expo`, `flutter-expert` |
| Database schema/migrations | Database | `database-migrations-sql-migrations`, `neon-postgres`, `claimable-postgres` |
| Code review / PR workflow | Git & Version Control | `iterate-pr`, `git-advanced-workflows`, `codex-review` |
| Observability / SLOs | Observability & Monitoring | `observability-monitoring-slo-implement`, `observability-engineer` |
| Startup / business planning | Business & Startup | `startup-business-analyst-business-case`, `saas-mvp-launcher` |
| Writing a new skill | Productivity & Workflow | `skill-writer`, `10-andruia-skill-smith` |
| Apple native UI | Apple HIG & Design | `hig-foundations`, `hig-components-content`, `swiftui-view-refactor` |
| Odoo ERP customization | Odoo & ERP | `odoo-module-developer`, `odoo-sales-crm-expert` |
| Cloudflare Workers | Cloudflare | (also check plugin cache skills) |