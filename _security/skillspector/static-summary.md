# SkillSpector static scan summary

- Scanned at: `2026-09-10T09:25:31.128943+00:00`
- Skillspector: `SkillSpector v2.11.2`
- Mode: static (`--no-llm`)
- Skills discovered: **1636**
- Scanned OK: **1633** / failed: **3**
- Workers: **16**
- Duration: **912.4s**
- High/Critical (by severity or score≥50): **353**

## Severity counts

- CRITICAL: 65
- HIGH: 46
- MEDIUM: 199
- LOW: 1323
- UNKNOWN: 3

## Ranked skills (highest risk first)

| Score | Severity | Rec | Issues | Skill | Top rules |
|------:|----------|-----|-------:|-------|-----------|
| 100 | CRITICAL | DO_NOT_INSTALL | 56 | `007` | PE3×26, AR3×5, P1×4, P6×3, YR4×3 |
| 100 | CRITICAL | DO_NOT_INSTALL | 26 | `2slides-ppt-generator` | TT3×7, PE3×6, E1×5, SC1×3, SC4×3 |
| 100 | CRITICAL | DO_NOT_INSTALL | 17 | `aws-penetration-testing` | SSRF1×8, PE2×2, E5, EA2, PE1 |
| 100 | CRITICAL | DO_NOT_INSTALL | 15 | `claude-code-expert` | AS1×7, EA5×5, PE2, SC2, TM1 |
| 100 | CRITICAL | DO_NOT_INSTALL | 31 | `cloud-penetration-testing` | SSRF1×14, PE3×5, E5×3, PE2×3, SC2×2 |
| 100 | CRITICAL | DO_NOT_INSTALL | 184 | `cloudflare` | E1×124, RP1×32, TM1×11, PE3×8, EA2×3 |
| 100 | CRITICAL | DO_NOT_INSTALL | 65 | `comfyui-gateway` | PE3×22, RP1×14, E1×10, TM3×8, PE2×5 |
| 100 | CRITICAL | DO_NOT_INSTALL | 35 | `command-development` | AS1×17, TM1×6, P2×5, RA2×3, PE2×2 |
| 100 | CRITICAL | DO_NOT_INSTALL | 9 | `competitor-analysis` | AE1×3, TM1×3, AS1, LP1, TM2 |
| 100 | CRITICAL | DO_NOT_INSTALL | 25 | `computer-use-agents` | EA2×15, RP1×3, TM1×3, AR1, E1 |
| 100 | CRITICAL | DO_NOT_INSTALL | 26 | `container-security-hardening` | RP1×10, TM1×7, PE2×3, PE5×2, AR2 |
| 100 | CRITICAL | DO_NOT_INSTALL | 15 | `diary` | AST4×2, EA2×2, TT2×2, AST7, E1 |
| 100 | CRITICAL | DO_NOT_INSTALL | 37 | `ecl-harness-engineer` | P2×8, RP1×8, PE3×7, TM1×6, AE1×2 |
| 100 | CRITICAL | DO_NOT_INSTALL | 27 | `environment-setup-guide` | PE2×12, PE3×8, TM3×3, E1, RA2 |
| 100 | CRITICAL | DO_NOT_INSTALL | 7 | `ethical-hacking-methodology` | YR4×3, PE3×2, PE2, YR1 |
| 100 | CRITICAL | DO_NOT_INSTALL | 11 | `hook-development` | PE3×3, AE1×2, TM1×2, E1, LP3 |
| 100 | CRITICAL | DO_NOT_INSTALL | 21 | `hugging-face-model-trainer` | PE2×6, AST4×4, E5×3, TM2×3, PE1×2 |
| 100 | CRITICAL | DO_NOT_INSTALL | 29 | `last30days` | PE3×16, E1×4, PE2×3, RA2×2, EA4 |
| 100 | CRITICAL | DO_NOT_INSTALL | 7 | `linkedin-content-generator` | MP3×3, AE1, LP3, P6, RA2 |
| 100 | CRITICAL | DO_NOT_INSTALL | 40 | `linux-privilege-escalation` | PE2×24, PE3×8, TM2×2, YR1×2, YR4×2 |
| 100 | CRITICAL | DO_NOT_INSTALL | 24 | `macos-spm-app-packaging` | RA2×17, PE3×4, TM1×2, LP3 |
| 100 | CRITICAL | DO_NOT_INSTALL | 16 | `manage-skills` | AS3×9, AS1×3, TM1×2, AE1, RA2 |
| 100 | CRITICAL | DO_NOT_INSTALL | 14 | `mcp-builder` | AE1×3, E1×2, SC1×2, SC4×2, EA1 |
| 100 | CRITICAL | DO_NOT_INSTALL | 5 | `metasploit-framework` | YR4×2, P1, PE2, YR1 |
| 100 | CRITICAL | DO_NOT_INSTALL | 42 | `network-101` | PE2×33, TM2×4, TM1×2, YR4×2, RA2 |
| 100 | CRITICAL | DO_NOT_INSTALL | 25 | `notebooklm` | AST4×8, AS3×4, EA2×2, PE3×2, RA2×2 |
| 100 | CRITICAL | DO_NOT_INSTALL | 10 | `plugin-structure` | AE1×4, AS3×2, PE3, RA1, RA2 |
| 100 | CRITICAL | DO_NOT_INSTALL | 26 | `pptx` | RA2×12, AST4×5, P2×4, PE2×2, AE1 |
| 100 | CRITICAL | DO_NOT_INSTALL | 26 | `pptx-official` | RA2×12, AST4×5, P2×4, PE2×2, AE1 |
| 100 | CRITICAL | DO_NOT_INSTALL | 26 | `privilege-escalation-methods` | PE2×18, TM2×3, PE3×2, YR4×2, YR1 |
| 100 | CRITICAL | DO_NOT_INSTALL | 97 | `remote-gpu-trainer` | RA2×36, PE3×24, PE2×14, AR2×3, RP1×3 |
| 100 | CRITICAL | DO_NOT_INSTALL | 8 | `sharp-edges` | P1×2, AR2, EA2, EA4, RA1 |
| 100 | CRITICAL | DO_NOT_INSTALL | 33 | `skill-developer` | RP1×16, TM3×8, AS1×6, P3, RA2 |
| 100 | CRITICAL | DO_NOT_INSTALL | 18 | `skill-installer` | PE3×8, AS3×5, AST4, LP3, RA1 |
| 100 | CRITICAL | DO_NOT_INSTALL | 25 | `stability-ai` | AE1×13, PE3×5, E1×2, P6×2, LP3 |
| 100 | CRITICAL | DO_NOT_INSTALL | 6 | `survey-generator` | EA2×2, AE1, E1, LP1, TT3 |
| 100 | CRITICAL | DO_NOT_INSTALL | 53 | `telegram` | E1×23, SC1×12, PE3×9, SC4×4, YR1×2 |
| 100 | CRITICAL | DO_NOT_INSTALL | 51 | `turnstile-spin` | E1×21, AE1×10, AS3×7, EA2×4, P9×4 |
| 100 | CRITICAL | DO_NOT_INSTALL | 38 | `ui-ux-pro-max` | E1×15, EA2×7, RP1×4, P6×3, OH1×2 |
| 100 | CRITICAL | DO_NOT_INSTALL | 20 | `varlock` | PE3×12, AS3×2, E2×2, SC2×2, RA2 |
| 100 | CRITICAL | DO_NOT_INSTALL | 18 | `vercel-optimize` | AE1×11, EA2×3, YR1×2, LP3, P6 |
| 100 | CRITICAL | DO_NOT_INSTALL | 10 | `vulnerability-scanner` | PE3×3, AR3×2, TM3×2, AST4, EA4 |
| 100 | CRITICAL | DO_NOT_INSTALL | 44 | `whatsapp-cloud-api` | PE3×17, SC1×11, SC4×6, E1×4, TT3×3 |
| 100 | CRITICAL | DO_NOT_INSTALL | 8 | `wordpress-penetration-testing` | E1×2, YR2×2, YR4×2, P1, YR1 |
| 99 | CRITICAL | DO_NOT_INSTALL | 12 | `make-me-an-expert` | AS3×4, RA2×3, AE1×2, AR2, AST4 |
| 98 | CRITICAL | DO_NOT_INSTALL | 8 | `active-directory-attacks` | TM1×2, YR1×2, YR4×2, EA2, PE2 |
| 98 | CRITICAL | DO_NOT_INSTALL | 12 | `senior-frontend` | E1×6, AE1×2, PE3×2, LP3, OH1 |
| 96 | CRITICAL | DO_NOT_INSTALL | 10 | `android-dev` | PE3×5, AE1×2, RP1×2, P2 |
| 96 | CRITICAL | DO_NOT_INSTALL | 89 | `shadcn` | RP1×73, P9×10, EA2×2, RA1×2, AS1 |
| 95 | CRITICAL | DO_NOT_INSTALL | 11 | `hig-technologies` | EA2×6, P6×3, AE1, MP3 |
| 94 | CRITICAL | DO_NOT_INSTALL | 14 | `ssh-penetration-testing` | PE3×9, E1, E3, PE2, YR1 |
| 93 | CRITICAL | DO_NOT_INSTALL | 38 | `file-path-traversal` | PE3×35, E1, PE2, YR2 |
| 92 | CRITICAL | DO_NOT_INSTALL | 6 | `bash-defensive-patterns` | AE1×2, EA2, RA2, TM1, TM2 |
| 92 | CRITICAL | DO_NOT_INSTALL | 10 | `readme` | PE3×3, PE2×2, RP1×2, TM1×2, EA2 |
| 90 | CRITICAL | DO_NOT_INSTALL | 7 | `gcp-cloud-run` | TM1×2, AR1, E1, PE2, RA2 |
| 89 | CRITICAL | DO_NOT_INSTALL | 7 | `bun-development` | PE3×2, SC2×2, TM2×2, RP1 |
| 89 | CRITICAL | DO_NOT_INSTALL | 14 | `vibecode-production-qa-validator` | RP1×9, SC2×2, TM2×2, PE3 |
| 88 | CRITICAL | DO_NOT_INSTALL | 7 | `devops-deploy` | E1×2, EA2×2, TM1×2, YR1 |
| 87 | CRITICAL | DO_NOT_INSTALL | 9 | `hig-patterns` | EA2×3, RA2×2, AE1, AR2, EA3 |
| 85 | CRITICAL | DO_NOT_INSTALL | 7 | `claude-in-chrome-troubleshooting` | AS1×3, TM1×3, RA2 |
| 83 | CRITICAL | DO_NOT_INSTALL | 7 | `conductor-manage` | RA2×3, AE1×2, TM1×2 |
| 82 | CRITICAL | DO_NOT_INSTALL | 6 | `gitops-workflow` | PE3×2, EA2, PE2, SC2, TM2 |
| 82 | CRITICAL | DO_NOT_INSTALL | 6 | `super-code` | TM1×3, AE1×2, EA2 |
| 82 | CRITICAL | DO_NOT_INSTALL | 13 | `writing-skills` | RA1×8, AS3×3, AE1, RA2 |
| 81 | CRITICAL | DO_NOT_INSTALL | 5 | `distributed-debugging-debug-trace` | AE1×2, AR3, P1, TM3 |
| 80 | HIGH | DO_NOT_INSTALL | 46 | `monte-carlo-push-ingestion` | AST7×29, E1×13, PE3×2, LP3, SC2 |
| 80 | HIGH | DO_NOT_INSTALL | 5 | `skill-audit` | P1×2, PE3×2, YR4 |
| 79 | HIGH | DO_NOT_INSTALL | 14 | `mobile-design` | PE3×10, LP3, MP2, MP3, RA2 |
| 78 | HIGH | DO_NOT_INSTALL | 25 | `docx` | RA2×12, P2×6, AST4×3, PE2×3, LP3 |
| 78 | HIGH | DO_NOT_INSTALL | 25 | `docx-official` | RA2×12, P2×6, AST4×3, PE2×3, LP3 |
| 78 | HIGH | DO_NOT_INSTALL | 5 | `skill-scanner` | AE1, E1, EA2, P3, PE3 |
| 77 | HIGH | DO_NOT_INSTALL | 15 | `claude-api` | E1×6, E4×3, P9×3, EA2×2, MP2 |
| 76 | HIGH | DO_NOT_INSTALL | 5 | `agent-evaluation` | P1×2, AE4, P6, YR4 |
| 73 | HIGH | DO_NOT_INSTALL | 6 | `lovable-cleanup` | P2×3, PE3×2, YR4 |
| 71 | HIGH | DO_NOT_INSTALL | 5 | `yao-meta-skill` | AE1×2, EA2×2, RA1 |
| 70 | HIGH | DO_NOT_INSTALL | 3 | `pentest-commands` | YR4×2, YR1 |
| 70 | HIGH | DO_NOT_INSTALL | 20 | `playwright-skill` | RP1×13, AE1×3, EA3, LP3, SC1 |
| 70 | HIGH | DO_NOT_INSTALL | 5 | `skill-development` | RA1×3, AE1, AS3 |
| 69 | HIGH | DO_NOT_INSTALL | 17 | `ai-studio-image` | PE3×10, SC1×3, SC4×2, LP3, P6 |
| 69 | HIGH | DO_NOT_INSTALL | 12 | `skill-creator` | AS3×5, E3×3, RA2×2, LP3, RA1 |
| 68 | HIGH | DO_NOT_INSTALL | 4 | `ai-product` | EA2, P1, P6, YR4 |
| 68 | HIGH | DO_NOT_INSTALL | 27 | `audio-transcriber` | SC1×15, AST4×6, PE2×2, AS3, EA2 |
| 68 | HIGH | DO_NOT_INSTALL | 5 | `audit-skills` | TM1×3, RA2, SC2 |
| 67 | HIGH | DO_NOT_INSTALL | 24 | `hugging-face-jobs` | E5×11, E1×4, PE1×4, EA2×2, EA1 |
| 67 | HIGH | DO_NOT_INSTALL | 26 | `junta-leiloeiros` | TM3×8, SC1×7, SC4×6, E1×2, AST4 |
| 66 | HIGH | DO_NOT_INSTALL | 20 | `k6-load-testing` | E1×12, PE2×5, PE3×2, TM2 |
| 65 | HIGH | DO_NOT_INSTALL | 4 | `browser-testing-with-devtools` | P1, RP1, YR1, YR4 |
| 65 | HIGH | DO_NOT_INSTALL | 8 | `hugging-face-community-evals` | AST4×5, AE1, E2, LP3 |
| 65 | HIGH | DO_NOT_INSTALL | 5 | `videodb` | LP1×2, PE3×2, RA2 |
| 64 | HIGH | DO_NOT_INSTALL | 20 | `scanning-tools` | PE2×15, RP1×2, YR4×2, TM1 |
| 64 | HIGH | DO_NOT_INSTALL | 18 | `typescript-expert` | RP1×14, TM1×2, AST4, LP3 |
| 64 | HIGH | DO_NOT_INSTALL | 5 | `webapp-testing` | AST4×2, TM1×2, LP3 |
| 63 | HIGH | DO_NOT_INSTALL | 10 | `linux-shell-scripting` | PE2×4, RA2×4, PE3, TM1 |
| 62 | HIGH | DO_NOT_INSTALL | 9 | `inventory-demand-planning` | AE4×4, AR2×2, EA2, EA3, P9 |
| 62 | HIGH | DO_NOT_INSTALL | 45 | `shopify-development` | PE3×37, SC1×3, SSRF3×2, AST4, LP3 |
| 62 | HIGH | DO_NOT_INSTALL | 4 | `skill-writer` | RA1×3, AE1 |
| 61 | HIGH | DO_NOT_INSTALL | 3 | `git-pr-review` | P1, P6, YR4 |
| 61 | HIGH | DO_NOT_INSTALL | 15 | `instagram` | SC1×5, SC4×4, E1×3, LP3, SC6 |
| 60 | HIGH | DO_NOT_INSTALL | 18 | `mcp-integration` | E1×13, EA1×2, PE3×2, P1 |
| 60 | HIGH | DO_NOT_INSTALL | 5 | `wellally-tech` | PE3×3, E1, P3 |
| 59 | HIGH | DO_NOT_INSTALL | 4 | `plugin-settings` | AS1×2, PE2, PE3 |
| 58 | HIGH | DO_NOT_INSTALL | 6 | `xss-html-injection` | E1×2, P2×2, EA3, YR4 |
| 57 | HIGH | DO_NOT_INSTALL | 11 | `claimable-postgres` | RP1×4, EA2×3, PE3×3, E1 |
| 57 | HIGH | DO_NOT_INSTALL | 6 | `frontend-lighthouse` | RP1×3, AE1×2, AS3 |
| 57 | HIGH | DO_NOT_INSTALL | 6 | `nextjs-on-cloudflare` | RP1×3, AE1×2, AS3 |
| 56 | HIGH | DO_NOT_INSTALL | 5 | `cron-doctor` | AE1×3, RA2×2 |
| 56 | HIGH | DO_NOT_INSTALL | 9 | `weaviate-cookbooks` | PE3×3, RP1×3, P9×2, PE2 |
| 54 | HIGH | DO_NOT_INSTALL | 7 | `monorepo-management` | RP1×4, PE3, RA2, TM2 |
| 53 | HIGH | DO_NOT_INSTALL | 7 | `turborepo-caching` | RP1×4, PE3×2, TM2 |
| 52 | HIGH | DO_NOT_INSTALL | 4 | `systematic-debugging` | PE3×2, E4, EA4 |
| 51 | HIGH | DO_NOT_INSTALL | 4 | `web-scraper` | AR1, EA2, PE1, SC2 |
| 50 | MEDIUM | CAUTION | 8 | `agentflow` | EA5×6, RA2×2 |
| 50 | MEDIUM | CAUTION | 3 | `claude-code-guide` | MP3×2, P1 |
| 50 | MEDIUM | CAUTION | 8 | `hugging-face-paper-publisher` | PE3×5, AE4, E5, LP3 |
| 50 | MEDIUM | CAUTION | 2 | `security-scanning-security-hardening` | EA2, YR1 |
| 49 | MEDIUM | CAUTION | 6 | `apify-actor-development` | E1×3, SC2×2, RP1 |
| 48 | MEDIUM | CAUTION | 4 | `ai-md` | EA2×2, AS1, PE3 |
| 48 | MEDIUM | CAUTION | 4 | `api-fuzzing-bug-bounty` | PE3×2, E1, TM1 |
| 48 | MEDIUM | CAUTION | 3 | `cc-skill-continuous-learning` | AS1, AS3, EA2 |
| 48 | MEDIUM | CAUTION | 4 | `hugging-face-cli` | PE3×3, TM1 |
| 47 | MEDIUM | CAUTION | 7 | `javascript-testing-patterns` | E1×5, AE1×2 |
| 47 | MEDIUM | CAUTION | 7 | `neon-postgres` | RP1×5, PE3, TM1 |
| 47 | MEDIUM | CAUTION | 4 | `user-thoughts` | P2×2, PE3, RA2 |
| 47 | MEDIUM | CAUTION | 3 | `windows-privilege-escalation` | YR4×2, YR1 |
| 46 | MEDIUM | CAUTION | 16 | `apify-audience-analysis` | PE3×11, E1×4, LP3 |
| 46 | MEDIUM | CAUTION | 16 | `apify-brand-reputation-monitoring` | PE3×11, E1×4, LP3 |
| 46 | MEDIUM | CAUTION | 16 | `apify-competitor-intelligence` | PE3×11, E1×4, LP3 |
| 46 | MEDIUM | CAUTION | 16 | `apify-content-analytics` | PE3×11, E1×4, LP3 |
| 46 | MEDIUM | CAUTION | 16 | `apify-ecommerce` | PE3×11, E1×4, LP3 |
| 46 | MEDIUM | CAUTION | 16 | `apify-influencer-discovery` | PE3×11, E1×4, LP3 |
| 46 | MEDIUM | CAUTION | 16 | `apify-lead-generation` | PE3×11, E1×4, LP3 |
| 46 | MEDIUM | CAUTION | 16 | `apify-market-research` | PE3×11, E1×4, LP3 |
| 46 | MEDIUM | CAUTION | 16 | `apify-trend-analysis` | PE3×11, E1×4, LP3 |
| 46 | MEDIUM | CAUTION | 17 | `apify-ultimate-scraper` | PE3×12, E1×4, LP3 |
| 46 | MEDIUM | CAUTION | 12 | `cicd-automation-workflow-automate` | PE3×8, RP1×3, EA2 |
| 46 | MEDIUM | CAUTION | 5 | `os-scripting` | P1×3, PE2, RA2 |
| 45 | MEDIUM | CAUTION | 5 | `agent-orchestrator` | AE1, AST4, LP3, SC1, SC4 |
| 45 | MEDIUM | CAUTION | 3 | `aws-serverless` | E1, MP3, TM1 |
| 45 | MEDIUM | CAUTION | 3 | `error-handling-patterns` | AE1×2, OH3 |
| 45 | MEDIUM | CAUTION | 12 | `git-hooks-automation` | RP1×9, TM1×3 |
| 44 | MEDIUM | CAUTION | 3 | `api-testing-observability-api-mock` | AE1×2, SSRF2 |
| 44 | MEDIUM | CAUTION | 4 | `matematico-tao` | AE4×2, AE1, LP3 |
| 44 | MEDIUM | CAUTION | 4 | `prompt-engineering-patterns` | P6×3, LP3 |
| 44 | MEDIUM | CAUTION | 4 | `skill-creator-ms` | RA1×3, RP1 |
| 43 | MEDIUM | CAUTION | 2 | `azure-servicebus-ts` | E4, P3 |
| 43 | MEDIUM | CAUTION | 2 | `claude-settings-audit` | AS1, AS2 |
| 43 | MEDIUM | CAUTION | 46 | `linear-claude-skill` | RP1×42, PE3×2, RA2×2 |
| 43 | MEDIUM | CAUTION | 5 | `transformers-js` | AE1×5 |
| 43 | MEDIUM | CAUTION | 4 | `uv-package-manager` | RA2, SC2, TM2, YR1 |
| 43 | MEDIUM | CAUTION | 4 | `writing-great-skills` | AE1×4 |
| 42 | MEDIUM | CAUTION | 7 | `ad-creative` | E1×3, RP1×3, AR2 |
| 42 | MEDIUM | CAUTION | 3 | `backend-dev-guidelines` | PE3×2, TM1 |
| 42 | MEDIUM | CAUTION | 2 | `beautiful-prose` | AR2, P6 |
| 42 | MEDIUM | CAUTION | 4 | `deploy-to-vercel` | PE3×2, LP3, RA2 |
| 42 | MEDIUM | CAUTION | 4 | `drizzle-migration-conflict` | AS3, LP3, P6, RA2 |
| 41 | MEDIUM | CAUTION | 2 | `create-plugin` | MP3, RA1 |
| 41 | MEDIUM | CAUTION | 3 | `ingest-youtube` | AE1, AST4, LP3 |
| 41 | MEDIUM | CAUTION | 7 | `paypal-integration` | E1×4, EA2×2, PE3 |
| 40 | MEDIUM | CAUTION | 10 | `hubspot-integration` | PE3×6, E1×4 |
| 40 | MEDIUM | CAUTION | 2 | `linkerd-patterns` | SC2, TM2 |
| 40 | MEDIUM | CAUTION | 2 | `task-intelligence` | AE1, PE3 |
| 38 | MEDIUM | CAUTION | 6 | `api-design-principles` | E1×4, TM1×2 |
| 38 | MEDIUM | CAUTION | 11 | `cred-omega` | PE3×9, PE2×2 |
| 38 | MEDIUM | CAUTION | 4 | `odoo-backup-strategy` | E5×2, RA2, TM1 |
| 37 | MEDIUM | CAUTION | 4 | `autonomous-agents` | EA2×2, AR3, OH3 |
| 37 | MEDIUM | CAUTION | 21 | `convex` | RP1×16, E1×4, PE3 |
| 37 | MEDIUM | CAUTION | 2 | `error-debugging-error-trace` | AE1×2 |
| 37 | MEDIUM | CAUTION | 2 | `error-diagnostics-error-trace` | AE1×2 |
| 37 | MEDIUM | CAUTION | 2 | `file-uploads` | AR3, PE3 |
| 37 | MEDIUM | CAUTION | 2 | `framework-migration-code-migrate` | AE1×2 |
| 37 | MEDIUM | CAUTION | 4 | `frontend-slides` | E1, EA2, LP3, P2 |
| 37 | MEDIUM | CAUTION | 2 | `git-pr-workflows-pr-enhance` | AE1×2 |
| 37 | MEDIUM | CAUTION | 2 | `nodejs-backend-patterns` | AE1×2 |
| 37 | MEDIUM | CAUTION | 2 | `project-skill-audit` | AE1×2 |
| 37 | MEDIUM | CAUTION | 2 | `theme-factory` | AE1×2 |
| 37 | MEDIUM | CAUTION | 2 | `typescript-advanced-types` | AE1×2 |
| 37 | MEDIUM | CAUTION | 6 | `web-performance-optimization` | RP1×3, E1×2, P2 |
| 36 | MEDIUM | CAUTION | 4 | `codebase-audit-pre-push` | PE3×3, EA4 |
| 36 | MEDIUM | CAUTION | 7 | `html-injection-testing` | P2×6, E1 |
| 36 | MEDIUM | CAUTION | 10 | `native-data-fetching` | PE3×7, E1×3 |
| 36 | MEDIUM | CAUTION | 3 | `pipecat-friday-agent` | PE3×2, LP3 |
| 36 | MEDIUM | CAUTION | 5 | `skill-sentinel` | E1, LP3, PE3, SC1, SC4 |
| 36 | MEDIUM | CAUTION | 4 | `wcag-audit-patterns` | P2×2, RP1×2 |
| 35 | MEDIUM | CAUTION | 5 | `atlas-contract` | EA2×4, P1 |
| 35 | MEDIUM | CAUTION | 4 | `papers-skill` | E1×2, AR2, LP3 |
| 34 | MEDIUM | CAUTION | 4 | `react-best-practices` | OH1×2, RP1×2 |
| 34 | MEDIUM | CAUTION | 7 | `vibe-code-cleanup` | RP1×5, PE3×2 |
| 33 | MEDIUM | CAUTION | 3 | `bats-testing-patterns` | PE2×2, TM1 |
| 33 | MEDIUM | CAUTION | 2 | `discord-automation` | P3×2 |
| 33 | MEDIUM | CAUTION | 2 | `skill-optimizer` | AE1, AS3 |
| 33 | MEDIUM | CAUTION | 5 | `youtube-notetaker` | AST4×2, TT2×2, LP3 |
| 32 | MEDIUM | CAUTION | 3 | `autonomous-agent-patterns` | EA2×2, TM1 |
| 32 | MEDIUM | CAUTION | 3 | `mmx-cli` | EA2, PE3, RA2 |
| 32 | MEDIUM | CAUTION | 2 | `open-dynamic-workflows` | AE1, RP1 |
| 32 | MEDIUM | CAUTION | 2 | `sqlmap-database-pentesting` | PE3, YR4 |
| 31 | MEDIUM | CAUTION | 2 | `agent-development` | EA1, MP3 |
| 31 | MEDIUM | CAUTION | 5 | `dbos-golang` | E1×4, P3 |
| 31 | MEDIUM | CAUTION | 4 | `dbos-typescript` | E1×3, P3 |
| 31 | MEDIUM | CAUTION | 2 | `decision-navigator` | AR2×2 |
| 31 | MEDIUM | CAUTION | 2 | `k8s-manifest-generator` | PE3, TM4 |
| 31 | MEDIUM | CAUTION | 5 | `memory-forensics` | PE2×4, YR1 |
| 31 | MEDIUM | CAUTION | 2 | `product-manager-toolkit` | E4, LP3 |
| 31 | MEDIUM | CAUTION | 3 | `shellcheck-configuration` | PE2, RA2, TM2 |
| 31 | MEDIUM | CAUTION | 7 | `tools-page-seo-optimizer` | AS3×6, P2 |
| 30 | MEDIUM | CAUTION | 4 | `api-security-best-practices` | PE3×4 |
| 30 | MEDIUM | CAUTION | 2 | `atlas-ledger` | EA2, P1 |
| 30 | MEDIUM | CAUTION | 2 | `auri-core` | AE3, AS3 |
| 30 | MEDIUM | CAUTION | 3 | `auth-implementation-patterns` | PE3×3 |
| 30 | MEDIUM | CAUTION | 7 | `azd-deployment` | PE3×7 |
| 30 | MEDIUM | CAUTION | 4 | `copilot-sdk` | E1, EA1, EA2, MP2 |
| 30 | MEDIUM | CAUTION | 3 | `dbos-python` | E1×2, P3 |
| 30 | MEDIUM | CAUTION | 3 | `helm-chart-scaffolding` | E5, LP3, PE3 |
| 30 | MEDIUM | CAUTION | 2 | `hig-inputs` | EA2, P1 |
| 30 | MEDIUM | CAUTION | 8 | `plaid-fintech` | PE3×8 |
| 30 | MEDIUM | CAUTION | 4 | `planning-with-files` | P2×4 |
| 30 | MEDIUM | CAUTION | 3 | `playwright-java` | P2, P4, RA2 |
| 30 | MEDIUM | CAUTION | 2 | `re-create` | AR1×2 |
| 30 | MEDIUM | CAUTION | 3 | `remotion` | RP1×2, AS2 |
| 30 | MEDIUM | CAUTION | 3 | `spline-3d-integration` | P2×3 |
| 29 | MEDIUM | CAUTION | 6 | `astro` | RP1×5, P2 |
| 29 | MEDIUM | CAUTION | 4 | `azure-microsoft-playwright-testing-ts` | RP1×3, PE3 |
| 29 | MEDIUM | CAUTION | 1 | `cc-skill-strategic-compact` | AS1 |
| 29 | MEDIUM | CAUTION | 5 | `git-advanced-workflows` | TM1×5 |
| 29 | MEDIUM | CAUTION | 2 | `n8n-validation-expert` | EA4, MP3 |
| 29 | MEDIUM | CAUTION | 5 | `smtp-penetration-testing` | PE2×4, YR4 |
| 29 | MEDIUM | CAUTION | 5 | `xlsx` | AST4×3, LP3, P4 |
| 29 | MEDIUM | CAUTION | 5 | `xlsx-official` | AST4×3, LP3, P4 |
| 28 | MEDIUM | CAUTION | 8 | `api-documentation-generator` | E1×7, PE3 |
| 28 | MEDIUM | CAUTION | 2 | `architecture-decision-records` | E4×2 |
| 28 | MEDIUM | CAUTION | 2 | `bulletmind` | P6, P9 |
| 28 | MEDIUM | CAUTION | 2 | `deployment-procedures` | AR2, EA2 |
| 28 | MEDIUM | CAUTION | 44 | `hasdata` | E1×43, TM1 |
| 28 | MEDIUM | CAUTION | 6 | `lint-and-validate` | RP1×4, AST4, LP3 |
| 28 | MEDIUM | CAUTION | 3 | `pentest-checklist` | PE2×2, YR4 |
| 27 | MEDIUM | CAUTION | 12 | `app-builder` | RP1×11, PE3 |
| 27 | MEDIUM | CAUTION | 2 | `bash-linux` | E1, TM1 |
| 27 | MEDIUM | CAUTION | 1 | `diagnosing-bugs` | P6 |
| 27 | MEDIUM | CAUTION | 2 | `gdpr-data-handling` | AR3, EA2 |
| 27 | MEDIUM | CAUTION | 2 | `manifest` | AS1, RA2 |
| 27 | MEDIUM | CAUTION | 2 | `security-scanning-security-sast` | EA2, TM1 |
| 26 | MEDIUM | CAUTION | 2 | `ai-wrapper-product` | AR1×2 |
| 26 | MEDIUM | CAUTION | 2 | `angular-best-practices` | P2×2 |
| 26 | MEDIUM | CAUTION | 2 | `azure-communication-common-java` | PE3×2 |
| 26 | MEDIUM | CAUTION | 2 | `azure-monitor-opentelemetry-exporter-java` | PE3×2 |
| 26 | MEDIUM | CAUTION | 2 | `azure-speech-to-text-rest-py` | PE3×2 |
| 26 | MEDIUM | CAUTION | 3 | `conductor-setup` | PE3×3 |
| 26 | MEDIUM | CAUTION | 5 | `discord-bot-architect` | PE3×5 |
| 26 | MEDIUM | CAUTION | 5 | `hugging-face-evaluation` | PE3×5 |
| 26 | MEDIUM | CAUTION | 5 | `kubestellar-console` | PE3×5 |
| 26 | MEDIUM | CAUTION | 9 | `mailtrap-sending-emails` | P9×7, E1, MP2 |
| 26 | MEDIUM | CAUTION | 4 | `quality-nonconformance` | AE4×2, EA2, P9 |
| 26 | MEDIUM | CAUTION | 11 | `vercel-cli-with-tokens` | PE3×11 |
| 26 | MEDIUM | CAUTION | 2 | `voice-ai-engine-development` | PE3×2 |
| 25 | MEDIUM | CAUTION | 1 | `agent-creator` | AE1 |
| 25 | MEDIUM | CAUTION | 4 | `app-store-optimization` | AS3×2, LP3, RA2 |
| 25 | MEDIUM | CAUTION | 2 | `broken-authentication` | EA2, YR4 |
| 25 | MEDIUM | CAUTION | 2 | `burpsuite-project-parser` | MP2, YR4 |
| 25 | MEDIUM | CAUTION | 2 | `clarity-gate` | EA2, P2 |
| 25 | MEDIUM | CAUTION | 1 | `comprehensive-review-pr-enhance` | AE1 |
| 25 | MEDIUM | CAUTION | 2 | `conductor-revert` | TM1×2 |
| 25 | MEDIUM | CAUTION | 3 | `firmware-analyst` | PE2×2, PE3 |
| 25 | MEDIUM | CAUTION | 1 | `plugin-validator` | AE1 |
| 25 | MEDIUM | CAUTION | 2 | `red-team-tactics` | PE2, TM2 |
| 24 | MEDIUM | CAUTION | 2 | `go-rod-master` | LP3, PE3 |
| 24 | MEDIUM | CAUTION | 14 | `remotion-best-practices` | RP1×12, E1, EA4 |
| 24 | MEDIUM | CAUTION | 2 | `ste-writing` | LP3, PE3 |
| 23 | MEDIUM | CAUTION | 5 | `electron-development` | RA2×3, RP1×2 |
| 23 | MEDIUM | CAUTION | 2 | `fastapi-templates` | PE3×2 |
| 23 | MEDIUM | CAUTION | 2 | `landing-page-generator` | LP3, OH1 |
| 23 | MEDIUM | CAUTION | 2 | `llm-application-dev-prompt-optimize` | AR2, EA3 |
| 23 | MEDIUM | CAUTION | 2 | `model-authoring` | EA3, MP3 |
| 22 | MEDIUM | CAUTION | 56 | `agentphone` | E1×51, P9×5 |
| 22 | MEDIUM | CAUTION | 2 | `azure-monitor-query-java` | E1, PE3 |
| 22 | MEDIUM | CAUTION | 1 | `basecamp-automation` | P3 |
| 22 | MEDIUM | CAUTION | 2 | `burp-suite-testing` | PE3×2 |
| 22 | MEDIUM | CAUTION | 4 | `claude-monitor` | AST4×3, LP3 |
| 22 | MEDIUM | CAUTION | 16 | `cloudflare-email-service` | E1×9, RP1×7 |
| 22 | MEDIUM | CAUTION | 1 | `faf-expert` | EA5 |
| 22 | MEDIUM | CAUTION | 1 | `gemini-api-integration` | AR3 |
| 22 | MEDIUM | CAUTION | 2 | `github-actions-templates` | PE3×2 |
| 22 | MEDIUM | CAUTION | 1 | `hasdata-cli` | RA1 |
| 22 | MEDIUM | CAUTION | 2 | `laravel-security-audit` | PE3×2 |
| 22 | MEDIUM | CAUTION | 2 | `mtls-configuration` | EA2, TM4 |
| 22 | MEDIUM | CAUTION | 1 | `n8n-mcp-tools-expert` | MP3 |
| 22 | MEDIUM | CAUTION | 1 | `n8n-workflow-patterns` | P3 |
| 22 | MEDIUM | CAUTION | 2 | `odoo-docker-deployment` | PE3×2 |
| 22 | MEDIUM | CAUTION | 1 | `polis-protocol` | EA5 |
| 22 | MEDIUM | CAUTION | 2 | `senior-architect` | LP3, PE3 |
| 22 | MEDIUM | CAUTION | 2 | `senior-fullstack` | LP3, PE3 |
| 22 | MEDIUM | CAUTION | 1 | `slack-automation` | P3 |
| 21 | MEDIUM | CAUTION | 1 | `analyze-project` | AR2 |
| 21 | MEDIUM | CAUTION | 1 | `azure-servicebus-dotnet` | E4 |
| 21 | MEDIUM | CAUTION | 1 | `claude-win11-speckit-update-skill` | RA1 |
| 21 | MEDIUM | CAUTION | 1 | `database-cloud-optimization-cost-optimize` | P6 |
| 21 | MEDIUM | CAUTION | 1 | `design-md` | P6 |
| 21 | MEDIUM | CAUTION | 1 | `gdb-cli` | YR1 |
| 21 | MEDIUM | CAUTION | 1 | `hig-components-menus` | P6 |
| 21 | MEDIUM | CAUTION | 2 | `hig-foundations` | OH3, P2 |
| 21 | MEDIUM | CAUTION | 1 | `humanize-chinese` | P6 |
| 21 | MEDIUM | CAUTION | 2 | `javascript-typescript-typescript-scaffold` | PE3, TM3 |
| 21 | MEDIUM | CAUTION | 1 | `keyword-extractor` | P6 |
| 21 | MEDIUM | CAUTION | 1 | `lemmaly` | RA1 |
| 21 | MEDIUM | CAUTION | 8 | `llm-council` | E1×6, RA2×2 |
| 21 | MEDIUM | CAUTION | 4 | `makepad-deployment` | PE2×2, RA2×2 |
| 21 | MEDIUM | CAUTION | 1 | `microsoft-teams-automation` | E4 |
| 21 | MEDIUM | CAUTION | 1 | `paywall-upgrade-cro` | P6 |
| 21 | MEDIUM | CAUTION | 1 | `pre-release-review` | P6 |
| 21 | MEDIUM | CAUTION | 1 | `professional-proofreader` | P6 |
| 21 | MEDIUM | CAUTION | 1 | `speckit-updater` | RA1 |
| 21 | MEDIUM | CAUTION | 4 | `upstash-qstash` | E1×2, RA2, SSRF2 |
| 20 | LOW | CAUTION | 1 | `agenttrace-session-audit` | MP3 |
| 20 | LOW | CAUTION | 1 | `api-endpoint-builder` | TM1 |
| 20 | LOW | CAUTION | 1 | `architecture` | MP3 |
| 20 | LOW | CAUTION | 1 | `ask-matt` | MP3 |
| 20 | LOW | CAUTION | 1 | `audit-context-building` | MP3 |
| 20 | LOW | CAUTION | 1 | `c-pro` | MP3 |
| 20 | LOW | CAUTION | 1 | `carrier-relationship-management` | AR2 |
| 20 | LOW | CAUTION | 1 | `cc-skill-backend-patterns` | TM1 |
| 20 | LOW | CAUTION | 1 | `cc-skill-coding-standards` | TM1 |
| 20 | LOW | CAUTION | 1 | `incident-response-incident-response` | MP3 |
| 20 | LOW | CAUTION | 1 | `linkedin-profile-optimizer` | MP3 |
| 20 | LOW | CAUTION | 1 | `personal-tool-builder` | MP3 |
| 20 | LOW | CAUTION | 3 | `revops` | RA2×2, EA2 |
| 20 | LOW | CAUTION | 1 | `robius-matrix-integration` | YR4 |
| 20 | LOW | CAUTION | 1 | `rust-async-patterns` | YR4 |
| 20 | LOW | SAFE | 1 | `security-compliance-compliance-check` | YR4 |
| 20 | LOW | CAUTION | 1 | `sql-pro` | AR3 |
| 20 | LOW | CAUTION | 1 | `voice-agents` | MP3 |
| 19 | LOW | CAUTION | 3 | `weaviate` | AST7, LP3, PE2 |
| 19 | LOW | CAUTION | 3 | `youtube-summarizer` | PE2×2, RA2 |
| 18 | LOW | CAUTION | 3 | `agents-sdk` | RP1×2, EA2 |
| 18 | LOW | CAUTION | 1 | `anti-reversing-techniques` | YR1 |
| 18 | LOW | CAUTION | 1 | `context-management-context-save` | E4 |
| 18 | LOW | SAFE | 1 | `ddd-strategic-design` | E4 |
| 18 | LOW | CAUTION | 7 | `dependency-upgrade` | RP1×6, E1 |
| 18 | LOW | CAUTION | 2 | `evolution` | P2, SC2 |
| 18 | LOW | CAUTION | 1 | `go-playwright` | AR3 |
| 18 | LOW | CAUTION | 8 | `incident-runbook-templates` | E1×7, EA2 |
| 18 | LOW | CAUTION | 3 | `security-scanning-security-dependencies` | EA2×2, RP1 |
| 18 | LOW | CAUTION | 1 | `semgrep-rule-creator` | YR2 |
| 18 | LOW | SAFE | 1 | `team-collaboration-standup-notes` | E4 |
| 17 | LOW | CAUTION | 1 | `ai-native-cli` | PE3 |
| 17 | LOW | CAUTION | 1 | `angular` | P2 |
| 17 | LOW | CAUTION | 1 | `angular-ui-patterns` | P2 |
| 17 | LOW | SAFE | 1 | `azure-ai-agents-persistent-java` | PE3 |
| 17 | LOW | CAUTION | 1 | `azure-appconfiguration-java` | PE3 |
| 17 | LOW | CAUTION | 1 | `azure-communication-chat-java` | PE3 |
| 17 | LOW | CAUTION | 1 | `azure-compute-batch-java` | PE3 |
| 17 | LOW | CAUTION | 1 | `azure-cosmos-java` | PE3 |
| 17 | LOW | CAUTION | 1 | `azure-messaging-webpubsub-java` | PE3 |
| 17 | LOW | CAUTION | 1 | `azure-messaging-webpubsubservice-py` | PE3 |
| 17 | LOW | SAFE | 1 | `azure-monitor-ingestion-java` | PE3 |
| 17 | LOW | CAUTION | 1 | `azure-postgres-ts` | PE3 |
| 17 | LOW | CAUTION | 1 | `azure-resource-manager-playwright-dotnet` | PE3 |
| 17 | LOW | CAUTION | 1 | `azure-web-pubsub-ts` | PE3 |
| 17 | LOW | CAUTION | 3 | `bumblebee` | PE2×2, LP3 |
| 17 | LOW | CAUTION | 1 | `cold-email` | AR1 |
| 17 | LOW | CAUTION | 1 | `content-strategy` | PE3 |
| 17 | LOW | CAUTION | 5 | `expo-api-routes` | E1×4, RP1 |
| 17 | LOW | CAUTION | 1 | `git-pr-workflows-git-workflow` | TM1 |
| 17 | LOW | CAUTION | 1 | `github-workflow-automation` | TM1 |
| 17 | LOW | CAUTION | 1 | `google-docs-automation` | PE3 |
| 17 | LOW | CAUTION | 1 | `hugging-face-datasets` | PE3 |
| 17 | LOW | CAUTION | 1 | `odoo-performance-tuner` | P1 |
| 17 | LOW | CAUTION | 1 | `production-scheduling` | AR1 |
| 17 | LOW | CAUTION | 1 | `salesforce-development` | PE3 |
| 17 | LOW | CAUTION | 1 | `sveltekit` | P2 |
| 17 | LOW | CAUTION | 3 | `using-git-worktrees` | EA2×2, RA2 |
| 16 | LOW | CAUTION | 1 | `cc-skill-security-review` | OH1 |
| 16 | LOW | SAFE | 3 | `codebase-cleanup-deps-audit` | E1×2, RP1 |
| 16 | LOW | SAFE | 3 | `dependency-management-deps-audit` | E1×2, RP1 |
| 16 | LOW | CAUTION | 2 | `food-database-query` | AE4, AS3 |
| 16 | LOW | CAUTION | 1 | `frontend-mobile-security-xss-scan` | OH1 |
| 16 | LOW | CAUTION | 4 | `image-generator` | E1×3, RA2 |
| 16 | LOW | CAUTION | 3 | `mailtrap-managing-contacts` | P9×2, E1 |
| 16 | LOW | CAUTION | 2 | `monte-carlo-validation-notebook` | AST4, LP3 |
| 16 | LOW | CAUTION | 2 | `oss-hunter` | AST4, LP3 |
| 16 | LOW | CAUTION | 2 | `performance-profiling` | AST4, LP3 |
| 16 | LOW | CAUTION | 1 | `schema-markup-generator` | OH1 |
| 16 | LOW | CAUTION | 5 | `xvary-stock-research` | E1×4, LP3 |
| 15 | LOW | CAUTION | 2 | `adhx` | AS3, P4 |
| 15 | LOW | CAUTION | 1 | `aegisops-ai` | PE3 |
| 15 | LOW | CAUTION | 1 | `geminiignore-finops` | PE3 |
| 15 | LOW | CAUTION | 1 | `nestjs-expert` | PE3 |
| 15 | LOW | CAUTION | 1 | `news-sentiment-engine` | PE3 |
| 15 | LOW | CAUTION | 1 | `posix-shell-pro` | PE3 |
| 15 | LOW | CAUTION | 3 | `python-testing-patterns` | E1×2, RA2 |
| 15 | LOW | CAUTION | 1 | `saas-mvp-launcher` | PE3 |
| 15 | LOW | CAUTION | 2 | `sast-configuration` | EA2, RP1 |
| 15 | LOW | CAUTION | 4 | `shodan-reconnaissance` | E1×3, PE2 |
| 15 | LOW | CAUTION | 1 | `telegram-bot-builder` | PE3 |
| 15 | LOW | CAUTION | 1 | `x402-express-wrapper` | PE3 |
| 15 | LOW | CAUTION | 3 | `yield-intelligence` | E1×2, EA2 |
| 14 | LOW | CAUTION | 2 | `blueprint` | AS3, RA2 |
| 14 | LOW | CAUTION | 4 | `context-compression` | MP2×4 |
| 14 | LOW | CAUTION | 2 | `react-native-skills` | P4, RP1 |
| 14 | LOW | CAUTION | 5 | `returns-reverse-logistics` | EA2×5 |
| 14 | LOW | CAUTION | 2 | `sankhya-dashboard-html-jsp-custom-best-pratices` | AS3, RA2 |
| 14 | LOW | CAUTION | 3 | `skill-suggester` | P7×3 |
| 13 | LOW | CAUTION | 2 | `constant-time-analysis` | RA2×2 |
| 13 | LOW | CAUTION | 2 | `docker-expert` | RP1, TM3 |
| 13 | LOW | CAUTION | 3 | `ffuf-web-fuzzing` | E1×2, RA2 |
| 13 | LOW | CAUTION | 2 | `seo-image-gen` | P7, RA2 |
| 13 | LOW | CAUTION | 2 | `tmux` | EA2, RA2 |
| 13 | LOW | CAUTION | 3 | `verification-before-completion` | EA2×3 |
| 12 | LOW | CAUTION | 6 | `accesslint-diff` | RP1×6 |
| 12 | LOW | CAUTION | 3 | `accesslint-scan` | RP1×3 |
| 12 | LOW | SAFE | 2 | `airflow-dag-patterns` | E1, EA2 |
| 12 | LOW | CAUTION | 3 | `awt-e2e-testing` | RP1×3 |
| 12 | LOW | CAUTION | 4 | `browser-automation` | RP1×4 |
| 12 | LOW | CAUTION | 3 | `building-native-ui` | RP1×3 |
| 12 | LOW | SAFE | 3 | `changelog-automation` | RP1×3 |
| 12 | LOW | CAUTION | 4 | `database-migration` | RP1×4 |
| 12 | LOW | CAUTION | 3 | `database-migrations-migration-observability` | E1×3 |
| 12 | LOW | CAUTION | 5 | `drizzle-orm-expert` | RP1×5 |
| 12 | LOW | CAUTION | 4 | `e2e-testing-patterns` | RP1×4 |
| 12 | LOW | SAFE | 2 | `error-debugging-error-analysis` | E1, EA2 |
| 12 | LOW | SAFE | 2 | `error-diagnostics-error-analysis` | E1, EA2 |
| 12 | LOW | CAUTION | 2 | `filesystem-context` | AS3×2 |
| 12 | LOW | SAFE | 3 | `framework-migration-deps-upgrade` | RP1×3 |
| 12 | LOW | CAUTION | 5 | `hugging-face-dataset-viewer` | RP1×5 |
| 12 | LOW | CAUTION | 6 | `ii-commons` | RP1×6 |
| 12 | LOW | CAUTION | 3 | `jobgpt` | RP1×3 |
| 12 | LOW | CAUTION | 15 | `linkedin-cli` | P9×15 |
| 12 | LOW | CAUTION | 3 | `mailtrap-testing-with-sandbox` | P9×3 |
| 12 | LOW | CAUTION | 2 | `mcp-builder-ms` | E1, RP1 |
| 12 | LOW | CAUTION | 4 | `nx-workspace-patterns` | RP1×4 |
| 12 | LOW | CAUTION | 9 | `prisma-expert` | RP1×9 |
| 12 | LOW | CAUTION | 2 | `production-audit` | E1, EA2 |
| 12 | LOW | CAUTION | 11 | `protect-mcp-governance` | RP1×11 |
| 12 | LOW | SAFE | 4 | `react-modernization` | RP1×4 |
| 12 | LOW | CAUTION | 4 | `react-native-architecture` | RP1×4 |
| 12 | LOW | CAUTION | 2 | `segment-cdp` | E1, EA2 |
| 12 | LOW | CAUTION | 2 | `skill-check` | AS3×2 |
| 12 | LOW | CAUTION | 2 | `smart-git-automation` | EA2×2 |
| 12 | LOW | CAUTION | 9 | `trigger-dev` | RP1×9 |
| 12 | LOW | CAUTION | 5 | `upgrading-expo` | RP1×5 |
| 12 | LOW | CAUTION | 5 | `web3-testing` | RP1×5 |
| 11 | LOW | CAUTION | 2 | `azure-cosmos-db-py` | TM3×2 |
| 11 | LOW | CAUTION | 2 | `email-systems` | EA2×2 |
| 11 | LOW | CAUTION | 2 | `finishing-a-development-branch` | EA2×2 |
| 11 | LOW | CAUTION | 2 | `privacy-by-design` | EA2×2 |
| 11 | LOW | CAUTION | 2 | `production-code-audit` | EA2×2 |
| 11 | LOW | CAUTION | 2 | `python-pptx-generator` | EA2×2 |
| 10 | LOW | CAUTION | 2 | `ejentum-reasoning-harness` | RP1×2 |
| 10 | LOW | CAUTION | 2 | `expo-dev-client` | RP1×2 |
| 10 | LOW | CAUTION | 2 | `expo-ui-jetpack-compose` | RP1×2 |
| 10 | LOW | CAUTION | 2 | `expo-ui-swift-ui` | RP1×2 |
| 10 | LOW | CAUTION | 2 | `github-actions-advanced` | RP1×2 |
| 10 | LOW | CAUTION | 2 | `radix-ui-design-system` | RP1×2 |
| 10 | LOW | CAUTION | 2 | `vercel-deployment` | RP1×2 |
| 10 | LOW | CAUTION | 2 | `vscode-extension-guide-en` | RP1×2 |
| 10 | LOW | CAUTION | 11 | `workers-best-practices` | E1×11 |
| 9 | LOW | CAUTION | 8 | `agentmail` | E1×8 |
| 9 | LOW | CAUTION | 5 | `azure-storage-blob-py` | E5×5 |
| 9 | LOW | CAUTION | 4 | `azure-storage-file-share-py` | E5×4 |
| 9 | LOW | CAUTION | 2 | `prompt-engineer` | EA3, RA2 |
| 9 | LOW | CAUTION | 2 | `red-team-tools` | E1×2 |
| 9 | LOW | CAUTION | 1 | `subagent-orchestrator` | RP1 |
| 8 | LOW | CAUTION | 1 | `agent-memory-systems` | MP2 |
| 8 | LOW | CAUTION | 1 | `agent-squad` | EA4 |
| 8 | LOW | CAUTION | 1 | `asana-automation` | RA2 |
| 8 | LOW | CAUTION | 3 | `async-python-patterns` | E1×3 |
| 8 | LOW | CAUTION | 1 | `bamboohr-automation` | EA2 |
| 8 | LOW | CAUTION | 5 | `calendly-automation` | E1×5 |
| 8 | LOW | CAUTION | 1 | `ckw-design` | AE4 |
| 8 | LOW | SAFE | 1 | `commit` | EA2 |
| 8 | LOW | CAUTION | 1 | `conductor-implement` | EA2 |
| 8 | LOW | CAUTION | 1 | `context-fundamentals` | MP2 |
| 8 | LOW | CAUTION | 1 | `design-taste-frontend` | EA2 |
| 8 | LOW | CAUTION | 4 | `efficient-web-research` | E1×4 |
| 8 | LOW | CAUTION | 1 | `elon-musk` | AE4 |
| 8 | LOW | SAFE | 1 | `executing-plans` | EA2 |
| 8 | LOW | CAUTION | 1 | `gitlab-ci-patterns` | EA2 |
| 8 | LOW | CAUTION | 1 | `hig-components-layout` | MP2 |
| 8 | LOW | CAUTION | 1 | `invariant-guard` | AE4 |
| 8 | LOW | CAUTION | 1 | `learn` | EA1 |
| 8 | LOW | CAUTION | 1 | `lookdev` | EA2 |
| 8 | LOW | CAUTION | 1 | `makepad-platform` | MP2 |
| 8 | LOW | CAUTION | 1 | `mathguard` | AE4 |
| 8 | LOW | CAUTION | 1 | `monte-carlo-prevent` | AS3 |
| 8 | LOW | CAUTION | 5 | `n8n-node-configuration` | E1×5 |
| 8 | LOW | CAUTION | 1 | `networkx` | EA2 |
| 8 | LOW | CAUTION | 1 | `nutrition-analyzer` | AE4 |
| 8 | LOW | CAUTION | 1 | `odoo-shopify-integration` | EA2 |
| 8 | LOW | SAFE | 3 | `openapi-spec-generation` | E1×3 |
| 8 | LOW | CAUTION | 1 | `plugin-dev-agent-creator` | RA2 |
| 8 | LOW | CAUTION | 1 | `rag-engineer` | MP2 |
| 8 | LOW | CAUTION | 1 | `scientific-writing` | AE4 |
| 8 | LOW | CAUTION | 1 | `seaborn` | AE4 |
| 8 | LOW | CAUTION | 2 | `secrets-management` | RP1, TM1 |
| 8 | LOW | CAUTION | 1 | `seo-aeo-blog-writer` | AS3 |
| 8 | LOW | CAUTION | 1 | `seo-aeo-content-cluster` | AS3 |
| 8 | LOW | CAUTION | 1 | `seo-aeo-content-quality-auditor` | AS3 |
| 8 | LOW | SAFE | 1 | `seo-aeo-internal-linking` | AS3 |
| 8 | LOW | SAFE | 1 | `seo-aeo-keyword-research` | AS3 |
| 8 | LOW | CAUTION | 1 | `seo-aeo-landing-page-writer` | AS3 |
| 8 | LOW | CAUTION | 1 | `seo-aeo-meta-description-generator` | AS3 |
| 8 | LOW | CAUTION | 1 | `seo-aeo-schema-generator` | AS3 |
| 8 | LOW | CAUTION | 1 | `server-management` | PE2 |
| 8 | LOW | CAUTION | 1 | `skill-recommender` | AS3 |
| 8 | LOW | SAFE | 1 | `track-management` | RA2 |
| 8 | LOW | CAUTION | 1 | `ui-a11y` | AS3 |
| 8 | LOW | CAUTION | 1 | `ui-component` | AS3 |
| 8 | LOW | CAUTION | 1 | `ui-page` | AS3 |
| 8 | LOW | CAUTION | 1 | `ui-pattern` | AS3 |
| 8 | LOW | CAUTION | 1 | `ui-review` | AS3 |
| 8 | LOW | CAUTION | 1 | `ui-setup` | AS3 |
| 8 | LOW | CAUTION | 1 | `ui-tokens` | AS3 |
| 8 | LOW | CAUTION | 1 | `ux-audit` | AS3 |
| 8 | LOW | CAUTION | 1 | `ux-copy` | AS3 |
| 8 | LOW | CAUTION | 1 | `ux-feedback` | AS3 |
| 8 | LOW | CAUTION | 1 | `ux-flow` | AS3 |
| 7 | LOW | CAUTION | 1 | `ai-engineer` | EA2 |
| 7 | LOW | CAUTION | 1 | `api-patterns` | LP3 |
| 7 | LOW | CAUTION | 1 | `application-performance-performance-optimization` | EA2 |
| 7 | LOW | CAUTION | 1 | `backend-development-feature-development` | EA2 |
| 7 | LOW | CAUTION | 1 | `bash-pro` | PE2 |
| 7 | LOW | CAUTION | 1 | `behavioral-modes` | RA2 |
| 7 | LOW | CAUTION | 1 | `brooks-lint` | RP1 |
| 7 | LOW | CAUTION | 1 | `churn-prevention` | EA2 |
| 7 | LOW | CAUTION | 2 | `citation-management` | E1×2 |
| 7 | LOW | CAUTION | 1 | `cloudflare-workers-expert` | RP1 |
| 7 | LOW | CAUTION | 1 | `codex-review` | RP1 |
| 7 | LOW | CAUTION | 1 | `content-creator` | LP3 |
| 7 | LOW | CAUTION | 1 | `context-agent` | LP3 |
| 7 | LOW | CAUTION | 1 | `context-guardian` | LP3 |
| 7 | LOW | CAUTION | 1 | `context7-auto-research` | RP1 |
| 7 | LOW | CAUTION | 1 | `customs-trade-compliance` | EA2 |
| 7 | LOW | CAUTION | 1 | `database-design` | LP3 |
| 7 | LOW | CAUTION | 1 | `deployment-engineer` | EA2 |
| 7 | LOW | CAUTION | 1 | `emblemai-crypto-wallet` | RP1 |
| 7 | LOW | CAUTION | 1 | `energy-procurement` | P9 |
| 7 | LOW | CAUTION | 1 | `exa-search` | RP1 |
| 7 | LOW | CAUTION | 1 | `faf-wizard` | RP1 |
| 7 | LOW | CAUTION | 1 | `favicon` | PE2 |
| 7 | LOW | CAUTION | 1 | `firecrawl-scraper` | RP1 |
| 7 | LOW | CAUTION | 1 | `flowhunt-skill` | RP1 |
| 7 | LOW | CAUTION | 1 | `form-cro` | EA2 |
| 7 | LOW | CAUTION | 1 | `frontend-ui-dark-ts` | RP1 |
| 7 | LOW | CAUTION | 1 | `geo-fundamentals` | LP3 |
| 7 | LOW | CAUTION | 1 | `global-chat-agent-discovery` | RP1 |
| 7 | LOW | CAUTION | 1 | `graphql` | RP1 |
| 7 | LOW | CAUTION | 1 | `grpc-golang` | P9 |
| 7 | LOW | CAUTION | 1 | `hig-platforms` | EA2 |
| 7 | LOW | CAUTION | 1 | `hig-project-context` | RA2 |
| 7 | LOW | CAUTION | 1 | `hugging-face-vision-trainer` | LP3 |
| 7 | LOW | CAUTION | 1 | `i18n-localization` | LP3 |
| 7 | LOW | CAUTION | 1 | `infinity` | EA2 |
| 7 | LOW | CAUTION | 1 | `interview-coach` | RP1 |
| 7 | LOW | CAUTION | 1 | `kubernetes-architect` | EA2 |
| 7 | LOW | CAUTION | 1 | `leiloeiro-avaliacao` | LP3 |
| 7 | LOW | CAUTION | 1 | `leiloeiro-edital` | LP3 |
| 7 | LOW | CAUTION | 1 | `leiloeiro-ia` | LP3 |
| 7 | LOW | CAUTION | 1 | `leiloeiro-juridico` | LP3 |
| 7 | LOW | CAUTION | 1 | `leiloeiro-mercado` | LP3 |
| 7 | LOW | CAUTION | 1 | `leiloeiro-risco` | LP3 |
| 7 | LOW | CAUTION | 1 | `logic-lens` | RP1 |
| 7 | LOW | CAUTION | 1 | `logistics-exception-management` | EA2 |
| 7 | LOW | CAUTION | 1 | `longbridge` | RP1 |
| 7 | LOW | CAUTION | 1 | `macos-menubar-tuist-app` | RA2 |
| 7 | LOW | CAUTION | 2 | `makepad-splash` | E1×2 |
| 7 | LOW | SAFE | 2 | `mercury-mcp` | E1×2 |
| 7 | LOW | CAUTION | 1 | `monte-carlo-monitor-creation` | P9 |
| 7 | LOW | SAFE | 1 | `moyu` | EA2 |
| 7 | LOW | CAUTION | 2 | `n8n-code-javascript` | E1×2 |
| 7 | LOW | CAUTION | 1 | `not-a-vibe-coder` | EA2 |
| 7 | LOW | CAUTION | 1 | `pdf` | LP3 |
| 7 | LOW | CAUTION | 1 | `pdf-official` | LP3 |
| 7 | LOW | CAUTION | 1 | `performance-engineer` | EA2 |
| 7 | LOW | CAUTION | 1 | `plan-writing` | RP1 |
| 7 | LOW | CAUTION | 1 | `recallmax` | RP1 |
| 7 | LOW | CAUTION | 1 | `recsys-pipeline-architect` | RP1 |
| 7 | LOW | CAUTION | 1 | `requesting-code-review` | EA2 |
| 7 | LOW | CAUTION | 1 | `rich-elicitation` | EA2 |
| 7 | LOW | CAUTION | 1 | `sales-enablement` | EA2 |
| 7 | LOW | CAUTION | 1 | `sandbox-migrate-to-next` | RP1 |
| 7 | LOW | CAUTION | 1 | `screenshots` | RP1 |
| 7 | LOW | CAUTION | 1 | `seo` | RP1 |
| 7 | LOW | SAFE | 1 | `seo-fundamentals` | LP3 |
| 7 | LOW | CAUTION | 1 | `skill-issue` | RP1 |
| 7 | LOW | CAUTION | 1 | `skill-rails-upgrade` | EA2 |
| 7 | LOW | CAUTION | 1 | `slack-bot-builder` | EA2 |
| 7 | LOW | CAUTION | 6 | `slack-gif-creator` | SC1×4, SC4×2 |
| 7 | LOW | CAUTION | 1 | `socialclaw` | RP1 |
| 7 | LOW | CAUTION | 1 | `squirrel` | RP1 |
| 7 | LOW | CAUTION | 1 | `stitch-loop` | RP1 |
| 7 | LOW | CAUTION | 1 | `systems-programming-rust-project` | RA2 |
| 7 | LOW | CAUTION | 1 | `tavily-web` | RP1 |
| 7 | LOW | CAUTION | 1 | `telegram-mini-app` | EA2 |
| 7 | LOW | CAUTION | 1 | `threejs-animation` | EA4 |
| 7 | LOW | CAUTION | 1 | `tool-use-guardian` | RP1 |
| 7 | LOW | CAUTION | 1 | `unship` | RP1 |
| 7 | LOW | CAUTION | 1 | `uxui-principles` | RP1 |
| 7 | LOW | CAUTION | 1 | `videodb-skills` | RP1 |
| 7 | LOW | CAUTION | 1 | `x-twitter-scraper` | RP1 |
| 7 | LOW | CAUTION | 1 | `youtube-full` | RP1 |
| 6 | LOW | CAUTION | 1 | `ai-engineering-toolkit` | RA2 |
| 6 | LOW | CAUTION | 1 | `anti-sycophancy` | RA2 |
| 6 | LOW | CAUTION | 1 | `appdeploy` | E1 |
| 6 | LOW | CAUTION | 27 | `canvas-design` | EA3×27 |
| 6 | LOW | CAUTION | 1 | `deployment-pipeline-design` | E1 |
| 6 | LOW | CAUTION | 1 | `hugging-face-papers` | E1 |
| 6 | LOW | CAUTION | 1 | `maxia` | E1 |
| 6 | LOW | CAUTION | 1 | `moodle-external-api-development` | E1 |
| 6 | LOW | CAUTION | 1 | `odoo-rpc-api` | E1 |
| 6 | LOW | CAUTION | 1 | `postgresql` | OH3 |
| 6 | LOW | SAFE | 1 | `python-packaging` | RA2 |
| 6 | LOW | CAUTION | 1 | `shopify-apps` | SSRF3 |
| 6 | LOW | CAUTION | 1 | `speed` | RA2 |
| 6 | LOW | CAUTION | 1 | `subagent-driven-development` | RA2 |
| 6 | LOW | CAUTION | 1 | `vibers-code-review` | E1 |
| 5 | LOW | CAUTION | 1 | `apify-actorization` | E1 |
| 5 | LOW | CAUTION | 1 | `azure-functions` | E1 |
| 5 | LOW | CAUTION | 1 | `azure-mgmt-apicenter-dotnet` | E1 |
| 5 | LOW | CAUTION | 1 | `buywhere-product-catalog` | E1 |
| 5 | LOW | SAFE | 1 | `code-documentation-doc-generate` | E1 |
| 5 | LOW | SAFE | 1 | `documentation-generation-doc-generate` | E1 |
| 5 | LOW | CAUTION | 1 | `expo-cicd-workflows` | E1 |
| 5 | LOW | CAUTION | 1 | `jq` | E1 |
| 5 | LOW | CAUTION | 1 | `kaizen` | E1 |
| 5 | LOW | CAUTION | 1 | `m365-agents-dotnet` | E1 |
| 5 | LOW | CAUTION | 1 | `m365-agents-py` | E1 |
| 5 | LOW | CAUTION | 1 | `microsoft-azure-webjobs-extensions-authentication-events-dotnet` | E1 |
| 5 | LOW | CAUTION | 1 | `molykit` | E1 |
| 5 | LOW | CAUTION | 1 | `n8n-expression-syntax` | E1 |
| 5 | LOW | SAFE | 1 | `nextjs-app-router-patterns` | E1 |
| 5 | LOW | CAUTION | 1 | `pagespeed-enhancer` | E1 |
| 5 | LOW | CAUTION | 1 | `robius-app-architecture` | RA2 |
| 5 | LOW | CAUTION | 1 | `team-collaboration-issue` | E1 |
| 5 | LOW | CAUTION | 1 | `temporal-python-testing` | E1 |
| 3 | LOW | SAFE | 1 | `employment-contract-templates` | EA3 |
| 3 | LOW | CAUTION | 1 | `hig-components-controls` | EA3 |
| 3 | LOW | CAUTION | 1 | `hig-components-system` | EA3 |
| 3 | LOW | CAUTION | 1 | `model-compression-exploration` | EA3 |
| 3 | LOW | SAFE | 1 | `multi-agent-brainstorming` | EA3 |
| 3 | LOW | CAUTION | 1 | `odoo-upgrade-advisor` | EA3 |
| 3 | LOW | CAUTION | 1 | `sql-injection-testing` | EA3 |
| 3 | LOW | CAUTION | 1 | `working-with-coreai` | EA3 |
| 0 | LOW | CAUTION | 0 | `00-andruia-consultant` | — |
| 0 | LOW | CAUTION | 0 | `10-andruia-skill-smith` | — |
| 0 | LOW | CAUTION | 0 | `20-andruia-niche-intelligence` | — |
| 0 | LOW | CAUTION | 0 | `3d-web-experience` | — |
| 0 | LOW | CAUTION | 0 | `ab-test-setup` | — |
| 0 | LOW | CAUTION | 0 | `acceptance-orchestrator` | — |
| 0 | LOW | SAFE | 0 | `accessibility-compliance-accessibility-audit` | — |
| 0 | LOW | CAUTION | 0 | `accesslint-audit` | — |
| 0 | LOW | CAUTION | 0 | `accint-solve` | — |
| 0 | LOW | CAUTION | 0 | `activecampaign-automation` | — |
| 0 | LOW | SAFE | 0 | `address-github-comments` | — |
| 0 | LOW | CAUTION | 0 | `advanced-evaluation` | — |
| 0 | LOW | CAUTION | 0 | `advogado-criminal` | — |
| 0 | LOW | CAUTION | 0 | `advogado-especialista` | — |
| 0 | LOW | CAUTION | 0 | `agent-framework-azure-ai-py` | — |
| 0 | LOW | CAUTION | 0 | `agent-manager-skill` | — |
| 0 | LOW | CAUTION | 0 | `agent-memory-mcp` | — |
| 0 | LOW | CAUTION | 0 | `agent-orchestration-improve-agent` | — |
| 0 | LOW | CAUTION | 0 | `agent-orchestration-multi-agent-optimize` | — |
| 0 | LOW | CAUTION | 0 | `agent-tool-builder` | — |
| 0 | LOW | CAUTION | 0 | `agentfolio` | — |
| 0 | LOW | CAUTION | 0 | `agentic-actions-auditor` | — |
| 0 | LOW | CAUTION | 0 | `agents-md` | — |
| 0 | LOW | CAUTION | 0 | `agents-v2-py` | — |
| 0 | LOW | CAUTION | 0 | `ai-agent-development` | — |
| 0 | LOW | CAUTION | 0 | `ai-agents-architect` | — |
| 0 | LOW | CAUTION | 0 | `ai-analyzer` | — |
| 0 | LOW | SAFE | 0 | `ai-dev-jobs-mcp` | — |
| 0 | LOW | CAUTION | 0 | `ai-loop` | — |
| 0 | LOW | CAUTION | 0 | `ai-ml` | — |
| 0 | LOW | CAUTION | 0 | `ai-seo` | — |
| 0 | LOW | CAUTION | 0 | `airtable-automation` | — |
| 0 | LOW | CAUTION | 0 | `akf-trust-metadata` | — |
| 0 | LOW | CAUTION | 0 | `algolia-search` | — |
| 0 | LOW | CAUTION | 0 | `algorithmic-art` | — |
| 0 | LOW | CAUTION | 0 | `alpha-vantage` | — |
| 0 | LOW | CAUTION | 0 | `amazon-alexa` | — |
| 0 | LOW | CAUTION | 0 | `amplitude-automation` | — |
| 0 | LOW | CAUTION | 0 | `analytics-product` | — |
| 0 | LOW | SAFE | 0 | `analytics-tracking` | — |
| 0 | LOW | CAUTION | 0 | `andrej-karpathy` | — |
| 0 | LOW | CAUTION | 0 | `android-cli` | — |
| 0 | LOW | CAUTION | 0 | `android-jetpack-compose-expert` | — |
| 0 | LOW | CAUTION | 0 | `android-ui-journey-testing` | — |
| 0 | LOW | CAUTION | 0 | `android_ui_verification` | — |
| 0 | LOW | CAUTION | 0 | `angular-migration` | — |
| 0 | LOW | CAUTION | 0 | `angular-state-management` | — |
| 0 | LOW | CAUTION | 0 | `animejs-animation` | — |
| 0 | LOW | CAUTION | 0 | `antigravity-agent-manager` | — |
| 0 | LOW | CAUTION | 0 | `antigravity-design-expert` | — |
| 0 | LOW | CAUTION | 0 | `antigravity-skill-orchestrator` | — |
| 0 | LOW | CAUTION | 0 | `antigravity-workflows` | — |
| 0 | LOW | CAUTION | 0 | `aomi-transact` | — |
| 0 | LOW | CAUTION | 0 | `api-documentation` | — |
| 0 | LOW | CAUTION | 0 | `api-documenter` | — |
| 0 | LOW | SAFE | 0 | `api-security-testing` | — |
| 0 | LOW | CAUTION | 0 | `app-store-changelog` | — |
| 0 | LOW | CAUTION | 0 | `apple-notes-search` | — |
| 0 | LOW | CAUTION | 0 | `architect-review` | — |
| 0 | LOW | SAFE | 0 | `architecture-patterns` | — |
| 0 | LOW | CAUTION | 0 | `arm-cortex-expert` | — |
| 0 | LOW | CAUTION | 0 | `arrowspace` | — |
| 0 | LOW | CAUTION | 0 | `article-illustrations` | — |
| 0 | LOW | CAUTION | 0 | `ask-questions-if-underspecified` | — |
| 0 | LOW | CAUTION | 0 | `astropy` | — |
| 0 | LOW | CAUTION | 0 | `attack-tree-construction` | — |
| 0 | LOW | CAUTION | 0 | `avalonia-layout-zafiro` | — |
| 0 | LOW | CAUTION | 0 | `avalonia-viewmodels-zafiro` | — |
| 0 | LOW | CAUTION | 0 | `avalonia-zafiro-development` | — |
| 0 | LOW | CAUTION | 0 | `avoid-ai-writing` | — |
| 0 | LOW | CAUTION | 0 | `awareness-stage-mapper` | — |
| 0 | LOW | CAUTION | 0 | `aws-cost-cleanup` | — |
| 0 | LOW | CAUTION | 0 | `aws-cost-optimizer` | — |
| 0 | LOW | SAFE | 0 | `aws-skills` | — |
| 0 | LOW | CAUTION | 0 | `ax-extract-workflow` | — |
| 0 | LOW | CAUTION | 0 | `axiom` | — |
| 0 | LOW | CAUTION | 0 | `azure-ai-agents-persistent-dotnet` | — |
| 0 | LOW | CAUTION | 0 | `azure-ai-anomalydetector-java` | — |
| 0 | LOW | CAUTION | 0 | `azure-ai-contentsafety-java` | — |
| 0 | LOW | CAUTION | 0 | `azure-ai-contentsafety-py` | — |
| 0 | LOW | CAUTION | 0 | `azure-ai-contentsafety-ts` | — |
| 0 | LOW | CAUTION | 0 | `azure-ai-contentunderstanding-py` | — |
| 0 | LOW | CAUTION | 0 | `azure-ai-document-intelligence-dotnet` | — |
| 0 | LOW | CAUTION | 0 | `azure-ai-document-intelligence-ts` | — |
| 0 | LOW | CAUTION | 0 | `azure-ai-formrecognizer-java` | — |
| 0 | LOW | CAUTION | 0 | `azure-ai-ml-py` | — |
| 0 | LOW | CAUTION | 0 | `azure-ai-openai-dotnet` | — |
| 0 | LOW | CAUTION | 0 | `azure-ai-projects-dotnet` | — |
| 0 | LOW | CAUTION | 0 | `azure-ai-projects-java` | — |
| 0 | LOW | CAUTION | 0 | `azure-ai-projects-py` | — |
| 0 | LOW | CAUTION | 0 | `azure-ai-projects-ts` | — |
| 0 | LOW | SAFE | 0 | `azure-ai-textanalytics-py` | — |
| 0 | LOW | CAUTION | 0 | `azure-ai-transcription-py` | — |
| 0 | LOW | CAUTION | 0 | `azure-ai-translation-document-py` | — |
| 0 | LOW | SAFE | 0 | `azure-ai-translation-text-py` | — |
| 0 | LOW | CAUTION | 0 | `azure-ai-translation-ts` | — |
| 0 | LOW | CAUTION | 0 | `azure-ai-vision-imageanalysis-java` | — |
| 0 | LOW | CAUTION | 0 | `azure-ai-vision-imageanalysis-py` | — |
| 0 | LOW | CAUTION | 0 | `azure-ai-voicelive-dotnet` | — |
| 0 | LOW | SAFE | 0 | `azure-ai-voicelive-java` | — |
| 0 | LOW | CAUTION | 0 | `azure-ai-voicelive-py` | — |
| 0 | LOW | CAUTION | 0 | `azure-ai-voicelive-ts` | — |
| 0 | LOW | CAUTION | 0 | `azure-appconfiguration-py` | — |
| 0 | LOW | CAUTION | 0 | `azure-appconfiguration-ts` | — |
| 0 | LOW | CAUTION | 0 | `azure-communication-callautomation-java` | — |
| 0 | LOW | CAUTION | 0 | `azure-communication-callingserver-java` | — |
| 0 | LOW | SAFE | 0 | `azure-communication-sms-java` | — |
| 0 | LOW | CAUTION | 0 | `azure-containerregistry-py` | — |
| 0 | LOW | CAUTION | 0 | `azure-cosmos-py` | — |
| 0 | LOW | CAUTION | 0 | `azure-cosmos-rust` | — |
| 0 | LOW | CAUTION | 0 | `azure-cosmos-ts` | — |
| 0 | LOW | CAUTION | 0 | `azure-data-tables-java` | — |
| 0 | LOW | CAUTION | 0 | `azure-data-tables-py` | — |
| 0 | LOW | CAUTION | 0 | `azure-eventgrid-dotnet` | — |
| 0 | LOW | CAUTION | 0 | `azure-eventgrid-java` | — |
| 0 | LOW | CAUTION | 0 | `azure-eventgrid-py` | — |
| 0 | LOW | CAUTION | 0 | `azure-eventhub-dotnet` | — |
| 0 | LOW | CAUTION | 0 | `azure-eventhub-java` | — |
| 0 | LOW | CAUTION | 0 | `azure-eventhub-py` | — |
| 0 | LOW | SAFE | 0 | `azure-eventhub-rust` | — |
| 0 | LOW | CAUTION | 0 | `azure-eventhub-ts` | — |
| 0 | LOW | CAUTION | 0 | `azure-identity-dotnet` | — |
| 0 | LOW | CAUTION | 0 | `azure-identity-java` | — |
| 0 | LOW | CAUTION | 0 | `azure-identity-py` | — |
| 0 | LOW | CAUTION | 0 | `azure-identity-rust` | — |
| 0 | LOW | CAUTION | 0 | `azure-identity-ts` | — |
| 0 | LOW | CAUTION | 0 | `azure-keyvault-certificates-rust` | — |
| 0 | LOW | CAUTION | 0 | `azure-keyvault-keys-rust` | — |
| 0 | LOW | CAUTION | 0 | `azure-keyvault-keys-ts` | — |
| 0 | LOW | CAUTION | 0 | `azure-keyvault-py` | — |
| 0 | LOW | CAUTION | 0 | `azure-keyvault-secrets-rust` | — |
| 0 | LOW | CAUTION | 0 | `azure-keyvault-secrets-ts` | — |
| 0 | LOW | CAUTION | 0 | `azure-maps-search-dotnet` | — |
| 0 | LOW | CAUTION | 0 | `azure-mgmt-apicenter-py` | — |
| 0 | LOW | CAUTION | 0 | `azure-mgmt-apimanagement-dotnet` | — |
| 0 | LOW | CAUTION | 0 | `azure-mgmt-apimanagement-py` | — |
| 0 | LOW | CAUTION | 0 | `azure-mgmt-applicationinsights-dotnet` | — |
| 0 | LOW | CAUTION | 0 | `azure-mgmt-arizeaiobservabilityeval-dotnet` | — |
| 0 | LOW | CAUTION | 0 | `azure-mgmt-botservice-dotnet` | — |
| 0 | LOW | CAUTION | 0 | `azure-mgmt-botservice-py` | — |
| 0 | LOW | CAUTION | 0 | `azure-mgmt-fabric-dotnet` | — |
| 0 | LOW | CAUTION | 0 | `azure-mgmt-fabric-py` | — |
| 0 | LOW | CAUTION | 0 | `azure-mgmt-mongodbatlas-dotnet` | — |
| 0 | LOW | CAUTION | 0 | `azure-mgmt-weightsandbiases-dotnet` | — |
| 0 | LOW | CAUTION | 0 | `azure-monitor-ingestion-py` | — |
| 0 | LOW | CAUTION | 0 | `azure-monitor-opentelemetry-exporter-py` | — |
| 0 | LOW | CAUTION | 0 | `azure-monitor-opentelemetry-py` | — |
| 0 | LOW | CAUTION | 0 | `azure-monitor-opentelemetry-ts` | — |
| 0 | LOW | SAFE | 0 | `azure-monitor-query-py` | — |
| 0 | LOW | CAUTION | 0 | `azure-resource-manager-cosmosdb-dotnet` | — |
| 0 | LOW | CAUTION | 0 | `azure-resource-manager-durabletask-dotnet` | — |
| 0 | LOW | CAUTION | 0 | `azure-resource-manager-mysql-dotnet` | — |
| 0 | LOW | CAUTION | 0 | `azure-resource-manager-postgresql-dotnet` | — |
| 0 | LOW | CAUTION | 0 | `azure-resource-manager-redis-dotnet` | — |
| 0 | LOW | CAUTION | 0 | `azure-resource-manager-sql-dotnet` | — |
| 0 | LOW | CAUTION | 0 | `azure-search-documents-dotnet` | — |
| 0 | LOW | CAUTION | 0 | `azure-search-documents-py` | — |
| 0 | LOW | CAUTION | 0 | `azure-search-documents-ts` | — |
| 0 | LOW | CAUTION | 0 | `azure-security-keyvault-keys-dotnet` | — |
| 0 | LOW | CAUTION | 0 | `azure-security-keyvault-keys-java` | — |
| 0 | LOW | CAUTION | 0 | `azure-security-keyvault-secrets-java` | — |
| 0 | LOW | CAUTION | 0 | `azure-servicebus-py` | — |
| 0 | LOW | CAUTION | 0 | `azure-storage-blob-java` | — |
| 0 | LOW | CAUTION | 0 | `azure-storage-blob-rust` | — |
| 0 | LOW | CAUTION | 0 | `azure-storage-blob-ts` | — |
| 0 | LOW | CAUTION | 0 | `azure-storage-file-datalake-py` | — |
| 0 | LOW | CAUTION | 0 | `azure-storage-file-share-ts` | — |
| 0 | LOW | CAUTION | 0 | `azure-storage-queue-py` | — |
| 0 | LOW | CAUTION | 0 | `azure-storage-queue-ts` | — |
| 0 | LOW | CAUTION | 0 | `backend-architect` | — |
| 0 | LOW | CAUTION | 0 | `backend-security-coder` | — |
| 0 | LOW | CAUTION | 0 | `backtesting-frameworks` | — |
| 0 | LOW | CAUTION | 0 | `baseline-ui` | — |
| 0 | LOW | CAUTION | 0 | `bash-scripting` | — |
| 0 | LOW | CAUTION | 0 | `bazel-build-optimization` | — |
| 0 | LOW | CAUTION | 0 | `bdi-mental-states` | — |
| 0 | LOW | SAFE | 0 | `bdistill-behavioral-xray` | — |
| 0 | LOW | CAUTION | 0 | `bdistill-knowledge-extraction` | — |
| 0 | LOW | CAUTION | 0 | `bevy-ecs-expert` | — |
| 0 | LOW | CAUTION | 0 | `bilig-workpaper` | — |
| 0 | LOW | CAUTION | 0 | `bill-gates` | — |
| 0 | LOW | CAUTION | 0 | `billing-automation` | — |
| 0 | LOW | CAUTION | 0 | `binary-analysis-patterns` | — |
| 0 | LOW | CAUTION | 0 | `biopython` | — |
| 0 | LOW | CAUTION | 0 | `bitbucket-automation` | — |
| 0 | LOW | CAUTION | 0 | `blockchain-developer` | — |
| 0 | LOW | CAUTION | 0 | `blockrun` | — |
| 0 | LOW | CAUTION | 0 | `blog-writing-guide` | — |
| 0 | LOW | CAUTION | 0 | `box-automation` | — |
| 0 | LOW | SAFE | 0 | `brainstorming` | — |
| 0 | LOW | CAUTION | 0 | `brand-guidelines` | — |
| 0 | LOW | CAUTION | 0 | `brand-guidelines-anthropic` | — |
| 0 | LOW | CAUTION | 0 | `brand-guidelines-community` | — |
| 0 | LOW | SAFE | 0 | `brand-perception-psychologist` | — |
| 0 | LOW | CAUTION | 0 | `brave-man` | — |
| 0 | LOW | CAUTION | 0 | `brevo-automation` | — |
| 0 | LOW | CAUTION | 0 | `browser-extension-builder` | — |
| 0 | LOW | CAUTION | 0 | `bug-hunter` | — |
| 0 | LOW | CAUTION | 0 | `bugs-are-annoying` | — |
| 0 | LOW | CAUTION | 0 | `build` | — |
| 0 | LOW | CAUTION | 0 | `bullmq-specialist` | — |
| 0 | LOW | CAUTION | 0 | `business-analyst` | — |
| 0 | LOW | CAUTION | 0 | `busybox-on-windows` | — |
| 0 | LOW | CAUTION | 0 | `c4-architecture-c4-architecture` | — |
| 0 | LOW | CAUTION | 0 | `c4-code` | — |
| 0 | LOW | CAUTION | 0 | `c4-component` | — |
| 0 | LOW | CAUTION | 0 | `c4-container` | — |
| 0 | LOW | CAUTION | 0 | `c4-context` | — |
| 0 | LOW | CAUTION | 0 | `cal-com-automation` | — |
| 0 | LOW | SAFE | 0 | `canva-automation` | — |
| 0 | LOW | CAUTION | 0 | `cc-skill-clickhouse-io` | — |
| 0 | LOW | CAUTION | 0 | `cc-skill-frontend-patterns` | — |
| 0 | LOW | CAUTION | 0 | `cc-skill-project-guidelines-example` | — |
| 0 | LOW | CAUTION | 0 | `cdk-patterns` | — |
| 0 | LOW | CAUTION | 0 | `chat-widget` | — |
| 0 | LOW | CAUTION | 0 | `chrome-extension-developer` | — |
| 0 | LOW | CAUTION | 0 | `circleci-automation` | — |
| 0 | LOW | CAUTION | 0 | `cirq` | — |
| 0 | LOW | CAUTION | 0 | `clarvia-aeo-check` | — |
| 0 | LOW | SAFE | 0 | `claude-ally-health` | — |
| 0 | LOW | CAUTION | 0 | `claude-d3js-skill` | — |
| 0 | LOW | SAFE | 0 | `claude-scientific-skills` | — |
| 0 | LOW | SAFE | 0 | `claude-speed-reader` | — |
| 0 | LOW | CAUTION | 0 | `clean-code` | — |
| 0 | LOW | CAUTION | 0 | `clerk-auth` | — |
| 0 | LOW | CAUTION | 0 | `clickup-automation` | — |
| 0 | LOW | CAUTION | 0 | `close-automation` | — |
| 0 | LOW | CAUTION | 0 | `closed-loop-delivery` | — |
| 0 | LOW | CAUTION | 0 | `cloud-architect` | — |
| 0 | LOW | CAUTION | 0 | `cloud-devops` | — |
| 0 | LOW | CAUTION | 0 | `cloudflare-one` | — |
| 0 | LOW | CAUTION | 0 | `cloudflare-one-migrations` | — |
| 0 | LOW | CAUTION | 0 | `cloudformation-best-practices` | — |
| 0 | LOW | CAUTION | 0 | `coda-automation` | — |
| 0 | LOW | SAFE | 0 | `code-documentation-code-explain` | — |
| 0 | LOW | CAUTION | 0 | `code-refactoring-context-restore` | — |
| 0 | LOW | CAUTION | 0 | `code-refactoring-refactor-clean` | — |
| 0 | LOW | CAUTION | 0 | `code-refactoring-tech-debt` | — |
| 0 | LOW | CAUTION | 0 | `code-review-ai-ai-review` | — |
| 0 | LOW | CAUTION | 0 | `code-review-checklist` | — |
| 0 | LOW | SAFE | 0 | `code-review-excellence` | — |
| 0 | LOW | CAUTION | 0 | `code-reviewer` | — |
| 0 | LOW | CAUTION | 0 | `code-simplifier` | — |
| 0 | LOW | CAUTION | 0 | `codebase-cleanup-refactor-clean` | — |
| 0 | LOW | CAUTION | 0 | `codebase-cleanup-tech-debt` | — |
| 0 | LOW | CAUTION | 0 | `codebase-design` | — |
| 0 | LOW | CAUTION | 0 | `codebase-to-wordpress-converter` | — |
| 0 | LOW | CAUTION | 0 | `codex-fable5` | — |
| 0 | LOW | SAFE | 0 | `competitive-landscape` | — |
| 0 | LOW | CAUTION | 0 | `competitor-alternatives` | — |
| 0 | LOW | CAUTION | 0 | `complexity-cuts` | — |
| 0 | LOW | CAUTION | 0 | `composition-patterns` | — |
| 0 | LOW | CAUTION | 0 | `comprehensive-review-full-review` | — |
| 0 | LOW | CAUTION | 0 | `computer-vision-expert` | — |
| 0 | LOW | CAUTION | 0 | `concise-planning` | — |
| 0 | LOW | CAUTION | 0 | `conductor-new-track` | — |
| 0 | LOW | CAUTION | 0 | `conductor-status` | — |
| 0 | LOW | CAUTION | 0 | `conductor-validator` | — |
| 0 | LOW | CAUTION | 0 | `confluence-automation` | — |
| 0 | LOW | CAUTION | 0 | `content-marketer` | — |
| 0 | LOW | CAUTION | 0 | `context-degradation` | — |
| 0 | LOW | CAUTION | 0 | `context-driven-development` | — |
| 0 | LOW | CAUTION | 0 | `context-management-context-restore` | — |
| 0 | LOW | CAUTION | 0 | `context-manager` | — |
| 0 | LOW | CAUTION | 0 | `context-optimization` | — |
| 0 | LOW | CAUTION | 0 | `context-window-management` | — |
| 0 | LOW | CAUTION | 0 | `conversation-memory` | — |
| 0 | LOW | CAUTION | 0 | `convertkit-automation` | — |
| 0 | LOW | CAUTION | 0 | `copy-editing` | — |
| 0 | LOW | CAUTION | 0 | `copywriting` | — |
| 0 | LOW | CAUTION | 0 | `copywriting-psychologist` | — |
| 0 | LOW | CAUTION | 0 | `core-components` | — |
| 0 | LOW | CAUTION | 0 | `cost-optimization` | — |
| 0 | LOW | CAUTION | 0 | `cpp-pro` | — |
| 0 | LOW | CAUTION | 0 | `cqrs-implementation` | — |
| 0 | LOW | CAUTION | 0 | `create-branch` | — |
| 0 | LOW | CAUTION | 0 | `create-issue-gate` | — |
| 0 | LOW | SAFE | 0 | `create-pr` | — |
| 0 | LOW | CAUTION | 0 | `crewai` | — |
| 0 | LOW | CAUTION | 0 | `crossframe-casebook` | — |
| 0 | LOW | CAUTION | 0 | `crossframe-critical` | — |
| 0 | LOW | CAUTION | 0 | `crossframe-debate` | — |
| 0 | LOW | CAUTION | 0 | `crossframe-dialogue` | — |
| 0 | LOW | CAUTION | 0 | `crossframe-essay` | — |
| 0 | LOW | CAUTION | 0 | `crossframe-notebook` | — |
| 0 | LOW | CAUTION | 0 | `crossframe-org` | — |
| 0 | LOW | CAUTION | 0 | `crossframe-public` | — |
| 0 | LOW | CAUTION | 0 | `crossframe-review` | — |
| 0 | LOW | CAUTION | 0 | `crossframe-suite` | — |
| 0 | LOW | CAUTION | 0 | `crossframe-teach` | — |
| 0 | LOW | CAUTION | 0 | `crypto-bd-agent` | — |
| 0 | LOW | CAUTION | 0 | `csharp-pro` | — |
| 0 | LOW | SAFE | 0 | `customer-psychographic-profiler` | — |
| 0 | LOW | CAUTION | 0 | `customer-support` | — |
| 0 | LOW | CAUTION | 0 | `cv-generator` | — |
| 0 | LOW | CAUTION | 0 | `daily` | — |
| 0 | LOW | CAUTION | 0 | `daily-gift` | — |
| 0 | LOW | CAUTION | 0 | `daily-news-report` | — |
| 0 | LOW | CAUTION | 0 | `data-engineer` | — |
| 0 | LOW | CAUTION | 0 | `data-engineering-data-driven-feature` | — |
| 0 | LOW | CAUTION | 0 | `data-engineering-data-pipeline` | — |
| 0 | LOW | CAUTION | 0 | `data-quality-frameworks` | — |
| 0 | LOW | CAUTION | 0 | `data-scientist` | — |
| 0 | LOW | CAUTION | 0 | `data-storytelling` | — |
| 0 | LOW | CAUTION | 0 | `data-structure-protocol` | — |
| 0 | LOW | CAUTION | 0 | `database` | — |
| 0 | LOW | CAUTION | 0 | `database-admin` | — |
| 0 | LOW | CAUTION | 0 | `database-architect` | — |
| 0 | LOW | SAFE | 0 | `database-migrations-sql-migrations` | — |
| 0 | LOW | CAUTION | 0 | `database-optimizer` | — |
| 0 | LOW | CAUTION | 0 | `datadog-automation` | — |
| 0 | LOW | SAFE | 0 | `dbt-transformation-patterns` | — |
| 0 | LOW | SAFE | 0 | `ddd-context-mapping` | — |
| 0 | LOW | SAFE | 0 | `ddd-tactical-patterns` | — |
| 0 | LOW | CAUTION | 0 | `debug-buttercup` | — |
| 0 | LOW | CAUTION | 0 | `debugger` | — |
| 0 | LOW | SAFE | 0 | `debugging-strategies` | — |
| 0 | LOW | CAUTION | 0 | `debugging-toolkit` | — |
| 0 | LOW | CAUTION | 0 | `debugging-toolkit-smart-debug` | — |
| 0 | LOW | CAUTION | 0 | `deep-research` | — |
| 0 | LOW | CAUTION | 0 | `defi-protocol-templates` | — |
| 0 | LOW | SAFE | 0 | `defuddle` | — |
| 0 | LOW | CAUTION | 0 | `deployment-validation-config-validate` | — |
| 0 | LOW | SAFE | 0 | `design-orchestration` | — |
| 0 | LOW | CAUTION | 0 | `design-spells` | — |
| 0 | LOW | CAUTION | 0 | `deterministic-design` | — |
| 0 | LOW | CAUTION | 0 | `devcontainer-setup` | — |
| 0 | LOW | CAUTION | 0 | `development` | — |
| 0 | LOW | CAUTION | 0 | `devops-troubleshooter` | — |
| 0 | LOW | CAUTION | 0 | `differential-review` | — |
| 0 | LOW | CAUTION | 0 | `dispatching-parallel-agents` | — |
| 0 | LOW | CAUTION | 0 | `distributed-tracing` | — |
| 0 | LOW | CAUTION | 0 | `django-access-review` | — |
| 0 | LOW | CAUTION | 0 | `django-perf-review` | — |
| 0 | LOW | CAUTION | 0 | `django-pro` | — |
| 0 | LOW | CAUTION | 0 | `doc-coauthoring` | — |
| 0 | LOW | CAUTION | 0 | `doc2math` | — |
| 0 | LOW | CAUTION | 0 | `docs-architect` | — |
| 0 | LOW | CAUTION | 0 | `documentation` | — |
| 0 | LOW | CAUTION | 0 | `documentation-templates` | — |
| 0 | LOW | CAUTION | 0 | `docusign-automation` | — |
| 0 | LOW | CAUTION | 0 | `domain-driven-design` | — |
| 0 | LOW | CAUTION | 0 | `domain-modeling` | — |
| 0 | LOW | CAUTION | 0 | `dos-verify-done-claims` | — |
| 0 | LOW | CAUTION | 0 | `dotnet-architect` | — |
| 0 | LOW | CAUTION | 0 | `dotnet-backend` | — |
| 0 | LOW | CAUTION | 0 | `dotnet-backend-patterns` | — |
| 0 | LOW | CAUTION | 0 | `dropbox-automation` | — |
| 0 | LOW | CAUTION | 0 | `durable-objects` | — |
| 0 | LOW | CAUTION | 0 | `dwarf-expert` | — |
| 0 | LOW | CAUTION | 0 | `dx-optimizer` | — |
| 0 | LOW | CAUTION | 0 | `e2e-testing` | — |
| 0 | LOW | CAUTION | 0 | `earllm-build` | — |
| 0 | LOW | CAUTION | 0 | `elixir-pro` | — |
| 0 | LOW | CAUTION | 0 | `email-sequence` | — |
| 0 | LOW | CAUTION | 0 | `embedding-strategies` | — |
| 0 | LOW | CAUTION | 0 | `emergency-card` | — |
| 0 | LOW | CAUTION | 0 | `emil-design-eng` | — |
| 0 | LOW | SAFE | 0 | `emotional-arc-designer` | — |
| 0 | LOW | CAUTION | 0 | `enhance-prompt` | — |
| 0 | LOW | CAUTION | 0 | `error-debugging-multi-agent-review` | — |
| 0 | LOW | CAUTION | 0 | `error-detective` | — |
| 0 | LOW | CAUTION | 0 | `error-diagnostics-smart-debug` | — |
| 0 | LOW | CAUTION | 0 | `evaluation` | — |
| 0 | LOW | CAUTION | 0 | `event-sourcing-architect` | — |
| 0 | LOW | CAUTION | 0 | `event-staffing-compliance` | — |
| 0 | LOW | CAUTION | 0 | `event-staffing-ordering` | — |
| 0 | LOW | CAUTION | 0 | `event-store-design` | — |
| 0 | LOW | CAUTION | 0 | `examprep-ai` | — |
| 0 | LOW | SAFE | 0 | `explain-like-socrates` | — |
| 0 | LOW | CAUTION | 0 | `expo-deployment` | — |
| 0 | LOW | CAUTION | 0 | `expo-tailwind-setup` | — |
| 0 | LOW | SAFE | 0 | `fal-audio` | — |
| 0 | LOW | SAFE | 0 | `fal-generate` | — |
| 0 | LOW | SAFE | 0 | `fal-image-edit` | — |
| 0 | LOW | SAFE | 0 | `fal-platform` | — |
| 0 | LOW | SAFE | 0 | `fal-upscale` | — |
| 0 | LOW | SAFE | 0 | `fal-workflow` | — |
| 0 | LOW | CAUTION | 0 | `family-health-analyzer` | — |
| 0 | LOW | CAUTION | 0 | `fastapi-pro` | — |
| 0 | LOW | CAUTION | 0 | `fastapi-router-py` | — |
| 0 | LOW | SAFE | 0 | `fda-food-safety-auditor` | — |
| 0 | LOW | SAFE | 0 | `fda-medtech-compliance-auditor` | — |
| 0 | LOW | SAFE | 0 | `ffuf-claude-skill` | — |
| 0 | LOW | CAUTION | 0 | `figma-automation` | — |
| 0 | LOW | CAUTION | 0 | `file-organizer` | — |
| 0 | LOW | CAUTION | 0 | `find-bugs` | — |
| 0 | LOW | CAUTION | 0 | `firebase` | — |
| 0 | LOW | CAUTION | 0 | `fitness-analyzer` | — |
| 0 | LOW | SAFE | 0 | `fix-review` | — |
| 0 | LOW | SAFE | 0 | `fixing-accessibility` | — |
| 0 | LOW | SAFE | 0 | `fixing-metadata` | — |
| 0 | LOW | CAUTION | 0 | `fixing-motion-performance` | — |
| 0 | LOW | CAUTION | 0 | `flutter-expert` | — |
| 0 | LOW | CAUTION | 0 | `fp-async` | — |
| 0 | LOW | CAUTION | 0 | `fp-backend` | — |
| 0 | LOW | CAUTION | 0 | `fp-data-transforms` | — |
| 0 | LOW | CAUTION | 0 | `fp-either-ref` | — |
| 0 | LOW | CAUTION | 0 | `fp-errors` | — |
| 0 | LOW | CAUTION | 0 | `fp-option-ref` | — |
| 0 | LOW | CAUTION | 0 | `fp-pipe-ref` | — |
| 0 | LOW | CAUTION | 0 | `fp-pragmatic` | — |
| 0 | LOW | CAUTION | 0 | `fp-react` | — |
| 0 | LOW | CAUTION | 0 | `fp-refactor` | — |
| 0 | LOW | CAUTION | 0 | `fp-taskeither-ref` | — |
| 0 | LOW | CAUTION | 0 | `fp-ts-errors` | — |
| 0 | LOW | CAUTION | 0 | `fp-ts-pragmatic` | — |
| 0 | LOW | CAUTION | 0 | `fp-ts-react` | — |
| 0 | LOW | CAUTION | 0 | `fp-types-ref` | — |
| 0 | LOW | CAUTION | 0 | `framework-migration-legacy-modernize` | — |
| 0 | LOW | CAUTION | 0 | `free-tool-strategy` | — |
| 0 | LOW | CAUTION | 0 | `freshdesk-automation` | — |
| 0 | LOW | CAUTION | 0 | `freshservice-automation` | — |
| 0 | LOW | CAUTION | 0 | `frontend-api-integration-patterns` | — |
| 0 | LOW | CAUTION | 0 | `frontend-design` | — |
| 0 | LOW | CAUTION | 0 | `frontend-dev-guidelines` | — |
| 0 | LOW | CAUTION | 0 | `frontend-developer` | — |
| 0 | LOW | CAUTION | 0 | `frontend-mobile-development-component-scaffold` | — |
| 0 | LOW | CAUTION | 0 | `frontend-security-coder` | — |
| 0 | LOW | CAUTION | 0 | `fsi-compliance-checker` | — |
| 0 | LOW | CAUTION | 0 | `full-output-enforcement` | — |
| 0 | LOW | CAUTION | 0 | `full-stack-orchestration-full-stack-feature` | — |
| 0 | LOW | CAUTION | 0 | `game-development` | — |
| 0 | LOW | CAUTION | 0 | `gemini-api-dev` | — |
| 0 | LOW | CAUTION | 0 | `geoffrey-hinton` | — |
| 0 | LOW | CAUTION | 0 | `gh-image` | — |
| 0 | LOW | CAUTION | 0 | `gh-review-requests` | — |
| 0 | LOW | CAUTION | 0 | `gha-security-review` | — |
| 0 | LOW | CAUTION | 0 | `git-pr-workflows-onboard` | — |
| 0 | LOW | CAUTION | 0 | `git-pushing` | — |
| 0 | LOW | CAUTION | 0 | `github` | — |
| 0 | LOW | CAUTION | 0 | `github-actions-debugger` | — |
| 0 | LOW | CAUTION | 0 | `github-automation` | — |
| 0 | LOW | CAUTION | 0 | `github-issue-creator` | — |
| 0 | LOW | CAUTION | 0 | `gitlab-automation` | — |
| 0 | LOW | CAUTION | 0 | `gmail-automation` | — |
| 0 | LOW | SAFE | 0 | `go-concurrency-patterns` | — |
| 0 | LOW | CAUTION | 0 | `goal-analyzer` | — |
| 0 | LOW | CAUTION | 0 | `godot-4-migration` | — |
| 0 | LOW | SAFE | 0 | `godot-gdscript-patterns` | — |
| 0 | LOW | CAUTION | 0 | `golang-pro` | — |
| 0 | LOW | CAUTION | 0 | `google-analytics-automation` | — |
| 0 | LOW | CAUTION | 0 | `google-calendar-automation` | — |
| 0 | LOW | CAUTION | 0 | `google-drive-automation` | — |
| 0 | LOW | CAUTION | 0 | `google-sheets-automation` | — |
| 0 | LOW | CAUTION | 0 | `google-slides-automation` | — |
| 0 | LOW | CAUTION | 0 | `googlesheets-automation` | — |
| 0 | LOW | CAUTION | 0 | `gpt-taste` | — |
| 0 | LOW | CAUTION | 0 | `grafana-dashboards` | — |
| 0 | LOW | CAUTION | 0 | `graphql-architect` | — |
| 0 | LOW | CAUTION | 0 | `grill-me` | — |
| 0 | LOW | CAUTION | 0 | `grill-with-docs` | — |
| 0 | LOW | CAUTION | 0 | `grilling` | — |
| 0 | LOW | CAUTION | 0 | `growth-engine` | — |
| 0 | LOW | CAUTION | 0 | `handoff` | — |
| 0 | LOW | CAUTION | 0 | `haskell-pro` | — |
| 0 | LOW | SAFE | 0 | `headline-psychologist` | — |
| 0 | LOW | CAUTION | 0 | `health-trend-analyzer` | — |
| 0 | LOW | CAUTION | 0 | `helium-mcp` | — |
| 0 | LOW | SAFE | 0 | `hello` | — |
| 0 | LOW | CAUTION | 0 | `helpdesk-automation` | — |
| 0 | LOW | CAUTION | 0 | `hierarchical-agent-memory` | — |
| 0 | LOW | CAUTION | 0 | `hig-components-content` | — |
| 0 | LOW | CAUTION | 0 | `hig-components-dialogs` | — |
| 0 | LOW | CAUTION | 0 | `hig-components-search` | — |
| 0 | LOW | CAUTION | 0 | `hig-components-status` | — |
| 0 | LOW | CAUTION | 0 | `high-end-visual-design` | — |
| 0 | LOW | CAUTION | 0 | `hono` | — |
| 0 | LOW | CAUTION | 0 | `hosted-agents` | — |
| 0 | LOW | CAUTION | 0 | `hosted-agents-v2-py` | — |
| 0 | LOW | CAUTION | 0 | `hr-pro` | — |
| 0 | LOW | CAUTION | 0 | `hubspot-automation` | — |
| 0 | LOW | CAUTION | 0 | `hugging-face-gradio` | — |
| 0 | LOW | CAUTION | 0 | `hugging-face-tool-builder` | — |
| 0 | LOW | CAUTION | 0 | `hugging-face-trackio` | — |
| 0 | LOW | CAUTION | 0 | `hybrid-cloud-architect` | — |
| 0 | LOW | CAUTION | 0 | `hybrid-cloud-networking` | — |
| 0 | LOW | SAFE | 0 | `hybrid-search-implementation` | — |
| 0 | LOW | CAUTION | 0 | `iconsax-library` | — |
| 0 | LOW | CAUTION | 0 | `idea-darwin` | — |
| 0 | LOW | CAUTION | 0 | `idea-os` | — |
| 0 | LOW | SAFE | 0 | `identity-mirror` | — |
| 0 | LOW | CAUTION | 0 | `idor-testing` | — |
| 0 | LOW | CAUTION | 0 | `ilya-sutskever` | — |
| 0 | LOW | CAUTION | 0 | `image-studio` | — |
| 0 | LOW | CAUTION | 0 | `imagen` | — |
| 0 | LOW | CAUTION | 0 | `improve-codebase-architecture` | — |
| 0 | LOW | CAUTION | 0 | `incident-responder` | — |
| 0 | LOW | CAUTION | 0 | `incident-response-smart-fix` | — |
| 0 | LOW | CAUTION | 0 | `indexing-issue-auditor` | — |
| 0 | LOW | CAUTION | 0 | `industrial-brutalist-ui` | — |
| 0 | LOW | CAUTION | 0 | `infinite-gratitude` | — |
| 0 | LOW | CAUTION | 0 | `inngest` | — |
| 0 | LOW | CAUTION | 0 | `instagram-automation` | — |
| 0 | LOW | CAUTION | 0 | `interactive-portfolio` | — |
| 0 | LOW | CAUTION | 0 | `intercom-automation` | — |
| 0 | LOW | CAUTION | 0 | `internal-comms` | — |
| 0 | LOW | CAUTION | 0 | `internal-comms-anthropic` | — |
| 0 | LOW | CAUTION | 0 | `internal-comms-community` | — |
| 0 | LOW | CAUTION | 0 | `ios-debugger-agent` | — |
| 0 | LOW | CAUTION | 0 | `ios-developer` | — |
| 0 | LOW | CAUTION | 0 | `issues` | — |
| 0 | LOW | CAUTION | 0 | `istio-traffic-management` | — |
| 0 | LOW | CAUTION | 0 | `it-manager-hospital` | — |
| 0 | LOW | CAUTION | 0 | `it-manager-pro` | — |
| 0 | LOW | CAUTION | 0 | `iterate-pr` | — |
| 0 | LOW | CAUTION | 0 | `itil-expert` | — |
| 0 | LOW | CAUTION | 0 | `java-pro` | — |
| 0 | LOW | CAUTION | 0 | `javascript-mastery` | — |
| 0 | LOW | CAUTION | 0 | `javascript-pro` | — |
| 0 | LOW | SAFE | 0 | `jira-automation` | — |
| 0 | LOW | SAFE | 0 | `jobs-to-be-done-analyst` | — |
| 0 | LOW | CAUTION | 0 | `json-canvas` | — |
| 0 | LOW | CAUTION | 0 | `julia-pro` | — |
| 0 | LOW | CAUTION | 0 | `k8s-security-policies` | — |
| 0 | LOW | CAUTION | 0 | `klaviyo-automation` | — |
| 0 | LOW | CAUTION | 0 | `kotler-macro-analyzer` | — |
| 0 | LOW | CAUTION | 0 | `kotlin-coroutines-expert` | — |
| 0 | LOW | CAUTION | 0 | `kpi-dashboard-design` | — |
| 0 | LOW | CAUTION | 0 | `kubernetes-deployment` | — |
| 0 | LOW | CAUTION | 0 | `lambda-lang` | — |
| 0 | LOW | CAUTION | 0 | `lambdatest-agent-skills` | — |
| 0 | LOW | CAUTION | 0 | `langchain-architecture` | — |
| 0 | LOW | CAUTION | 0 | `langfuse` | — |
| 0 | LOW | CAUTION | 0 | `langgraph` | — |
| 0 | LOW | CAUTION | 0 | `laravel-expert` | — |
| 0 | LOW | CAUTION | 0 | `latex-paper-conversion` | — |
| 0 | LOW | CAUTION | 0 | `launch-strategy` | — |
| 0 | LOW | CAUTION | 0 | `lead-magnets` | — |
| 0 | LOW | CAUTION | 0 | `legacy-modernizer` | — |
| 0 | LOW | CAUTION | 0 | `legal-advisor` | — |
| 0 | LOW | CAUTION | 0 | `lesson-generator` | — |
| 0 | LOW | CAUTION | 0 | `lex` | — |
| 0 | LOW | CAUTION | 0 | `lightning-architecture-review` | — |
| 0 | LOW | CAUTION | 0 | `lightning-channel-factories` | — |
| 0 | LOW | SAFE | 0 | `lightning-factory-explainer` | — |
| 0 | LOW | SAFE | 0 | `linear-automation` | — |
| 0 | LOW | CAUTION | 0 | `linkedin-automation` | — |
| 0 | LOW | CAUTION | 0 | `linux-troubleshooting` | — |
| 0 | LOW | CAUTION | 0 | `llm-app-patterns` | — |
| 0 | LOW | SAFE | 0 | `llm-application-dev-ai-assistant` | — |
| 0 | LOW | CAUTION | 0 | `llm-application-dev-langchain-agent` | — |
| 0 | LOW | CAUTION | 0 | `llm-evaluation` | — |
| 0 | LOW | CAUTION | 0 | `llm-ops` | — |
| 0 | LOW | CAUTION | 0 | `llm-prompt-optimizer` | — |
| 0 | LOW | CAUTION | 0 | `llm-structured-output` | — |
| 0 | LOW | CAUTION | 0 | `local-legal-seo-audit` | — |
| 0 | LOW | CAUTION | 0 | `local-llm-expert` | — |
| 0 | LOW | CAUTION | 0 | `lookdev-auto` | — |
| 0 | LOW | CAUTION | 0 | `loop-library` | — |
| 0 | LOW | CAUTION | 0 | `loss-aversion-designer` | — |
| 0 | LOW | CAUTION | 0 | `m365-agents-ts` | — |
| 0 | LOW | CAUTION | 0 | `machine-learning-ops-ml-pipeline` | — |
| 0 | LOW | CAUTION | 0 | `macos-screen-recorder` | — |
| 0 | LOW | CAUTION | 0 | `magic-animator` | — |
| 0 | LOW | CAUTION | 0 | `magic-ui-generator` | — |
| 0 | LOW | CAUTION | 0 | `mailchimp-automation` | — |
| 0 | LOW | CAUTION | 0 | `mailtrap-setting-up-sending-domain` | — |
| 0 | LOW | CAUTION | 0 | `make-automation` | — |
| 0 | LOW | CAUTION | 0 | `makepad-animation` | — |
| 0 | LOW | CAUTION | 0 | `makepad-basics` | — |
| 0 | LOW | CAUTION | 0 | `makepad-dsl` | — |
| 0 | LOW | CAUTION | 0 | `makepad-event-action` | — |
| 0 | LOW | CAUTION | 0 | `makepad-font` | — |
| 0 | LOW | CAUTION | 0 | `makepad-layout` | — |
| 0 | LOW | CAUTION | 0 | `makepad-reference` | — |
| 0 | LOW | CAUTION | 0 | `makepad-shaders` | — |
| 0 | LOW | SAFE | 0 | `makepad-skills` | — |
| 0 | LOW | CAUTION | 0 | `makepad-widgets` | — |
| 0 | LOW | CAUTION | 0 | `malware-analyst` | — |
| 0 | LOW | CAUTION | 0 | `market-sizing-analysis` | — |
| 0 | LOW | CAUTION | 0 | `marketing-ideas` | — |
| 0 | LOW | SAFE | 0 | `marketing-psychology` | — |
| 0 | LOW | CAUTION | 0 | `matplotlib` | — |
| 0 | LOW | CAUTION | 0 | `mcp-tool-developer` | — |
| 0 | LOW | SAFE | 0 | `memory-safety-patterns` | — |
| 0 | LOW | SAFE | 0 | `memory-systems` | — |
| 0 | LOW | CAUTION | 0 | `mental-health-analyzer` | — |
| 0 | LOW | CAUTION | 0 | `mermaid-expert` | — |
| 0 | LOW | CAUTION | 0 | `mesh-memory` | — |
| 0 | LOW | CAUTION | 0 | `micro-saas-launcher` | — |
| 0 | LOW | SAFE | 0 | `microservices-patterns` | — |
| 0 | LOW | CAUTION | 0 | `minecraft-bukkit-pro` | — |
| 0 | LOW | CAUTION | 0 | `minimalist-ui` | — |
| 0 | LOW | CAUTION | 0 | `miro-automation` | — |
| 0 | LOW | CAUTION | 0 | `mise-configurator` | — |
| 0 | LOW | CAUTION | 0 | `mixpanel-automation` | — |
| 0 | LOW | CAUTION | 0 | `ml-engineer` | — |
| 0 | LOW | CAUTION | 0 | `ml-pipeline-workflow` | — |
| 0 | LOW | CAUTION | 0 | `mlops-engineer` | — |
| 0 | LOW | CAUTION | 0 | `moatmri` | — |
| 0 | LOW | CAUTION | 0 | `mobile-developer` | — |
| 0 | LOW | CAUTION | 0 | `mobile-security-coder` | — |
| 0 | LOW | CAUTION | 0 | `mock-hunter` | — |
| 0 | LOW | CAUTION | 0 | `modern-javascript-patterns` | — |
| 0 | LOW | CAUTION | 0 | `monday-automation` | — |
| 0 | LOW | CAUTION | 0 | `monetization` | — |
| 0 | LOW | CAUTION | 0 | `monopoly` | — |
| 0 | LOW | CAUTION | 0 | `monorepo-architect` | — |
| 0 | LOW | CAUTION | 0 | `multi-advisor` | — |
| 0 | LOW | CAUTION | 0 | `multi-agent-architect` | — |
| 0 | LOW | CAUTION | 0 | `multi-agent-patterns` | — |
| 0 | LOW | CAUTION | 0 | `multi-agent-task-orchestrator` | — |
| 0 | LOW | CAUTION | 0 | `multi-cloud-architecture` | — |
| 0 | LOW | CAUTION | 0 | `multi-platform-apps-multi-platform` | — |
| 0 | LOW | CAUTION | 0 | `n8n-code-python` | — |
| 0 | LOW | SAFE | 0 | `nanobanana-ppt-skills` | — |
| 0 | LOW | CAUTION | 0 | `nerdzao-elite` | — |
| 0 | LOW | CAUTION | 0 | `nerdzao-elite-gemini-high` | — |
| 0 | LOW | CAUTION | 0 | `network-engineer` | — |
| 0 | LOW | CAUTION | 0 | `new-rails-project` | — |
| 0 | LOW | CAUTION | 0 | `nextjs-best-practices` | — |
| 0 | LOW | CAUTION | 0 | `nextjs-seo-indexing` | — |
| 0 | LOW | CAUTION | 0 | `nextjs-supabase-auth` | — |
| 0 | LOW | CAUTION | 0 | `nft-standards` | — |
| 0 | LOW | CAUTION | 0 | `nodejs-best-practices` | — |
| 0 | LOW | CAUTION | 0 | `nosql-expert` | — |
| 0 | LOW | CAUTION | 0 | `not-human-search-mcp` | — |
| 0 | LOW | CAUTION | 0 | `notion-automation` | — |
| 0 | LOW | CAUTION | 0 | `notion-template-business` | — |
| 0 | LOW | SAFE | 0 | `objection-preemptor` | — |
| 0 | LOW | CAUTION | 0 | `observability-engineer` | — |
| 0 | LOW | SAFE | 0 | `observability-monitoring-monitor-setup` | — |
| 0 | LOW | CAUTION | 0 | `observability-monitoring-slo-implement` | — |
| 0 | LOW | CAUTION | 0 | `obsidian-bases` | — |
| 0 | LOW | CAUTION | 0 | `obsidian-cli` | — |
| 0 | LOW | CAUTION | 0 | `obsidian-clipper-template-creator` | — |
| 0 | LOW | CAUTION | 0 | `obsidian-markdown` | — |
| 0 | LOW | CAUTION | 0 | `occupational-health-analyzer` | — |
| 0 | LOW | CAUTION | 0 | `odoo-accounting-setup` | — |
| 0 | LOW | CAUTION | 0 | `odoo-automated-tests` | — |
| 0 | LOW | CAUTION | 0 | `odoo-ecommerce-configurator` | — |
| 0 | LOW | CAUTION | 0 | `odoo-edi-connector` | — |
| 0 | LOW | CAUTION | 0 | `odoo-hr-payroll-setup` | — |
| 0 | LOW | CAUTION | 0 | `odoo-inventory-optimizer` | — |
| 0 | LOW | CAUTION | 0 | `odoo-l10n-compliance` | — |
| 0 | LOW | CAUTION | 0 | `odoo-manufacturing-advisor` | — |
| 0 | LOW | CAUTION | 0 | `odoo-migration-helper` | — |
| 0 | LOW | CAUTION | 0 | `odoo-module-developer` | — |
| 0 | LOW | CAUTION | 0 | `odoo-orm-expert` | — |
| 0 | LOW | CAUTION | 0 | `odoo-project-timesheet` | — |
| 0 | LOW | CAUTION | 0 | `odoo-purchase-workflow` | — |
| 0 | LOW | CAUTION | 0 | `odoo-qweb-templates` | — |
| 0 | LOW | CAUTION | 0 | `odoo-sales-crm-expert` | — |
| 0 | LOW | CAUTION | 0 | `odoo-security-rules` | — |
| 0 | LOW | CAUTION | 0 | `odoo-woocommerce-bridge` | — |
| 0 | LOW | CAUTION | 0 | `odoo-xml-views-builder` | — |
| 0 | LOW | SAFE | 0 | `office-productivity` | — |
| 0 | LOW | CAUTION | 0 | `on-call-handoff-patterns` | — |
| 0 | LOW | CAUTION | 0 | `onboarding-cro` | — |
| 0 | LOW | SAFE | 0 | `onboarding-psychologist` | — |
| 0 | LOW | CAUTION | 0 | `one-drive-automation` | — |
| 0 | LOW | CAUTION | 0 | `openclaw-github-repo-commander` | — |
| 0 | LOW | CAUTION | 0 | `options-flow-analyzer` | — |
| 0 | LOW | SAFE | 0 | `oral-health-analyzer` | — |
| 0 | LOW | CAUTION | 0 | `orchestrate-batch-refactor` | — |
| 0 | LOW | CAUTION | 0 | `osterwalder-canvas-architect` | — |
| 0 | LOW | CAUTION | 0 | `outlook-automation` | — |
| 0 | LOW | CAUTION | 0 | `outlook-calendar-automation` | — |
| 0 | LOW | CAUTION | 0 | `page-cro` | — |
| 0 | LOW | CAUTION | 0 | `pagerduty-automation` | — |
| 0 | LOW | CAUTION | 0 | `paid-ads` | — |
| 0 | LOW | CAUTION | 0 | `pakistan-payments-stack` | — |
| 0 | LOW | CAUTION | 0 | `parallel-agents` | — |
| 0 | LOW | CAUTION | 0 | `payment-integration` | — |
| 0 | LOW | CAUTION | 0 | `pci-compliance` | — |
| 0 | LOW | CAUTION | 0 | `pdf-conversion-router` | — |
| 0 | LOW | CAUTION | 0 | `performance-optimizer` | — |
| 0 | LOW | CAUTION | 0 | `performance-testing-review-ai-review` | — |
| 0 | LOW | CAUTION | 0 | `performance-testing-review-multi-agent-review` | — |
| 0 | LOW | CAUTION | 0 | `permission-manager` | — |
| 0 | LOW | CAUTION | 0 | `phase-gated-debugging` | — |
| 0 | LOW | CAUTION | 0 | `photopea-embedded-editor` | — |
| 0 | LOW | CAUTION | 0 | `php-pro` | — |
| 0 | LOW | CAUTION | 0 | `pipedrive-automation` | — |
| 0 | LOW | SAFE | 0 | `pitch-psychologist` | — |
| 0 | LOW | CAUTION | 0 | `plotly` | — |
| 0 | LOW | CAUTION | 0 | `podcast-generation` | — |
| 0 | LOW | CAUTION | 0 | `polars` | — |
| 0 | LOW | SAFE | 0 | `popup-cro` | — |
| 0 | LOW | CAUTION | 0 | `postgres-best-practices` | — |
| 0 | LOW | SAFE | 0 | `postgresql-optimization` | — |
| 0 | LOW | CAUTION | 0 | `posthog-automation` | — |
| 0 | LOW | CAUTION | 0 | `postmark-automation` | — |
| 0 | LOW | CAUTION | 0 | `postmortem-writing` | — |
| 0 | LOW | CAUTION | 0 | `powershell-windows` | — |
| 0 | LOW | CAUTION | 0 | `pr-merge-champion` | — |
| 0 | LOW | CAUTION | 0 | `pr-writer` | — |
| 0 | LOW | CAUTION | 0 | `premium-3d-website` | — |
| 0 | LOW | SAFE | 0 | `price-psychology-strategist` | — |
| 0 | LOW | CAUTION | 0 | `pricing-strategy` | — |
| 0 | LOW | CAUTION | 0 | `product-design` | — |
| 0 | LOW | CAUTION | 0 | `product-inventor` | — |
| 0 | LOW | CAUTION | 0 | `product-manager` | — |
| 0 | LOW | CAUTION | 0 | `product-marketing-context` | — |
| 0 | LOW | CAUTION | 0 | `programmatic-seo` | — |
| 0 | LOW | SAFE | 0 | `progressive-estimation` | — |
| 0 | LOW | CAUTION | 0 | `progressive-web-app` | — |
| 0 | LOW | SAFE | 0 | `project-development` | — |
| 0 | LOW | SAFE | 0 | `projection-patterns` | — |
| 0 | LOW | CAUTION | 0 | `prometheus-configuration` | — |
| 0 | LOW | CAUTION | 0 | `prompt-caching` | — |
| 0 | LOW | CAUTION | 0 | `prompt-engineering` | — |
| 0 | LOW | CAUTION | 0 | `prompt-library` | — |
| 0 | LOW | SAFE | 0 | `protocol-reverse-engineering` | — |
| 0 | LOW | CAUTION | 0 | `prototype` | — |
| 0 | LOW | CAUTION | 0 | `pubmed-database` | — |
| 0 | LOW | CAUTION | 0 | `puzzle-activity-planner` | — |
| 0 | LOW | SAFE | 0 | `pydantic-ai` | — |
| 0 | LOW | CAUTION | 0 | `pydantic-models-py` | — |
| 0 | LOW | SAFE | 0 | `pypict-skill` | — |
| 0 | LOW | CAUTION | 0 | `python-development` | — |
| 0 | LOW | CAUTION | 0 | `python-development-python-scaffold` | — |
| 0 | LOW | CAUTION | 0 | `python-fastapi-development` | — |
| 0 | LOW | CAUTION | 0 | `python-patterns` | — |
| 0 | LOW | CAUTION | 0 | `python-performance-optimization` | — |
| 0 | LOW | CAUTION | 0 | `python-pro` | — |
| 0 | LOW | CAUTION | 0 | `qiskit` | — |
| 0 | LOW | CAUTION | 0 | `quant-analyst` | — |
| 0 | LOW | CAUTION | 0 | `rag-implementation` | — |
| 0 | LOW | CAUTION | 0 | `rayden-code` | — |
| 0 | LOW | CAUTION | 0 | `rayden-use` | — |
| 0 | LOW | CAUTION | 0 | `react-component-performance` | — |
| 0 | LOW | CAUTION | 0 | `react-flow-architect` | — |
| 0 | LOW | CAUTION | 0 | `react-flow-node-ts` | — |
| 0 | LOW | CAUTION | 0 | `react-nextjs-development` | — |
| 0 | LOW | CAUTION | 0 | `react-patterns` | — |
| 0 | LOW | CAUTION | 0 | `react-state-management` | — |
| 0 | LOW | CAUTION | 0 | `react-ui-patterns` | — |
| 0 | LOW | CAUTION | 0 | `receiving-code-review` | — |
| 0 | LOW | CAUTION | 0 | `recursive-context-pruning-token-budgeting` | — |
| 0 | LOW | CAUTION | 0 | `reddit-automation` | — |
| 0 | LOW | CAUTION | 0 | `redesign-existing-projects` | — |
| 0 | LOW | CAUTION | 0 | `reference-builder` | — |
| 0 | LOW | CAUTION | 0 | `referral-program` | — |
| 0 | LOW | CAUTION | 0 | `rehabilitation-analyzer` | — |
| 0 | LOW | SAFE | 0 | `render-automation` | — |
| 0 | LOW | CAUTION | 0 | `reverse-engineer` | — |
| 0 | LOW | CAUTION | 0 | `review-animations` | — |
| 0 | LOW | CAUTION | 0 | `risk-manager` | — |
| 0 | LOW | SAFE | 0 | `risk-metrics-calculation` | — |
| 0 | LOW | CAUTION | 0 | `robius-event-action` | — |
| 0 | LOW | CAUTION | 0 | `robius-state-management` | — |
| 0 | LOW | CAUTION | 0 | `robius-widget-patterns` | — |
| 0 | LOW | CAUTION | 0 | `ruby-pro` | — |
| 0 | LOW | CAUTION | 0 | `runapi-cli` | — |
| 0 | LOW | CAUTION | 0 | `runaway-guard` | — |
| 0 | LOW | CAUTION | 0 | `rust-pro` | — |
| 0 | LOW | CAUTION | 0 | `saas-multi-tenant` | — |
| 0 | LOW | CAUTION | 0 | `saga-orchestration` | — |
| 0 | LOW | CAUTION | 0 | `sales-automator` | — |
| 0 | LOW | CAUTION | 0 | `salesforce-automation` | — |
| 0 | LOW | CAUTION | 0 | `sam-altman` | — |
| 0 | LOW | CAUTION | 0 | `sandbox-next` | — |
| 0 | LOW | CAUTION | 0 | `sandbox-stable` | — |
| 0 | LOW | CAUTION | 0 | `satori` | — |
| 0 | LOW | CAUTION | 0 | `scala-pro` | — |
| 0 | LOW | CAUTION | 0 | `scanpy` | — |
| 0 | LOW | SAFE | 0 | `scarcity-urgency-psychologist` | — |
| 0 | LOW | SAFE | 0 | `schema-markup` | — |
| 0 | LOW | CAUTION | 0 | `scikit-learn` | — |
| 0 | LOW | SAFE | 0 | `screen-reader-testing` | — |
| 0 | LOW | CAUTION | 0 | `screenstudio-alt` | — |
| 0 | LOW | CAUTION | 0 | `scroll-experience` | — |
| 0 | LOW | CAUTION | 0 | `search-specialist` | — |
| 0 | LOW | CAUTION | 0 | `security-audit` | — |
| 0 | LOW | CAUTION | 0 | `security-auditor` | — |
| 0 | LOW | CAUTION | 0 | `security-bluebook-builder` | — |
| 0 | LOW | SAFE | 0 | `security-requirement-extraction` | — |
| 0 | LOW | CAUTION | 0 | `seek-and-analyze-video` | — |
| 0 | LOW | CAUTION | 0 | `segment-automation` | — |
| 0 | LOW | SAFE | 0 | `semgrep-rule-variant-creator` | — |
| 0 | LOW | CAUTION | 0 | `sendgrid-automation` | — |
| 0 | LOW | CAUTION | 0 | `sentry-automation` | — |
| 0 | LOW | CAUTION | 0 | `seo-audit` | — |
| 0 | LOW | CAUTION | 0 | `seo-authority-builder` | — |
| 0 | LOW | CAUTION | 0 | `seo-cannibalization-detector` | — |
| 0 | LOW | CAUTION | 0 | `seo-competitor-pages` | — |
| 0 | LOW | CAUTION | 0 | `seo-content` | — |
| 0 | LOW | CAUTION | 0 | `seo-content-auditor` | — |
| 0 | LOW | CAUTION | 0 | `seo-content-planner` | — |
| 0 | LOW | CAUTION | 0 | `seo-content-refresher` | — |
| 0 | LOW | CAUTION | 0 | `seo-content-writer` | — |
| 0 | LOW | CAUTION | 0 | `seo-dataforseo` | — |
| 0 | LOW | CAUTION | 0 | `seo-forensic-incident-response` | — |
| 0 | LOW | CAUTION | 0 | `seo-geo` | — |
| 0 | LOW | CAUTION | 0 | `seo-hreflang` | — |
| 0 | LOW | CAUTION | 0 | `seo-images` | — |
| 0 | LOW | CAUTION | 0 | `seo-keyword-strategist` | — |
| 0 | LOW | CAUTION | 0 | `seo-meta-optimizer` | — |
| 0 | LOW | CAUTION | 0 | `seo-page` | — |
| 0 | LOW | CAUTION | 0 | `seo-plan` | — |
| 0 | LOW | CAUTION | 0 | `seo-programmatic` | — |
| 0 | LOW | CAUTION | 0 | `seo-schema` | — |
| 0 | LOW | CAUTION | 0 | `seo-sitemap` | — |
| 0 | LOW | CAUTION | 0 | `seo-snippet-hunter` | — |
| 0 | LOW | CAUTION | 0 | `seo-structure-architect` | — |
| 0 | LOW | CAUTION | 0 | `seo-technical` | — |
| 0 | LOW | SAFE | 0 | `sequence-psychologist` | — |
| 0 | LOW | CAUTION | 0 | `service-mesh-expert` | — |
| 0 | LOW | CAUTION | 0 | `service-mesh-observability` | — |
| 0 | LOW | CAUTION | 0 | `setup-matt-pocock-skills` | — |
| 0 | LOW | CAUTION | 0 | `sexual-health-analyzer` | — |
| 0 | LOW | CAUTION | 0 | `shader-programming-glsl` | — |
| 0 | LOW | CAUTION | 0 | `sharp-coder` | — |
| 0 | LOW | CAUTION | 0 | `shopify-automation` | — |
| 0 | LOW | CAUTION | 0 | `signup-flow-cro` | — |
| 0 | LOW | SAFE | 0 | `similarity-search-patterns` | — |
| 0 | LOW | CAUTION | 0 | `simplify-code` | — |
| 0 | LOW | CAUTION | 0 | `site-architecture` | — |
| 0 | LOW | CAUTION | 0 | `skill-improver` | — |
| 0 | LOW | CAUTION | 0 | `skill-reviewer` | — |
| 0 | LOW | CAUTION | 0 | `skill-router` | — |
| 0 | LOW | SAFE | 0 | `skill-seekers` | — |
| 0 | LOW | SAFE | 0 | `skin-health-analyzer` | — |
| 0 | LOW | CAUTION | 0 | `skyvern-browser-automation` | — |
| 0 | LOW | CAUTION | 0 | `sleep-analyzer` | — |
| 0 | LOW | CAUTION | 0 | `slo-implementation` | — |
| 0 | LOW | CAUTION | 0 | `snowflake-development` | — |
| 0 | LOW | CAUTION | 0 | `social-content` | — |
| 0 | LOW | CAUTION | 0 | `social-metadata-hardening` | — |
| 0 | LOW | CAUTION | 0 | `social-orchestrator` | — |
| 0 | LOW | CAUTION | 0 | `social-post-writer-seo` | — |
| 0 | LOW | CAUTION | 0 | `social-proof-architect` | — |
| 0 | LOW | CAUTION | 0 | `software-architecture` | — |
| 0 | LOW | SAFE | 0 | `solidity-security` | — |
| 0 | LOW | CAUTION | 0 | `spark-optimization` | — |
| 0 | LOW | CAUTION | 0 | `spec-to-code-compliance` | — |
| 0 | LOW | SAFE | 0 | `sql-optimization-patterns` | — |
| 0 | LOW | CAUTION | 0 | `sql-sentinel` | — |
| 0 | LOW | CAUTION | 0 | `square-automation` | — |
| 0 | LOW | CAUTION | 0 | `sred-project-organizer` | — |
| 0 | LOW | SAFE | 0 | `sred-work-summary` | — |
| 0 | LOW | CAUTION | 0 | `startup-analyst` | — |
| 0 | LOW | CAUTION | 0 | `startup-business-analyst-business-case` | — |
| 0 | LOW | CAUTION | 0 | `startup-business-analyst-financial-projections` | — |
| 0 | LOW | CAUTION | 0 | `startup-business-analyst-market-opportunity` | — |
| 0 | LOW | CAUTION | 0 | `startup-financial-modeling` | — |
| 0 | LOW | SAFE | 0 | `startup-metrics-framework` | — |
| 0 | LOW | CAUTION | 0 | `statsmodels` | — |
| 0 | LOW | CAUTION | 0 | `steve-jobs` | — |
| 0 | LOW | CAUTION | 0 | `stitch-design-taste` | — |
| 0 | LOW | CAUTION | 0 | `stitch-ui-design` | — |
| 0 | LOW | SAFE | 0 | `stride-analysis-patterns` | — |
| 0 | LOW | CAUTION | 0 | `stripe-automation` | — |
| 0 | LOW | CAUTION | 0 | `stripe-integration` | — |
| 0 | LOW | SAFE | 0 | `subject-line-psychologist` | — |
| 0 | LOW | CAUTION | 0 | `supabase-automation` | — |
| 0 | LOW | SAFE | 0 | `superpowers-lab` | — |
| 0 | LOW | CAUTION | 0 | `supply-chain-risk-auditor` | — |
| 0 | LOW | CAUTION | 0 | `swift-concurrency-expert` | — |
| 0 | LOW | CAUTION | 0 | `swiftui-expert-skill` | — |
| 0 | LOW | CAUTION | 0 | `swiftui-liquid-glass` | — |
| 0 | LOW | CAUTION | 0 | `swiftui-performance-audit` | — |
| 0 | LOW | CAUTION | 0 | `swiftui-ui-patterns` | — |
| 0 | LOW | CAUTION | 0 | `swiftui-view-refactor` | — |
| 0 | LOW | CAUTION | 0 | `sympy` | — |
| 0 | LOW | SAFE | 0 | `tailwind-design-system` | — |
| 0 | LOW | CAUTION | 0 | `tailwind-patterns` | — |
| 0 | LOW | CAUTION | 0 | `tanstack-query-expert` | — |
| 0 | LOW | CAUTION | 0 | `tcm-constitution-analyzer` | — |
| 0 | LOW | CAUTION | 0 | `tdd` | — |
| 0 | LOW | CAUTION | 0 | `tdd-orchestrator` | — |
| 0 | LOW | SAFE | 0 | `tdd-workflow` | — |
| 0 | LOW | CAUTION | 0 | `tdd-workflows` | — |
| 0 | LOW | CAUTION | 0 | `tdd-workflows-tdd-cycle` | — |
| 0 | LOW | SAFE | 0 | `tdd-workflows-tdd-green` | — |
| 0 | LOW | CAUTION | 0 | `tdd-workflows-tdd-red` | — |
| 0 | LOW | CAUTION | 0 | `tdd-workflows-tdd-refactor` | — |
| 0 | LOW | CAUTION | 0 | `teach` | — |
| 0 | LOW | CAUTION | 0 | `team-composition-analysis` | — |
| 0 | LOW | CAUTION | 0 | `technical-change-tracker` | — |
| 0 | LOW | CAUTION | 0 | `telegram-automation` | — |
| 0 | LOW | CAUTION | 0 | `temporal-golang-pro` | — |
| 0 | LOW | CAUTION | 0 | `temporal-python-pro` | — |
| 0 | LOW | CAUTION | 0 | `terraform-aws-modules` | — |
| 0 | LOW | CAUTION | 0 | `terraform-infrastructure` | — |
| 0 | LOW | CAUTION | 0 | `terraform-module-library` | — |
| 0 | LOW | CAUTION | 0 | `terraform-skill` | — |
| 0 | LOW | CAUTION | 0 | `terraform-specialist` | — |
| 0 | LOW | CAUTION | 0 | `test-automator` | — |
| 0 | LOW | CAUTION | 0 | `test-driven-development` | — |
| 0 | LOW | CAUTION | 0 | `test-fixing` | — |
| 0 | LOW | CAUTION | 0 | `testing-patterns` | — |
| 0 | LOW | CAUTION | 0 | `testing-qa` | — |
| 0 | LOW | CAUTION | 0 | `the-honoured-one` | — |
| 0 | LOW | SAFE | 0 | `threat-mitigation-mapping` | — |
| 0 | LOW | SAFE | 0 | `threat-modeling-expert` | — |
| 0 | LOW | CAUTION | 0 | `threejs-fundamentals` | — |
| 0 | LOW | CAUTION | 0 | `threejs-geometry` | — |
| 0 | LOW | CAUTION | 0 | `threejs-interaction` | — |
| 0 | LOW | CAUTION | 0 | `threejs-lighting` | — |
| 0 | LOW | CAUTION | 0 | `threejs-loaders` | — |
| 0 | LOW | CAUTION | 0 | `threejs-materials` | — |
| 0 | LOW | CAUTION | 0 | `threejs-postprocessing` | — |
| 0 | LOW | CAUTION | 0 | `threejs-shaders` | — |
| 0 | LOW | CAUTION | 0 | `threejs-skills` | — |
| 0 | LOW | CAUTION | 0 | `threejs-textures` | — |
| 0 | LOW | CAUTION | 0 | `tiktok-automation` | — |
| 0 | LOW | CAUTION | 0 | `to-issues` | — |
| 0 | LOW | CAUTION | 0 | `to-prd` | — |
| 0 | LOW | CAUTION | 0 | `todoist-automation` | — |
| 0 | LOW | CAUTION | 0 | `tokenwise` | — |
| 0 | LOW | SAFE | 0 | `tool-design` | — |
| 0 | LOW | CAUTION | 0 | `top-web-vulnerabilities` | — |
| 0 | LOW | CAUTION | 0 | `travel-health-analyzer` | — |
| 0 | LOW | CAUTION | 0 | `trello-automation` | — |
| 0 | LOW | CAUTION | 0 | `triage` | — |
| 0 | LOW | CAUTION | 0 | `trpc-fullstack` | — |
| 0 | LOW | SAFE | 0 | `trust-calibrator` | — |
| 0 | LOW | CAUTION | 0 | `tutorial-engineer` | — |
| 0 | LOW | CAUTION | 0 | `twilio-communications` | — |
| 0 | LOW | CAUTION | 0 | `twitter-automation` | — |
| 0 | LOW | CAUTION | 0 | `typescript-pro` | — |
| 0 | LOW | SAFE | 0 | `ui-skills` | — |
| 0 | LOW | CAUTION | 0 | `ui-ux-designer` | — |
| 0 | LOW | CAUTION | 0 | `ui-visual-validator` | — |
| 0 | LOW | CAUTION | 0 | `uncle-bob-craft` | — |
| 0 | LOW | CAUTION | 0 | `uniprot-database` | — |
| 0 | LOW | CAUTION | 0 | `unit-testing-test-generate` | — |
| 0 | LOW | CAUTION | 0 | `unity-ai-game-creator` | — |
| 0 | LOW | CAUTION | 0 | `unity-developer` | — |
| 0 | LOW | SAFE | 0 | `unity-ecs-patterns` | — |
| 0 | LOW | CAUTION | 0 | `unreal-engine-cpp-pro` | — |
| 0 | LOW | CAUTION | 0 | `unslop` | — |
| 0 | LOW | CAUTION | 0 | `unsplash-integration` | — |
| 0 | LOW | CAUTION | 0 | `using-neon` | — |
| 0 | LOW | CAUTION | 0 | `using-superpowers` | — |
| 0 | LOW | SAFE | 0 | `ux-persuasion-engineer` | — |
| 0 | LOW | CAUTION | 0 | `variant-analysis` | — |
| 0 | LOW | SAFE | 0 | `varlock-claude-skill` | — |
| 0 | LOW | CAUTION | 0 | `vector-database-engineer` | — |
| 0 | LOW | SAFE | 0 | `vector-index-tuning` | — |
| 0 | LOW | CAUTION | 0 | `vercel-ai-sdk-expert` | — |
| 0 | LOW | CAUTION | 0 | `vercel-automation` | — |
| 0 | LOW | CAUTION | 0 | `vercel-react-view-transitions` | — |
| 0 | LOW | CAUTION | 0 | `vexor` | — |
| 0 | LOW | CAUTION | 0 | `vexor-cli` | — |
| 0 | LOW | CAUTION | 0 | `vibe-code-auditor` | — |
| 0 | LOW | SAFE | 0 | `viboscope` | — |
| 0 | LOW | CAUTION | 0 | `video-content-extractor` | — |
| 0 | LOW | CAUTION | 0 | `viral-generator-builder` | — |
| 0 | LOW | SAFE | 0 | `visual-emotion-engineer` | — |
| 0 | LOW | SAFE | 0 | `vizcom` | — |
| 0 | LOW | CAUTION | 0 | `voice-ai-development` | — |
| 0 | LOW | CAUTION | 0 | `warren-buffett` | — |
| 0 | LOW | CAUTION | 0 | `web-artifacts-builder` | — |
| 0 | LOW | CAUTION | 0 | `web-design-guidelines` | — |
| 0 | LOW | CAUTION | 0 | `web-media-getter` | — |
| 0 | LOW | CAUTION | 0 | `web-perf` | — |
| 0 | LOW | CAUTION | 0 | `web-project-brainstorming` | — |
| 0 | LOW | CAUTION | 0 | `web-security-testing` | — |
| 0 | LOW | CAUTION | 0 | `webflow-automation` | — |
| 0 | LOW | CAUTION | 0 | `wechat-official-account-strategist` | — |
| 0 | LOW | CAUTION | 0 | `weightloss-analyzer` | — |
| 0 | LOW | SAFE | 0 | `whatsapp-automation` | — |
| 0 | LOW | CAUTION | 0 | `wiki-architect` | — |
| 0 | LOW | CAUTION | 0 | `wiki-builder` | — |
| 0 | LOW | SAFE | 0 | `wiki-changelog` | — |
| 0 | LOW | CAUTION | 0 | `wiki-onboarding` | — |
| 0 | LOW | CAUTION | 0 | `wiki-page-writer` | — |
| 0 | LOW | CAUTION | 0 | `wiki-qa` | — |
| 0 | LOW | CAUTION | 0 | `wiki-researcher` | — |
| 0 | LOW | CAUTION | 0 | `wiki-vitepress` | — |
| 0 | LOW | CAUTION | 0 | `windows-shell-reliability` | — |
| 0 | LOW | CAUTION | 0 | `wireshark-analysis` | — |
| 0 | LOW | CAUTION | 0 | `wordpress` | — |
| 0 | LOW | CAUTION | 0 | `wordpress-centric-high-seo-optimized-blogwriting-skill` | — |
| 0 | LOW | CAUTION | 0 | `wordpress-plugin-development` | — |
| 0 | LOW | CAUTION | 0 | `wordpress-theme-development` | — |
| 0 | LOW | CAUTION | 0 | `wordpress-woocommerce-development` | — |
| 0 | LOW | CAUTION | 0 | `workflow-automation` | — |
| 0 | LOW | CAUTION | 0 | `workflow-orchestration-patterns` | — |
| 0 | LOW | SAFE | 0 | `workflow-patterns` | — |
| 0 | LOW | CAUTION | 0 | `wrangler` | — |
| 0 | LOW | CAUTION | 0 | `wrike-automation` | — |
| 0 | LOW | CAUTION | 0 | `writing-plans` | — |
| 0 | LOW | CAUTION | 0 | `x-article-publisher-skill` | — |
| 0 | LOW | CAUTION | 0 | `xiaohongshu-content-strategist` | — |
| 0 | LOW | CAUTION | 0 | `yann-lecun` | — |
| 0 | LOW | CAUTION | 0 | `yann-lecun-debate` | — |
| 0 | LOW | CAUTION | 0 | `yann-lecun-filosofia` | — |
| 0 | LOW | CAUTION | 0 | `yann-lecun-tecnico` | — |
| 0 | LOW | CAUTION | 0 | `yes-md` | — |
| 0 | LOW | CAUTION | 0 | `youtube-automation` | — |
| 0 | LOW | CAUTION | 0 | `youtube-seo-optimizer` | — |
| 0 | LOW | CAUTION | 0 | `zapier-make-patterns` | — |
| 0 | LOW | CAUTION | 0 | `zendesk-automation` | — |
| 0 | LOW | CAUTION | 0 | `zeroize-audit` | — |
| 0 | LOW | CAUTION | 0 | `zipai-optimizer` | — |
| 0 | LOW | CAUTION | 0 | `zod-validation-expert` | — |
| 0 | LOW | CAUTION | 0 | `zoho-crm-automation` | — |
| 0 | LOW | CAUTION | 0 | `zoom-automation` | — |
| 0 | LOW | CAUTION | 0 | `zustand-store-ts` | — |
| — | — | — | 0 | `crossframe` *(scan failed)* | — |
| — | — | — | 0 | `design-it` *(scan failed)* | — |
| — | — | — | 0 | `loki-mode` *(scan failed)* | — |

