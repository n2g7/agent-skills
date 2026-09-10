# LLM intent review of High/Critical skills

This is the SkillSpector **LLM pass** that `--no-llm` skipped: same questions the scanner would send to a model, applied to the 112 High/Critical skills from `static-summary.md`.

Evidence used (no bulk `SKILL.md` reads):

- Skill catalog name + description (`_catalog/skills-index.json`)
- Static rule IDs and counts (`static-summary.md`)
- SkillSpector LLM analyzer prompts: meta-analyzer, `SDI-2` (context-inappropriate capability), `SSD-*` (semantic attack phrasing)

## Framework (what SkillSpector would ask)

**Meta-analyzer** (`nodes/meta_analyzer.py`): for each static hit, is it a true vulnerability or a false positive? Intent = `malicious` / `negligent` / `benign`? Impact if exploited? *Does the skill context make this more or less dangerous?* Their own example: `"cyanide" in a cooking skill = CRITICAL; in a chemistry education skill = maybe OK`.

**SDI-2** (`semantic_developer_intent`): flag a capability only when it is **not justified** by the stated purpose. Do **not** flag sudo in a deploy skill, HTTP in a web-search skill, or credential-file access in an env-var manager.

**SSD-1..4**: prompt injection / paraphrased jailbreaks / natural-language exfil / gradual deception — residual semantic risk, not keyword hits. Applied here only from catalog wording + rule mix (AR1/AR2/AR3, P1, MP3, TT3).

Static `--no-llm` scoring treats every PE2/PE3/YR4/E1 hit as equally bad. The LLM pass is supposed to **keep** those hits when the skill is Metasploit, and **downgrade or re-label** them when a LinkedIn writer or a README generator trips the same regexes.

## Verdict at a glance

| Bucket | Meaning | Count |
|--------|---------|------:|
| A. Offensive by design | Privilege, exploits, or tradecraft **are** the product. High/Critical is expected and useful. | 16 |
| B. Dual-use / operational privilege | Stated job needs elevation, credentials, network, or agent-config access. Not "malware"; least-privilege still applies. | 65 |
| C. Unjustified privilege (SDI-2) | Stated job does **not** need the flagged capability. These are the ones to actually worry about. | 26 |
| D. Likely static noise | Score is dominated by URL/doc/whitespace/YARA-keyword hits, not a privilege story. | 5 |

**112 = 16 + 65 + 26 + 5.** Eight B skills and three C skills also carry a D (noise) overlay in the index (`B+D` / `C+D`); they are counted in B or C, not in D.

Intent labels below are SkillSpector’s (`benign` / `negligent` / `malicious-leaning`). Nothing is called confirmed-malicious without a full-file read.

---

## A. Offensive by design (16)

These skills exist to teach or perform pentest, exploit, or post-exploitation work. Static hits on `PE2` (sudo/root), `PE3` (credential files), `YR1`/`YR4` (malware/hack-tool YARA), `SSRF1` (instance metadata), `P1` (override instructions) are **the syllabus**, not a mismatch.

SkillSpector meta-analyzer: intent **benign** (authorized tradecraft), impact **critical if used off-scope**. Do not “clean” them by deleting the dangerous content — that would gut the skill. Do require explicit authorized-use warnings (`SQP-2`); `metasploit-framework` already has one.

| Skill | Score | Why this bucket | Dominant static rules |
|-------|------:|-----------------|------------------------|
| `aws-penetration-testing` | 100 | IAM priv-esc, SSRF-to-metadata, S3, Lambda, persistence for red team | SSRF1×8, PE2, E5, EA2 |
| `cloud-penetration-testing` | 100 | Azure/AWS/GCP security assessments of the same class | SSRF1×14, PE3, E5, PE2 |
| `linux-privilege-escalation` | 100 | Escalate low-priv user → root | PE2×24, PE3, YR1, YR4 |
| `privilege-escalation-methods` | 100 | Linux/Windows post-exploitation priv-esc | PE2×18, TM2, PE3, YR4, YR1 |
| `metasploit-framework` | 100 | Exploit framework; catalog already says authorized-use only | YR4, P1, PE2, YR1 |
| `ethical-hacking-methodology` | 100 | Full pentest lifecycle | YR4, PE3, PE2, YR1 |
| `network-101` | 100 | Pentest-lab service enumeration (HTTP/SMB/SNMP) | PE2×33, TM2, YR4 |
| `wordpress-penetration-testing` | 100 | WP offensive testing | E1, YR2, YR4, P1, YR1 |
| `active-directory-attacks` | 98 | AD attack paths | TM1, YR1, YR4, EA2, PE2 |
| `ssh-penetration-testing` | 94 | SSH offensive testing | PE3×9, E1, E3, PE2, YR1 |
| `file-path-traversal` | 93 | Identify **and exploit** traversal to steal files/creds | PE3×35, E1, PE2, YR2 |
| `scanning-tools` | 64 | Nmap / vuln-scanners / wireless / compliance **for assessment** | PE2×15, YR4, TM1 |
| `xss-html-injection` | 58 | XSS/HTML injection **exploitation** (session hijack, credential theft) | E1, P2, EA3, YR4 |
| `pentest-commands` | 70 | Command cheat-sheet for pentest (YARA-only hit is expected) | YR4, YR1 |
| `vulnerability-scanner` | 100 | Vuln analysis / attack-surface / OWASP — assessment tradecraft | PE3, AR3, TM3, AST4 |
| `007` | 100 | Red/Blue team, STRIDE/PASTA, incident response | PE3×26, **AR3×5**, P1×4, P6, YR4 |

### Overlay on `007` and `vulnerability-scanner`

Purpose is security work (bucket A), but `AR3` (nullify safety policies / “no restrictions”) and `P1` (ignore system instructions) are **not** required to teach STRIDE or run a vuln scan. Treat those specific hits as SSD-1 / jailbreak overlay: keep the skill, strip anti-refusal language.

---

## B. Dual-use / operational privilege (48)

SDI-2 **do-not-flag**: the capability is a direct requirement of the stated job. Static High/Critical here usually means “this skill is powerful,” not “this skill is pretending to be a calendar reminder while spawning shells.”

Still worth least-privilege review (narrow sudo, pin deps, don’t persist across sessions unless the job is persistence). Intent **benign**, impact **high**.

### B1. Defensive security / credential hygiene (7)

| Skill | Score | Justified capability |
|-------|------:|----------------------|
| `container-security-hardening` | 100 | Must discuss privileged containers, seccomp, non-root vs root |
| `varlock` | 100 | **Job is** secure env-var / credential management (`PE3`/`E2`) |
| `bash-defensive-patterns` | 92 | Defensive Bash; will mention the dangerous patterns it is guarding against |
| `linux-shell-scripting` | 63 | Sysadmin templates (backups, users) used in secops/pentest labs |
| `skill-audit` | 80 | Pre-install skill malware scanner — will match YARA/PE by design |
| `skill-scanner` | 78 | Same class: scan skills for injection / secrets / excess perms |
| `audit-skills` | 68 | Static audit of skills/bundles for malicious patterns |

### B2. Infra, cloud, ML jobs, packaging (14)