## High / Critical skills

- `007` — score=100, severity=CRITICAL, max_issue=HIGH, rules=PE3×26, AR3×5, P1×4, P6×3, YR4×3
- `2slides-ppt-generator` — score=100, severity=CRITICAL, max_issue=CRITICAL, rules=TT3×7, PE3×6, E1×5, SC1×3, SC4×3
- `aws-penetration-testing` — score=100, severity=CRITICAL, max_issue=HIGH, rules=SSRF1×8, PE2×2, E5, EA2, PE1
- `claude-code-expert` — score=100, severity=CRITICAL, max_issue=HIGH, rules=AS1×7, EA5×5, PE2, SC2, TM1
- `cloud-penetration-testing` — score=100, severity=CRITICAL, max_issue=HIGH, rules=SSRF1×14, PE3×5, E5×3, PE2×3, SC2×2
- `cloudflare` — score=100, severity=CRITICAL, max_issue=HIGH, rules=E1×124, RP1×32, TM1×11, PE3×8, EA2×3
- `comfyui-gateway` — score=100, severity=CRITICAL, max_issue=HIGH, rules=PE3×22, RP1×14, E1×10, TM3×8, PE2×5
- `command-development` — score=100, severity=CRITICAL, max_issue=HIGH, rules=AS1×17, TM1×6, P2×5, RA2×3, PE2×2
- `competitor-analysis` — score=100, severity=CRITICAL, max_issue=HIGH, rules=AE1×3, TM1×3, AS1, LP1, TM2
- `computer-use-agents` — score=100, severity=CRITICAL, max_issue=HIGH, rules=EA2×15, RP1×3, TM1×3, AR1, E1
- `container-security-hardening` — score=100, severity=CRITICAL, max_issue=HIGH, rules=RP1×10, TM1×7, PE2×3, PE5×2, AR2
- `diary` — score=100, severity=CRITICAL, max_issue=HIGH, rules=AST4×2, EA2×2, TT2×2, AST7, E1
- `ecl-harness-engineer` — score=100, severity=CRITICAL, max_issue=HIGH, rules=P2×8, RP1×8, PE3×7, TM1×6, AE1×2
- `environment-setup-guide` — score=100, severity=CRITICAL, max_issue=HIGH, rules=PE2×12, PE3×8, TM3×3, E1, RA2
- `ethical-hacking-methodology` — score=100, severity=CRITICAL, max_issue=CRITICAL, rules=YR4×3, PE3×2, PE2, YR1
- `hook-development` — score=100, severity=CRITICAL, max_issue=HIGH, rules=PE3×3, AE1×2, TM1×2, E1, LP3
- `hugging-face-model-trainer` — score=100, severity=CRITICAL, max_issue=HIGH, rules=PE2×6, AST4×4, E5×3, TM2×3, PE1×2
- `last30days` — score=100, severity=CRITICAL, max_issue=HIGH, rules=PE3×16, E1×4, PE2×3, RA2×2, EA4
- `linkedin-content-generator` — score=100, severity=CRITICAL, max_issue=HIGH, rules=MP3×3, AE1, LP3, P6, RA2
- `linux-privilege-escalation` — score=100, severity=CRITICAL, max_issue=CRITICAL, rules=PE2×24, PE3×8, TM2×2, YR1×2, YR4×2
- `macos-spm-app-packaging` — score=100, severity=CRITICAL, max_issue=HIGH, rules=RA2×17, PE3×4, TM1×2, LP3
- `manage-skills` — score=100, severity=CRITICAL, max_issue=HIGH, rules=AS3×9, AS1×3, TM1×2, AE1, RA2
- `mcp-builder` — score=100, severity=CRITICAL, max_issue=HIGH, rules=AE1×3, E1×2, SC1×2, SC4×2, EA1
- `metasploit-framework` — score=100, severity=CRITICAL, max_issue=CRITICAL, rules=YR4×2, P1, PE2, YR1
- `network-101` — score=100, severity=CRITICAL, max_issue=HIGH, rules=PE2×33, TM2×4, TM1×2, YR4×2, RA2
- `notebooklm` — score=100, severity=CRITICAL, max_issue=HIGH, rules=AST4×8, AS3×4, EA2×2, PE3×2, RA2×2
- `plugin-structure` — score=100, severity=CRITICAL, max_issue=HIGH, rules=AE1×4, AS3×2, PE3, RA1, RA2
- `pptx` — score=100, severity=CRITICAL, max_issue=HIGH, rules=RA2×12, AST4×5, P2×4, PE2×2, AE1
- `pptx-official` — score=100, severity=CRITICAL, max_issue=HIGH, rules=RA2×12, AST4×5, P2×4, PE2×2, AE1
- `privilege-escalation-methods` — score=100, severity=CRITICAL, max_issue=HIGH, rules=PE2×18, TM2×3, PE3×2, YR4×2, YR1
- `remote-gpu-trainer` — score=100, severity=CRITICAL, max_issue=HIGH, rules=RA2×36, PE3×24, PE2×14, AR2×3, RP1×3
- `sharp-edges` — score=100, severity=CRITICAL, max_issue=HIGH, rules=P1×2, AR2, EA2, EA4, RA1
- `skill-developer` — score=100, severity=CRITICAL, max_issue=HIGH, rules=RP1×16, TM3×8, AS1×6, P3, RA2
- `skill-installer` — score=100, severity=CRITICAL, max_issue=HIGH, rules=PE3×8, AS3×5, AST4, LP3, RA1
- `stability-ai` — score=100, severity=CRITICAL, max_issue=HIGH, rules=AE1×13, PE3×5, E1×2, P6×2, LP3
- `survey-generator` — score=100, severity=CRITICAL, max_issue=CRITICAL, rules=EA2×2, AE1, E1, LP1, TT3
- `telegram` — score=100, severity=CRITICAL, max_issue=CRITICAL, rules=E1×23, SC1×12, PE3×9, SC4×4, YR1×2
- `turnstile-spin` — score=100, severity=CRITICAL, max_issue=HIGH, rules=E1×21, AE1×10, AS3×7, EA2×4, P9×4
- `ui-ux-pro-max` — score=100, severity=CRITICAL, max_issue=HIGH, rules=E1×15, EA2×7, RP1×4, P6×3, OH1×2
- `varlock` — score=100, severity=CRITICAL, max_issue=HIGH, rules=PE3×12, AS3×2, E2×2, SC2×2, RA2
- `vercel-optimize` — score=100, severity=CRITICAL, max_issue=HIGH, rules=AE1×11, EA2×3, YR1×2, LP3, P6
- `vulnerability-scanner` — score=100, severity=CRITICAL, max_issue=HIGH, rules=PE3×3, AR3×2, TM3×2, AST4, EA4
- `whatsapp-cloud-api` — score=100, severity=CRITICAL, max_issue=CRITICAL, rules=PE3×17, SC1×11, SC4×6, E1×4, TT3×3
- `wordpress-penetration-testing` — score=100, severity=CRITICAL, max_issue=CRITICAL, rules=E1×2, YR2×2, YR4×2, P1, YR1
- `make-me-an-expert` — score=99, severity=CRITICAL, max_issue=HIGH, rules=AS3×4, RA2×3, AE1×2, AR2, AST4
- `active-directory-attacks` — score=98, severity=CRITICAL, max_issue=HIGH, rules=TM1×2, YR1×2, YR4×2, EA2, PE2
- `senior-frontend` — score=98, severity=CRITICAL, max_issue=HIGH, rules=E1×6, AE1×2, PE3×2, LP3, OH1
- `android-dev` — score=96, severity=CRITICAL, max_issue=HIGH, rules=PE3×5, AE1×2, RP1×2, P2
- `shadcn` — score=96, severity=CRITICAL, max_issue=HIGH, rules=RP1×73, P9×10, EA2×2, RA1×2, AS1
- `hig-technologies` — score=95, severity=CRITICAL, max_issue=HIGH, rules=EA2×6, P6×3, AE1, MP3
- `ssh-penetration-testing` — score=94, severity=CRITICAL, max_issue=HIGH, rules=PE3×9, E1, E3, PE2, YR1
- `file-path-traversal` — score=93, severity=CRITICAL, max_issue=CRITICAL, rules=PE3×35, E1, PE2, YR2
- `bash-defensive-patterns` — score=92, severity=CRITICAL, max_issue=HIGH, rules=AE1×2, EA2, RA2, TM1, TM2
- `readme` — score=92, severity=CRITICAL, max_issue=HIGH, rules=PE3×3, PE2×2, RP1×2, TM1×2, EA2
- `gcp-cloud-run` — score=90, severity=CRITICAL, max_issue=HIGH, rules=TM1×2, AR1, E1, PE2, RA2
- `bun-development` — score=89, severity=CRITICAL, max_issue=HIGH, rules=PE3×2, SC2×2, TM2×2, RP1
- `vibecode-production-qa-validator` — score=89, severity=CRITICAL, max_issue=HIGH, rules=RP1×9, SC2×2, TM2×2, PE3
- `devops-deploy` — score=88, severity=CRITICAL, max_issue=CRITICAL, rules=E1×2, EA2×2, TM1×2, YR1
- `hig-patterns` — score=87, severity=CRITICAL, max_issue=HIGH, rules=EA2×3, RA2×2, AE1, AR2, EA3
- `claude-in-chrome-troubleshooting` — score=85, severity=CRITICAL, max_issue=HIGH, rules=AS1×3, TM1×3, RA2
- `conductor-manage` — score=83, severity=CRITICAL, max_issue=HIGH, rules=RA2×3, AE1×2, TM1×2
- `gitops-workflow` — score=82, severity=CRITICAL, max_issue=HIGH, rules=PE3×2, EA2, PE2, SC2, TM2
- `super-code` — score=82, severity=CRITICAL, max_issue=HIGH, rules=TM1×3, AE1×2, EA2
- `writing-skills` — score=82, severity=CRITICAL, max_issue=HIGH, rules=RA1×8, AS3×3, AE1, RA2
- `distributed-debugging-debug-trace` — score=81, severity=CRITICAL, max_issue=HIGH, rules=AE1×2, AR3, P1, TM3
- `monte-carlo-push-ingestion` — score=80, severity=HIGH, max_issue=HIGH, rules=AST7×29, E1×13, PE3×2, LP3, SC2
- `skill-audit` — score=80, severity=HIGH, max_issue=HIGH, rules=P1×2, PE3×2, YR4
- `mobile-design` — score=79, severity=HIGH, max_issue=HIGH, rules=PE3×10, LP3, MP2, MP3, RA2
- `docx` — score=78, severity=HIGH, max_issue=HIGH, rules=RA2×12, P2×6, AST4×3, PE2×3, LP3
- `docx-official` — score=78, severity=HIGH, max_issue=HIGH, rules=RA2×12, P2×6, AST4×3, PE2×3, LP3
- `skill-scanner` — score=78, severity=HIGH, max_issue=HIGH, rules=AE1, E1, EA2, P3, PE3
- `claude-api` — score=77, severity=HIGH, max_issue=HIGH, rules=E1×6, E4×3, P9×3, EA2×2, MP2
- `agent-evaluation` — score=76, severity=HIGH, max_issue=HIGH, rules=P1×2, AE4, P6, YR4
- `lovable-cleanup` — score=73, severity=HIGH, max_issue=HIGH, rules=P2×3, PE3×2, YR4
- `yao-meta-skill` — score=71, severity=HIGH, max_issue=HIGH, rules=AE1×2, EA2×2, RA1
- `pentest-commands` — score=70, severity=HIGH, max_issue=CRITICAL, rules=YR4×2, YR1
- `playwright-skill` — score=70, severity=HIGH, max_issue=HIGH, rules=RP1×13, AE1×3, EA3, LP3, SC1
- `skill-development` — score=70, severity=HIGH, max_issue=HIGH, rules=RA1×3, AE1, AS3
- `ai-studio-image` — score=69, severity=HIGH, max_issue=HIGH, rules=PE3×10, SC1×3, SC4×2, LP3, P6
- `skill-creator` — score=69, severity=HIGH, max_issue=HIGH, rules=AS3×5, E3×3, RA2×2, LP3, RA1
- `ai-product` — score=68, severity=HIGH, max_issue=HIGH, rules=EA2, P1, P6, YR4
- `audio-transcriber` — score=68, severity=HIGH, max_issue=MEDIUM, rules=SC1×15, AST4×6, PE2×2, AS3, EA2
- `audit-skills` — score=68, severity=HIGH, max_issue=HIGH, rules=TM1×3, RA2, SC2
- `hugging-face-jobs` — score=67, severity=HIGH, max_issue=MEDIUM, rules=E5×11, E1×4, PE1×4, EA2×2, EA1
- `junta-leiloeiros` — score=67, severity=HIGH, max_issue=HIGH, rules=TM3×8, SC1×7, SC4×6, E1×2, AST4
- `k6-load-testing` — score=66, severity=HIGH, max_issue=HIGH, rules=E1×12, PE2×5, PE3×2, TM2
- `browser-testing-with-devtools` — score=65, severity=HIGH, max_issue=HIGH, rules=P1, RP1, YR1, YR4
- `hugging-face-community-evals` — score=65, severity=HIGH, max_issue=HIGH, rules=AST4×5, AE1, E2, LP3
- `videodb` — score=65, severity=HIGH, max_issue=HIGH, rules=LP1×2, PE3×2, RA2
- `scanning-tools` — score=64, severity=HIGH, max_issue=HIGH, rules=PE2×15, RP1×2, YR4×2, TM1
- `typescript-expert` — score=64, severity=HIGH, max_issue=HIGH, rules=RP1×14, TM1×2, AST4, LP3
- `webapp-testing` — score=64, severity=HIGH, max_issue=HIGH, rules=AST4×2, TM1×2, LP3
- `linux-shell-scripting` — score=63, severity=HIGH, max_issue=HIGH, rules=PE2×4, RA2×4, PE3, TM1
- `inventory-demand-planning` — score=62, severity=HIGH, max_issue=HIGH, rules=AE4×4, AR2×2, EA2, EA3, P9
- `shopify-development` — score=62, severity=HIGH, max_issue=HIGH, rules=PE3×37, SC1×3, SSRF3×2, AST4, LP3
- `skill-writer` — score=62, severity=HIGH, max_issue=HIGH, rules=RA1×3, AE1
- `git-pr-review` — score=61, severity=HIGH, max_issue=HIGH, rules=P1, P6, YR4
- `instagram` — score=61, severity=HIGH, max_issue=HIGH, rules=SC1×5, SC4×4, E1×3, LP3, SC6
- `mcp-integration` — score=60, severity=HIGH, max_issue=HIGH, rules=E1×13, EA1×2, PE3×2, P1
- `wellally-tech` — score=60, severity=HIGH, max_issue=HIGH, rules=PE3×3, E1, P3
- `plugin-settings` — score=59, severity=HIGH, max_issue=HIGH, rules=AS1×2, PE2, PE3
- `xss-html-injection` — score=58, severity=HIGH, max_issue=HIGH, rules=E1×2, P2×2, EA3, YR4
- `claimable-postgres` — score=57, severity=HIGH, max_issue=HIGH, rules=RP1×4, EA2×3, PE3×3, E1
- `frontend-lighthouse` — score=57, severity=HIGH, max_issue=HIGH, rules=RP1×3, AE1×2, AS3
- `nextjs-on-cloudflare` — score=57, severity=HIGH, max_issue=HIGH, rules=RP1×3, AE1×2, AS3
- `cron-doctor` — score=56, severity=HIGH, max_issue=HIGH, rules=AE1×3, RA2×2
- `weaviate-cookbooks` — score=56, severity=HIGH, max_issue=HIGH, rules=PE3×3, RP1×3, P9×2, PE2
- `monorepo-management` — score=54, severity=HIGH, max_issue=HIGH, rules=RP1×4, PE3, RA2, TM2
- `turborepo-caching` — score=53, severity=HIGH, max_issue=HIGH, rules=RP1×4, PE3×2, TM2
- `systematic-debugging` — score=52, severity=HIGH, max_issue=HIGH, rules=PE3×2, E4, EA4
- `web-scraper` — score=51, severity=HIGH, max_issue=HIGH, rules=AR1, EA2, PE1, SC2
- `agentflow` — score=50, severity=MEDIUM, max_issue=HIGH, rules=EA5×6, RA2×2
- `claude-code-guide` — score=50, severity=MEDIUM, max_issue=HIGH, rules=MP3×2, P1
- `hugging-face-paper-publisher` — score=50, severity=MEDIUM, max_issue=HIGH, rules=PE3×5, AE4, E5, LP3
- `security-scanning-security-hardening` — score=50, severity=MEDIUM, max_issue=CRITICAL, rules=EA2, YR1
- `apify-actor-development` — score=49, severity=MEDIUM, max_issue=HIGH, rules=E1×3, SC2×2, RP1
- `ai-md` — score=48, severity=MEDIUM, max_issue=HIGH, rules=EA2×2, AS1, PE3
- `api-fuzzing-bug-bounty` — score=48, severity=MEDIUM, max_issue=HIGH, rules=PE3×2, E1, TM1
- `cc-skill-continuous-learning` — score=48, severity=MEDIUM, max_issue=HIGH, rules=AS1, AS3, EA2
- `hugging-face-cli` — score=48, severity=MEDIUM, max_issue=HIGH, rules=PE3×3, TM1
- `javascript-testing-patterns` — score=47, severity=MEDIUM, max_issue=HIGH, rules=E1×5, AE1×2
- `neon-postgres` — score=47, severity=MEDIUM, max_issue=HIGH, rules=RP1×5, PE3, TM1
- `user-thoughts` — score=47, severity=MEDIUM, max_issue=HIGH, rules=P2×2, PE3, RA2
- `windows-privilege-escalation` — score=47, severity=MEDIUM, max_issue=HIGH, rules=YR4×2, YR1
- `apify-audience-analysis` — score=46, severity=MEDIUM, max_issue=HIGH, rules=PE3×11, E1×4, LP3
- `apify-brand-reputation-monitoring` — score=46, severity=MEDIUM, max_issue=HIGH, rules=PE3×11, E1×4, LP3
- `apify-competitor-intelligence` — score=46, severity=MEDIUM, max_issue=HIGH, rules=PE3×11, E1×4, LP3
- `apify-content-analytics` — score=46, severity=MEDIUM, max_issue=HIGH, rules=PE3×11, E1×4, LP3
- `apify-ecommerce` — score=46, severity=MEDIUM, max_issue=HIGH, rules=PE3×11, E1×4, LP3
- `apify-influencer-discovery` — score=46, severity=MEDIUM, max_issue=HIGH, rules=PE3×11, E1×4, LP3
- `apify-lead-generation` — score=46, severity=MEDIUM, max_issue=HIGH, rules=PE3×11, E1×4, LP3
- `apify-market-research` — score=46, severity=MEDIUM, max_issue=HIGH, rules=PE3×11, E1×4, LP3
- `apify-trend-analysis` — score=46, severity=MEDIUM, max_issue=HIGH, rules=PE3×11, E1×4, LP3
- `apify-ultimate-scraper` — score=46, severity=MEDIUM, max_issue=HIGH, rules=PE3×12, E1×4, LP3
- `cicd-automation-workflow-automate` — score=46, severity=MEDIUM, max_issue=HIGH, rules=PE3×8, RP1×3, EA2
- `os-scripting` — score=46, severity=MEDIUM, max_issue=HIGH, rules=P1×3, PE2, RA2
- `agent-orchestrator` — score=45, severity=MEDIUM, max_issue=HIGH, rules=AE1, AST4, LP3, SC1, SC4
- `aws-serverless` — score=45, severity=MEDIUM, max_issue=HIGH, rules=E1, MP3, TM1
- `error-handling-patterns` — score=45, severity=MEDIUM, max_issue=HIGH, rules=AE1×2, OH3
- `git-hooks-automation` — score=45, severity=MEDIUM, max_issue=HIGH, rules=RP1×9, TM1×3
- `api-testing-observability-api-mock` — score=44, severity=MEDIUM, max_issue=HIGH, rules=AE1×2, SSRF2
- `matematico-tao` — score=44, severity=MEDIUM, max_issue=HIGH, rules=AE4×2, AE1, LP3
- `prompt-engineering-patterns` — score=44, severity=MEDIUM, max_issue=HIGH, rules=P6×3, LP3
- `skill-creator-ms` — score=44, severity=MEDIUM, max_issue=HIGH, rules=RA1×3, RP1
- `azure-servicebus-ts` — score=43, severity=MEDIUM, max_issue=HIGH, rules=E4, P3
- `claude-settings-audit` — score=43, severity=MEDIUM, max_issue=HIGH, rules=AS1, AS2
- `linear-claude-skill` — score=43, severity=MEDIUM, max_issue=HIGH, rules=RP1×42, PE3×2, RA2×2
- `transformers-js` — score=43, severity=MEDIUM, max_issue=HIGH, rules=AE1×5
- `uv-package-manager` — score=43, severity=MEDIUM, max_issue=HIGH, rules=RA2, SC2, TM2, YR1
- `writing-great-skills` — score=43, severity=MEDIUM, max_issue=HIGH, rules=AE1×4
- `ad-creative` — score=42, severity=MEDIUM, max_issue=HIGH, rules=E1×3, RP1×3, AR2
- `backend-dev-guidelines` — score=42, severity=MEDIUM, max_issue=HIGH, rules=PE3×2, TM1
- `beautiful-prose` — score=42, severity=MEDIUM, max_issue=HIGH, rules=AR2, P6
- `deploy-to-vercel` — score=42, severity=MEDIUM, max_issue=HIGH, rules=PE3×2, LP3, RA2
- `drizzle-migration-conflict` — score=42, severity=MEDIUM, max_issue=HIGH, rules=AS3, LP3, P6, RA2
- `create-plugin` — score=41, severity=MEDIUM, max_issue=HIGH, rules=MP3, RA1
- `ingest-youtube` — score=41, severity=MEDIUM, max_issue=HIGH, rules=AE1, AST4, LP3
- `paypal-integration` — score=41, severity=MEDIUM, max_issue=HIGH, rules=E1×4, EA2×2, PE3
- `hubspot-integration` — score=40, severity=MEDIUM, max_issue=HIGH, rules=PE3×6, E1×4
- `linkerd-patterns` — score=40, severity=MEDIUM, max_issue=HIGH, rules=SC2, TM2
- `task-intelligence` — score=40, severity=MEDIUM, max_issue=HIGH, rules=AE1, PE3
- `api-design-principles` — score=38, severity=MEDIUM, max_issue=HIGH, rules=E1×4, TM1×2
- `cred-omega` — score=38, severity=MEDIUM, max_issue=HIGH, rules=PE3×9, PE2×2
- `odoo-backup-strategy` — score=38, severity=MEDIUM, max_issue=HIGH, rules=E5×2, RA2, TM1
- `autonomous-agents` — score=37, severity=MEDIUM, max_issue=HIGH, rules=EA2×2, AR3, OH3
- `convex` — score=37, severity=MEDIUM, max_issue=HIGH, rules=RP1×16, E1×4, PE3
- `error-debugging-error-trace` — score=37, severity=MEDIUM, max_issue=HIGH, rules=AE1×2
- `error-diagnostics-error-trace` — score=37, severity=MEDIUM, max_issue=HIGH, rules=AE1×2
- `file-uploads` — score=37, severity=MEDIUM, max_issue=HIGH, rules=AR3, PE3
- `framework-migration-code-migrate` — score=37, severity=MEDIUM, max_issue=HIGH, rules=AE1×2
- `frontend-slides` — score=37, severity=MEDIUM, max_issue=HIGH, rules=E1, EA2, LP3, P2
- `git-pr-workflows-pr-enhance` — score=37, severity=MEDIUM, max_issue=HIGH, rules=AE1×2
- `nodejs-backend-patterns` — score=37, severity=MEDIUM, max_issue=HIGH, rules=AE1×2
- `project-skill-audit` — score=37, severity=MEDIUM, max_issue=HIGH, rules=AE1×2
- `theme-factory` — score=37, severity=MEDIUM, max_issue=HIGH, rules=AE1×2
- `typescript-advanced-types` — score=37, severity=MEDIUM, max_issue=HIGH, rules=AE1×2
- `web-performance-optimization` — score=37, severity=MEDIUM, max_issue=HIGH, rules=RP1×3, E1×2, P2
- `codebase-audit-pre-push` — score=36, severity=MEDIUM, max_issue=HIGH, rules=PE3×3, EA4
- `html-injection-testing` — score=36, severity=MEDIUM, max_issue=HIGH, rules=P2×6, E1
- `native-data-fetching` — score=36, severity=MEDIUM, max_issue=HIGH, rules=PE3×7, E1×3
- `pipecat-friday-agent` — score=36, severity=MEDIUM, max_issue=HIGH, rules=PE3×2, LP3
- `skill-sentinel` — score=36, severity=MEDIUM, max_issue=HIGH, rules=E1, LP3, PE3, SC1, SC4
- `wcag-audit-patterns` — score=36, severity=MEDIUM, max_issue=HIGH, rules=P2×2, RP1×2
- `atlas-contract` — score=35, severity=MEDIUM, max_issue=HIGH, rules=EA2×4, P1
- `papers-skill` — score=35, severity=MEDIUM, max_issue=HIGH, rules=E1×2, AR2, LP3
- `react-best-practices` — score=34, severity=MEDIUM, max_issue=HIGH, rules=OH1×2, RP1×2
- `vibe-code-cleanup` — score=34, severity=MEDIUM, max_issue=HIGH, rules=RP1×5, PE3×2
- `bats-testing-patterns` — score=33, severity=MEDIUM, max_issue=HIGH, rules=PE2×2, TM1
- `discord-automation` — score=33, severity=MEDIUM, max_issue=HIGH, rules=P3×2
- `skill-optimizer` — score=33, severity=MEDIUM, max_issue=HIGH, rules=AE1, AS3
- `autonomous-agent-patterns` — score=32, severity=MEDIUM, max_issue=HIGH, rules=EA2×2, TM1
- `mmx-cli` — score=32, severity=MEDIUM, max_issue=HIGH, rules=EA2, PE3, RA2
- `open-dynamic-workflows` — score=32, severity=MEDIUM, max_issue=HIGH, rules=AE1, RP1
- `sqlmap-database-pentesting` — score=32, severity=MEDIUM, max_issue=HIGH, rules=PE3, YR4
- `agent-development` — score=31, severity=MEDIUM, max_issue=HIGH, rules=EA1, MP3
- `dbos-golang` — score=31, severity=MEDIUM, max_issue=HIGH, rules=E1×4, P3
- `dbos-typescript` — score=31, severity=MEDIUM, max_issue=HIGH, rules=E1×3, P3
- `decision-navigator` — score=31, severity=MEDIUM, max_issue=HIGH, rules=AR2×2
- `k8s-manifest-generator` — score=31, severity=MEDIUM, max_issue=HIGH, rules=PE3, TM4
- `memory-forensics` — score=31, severity=MEDIUM, max_issue=HIGH, rules=PE2×4, YR1
- `product-manager-toolkit` — score=31, severity=MEDIUM, max_issue=HIGH, rules=E4, LP3
- `shellcheck-configuration` — score=31, severity=MEDIUM, max_issue=HIGH, rules=PE2, RA2, TM2
- `tools-page-seo-optimizer` — score=31, severity=MEDIUM, max_issue=HIGH, rules=AS3×6, P2
- `api-security-best-practices` — score=30, severity=MEDIUM, max_issue=HIGH, rules=PE3×4
- `atlas-ledger` — score=30, severity=MEDIUM, max_issue=HIGH, rules=EA2, P1
- `auri-core` — score=30, severity=MEDIUM, max_issue=HIGH, rules=AE3, AS3
- `auth-implementation-patterns` — score=30, severity=MEDIUM, max_issue=HIGH, rules=PE3×3
- `azd-deployment` — score=30, severity=MEDIUM, max_issue=HIGH, rules=PE3×7
- `dbos-python` — score=30, severity=MEDIUM, max_issue=HIGH, rules=E1×2, P3
- `helm-chart-scaffolding` — score=30, severity=MEDIUM, max_issue=HIGH, rules=E5, LP3, PE3
- `hig-inputs` — score=30, severity=MEDIUM, max_issue=HIGH, rules=EA2, P1
- `plaid-fintech` — score=30, severity=MEDIUM, max_issue=HIGH, rules=PE3×8
- `planning-with-files` — score=30, severity=MEDIUM, max_issue=HIGH, rules=P2×4
- `playwright-java` — score=30, severity=MEDIUM, max_issue=HIGH, rules=P2, P4, RA2
- `re-create` — score=30, severity=MEDIUM, max_issue=HIGH, rules=AR1×2
- `remotion` — score=30, severity=MEDIUM, max_issue=HIGH, rules=RP1×2, AS2
- `spline-3d-integration` — score=30, severity=MEDIUM, max_issue=HIGH, rules=P2×3
- `astro` — score=29, severity=MEDIUM, max_issue=HIGH, rules=RP1×5, P2
- `azure-microsoft-playwright-testing-ts` — score=29, severity=MEDIUM, max_issue=HIGH, rules=RP1×3, PE3
- `cc-skill-strategic-compact` — score=29, severity=MEDIUM, max_issue=HIGH, rules=AS1
- `git-advanced-workflows` — score=29, severity=MEDIUM, max_issue=HIGH, rules=TM1×5
- `n8n-validation-expert` — score=29, severity=MEDIUM, max_issue=HIGH, rules=EA4, MP3
- `smtp-penetration-testing` — score=29, severity=MEDIUM, max_issue=HIGH, rules=PE2×4, YR4
- `api-documentation-generator` — score=28, severity=MEDIUM, max_issue=HIGH, rules=E1×7, PE3
- `architecture-decision-records` — score=28, severity=MEDIUM, max_issue=HIGH, rules=E4×2
- `bulletmind` — score=28, severity=MEDIUM, max_issue=HIGH, rules=P6, P9
- `deployment-procedures` — score=28, severity=MEDIUM, max_issue=HIGH, rules=AR2, EA2
- `hasdata` — score=28, severity=MEDIUM, max_issue=HIGH, rules=E1×43, TM1
- `pentest-checklist` — score=28, severity=MEDIUM, max_issue=HIGH, rules=PE2×2, YR4
- `app-builder` — score=27, severity=MEDIUM, max_issue=HIGH, rules=RP1×11, PE3
- `bash-linux` — score=27, severity=MEDIUM, max_issue=HIGH, rules=E1, TM1
- `diagnosing-bugs` — score=27, severity=MEDIUM, max_issue=HIGH, rules=P6
- `gdpr-data-handling` — score=27, severity=MEDIUM, max_issue=HIGH, rules=AR3, EA2
- `manifest` — score=27, severity=MEDIUM, max_issue=HIGH, rules=AS1, RA2
- `security-scanning-security-sast` — score=27, severity=MEDIUM, max_issue=HIGH, rules=EA2, TM1
- `ai-wrapper-product` — score=26, severity=MEDIUM, max_issue=HIGH, rules=AR1×2
- `angular-best-practices` — score=26, severity=MEDIUM, max_issue=HIGH, rules=P2×2
- `azure-communication-common-java` — score=26, severity=MEDIUM, max_issue=HIGH, rules=PE3×2
- `azure-monitor-opentelemetry-exporter-java` — score=26, severity=MEDIUM, max_issue=HIGH, rules=PE3×2
- `azure-speech-to-text-rest-py` — score=26, severity=MEDIUM, max_issue=HIGH, rules=PE3×2
- `conductor-setup` — score=26, severity=MEDIUM, max_issue=HIGH, rules=PE3×3
- `discord-bot-architect` — score=26, severity=MEDIUM, max_issue=HIGH, rules=PE3×5
- `hugging-face-evaluation` — score=26, severity=MEDIUM, max_issue=HIGH, rules=PE3×5
- `kubestellar-console` — score=26, severity=MEDIUM, max_issue=HIGH, rules=PE3×5
- `vercel-cli-with-tokens` — score=26, severity=MEDIUM, max_issue=HIGH, rules=PE3×11
- `voice-ai-engine-development` — score=26, severity=MEDIUM, max_issue=HIGH, rules=PE3×2
- `agent-creator` — score=25, severity=MEDIUM, max_issue=HIGH, rules=AE1
- `broken-authentication` — score=25, severity=MEDIUM, max_issue=HIGH, rules=EA2, YR4
- `burpsuite-project-parser` — score=25, severity=MEDIUM, max_issue=HIGH, rules=MP2, YR4
- `clarity-gate` — score=25, severity=MEDIUM, max_issue=HIGH, rules=EA2, P2
- `comprehensive-review-pr-enhance` — score=25, severity=MEDIUM, max_issue=HIGH, rules=AE1
- `conductor-revert` — score=25, severity=MEDIUM, max_issue=HIGH, rules=TM1×2
- `firmware-analyst` — score=25, severity=MEDIUM, max_issue=HIGH, rules=PE2×2, PE3
- `plugin-validator` — score=25, severity=MEDIUM, max_issue=HIGH, rules=AE1
- `red-team-tactics` — score=25, severity=MEDIUM, max_issue=HIGH, rules=PE2, TM2
- `go-rod-master` — score=24, severity=MEDIUM, max_issue=HIGH, rules=LP3, PE3
- `ste-writing` — score=24, severity=MEDIUM, max_issue=HIGH, rules=LP3, PE3
- `fastapi-templates` — score=23, severity=MEDIUM, max_issue=HIGH, rules=PE3×2
- `landing-page-generator` — score=23, severity=MEDIUM, max_issue=HIGH, rules=LP3, OH1
- `llm-application-dev-prompt-optimize` — score=23, severity=MEDIUM, max_issue=HIGH, rules=AR2, EA3
- `model-authoring` — score=23, severity=MEDIUM, max_issue=HIGH, rules=EA3, MP3
- `azure-monitor-query-java` — score=22, severity=MEDIUM, max_issue=HIGH, rules=E1, PE3
- `basecamp-automation` — score=22, severity=MEDIUM, max_issue=HIGH, rules=P3
- `burp-suite-testing` — score=22, severity=MEDIUM, max_issue=HIGH, rules=PE3×2
- `faf-expert` — score=22, severity=MEDIUM, max_issue=HIGH, rules=EA5
- `gemini-api-integration` — score=22, severity=MEDIUM, max_issue=HIGH, rules=AR3
- `github-actions-templates` — score=22, severity=MEDIUM, max_issue=HIGH, rules=PE3×2
- `hasdata-cli` — score=22, severity=MEDIUM, max_issue=HIGH, rules=RA1
- `laravel-security-audit` — score=22, severity=MEDIUM, max_issue=HIGH, rules=PE3×2
- `mtls-configuration` — score=22, severity=MEDIUM, max_issue=HIGH, rules=EA2, TM4
- `n8n-mcp-tools-expert` — score=22, severity=MEDIUM, max_issue=HIGH, rules=MP3
- `n8n-workflow-patterns` — score=22, severity=MEDIUM, max_issue=HIGH, rules=P3
- `odoo-docker-deployment` — score=22, severity=MEDIUM, max_issue=HIGH, rules=PE3×2
- `polis-protocol` — score=22, severity=MEDIUM, max_issue=HIGH, rules=EA5
- `senior-architect` — score=22, severity=MEDIUM, max_issue=HIGH, rules=LP3, PE3
- `senior-fullstack` — score=22, severity=MEDIUM, max_issue=HIGH, rules=LP3, PE3
- `slack-automation` — score=22, severity=MEDIUM, max_issue=HIGH, rules=P3
- `analyze-project` — score=21, severity=MEDIUM, max_issue=HIGH, rules=AR2
- `azure-servicebus-dotnet` — score=21, severity=MEDIUM, max_issue=HIGH, rules=E4
- `claude-win11-speckit-update-skill` — score=21, severity=MEDIUM, max_issue=HIGH, rules=RA1
- `database-cloud-optimization-cost-optimize` — score=21, severity=MEDIUM, max_issue=HIGH, rules=P6
- `design-md` — score=21, severity=MEDIUM, max_issue=HIGH, rules=P6
- `gdb-cli` — score=21, severity=MEDIUM, max_issue=HIGH, rules=YR1
- `hig-components-menus` — score=21, severity=MEDIUM, max_issue=HIGH, rules=P6
- `hig-foundations` — score=21, severity=MEDIUM, max_issue=HIGH, rules=OH3, P2
- `humanize-chinese` — score=21, severity=MEDIUM, max_issue=HIGH, rules=P6
- `javascript-typescript-typescript-scaffold` — score=21, severity=MEDIUM, max_issue=HIGH, rules=PE3, TM3
- `keyword-extractor` — score=21, severity=MEDIUM, max_issue=HIGH, rules=P6
- `lemmaly` — score=21, severity=MEDIUM, max_issue=HIGH, rules=RA1
- `microsoft-teams-automation` — score=21, severity=MEDIUM, max_issue=HIGH, rules=E4
- `paywall-upgrade-cro` — score=21, severity=MEDIUM, max_issue=HIGH, rules=P6
- `pre-release-review` — score=21, severity=MEDIUM, max_issue=HIGH, rules=P6
- `professional-proofreader` — score=21, severity=MEDIUM, max_issue=HIGH, rules=P6
- `speckit-updater` — score=21, severity=MEDIUM, max_issue=HIGH, rules=RA1
- `agenttrace-session-audit` — score=20, severity=LOW, max_issue=HIGH, rules=MP3
- `api-endpoint-builder` — score=20, severity=LOW, max_issue=HIGH, rules=TM1
- `architecture` — score=20, severity=LOW, max_issue=HIGH, rules=MP3
- `ask-matt` — score=20, severity=LOW, max_issue=HIGH, rules=MP3
- `audit-context-building` — score=20, severity=LOW, max_issue=HIGH, rules=MP3
- `c-pro` — score=20, severity=LOW, max_issue=HIGH, rules=MP3
- `carrier-relationship-management` — score=20, severity=LOW, max_issue=HIGH, rules=AR2
- `cc-skill-backend-patterns` — score=20, severity=LOW, max_issue=HIGH, rules=TM1
- `cc-skill-coding-standards` — score=20, severity=LOW, max_issue=HIGH, rules=TM1
- `incident-response-incident-response` — score=20, severity=LOW, max_issue=HIGH, rules=MP3
- `linkedin-profile-optimizer` — score=20, severity=LOW, max_issue=HIGH, rules=MP3
- `personal-tool-builder` — score=20, severity=LOW, max_issue=HIGH, rules=MP3
- `robius-matrix-integration` — score=20, severity=LOW, max_issue=HIGH, rules=YR4
- `rust-async-patterns` — score=20, severity=LOW, max_issue=HIGH, rules=YR4
- `security-compliance-compliance-check` — score=20, severity=LOW, max_issue=HIGH, rules=YR4
- `sql-pro` — score=20, severity=LOW, max_issue=HIGH, rules=AR3
- `voice-agents` — score=20, severity=LOW, max_issue=HIGH, rules=MP3
- `anti-reversing-techniques` — score=18, severity=LOW, max_issue=HIGH, rules=YR1
- `context-management-context-save` — score=18, severity=LOW, max_issue=HIGH, rules=E4
- `ddd-strategic-design` — score=18, severity=LOW, max_issue=HIGH, rules=E4
- `evolution` — score=18, severity=LOW, max_issue=HIGH, rules=P2, SC2
- `go-playwright` — score=18, severity=LOW, max_issue=HIGH, rules=AR3
- `semgrep-rule-creator` — score=18, severity=LOW, max_issue=HIGH, rules=YR2
- `team-collaboration-standup-notes` — score=18, severity=LOW, max_issue=HIGH, rules=E4
- `ai-native-cli` — score=17, severity=LOW, max_issue=HIGH, rules=PE3
- `angular` — score=17, severity=LOW, max_issue=HIGH, rules=P2
- `angular-ui-patterns` — score=17, severity=LOW, max_issue=HIGH, rules=P2
- `azure-ai-agents-persistent-java` — score=17, severity=LOW, max_issue=HIGH, rules=PE3
- `azure-appconfiguration-java` — score=17, severity=LOW, max_issue=HIGH, rules=PE3
- `azure-communication-chat-java` — score=17, severity=LOW, max_issue=HIGH, rules=PE3
- `azure-compute-batch-java` — score=17, severity=LOW, max_issue=HIGH, rules=PE3
- `azure-cosmos-java` — score=17, severity=LOW, max_issue=HIGH, rules=PE3
- `azure-messaging-webpubsub-java` — score=17, severity=LOW, max_issue=HIGH, rules=PE3
- `azure-messaging-webpubsubservice-py` — score=17, severity=LOW, max_issue=HIGH, rules=PE3
- `azure-monitor-ingestion-java` — score=17, severity=LOW, max_issue=HIGH, rules=PE3
- `azure-postgres-ts` — score=17, severity=LOW, max_issue=HIGH, rules=PE3
- `azure-resource-manager-playwright-dotnet` — score=17, severity=LOW, max_issue=HIGH, rules=PE3
- `azure-web-pubsub-ts` — score=17, severity=LOW, max_issue=HIGH, rules=PE3
- `cold-email` — score=17, severity=LOW, max_issue=HIGH, rules=AR1
- `content-strategy` — score=17, severity=LOW, max_issue=HIGH, rules=PE3
- `git-pr-workflows-git-workflow` — score=17, severity=LOW, max_issue=HIGH, rules=TM1
- `github-workflow-automation` — score=17, severity=LOW, max_issue=HIGH, rules=TM1
- `google-docs-automation` — score=17, severity=LOW, max_issue=HIGH, rules=PE3
- `hugging-face-datasets` — score=17, severity=LOW, max_issue=HIGH, rules=PE3
- `odoo-performance-tuner` — score=17, severity=LOW, max_issue=HIGH, rules=P1
- `production-scheduling` — score=17, severity=LOW, max_issue=HIGH, rules=AR1
- `salesforce-development` — score=17, severity=LOW, max_issue=HIGH, rules=PE3
- `sveltekit` — score=17, severity=LOW, max_issue=HIGH, rules=P2
- `cc-skill-security-review` — score=16, severity=LOW, max_issue=HIGH, rules=OH1
- `frontend-mobile-security-xss-scan` — score=16, severity=LOW, max_issue=HIGH, rules=OH1
- `schema-markup-generator` — score=16, severity=LOW, max_issue=HIGH, rules=OH1
- `aegisops-ai` — score=15, severity=LOW, max_issue=HIGH, rules=PE3
- `geminiignore-finops` — score=15, severity=LOW, max_issue=HIGH, rules=PE3
- `nestjs-expert` — score=15, severity=LOW, max_issue=HIGH, rules=PE3
- `news-sentiment-engine` — score=15, severity=LOW, max_issue=HIGH, rules=PE3
- `posix-shell-pro` — score=15, severity=LOW, max_issue=HIGH, rules=PE3
- `saas-mvp-launcher` — score=15, severity=LOW, max_issue=HIGH, rules=PE3
- `telegram-bot-builder` — score=15, severity=LOW, max_issue=HIGH, rules=PE3
- `x402-express-wrapper` — score=15, severity=LOW, max_issue=HIGH, rules=PE3

## Failed scans

- `crossframe` rc=-15: 
- `design-it` rc=-15: 
- `loki-mode` rc=-1: timeout after 180s