| Skill | Score | Justified capability |
|-------|------:|----------------------|
| `environment-setup-guide` | 100 | Installing toolchains: sudo, creds, package sources |
| `remote-gpu-trainer` | 100 | SSH to rented GPUs, checkpoints, teardown/billing — keys + persistence |
| `hugging-face-model-trainer` | 100 | Remote training jobs, secrets, cloud upload (`E5`) |
| `hugging-face-jobs` | 67 | Managed CPU/GPU/TPU jobs with Hub secrets |
| `hugging-face-community-evals` | 65 | Local eval runners / subprocess |
| `macos-spm-app-packaging` | 100 | Sign/notarize macOS apps (certs) and install artifacts |
| `devops-deploy` | 88 | Docker / GH Actions / Lambda / Terraform |
| `gitops-workflow` | 82 | ArgoCD/Flux deploy to Kubernetes |
| `gcp-cloud-run` | 90 | Production Cloud Run deploy (`PE2` expected; `AR1` overlay noted in C-adj) |
| `k6-load-testing` | 66 | Generate load against APIs; network is the point |
| `bun-development` | 89 | Runtime install / execute (`SC2` often = bun install script) |
| `android-dev` | 96 | Keystore / signing credentials |
| `claimable-postgres` | 57 | Provision throwaway Postgres (`DATABASE_URL`) |
| `computer-use-agents` | 100 | Desktop control **is** the product (`EA2` expected). `AR1` (never-refuse) is **not** required — see overlays |

### B3. Agent/skill/plugin ecosystem (AS1/AS3 is the job) (16)

Reading `.claude/`, other `SKILL.md` files, or installing skills is the purpose of these, not snooping.

| Skill | Score | Justified capability |
|-------|------:|----------------------|
| `manage-skills` | 100 | List/edit/toggle skills across 11 tools |
| `skill-installer` | 100 | Copy + register + verify new skills |
| `skill-developer` | 100 | Author Claude Code skills |
| `skill-development` | 70 | Scaffold skills inside plugins |
| `skill-creator` | 69 | Generate + install CLI skills |
| `skill-writer` | 62 | Write/update Agent Skills spec files |
| `writing-skills` | 82 | Create/update agent skills (`RA1` self-edit is in-scope) |
| `yao-meta-skill` | 71 | Package workflows into skills |
| `plugin-structure` | 100 | Scaffold plugin layout / auto-discovery |
| `plugin-settings` | 59 | Per-project plugin state (`.local.md`) — `PE2` sudo is **not** justified, overlay |
| `command-development` | 100 | Slash-command authoring (touches agent dirs) |
| `hook-development` | 100 | PreToolUse/Stop hooks, including blocking dangerous commands |
| `mcp-builder` | 100 | Build MCP servers that expose tools (`EA1` is the design tension) |
| `mcp-integration` | 60 | Wire MCP servers into a plugin |
| `claude-code-expert` | 100 | Claude Code CLI: hooks, `CLAUDE.md`, permissions |
| `claude-in-chrome-troubleshooting` | 85 | Debug Claude-in-Chrome MCP — will touch `.claude/` |
| `ecl-harness-engineer` | 100 | AGENTS.md / CI gates / agent harness |
| `make-me-an-expert` | 99 | Install/continue expert packs on disk |
| `conductor-manage` | 83 | Archive/restore/delete tracks (lifecycle = persistence) |

Full B membership is in the index at the bottom (65 including API/agent skills). Subtables above are illustrative, not disjoint.

### B4. Product/API integrations (HTTP + tokens expected) (11)

`E1` (external URL) and `SC1` (unpinned deps) on an API integration skill are usually **benign**. `TT3` (credential → network) is the same flow as “send the API key to the vendor” — chemistry, not cooking. Still verify the destination is the vendor, not a third party.

| Skill | Score | Justified capability |
|-------|------:|----------------------|
| `2slides-ppt-generator` | 100 | 2slides API + token (`TT3`/`E1` expected if dest is 2slides) |
| `telegram` | 100 | Bot API (`YR1` malware YARA is likely FP overlay) |
| `whatsapp-cloud-api` | 100 | Meta Cloud API + HMAC webhooks |
| `instagram` | 61 | Graph API (`SC6` typosquat is supply-chain overlay, not privilege) |
| `cloudflare` | 100 | Product catalog; see also bucket D for `E1×124` / `RP1×32` inflation |
| `turnstile-spin` | 100 | Turnstile siteverify (`AS3` reading other skills is **not** justified) |
| `comfyui-gateway` | 100 | Auth, webhooks, image delivery for a local/remote Comfy gateway |
| `claude-api` | 77 | Anthropic SDK |
| `stability-ai` | 100 | Stability API keys (`P6` prompt-leak overlay) |
| `ai-studio-image` | 69 | Google AI Studio / Gemini image gen |
| `notebooklm` | 25-issue CRITICAL | Drive a browser session against NotebookLM |
| `shopify-development` | 62 | Admin API tokens (`PE3×37` is loud but in-family) |
| `nextjs-on-cloudflare` | 57 | Deploy Next on Workers |
| `weaviate-cookbooks` | 56 | Weaviate clients / API keys |
| `videodb` | 65 | Ingest URLs / media APIs |
| `wellally-tech` | 60 | Health-data APIs (`P3` conversation-exfil overlay) |
| `monte-carlo-push-ingestion` | 80 | Push lineage to Monte Carlo |
| `audio-transcriber` | 68 | ffmpeg / LLM subprocess (`PE2` sudo not required) |
| `playwright-skill` | 70 | Browser E2E |
| `webapp-testing` | 64 | Playwright against local apps |
| `frontend-lighthouse` | 57 | Lighthouse CI (`AS3` overlay) |
| `vibecode-production-qa-validator` | 89 | 13-phase QA including a vuln scan |
| `agent-evaluation` | 76 | Agent behavioral tests (may mention jailbreaks → `YR4`/`P1`) |
| `diary` | 100 | Multi-project logger (local persistence justified; outbound `E1` less so) |
| `loki-mode` | 100 | **Explicit** “PRD to production, zero human intervention” — `EA2` is the pitch. Powerful by design; treat as high-agency dual-use, not a hidden pentest kit |
| `cron-doctor` | 56 | Talks about cron; should **not** install cron jobs (`RA2` likely over-firing) |
| `android-dev` | (listed in B2) | |
| `claimable-postgres` | (listed in B2) | |

---

## C. Unjustified privilege — SDI-2 true positives (32)

Stated purpose is content, design, docs, frontend, marketing, forecasting, or similar. Flagged capabilities (credential files, sudo, session persistence, memory poisoning, anti-refusal, agent-config snooping, credential-to-network) are **not** a direct requirement.

SkillSpector meta-analyzer: intent **negligent** (most) or **malicious-leaning** where anti-refusal / hidden-instruction rules dominate. Impact **high**. These are the skills that “have nothing to do with it yet have unnecessary high privileges.”

### C1. Content / docs / office files that trip creds, sudo, or persistence

| Skill | Score | Stated job | Why SDI-2 |
|-------|------:|------------|-----------|
| `last30days` | 100 | Research last 30 days on Reddit/X/Web | `PE3×16` credential-file access is not required to read public posts |
| `linkedin-content-generator` | 100 | LinkedIn posts/carousels | `MP3` memory poisoning, `RA2` persistence, `P6` prompt leak |
| `survey-generator` | 100 | Academic survey-paper artifacts | `TT3` credential→network, `EA2` autonomous high-impact |
| `pptx` / `pptx-official` | 100 | Edit `.pptx` ZIP/XML | `RA2×12` session persistence, `PE2` sudo, `P2` hidden instructions |
| `docx` / `docx-official` | 78 | Edit `.docx` ZIP/XML | Same pattern as pptx |
| `readme` | 92 | Write a thorough README | `PE3`/`PE2` creds and sudo |
| `mobile-design` | 79 | Mobile-first design guide | `PE3×10` credential files |
| `ai-studio-image` | (B4 tokens; `P6` overlay) | Image gen | Prompt-leak not required |

### C2. Frontend / design / product that should not touch secrets or jailbreaks

| Skill | Score | Stated job | Why SDI-2 |
|-------|------:|------------|-----------|
| `senior-frontend` | 98 | React/Next/Tailwind | `PE3` credential files |
| `ui-ux-pro-max` | 100 | UI/UX palettes and reviews | `E1×15`, `EA2`, `P6` |
| `hig-technologies` | 95 | Apple HIG / design context | `EA2`, `P6`, `MP3` |
| `hig-patterns` | 87 | Apple HIG interaction patterns | `EA2`, `RA2`, `AR2`, `EA3` |
| `inventory-demand-planning` | 62 | Safety stock / replenishment | `AR2` strip warnings, `EA2`, `P9` hidden padding |
| `ai-product` | 68 | AI product strategy | `P1`, `P6`, `YR4` |
| `super-code` | 82 | House coding style | `EA2` autonomous high-impact is out of scope |
| `lovable-cleanup` | 73 | Strip Lovable scaffolding | `PE3`, `P2` hidden instructions (YR4 likely noise) |

### C3. “Helpful” skills with anti-refusal, hidden instructions, or agent snooping

| Skill | Score | Stated job | Why SDI-2 |
|-------|------:|------------|-----------|
| `sharp-edges` | 100 | Catalog description is just the id | `P1`, `AR2`, `EA2`, `EA4`, `RA1` — jailbreak + self-mod with no stated purpose |
| `distributed-debugging-debug-trace` | 81 | Distributed tracing / debug setup | `AR3` “no restrictions” + `P1` ignore-instructions |
| `web-scraper` | 51 | Extract tables/prices | Network is B-like; **`AR1` never-refuse is not** |
| `competitor-analysis` | 100 | Browserbase competitor research | `AS1` agent-config snooping, `LP1` undeclared capability |
| `git-pr-review` | 61 | Write a PR description from commits | `P1`/`P6` (YR4 likely keyword FP) |
| `systematic-debugging` | 52 | Debug before proposing fixes | `PE3` creds, `E4` conversation exfil |
| `frontend-lighthouse` | 57 | Lighthouse CI budgets | `AS3` reading other skills |
| `nextjs-on-cloudflare` | 57 | Next on Workers | `AS3` same overlay |
| `turnstile-spin` | (otherwise B) | Turnstile setup | `AS3×7` overlay |
| `plugin-settings` | (otherwise B) | Plugin YAML state | `PE2` sudo overlay |
| `computer-use-agents` | (otherwise B) | Computer-use agents | `AR1` overlay |
| `gcp-cloud-run` | (otherwise B) | Cloud Run | `AR1` overlay |
| `007` / `vulnerability-scanner` | (otherwise A) | Security | `AR3` overlay |

### C4. Domain skills whose privilege volume does not match the job

| Skill | Score | Stated job | Why SDI-2 |
|-------|------:|------------|-----------|
| `junta-leiloeiros` | 67 | Scrape Brazilian commercial-board auctioneer lists | `TM3` unsafe defaults, fat `SC1`/`SC4` — public scraping ≠ creds/root |
| `monorepo-management` | 54 | Monorepo tooling | `PE3`/`RA2` not required to discuss workspaces |
| `turborepo-caching` | 53 | Turborepo cache | same |
| `diary` | (mostly B) | Dev logger | outbound `E1` should be proven necessary |
| `audio-transcriber` | (mostly B) | Audio → markdown | `PE2` sudo not required for ffmpeg |
| `wellally-tech` | (mostly B) | Health data APIs | `P3` “send conversation context out” is not required |
| `stability-ai` | (mostly B) | Image API | `P6` overlay |
| `cron-doctor` | (mostly B) | Validate cron expressions | installing persistence (`RA2`) is not the job |

---

## D. Likely static noise (16)

High issue counts here are mostly **documentation shape**, not privilege. Meta-analyzer would mark many as false positive (`intent=benign`, low impact). Do not treat these as “secretly Metasploit.”

Typical inflators:

- `RP1` — remote/mutable references (every docs URL looks like a rug-pull)
- `E1` — any `https://` in a product catalog
- `SC1`/`SC4` — unpinned or CVE-tagged examples in boilerplates
- `P9` — large blank regions (markdown layout, not hidden payloads)
- `AE1` — “referenced artifact not fully inspected” (coverage gap, not an exploit)
- `YR1`/`YR4` — word “exploit” / tool names in a QA or deploy doc
- `AST7` — dynamic `getattr` in SDKs

| Skill | Score | Why this looks like noise |
|-------|------:|---------------------------|
| `shadcn` | 96 | `RP1×73` + `P9×10` on a component catalog |
| `cloudflare` | 100 | `E1×124` + `RP1×32` on a product-chooser with many docs links (still has `PE3×8` worth a glance) |
| `typescript-expert` | 64 | `RP1×14` on TS/tooling docs |
| `playwright-skill` | 70 | `RP1×13` on browser-testing docs |
| `monte-carlo-push-ingestion` | 80 | `AST7×29` getattr-heavy SDK guide |
| `claude-api` | 77 | `P9×3` padding + expected `E1` |
| `browser-testing-with-devtools` | 65 | `YR1`/`YR4` on a DevTools MCP tester |
| `git-pr-review` | 61 | `YR4` next to a 3-issue PR-description skill (also C for `P1`/`P6`) |
| `agent-evaluation` | 76 | `YR4` while discussing agent attacks |
| `lovable-cleanup` | 73 | `YR4` on a Vite cleanup helper |
| `ai-product` | 68 | `YR4` on product strategy |
| `devops-deploy` | 88 | `YR1` on a deploy skill (rest is B) |
| `telegram` | 100 | `YR1×2` on a Bot API skill (rest is B) |
| `vercel-optimize` | 100 | `YR1×2` on a cost/perf auditor + lots of `AE1` |
| `instagram` | 61 | `SC6` typosquat + unpinned examples |
| `ecl-harness-engineer` | 100 | `RP1×8` / `P2×8` — `P2` hidden-comment hits may be real; RP1 is docs |

Noise ≠ ignore. If a D skill also has `PE3`/`AR*`/`TT3`, keep that subset (called out in A/C overlays).

---

## Full index (all 112)

Legend: **A** offensive-by-design · **B** dual-use/operational · **C** unjustified SDI-2 · **D** likely noise. Primary bucket first; overlays in notes.

| Skill | Sev | Score | Bucket | Notes |
|-------|-----|------:|--------|-------|
| `007` | CRITICAL | 100 | A | Red/Blue; **C overlay** `AR3`/`P1` |
| `2slides-ppt-generator` | CRITICAL | 100 | B | API token→vendor (`TT3` expected if dest is 2slides) |
| `aws-penetration-testing` | CRITICAL | 100 | A | |
| `claude-code-expert` | CRITICAL | 100 | B | Agent-config is the job |
| `cloud-penetration-testing` | CRITICAL | 100 | A | |
| `cloudflare` | CRITICAL | 100 | B+D | Product chooser; E1/RP1 inflated |
| `comfyui-gateway` | CRITICAL | 100 | B | Auth/webhooks |
| `command-development` | CRITICAL | 100 | B | **C overlay** `P2` hidden instructions |
| `competitor-analysis` | CRITICAL | 100 | C | `AS1`/`LP1` not needed for Browserbase research |
| `computer-use-agents` | CRITICAL | 100 | B | **C overlay** `AR1` |
| `container-security-hardening` | CRITICAL | 100 | B | |
| `diary` | CRITICAL | 100 | B | **C overlay** outbound `E1` |
| `ecl-harness-engineer` | CRITICAL | 100 | B+D | Harness authoring; RP1/P2 |
| `environment-setup-guide` | CRITICAL | 100 | B | |
| `ethical-hacking-methodology` | CRITICAL | 100 | A | |
| `hook-development` | CRITICAL | 100 | B | |
| `hugging-face-model-trainer` | CRITICAL | 100 | B | |
| `last30days` | CRITICAL | 100 | C | Research ≠ `PE3×16` |
| `linkedin-content-generator` | CRITICAL | 100 | C | Memory poison / persistence |
| `linux-privilege-escalation` | CRITICAL | 100 | A | |
| `loki-mode` | CRITICAL | 100 | B | Explicit zero-HITL agency |
| `macos-spm-app-packaging` | CRITICAL | 100 | B | |
| `manage-skills` | CRITICAL | 100 | B | |
| `mcp-builder` | CRITICAL | 100 | B | |
| `metasploit-framework` | CRITICAL | 100 | A | Already warns authorized-use |
| `network-101` | CRITICAL | 100 | A | |
| `notebooklm` | CRITICAL | 100 | B | |
| `plugin-structure` | CRITICAL | 100 | B | |
| `pptx` | CRITICAL | 100 | C | Office XML ≠ sudo/persistence |
| `pptx-official` | CRITICAL | 100 | C | |
| `privilege-escalation-methods` | CRITICAL | 100 | A | |
| `remote-gpu-trainer` | CRITICAL | 100 | B | |
| `sharp-edges` | CRITICAL | 100 | C | No real purpose; jailbreak-shaped rules |
| `skill-developer` | CRITICAL | 100 | B | **C overlay** `P3` context exfil |
| `skill-installer` | CRITICAL | 100 | B | |
| `stability-ai` | CRITICAL | 100 | B | **C overlay** `P6` |
| `survey-generator` | CRITICAL | 100 | C | |
| `telegram` | CRITICAL | 100 | B+D | API; YR1 likely FP |
| `turnstile-spin` | CRITICAL | 100 | B | **C overlay** `AS3` |
| `ui-ux-pro-max` | CRITICAL | 100 | C | |
| `varlock` | CRITICAL | 100 | B | Creds **are** the job |
| `vercel-optimize` | CRITICAL | 100 | D | YR1/AE1 on a perf auditor |
| `vulnerability-scanner` | CRITICAL | 100 | A | **C overlay** `AR3` |
| `whatsapp-cloud-api` | CRITICAL | 100 | B | |
| `wordpress-penetration-testing` | CRITICAL | 100 | A | |
| `make-me-an-expert` | CRITICAL | 99 | B | |
| `active-directory-attacks` | CRITICAL | 98 | A | |
| `senior-frontend` | CRITICAL | 98 | C | |
| `android-dev` | CRITICAL | 96 | B | Signing keys |
| `shadcn` | CRITICAL | 96 | D | RP1/P9 catalog noise |
| `hig-technologies` | CRITICAL | 95 | C | |
| `ssh-penetration-testing` | CRITICAL | 94 | A | |
| `file-path-traversal` | CRITICAL | 93 | A | Exploit + steal files |
| `bash-defensive-patterns` | CRITICAL | 92 | B | |
| `readme` | CRITICAL | 92 | C | |
| `gcp-cloud-run` | CRITICAL | 90 | B | **C overlay** `AR1` |
| `bun-development` | CRITICAL | 89 | B | |
| `vibecode-production-qa-validator` | CRITICAL | 89 | B | Includes a vuln-scan phase |
| `devops-deploy` | CRITICAL | 88 | B+D | Deploy + YR1 |
| `hig-patterns` | CRITICAL | 87 | C | |
| `claude-in-chrome-troubleshooting` | CRITICAL | 85 | B | |
| `conductor-manage` | CRITICAL | 83 | B | |
| `gitops-workflow` | CRITICAL | 82 | B | |
| `super-code` | CRITICAL | 82 | C | |
| `writing-skills` | CRITICAL | 82 | B | |
| `distributed-debugging-debug-trace` | CRITICAL | 81 | C | `AR3`/`P1` |
| `monte-carlo-push-ingestion` | HIGH | 80 | D | AST7-heavy SDK |
| `skill-audit` | HIGH | 80 | B | Defensive scanner |
| `mobile-design` | HIGH | 79 | C | |
| `docx` | HIGH | 78 | C | |
| `docx-official` | HIGH | 78 | C | |
| `skill-scanner` | HIGH | 78 | B | |
| `claude-api` | HIGH | 77 | B+D | |
| `agent-evaluation` | HIGH | 76 | B+D | |
| `lovable-cleanup` | HIGH | 73 | C+D | |
| `yao-meta-skill` | HIGH | 71 | B | |
| `pentest-commands` | HIGH | 70 | A | |
| `playwright-skill` | HIGH | 70 | B+D | |
| `skill-development` | HIGH | 70 | B | |
| `ai-studio-image` | HIGH | 69 | B | |
| `skill-creator` | HIGH | 69 | B | |
| `ai-product` | HIGH | 68 | C+D | |
| `audio-transcriber` | HIGH | 68 | B | **C overlay** `PE2` |
| `audit-skills` | HIGH | 68 | B | |
| `hugging-face-jobs` | HIGH | 67 | B | |
| `junta-leiloeiros` | HIGH | 67 | C | Public scrape ≠ this rule mix |
| `k6-load-testing` | HIGH | 66 | B | **C overlay** `PE2` sudo |
| `browser-testing-with-devtools` | HIGH | 65 | D | |
| `hugging-face-community-evals` | HIGH | 65 | B | |
| `videodb` | HIGH | 65 | B | |
| `scanning-tools` | HIGH | 64 | A | |
| `typescript-expert` | HIGH | 64 | D | |
| `webapp-testing` | HIGH | 64 | B | |
| `linux-shell-scripting` | HIGH | 63 | B | |
| `inventory-demand-planning` | HIGH | 62 | C | |
| `shopify-development` | HIGH | 62 | B | Loud `PE3` but Admin API tokens |
| `skill-writer` | HIGH | 62 | B | |
| `git-pr-review` | HIGH | 61 | C+D | |
| `instagram` | HIGH | 61 | B+D | |
| `mcp-integration` | HIGH | 60 | B | |
| `wellally-tech` | HIGH | 60 | B | **C overlay** `P3` |
| `plugin-settings` | HIGH | 59 | B | **C overlay** `PE2` |
| `xss-html-injection` | HIGH | 58 | A | |
| `claimable-postgres` | HIGH | 57 | B | |
| `frontend-lighthouse` | HIGH | 57 | B | **C overlay** `AS3` |
| `nextjs-on-cloudflare` | HIGH | 57 | B | **C overlay** `AS3` |
| `cron-doctor` | HIGH | 56 | B | **C overlay** `RA2` if it installs cron |
| `weaviate-cookbooks` | HIGH | 56 | B | |
| `monorepo-management` | HIGH | 54 | C | |
| `turborepo-caching` | HIGH | 53 | C | |
| `systematic-debugging` | HIGH | 52 | C | |
| `web-scraper` | HIGH | 51 | C | `AR1`; scraping itself is ordinary |

---

## What to do with this

1. **Do not purge bucket A.** Those skills are supposed to be dangerous. Prefer authorized-use warnings (`SQP-2`) and keep them out of unattended agent loops.
2. **Bucket B is “powerful, not sneaky.”** Tighten sudo, pin dependencies, and drop overlays (`AR1`, `AS3`, `P3`) that the job does not need.
3. **Bucket C is the real SDI-2 queue.** Start with `last30days`, `linkedin-content-generator`, `pptx`/`docx` pair, `sharp-edges`, `ui-ux-pro-max`, `hig-*`, `senior-frontend`, `readme`, `survey-generator`, `distributed-debugging-debug-trace`.
4. **Bucket D is why `--no-llm` over-fires.** A future SkillSpector run *with* the meta-analyzer would likely drop `shadcn`, `cloudflare`’s URL storm, and YARA hits on deploy/QA docs.

Limitation: this pass used catalog descriptions + static rule mixes, matching the SkillSpector LLM’s “manifest vs behavior” question at skill granularity. It did not open 112 `SKILL.md` files. Overlays marked **malicious-leaning** (`sharp-edges`, `AR3` on `007` / debug-trace) are the ones worth a targeted file read next — one skill at a time.
