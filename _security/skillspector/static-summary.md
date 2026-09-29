# SkillSpector static scan summary

- Scanned at: `2026-09-29T06:55:59.202928+00:00`
- Skillspector: `SkillSpector v2.12.0`
- Mode: static (`--no-llm`)
- Skills discovered: **2056**
- Scanned OK: **2056** / failed: **0**
- Workers: **8**
- Duration: **1809.1s**
- High/Critical (by SkillSpector severity): **172**

## Severity counts

- CRITICAL: 87
- HIGH: 85
- MEDIUM: 287
- LOW: 1597

## Ranked skills (highest risk first)

| Score | Severity | Rec | Issues | Skill | Top rules |
|------:|----------|-----|-------:|-------|-----------|
| 100 | CRITICAL | DO_NOT_INSTALL | 56 | `007` | PE3×26, AR3×5, P1×4, P6×3, YR4×3 |
| 100 | CRITICAL | DO_NOT_INSTALL | 26 | `2slides-ppt-generator` | TT3×7, PE3×6, E1×5, SC1×3, SC4×3 |
| 100 | CRITICAL | DO_NOT_INSTALL | 25 | `agents-generator` | P9×13, RP1×7, AE1×2, AR2, MP3 |
| 100 | CRITICAL | DO_NOT_INSTALL | 44 | `apple-container` | AE1×12, PE2×12, TM1×10, RA2×4, PE3×3 |
| 100 | CRITICAL | DO_NOT_INSTALL | 27 | `attack-chain` | PE2×5, YR4×5, PE3×4, RA2×4, YR1×4 |
| 100 | CRITICAL | DO_NOT_INSTALL | 18 | `aws-penetration-testing` | SSRF1×8, PE2×2, AE1, E5, EA2 |
| 100 | CRITICAL | DO_NOT_INSTALL | 15 | `claude-code-expert` | AS1×7, EA5×5, PE2, SC2, TM1 |
| 100 | CRITICAL | DO_NOT_INSTALL | 33 | `cloud-penetration-testing` | SSRF1×14, PE3×6, E5×3, PE2×3, SC2×2 |
| 100 | CRITICAL | DO_NOT_INSTALL | 184 | `cloudflare` | E1×124, RP1×32, TM1×11, PE3×8, EA2×3 |
| 100 | CRITICAL | DO_NOT_INSTALL | 12 | `cloudflare-security-audit` | TM3×4, EA2×2, AE1, P1, PE1 |
| 100 | CRITICAL | DO_NOT_INSTALL | 65 | `comfyui-gateway` | PE3×22, RP1×14, E1×10, TM3×8, PE2×5 |
| 100 | CRITICAL | DO_NOT_INSTALL | 40 | `command-development` | AS1×17, P2×6, TM1×6, AE1×4, RA2×3 |
| 100 | CRITICAL | DO_NOT_INSTALL | 15 | `competitor-analysis` | AE1×9, TM1×3, AS1, LP1, TM2 |
| 100 | CRITICAL | DO_NOT_INSTALL | 27 | `computer-use-agents` | EA2×17, RP1×3, TM1×3, AR1, E1 |
| 100 | CRITICAL | DO_NOT_INSTALL | 26 | `container-security-hardening` | RP1×10, TM1×7, PE2×3, PE5×2, AR2 |
| 100 | CRITICAL | DO_NOT_INSTALL | 14 | `diary` | AST4×2, EA2×2, TT2×2, AST7, E1 |
| 100 | CRITICAL | DO_NOT_INSTALL | 32 | `ecl-harness-engineer` | RP1×8, PE3×7, TM1×6, AE1×5, EA2×2 |
| 100 | CRITICAL | DO_NOT_INSTALL | 27 | `environment-setup-guide` | PE2×12, PE3×8, TM3×3, E1, RA2 |
| 100 | CRITICAL | DO_NOT_INSTALL | 7 | `ethical-hacking-methodology` | YR4×3, PE3×2, PE2, YR1 |
| 100 | CRITICAL | DO_NOT_INSTALL | 33 | `expo-brownfield` | RP1×21, RA2×3, TM1×3, AE1×2, P9×2 |
| 100 | CRITICAL | DO_NOT_INSTALL | 10 | `hig-patterns` | EA2×3, AE1×2, RA2×2, AR2, EA3 |
| 100 | CRITICAL | DO_NOT_INSTALL | 15 | `hook-development` | AE1×6, PE3×3, TM1×2, E1, LP3 |
| 100 | CRITICAL | DO_NOT_INSTALL | 26 | `hugging-face-jobs` | E5×11, E1×4, PE1×4, AE1×2, EA2×2 |
| 100 | CRITICAL | DO_NOT_INSTALL | 25 | `hugging-face-model-trainer` | PE2×9, AST4×4, E5×3, TM2×3, PE1×2 |
| 100 | CRITICAL | DO_NOT_INSTALL | 29 | `last30days` | PE3×16, E1×4, PE2×3, RA2×2, EA4 |
| 100 | CRITICAL | DO_NOT_INSTALL | 9 | `linkedin-content-generator` | AE1×3, MP3×3, LP3, P6, RA2 |
| 100 | CRITICAL | DO_NOT_INSTALL | 40 | `linux-privilege-escalation` | PE2×24, PE3×8, TM2×2, YR1×2, YR4×2 |
| 100 | CRITICAL | DO_NOT_INSTALL | 25 | `llm-security` | P2×5, P7×4, AR3×3, P1×3, YR4×3 |
| 100 | CRITICAL | DO_NOT_INSTALL | 144 | `loki-mode` | TM1×27, EA2×19, SC1×19, RP1×14, RA1×12 |
| 100 | CRITICAL | DO_NOT_INSTALL | 41 | `lore` | AE1×14, P2×8, AST4×6, P1×3, AR3×2 |
| 100 | CRITICAL | DO_NOT_INSTALL | 29 | `macos-spm-app-packaging` | RA2×17, AE1×5, PE3×4, TM1×2, LP3 |
| 100 | CRITICAL | DO_NOT_INSTALL | 14 | `make-me-an-expert` | AS3×4, RA2×4, AE1×3, AR2, AST4 |
| 100 | CRITICAL | DO_NOT_INSTALL | 18 | `manage-skills` | AS3×11, AS1×3, TM1×2, AE1, RA2 |
| 100 | CRITICAL | DO_NOT_INSTALL | 17 | `mcp-builder` | AE1×6, E1×2, SC1×2, SC4×2, EA1 |
| 100 | CRITICAL | DO_NOT_INSTALL | 5 | `metasploit-framework` | YR4×2, P1, PE2, YR1 |
| 100 | CRITICAL | DO_NOT_INSTALL | 49 | `monte-carlo-push-ingestion` | AST7×29, E1×13, AE1×3, PE3×2, LP3 |
| 100 | CRITICAL | DO_NOT_INSTALL | 43 | `network-101` | PE2×34, TM2×4, TM1×2, YR4×2, RA2 |
| 100 | CRITICAL | DO_NOT_INSTALL | 26 | `notebooklm` | AST4×8, AS3×4, EA2×2, PE3×2, RA2×2 |
| 100 | CRITICAL | DO_NOT_INSTALL | 1285 | `pentest-tools` | PE3×588, SSRF1×178, E1×144, P2×61, YR4×59 |
| 100 | CRITICAL | DO_NOT_INSTALL | 11 | `plugin-structure` | AE1×4, AS3×2, PE3×2, RA1, RA2 |
| 100 | CRITICAL | DO_NOT_INSTALL | 26 | `privilege-escalation-methods` | PE2×18, TM2×3, PE3×2, YR4×2, YR1 |
| 100 | CRITICAL | DO_NOT_INSTALL | 343 | `rclone-cli` | PE3×94, PE2×70, P2×38, TM1×29, RA1×19 |
| 100 | CRITICAL | DO_NOT_INSTALL | 112 | `remote-gpu-trainer` | RA2×40, PE3×26, PE2×14, AE1×10, AR2×3 |
| 100 | CRITICAL | DO_NOT_INSTALL | 59 | `reverse-engineering` | RA1×20, AE1×7, YR1×7, PE2×6, PE3×5 |
| 100 | CRITICAL | DO_NOT_INSTALL | 22 | `senior-frontend` | AE1×12, E1×6, PE3×2, LP3, OH1 |
| 100 | CRITICAL | DO_NOT_INSTALL | 91 | `shadcn` | RP1×73, P9×10, AE1×2, EA2×2, RA1×2 |
| 100 | CRITICAL | DO_NOT_INSTALL | 8 | `sharp-edges` | P1×2, AR2, EA2, EA4, RA1 |
| 100 | CRITICAL | DO_NOT_INSTALL | 33 | `skill-developer` | RP1×16, TM3×8, AS1×6, P3, RA2 |
| 100 | CRITICAL | DO_NOT_INSTALL | 18 | `skill-installer` | PE3×8, AS3×5, AST4, LP3, RA1 |
| 100 | CRITICAL | DO_NOT_INSTALL | 25 | `stability-ai` | AE1×13, PE3×5, E1×2, P6×2, LP3 |
| 100 | CRITICAL | DO_NOT_INSTALL | 9 | `survey-generator` | AE1×4, EA2×2, E1, LP1, TT3 |
| 100 | CRITICAL | DO_NOT_INSTALL | 56 | `telegram` | E1×23, SC1×12, PE3×9, SC4×4, AE1×3 |
| 100 | CRITICAL | DO_NOT_INSTALL | 48 | `turnstile-spin` | E1×21, AE1×12, EA2×4, P9×4, SC2×3 |
| 100 | CRITICAL | DO_NOT_INSTALL | 42 | `ui-ux-pro-max` | E1×15, EA2×7, PE3×5, RP1×4, P6×3 |
| 100 | CRITICAL | DO_NOT_INSTALL | 20 | `varlock` | PE3×12, AS3×2, E2×2, SC2×2, RA2 |
| 100 | CRITICAL | DO_NOT_INSTALL | 24 | `vercel-optimize` | AE1×17, EA2×3, YR1×2, LP3, P6 |
| 100 | CRITICAL | DO_NOT_INSTALL | 10 | `vulnerability-scanner` | PE3×3, AR3×2, TM3×2, AST4, EA4 |
| 100 | CRITICAL | DO_NOT_INSTALL | 54 | `whatsapp-cloud-api` | PE3×17, SC1×11, AE1×10, SC4×6, E1×4 |
| 100 | CRITICAL | DO_NOT_INSTALL | 8 | `wordpress-penetration-testing` | E1×2, YR2×2, YR4×2, P1, YR1 |
| 99 | CRITICAL | DO_NOT_INSTALL | 51 | `shopify-development` | PE3×41, SC1×3, AE1×2, SSRF3×2, AST4 |
| 98 | CRITICAL | DO_NOT_INSTALL | 8 | `active-directory-attacks` | TM1×2, YR1×2, YR4×2, EA2, PE2 |
| 98 | CRITICAL | DO_NOT_INSTALL | 5 | `feature-tracking` | P1×2, AR3, RA1, YR4 |
| 96 | CRITICAL | DO_NOT_INSTALL | 10 | `android-dev` | PE3×5, AE1×2, RP1×2, P2 |
| 95 | CRITICAL | DO_NOT_INSTALL | 11 | `hig-technologies` | EA2×6, P6×3, AE1, MP3 |
| 94 | CRITICAL | DO_NOT_INSTALL | 53 | `hugging-face-paper-publisher` | AE1×45, PE3×5, AE4, E5, LP3 |
| 94 | CRITICAL | DO_NOT_INSTALL | 9 | `security-and-hardening` | PE3×5, EA1, P2, SSRF1, YR4 |
| 94 | CRITICAL | DO_NOT_INSTALL | 14 | `ssh-penetration-testing` | PE3×9, E1, E3, PE2, YR1 |
| 93 | CRITICAL | DO_NOT_INSTALL | 38 | `file-path-traversal` | PE3×35, E1, PE2, YR2 |
| 92 | CRITICAL | DO_NOT_INSTALL | 6 | `bash-defensive-patterns` | AE1×2, EA2, RA2, TM1, TM2 |
| 92 | CRITICAL | DO_NOT_INSTALL | 10 | `readme` | PE3×3, PE2×2, RP1×2, TM1×2, EA2 |
| 90 | CRITICAL | DO_NOT_INSTALL | 7 | `gcp-cloud-run` | TM1×2, AR1, E1, PE2, RA2 |
| 89 | CRITICAL | DO_NOT_INSTALL | 7 | `bun-development` | PE3×2, SC2×2, TM2×2, RP1 |
| 89 | CRITICAL | DO_NOT_INSTALL | 14 | `vibecode-production-qa-validator` | RP1×9, SC2×2, TM2×2, PE3 |
| 89 | CRITICAL | DO_NOT_INSTALL | 6 | `web-scraper` | AE1×2, AR1, EA2, PE1, SC2 |
| 88 | CRITICAL | DO_NOT_INSTALL | 7 | `devops-deploy` | E1×2, EA2×2, TM1×2, YR1 |
| 88 | CRITICAL | DO_NOT_INSTALL | 8 | `super-code` | AE1×4, TM1×3, EA2 |
| 86 | CRITICAL | DO_NOT_INSTALL | 7 | `gitops-workflow` | PE3×3, EA2, PE2, SC2, TM2 |
| 85 | CRITICAL | DO_NOT_INSTALL | 7 | `claude-in-chrome-troubleshooting` | AS1×3, TM1×3, RA2 |
| 85 | CRITICAL | DO_NOT_INSTALL | 5 | `effective-agent-skills` | AE1×2, EA1, P1, YR4 |
| 85 | CRITICAL | DO_NOT_INSTALL | 19 | `mcp-integration` | E1×13, EA1×2, PE3×2, AE1, P1 |
| 84 | CRITICAL | DO_NOT_INSTALL | 11 | `hugging-face-community-evals` | AST4×5, AE1×4, E2, LP3 |
| 84 | CRITICAL | DO_NOT_INSTALL | 5 | `plugin-settings` | AS1×2, AE1, PE2, PE3 |
| 84 | CRITICAL | DO_NOT_INSTALL | 29 | `postgresql-cli` | P9×20, PE2×5, AE1, EA2, OH1 |
| 83 | CRITICAL | DO_NOT_INSTALL | 14 | `cicd-automation-workflow-automate` | PE3×8, RP1×3, AE1×2, EA2 |
| 83 | CRITICAL | DO_NOT_INSTALL | 7 | `conductor-manage` | RA2×3, AE1×2, TM1×2 |
| 82 | CRITICAL | DO_NOT_INSTALL | 13 | `writing-skills` | RA1×8, AS3×3, AE1, RA2 |
| 81 | CRITICAL | DO_NOT_INSTALL | 5 | `distributed-debugging-debug-trace` | AE1×2, AR3, P1, TM3 |
| 80 | HIGH | DO_NOT_INSTALL | 5 | `skill-audit` | P1×2, PE3×2, YR4 |
| 79 | HIGH | DO_NOT_INSTALL | 14 | `mobile-design` | PE3×10, LP3, MP2, MP3, RA2 |
| 79 | HIGH | DO_NOT_INSTALL | 11 | `pptx` | AST4×5, PE2×2, AE1, AST7, LP3 |
| 79 | HIGH | DO_NOT_INSTALL | 11 | `pptx-official` | AST4×5, PE2×2, AE1, AST7, LP3 |
| 78 | HIGH | DO_NOT_INSTALL | 36 | `firmware-pentest` | PE2×29, TM2×4, YR4×3 |
| 78 | HIGH | DO_NOT_INSTALL | 5 | `skill-scanner` | AE1, E1, EA2, P3, PE3 |
| 77 | HIGH | DO_NOT_INSTALL | 15 | `claude-api` | E1×6, E4×3, P9×3, EA2×2, MP2 |
| 77 | HIGH | DO_NOT_INSTALL | 5 | `claude-delegate` | EA2×2, AE1, EA5, PE3 |
| 77 | HIGH | DO_NOT_INSTALL | 11 | `gemini-deep-research` | PE3×4, SC1×2, SC4×2, EA4, LP3 |
| 77 | HIGH | DO_NOT_INSTALL | 5 | `systematic-debugging` | PE3×2, AE1, E4, EA4 |
| 76 | HIGH | DO_NOT_INSTALL | 5 | `agent-evaluation` | P1×2, AE4, P6, YR4 |
| 76 | HIGH | DO_NOT_INSTALL | 13 | `telegram-bot-messaging` | AE1×9, EA4, LP3, PE2, RA2 |
| 74 | HIGH | DO_NOT_INSTALL | 6 | `spline-3d-integration` | AE1×3, P2×3 |
| 74 | HIGH | DO_NOT_INSTALL | 7 | `using-lwc` | RA2×2, RP1×2, AE1, LP3, P1 |
| 73 | HIGH | DO_NOT_INSTALL | 6 | `lovable-cleanup` | P2×3, PE3×2, YR4 |
| 72 | HIGH | DO_NOT_INSTALL | 6 | `audit-skills` | TM1×3, RA2×2, SC2 |
| 72 | HIGH | DO_NOT_INSTALL | 8 | `marketing-plan` | AE4×4, AR1, AS3, EA2, RA1 |
| 71 | HIGH | DO_NOT_INSTALL | 8 | `aider-delegate` | EA2×4, TM1×2, AE1, EA3 |
| 71 | HIGH | DO_NOT_INSTALL | 5 | `yao-meta-skill` | AE1×2, EA2×2, RA1 |
| 70 | HIGH | DO_NOT_INSTALL | 24 | `k6-load-testing` | E1×12, PE3×6, PE2×5, TM2 |
| 70 | HIGH | DO_NOT_INSTALL | 3 | `pentest-commands` | YR4×2, YR1 |
| 70 | HIGH | DO_NOT_INSTALL | 21 | `playwright-skill` | RP1×13, AE1×4, EA3, LP3, SC1 |
| 70 | HIGH | DO_NOT_INSTALL | 6 | `redis-cli` | AE1×2, PE2×2, PE3, RP1 |
| 70 | HIGH | DO_NOT_INSTALL | 5 | `skill-development` | RA1×3, AE1, AS3 |
| 69 | HIGH | DO_NOT_INSTALL | 17 | `ai-studio-image` | PE3×10, SC1×3, SC4×2, LP3, P6 |
| 69 | HIGH | DO_NOT_INSTALL | 5 | `neon-functions` | AE1×2, P9, PE3, RP1 |
| 69 | HIGH | DO_NOT_INSTALL | 12 | `skill-creator` | AS3×5, E3×3, RA2×2, LP3, RA1 |
| 68 | HIGH | DO_NOT_INSTALL | 4 | `ai-product` | EA2, P1, P6, YR4 |
| 68 | HIGH | DO_NOT_INSTALL | 27 | `audio-transcriber` | SC1×15, AST4×6, PE2×2, AS3, EA2 |
| 68 | HIGH | DO_NOT_INSTALL | 5 | `auth-implementation-patterns` | PE3×3, AE1×2 |
| 68 | HIGH | DO_NOT_INSTALL | 8 | `frontend-observability` | P9×3, AE1×2, MP2×2, RP1 |
| 68 | HIGH | DO_NOT_INSTALL | 5 | `go-rod-master` | AE1×3, LP3, PE3 |
| 68 | HIGH | DO_NOT_INSTALL | 17 | `remotion-best-practices` | RP1×12, AE1×3, E1, EA4 |
| 67 | HIGH | DO_NOT_INSTALL | 8 | `ad-creative` | E1×3, RP1×3, AE1, AR2 |
| 67 | HIGH | DO_NOT_INSTALL | 5 | `drizzle-migration-conflict` | AE1, AS3, LP3, P6, RA2 |
| 67 | HIGH | DO_NOT_INSTALL | 7 | `xlsx` | AST4×3, AE1×2, LP3, P4 |
| 67 | HIGH | DO_NOT_INSTALL | 7 | `xlsx-official` | AST4×3, AE1×2, LP3, P4 |
| 66 | HIGH | DO_NOT_INSTALL | 4 | `codex-delegate` | EA5×2, AE1, EA2 |
| 66 | HIGH | DO_NOT_INSTALL | 10 | `find-complementary-founders` | AE1×7, AE4, EA2, LP3 |
| 65 | HIGH | DO_NOT_INSTALL | 4 | `browser-testing-with-devtools` | P1, RP1, YR1, YR4 |
| 65 | HIGH | DO_NOT_INSTALL | 10 | `docx` | AST4×3, P2×3, PE2×3, LP3 |
| 65 | HIGH | DO_NOT_INSTALL | 10 | `docx-official` | AST4×3, P2×3, PE2×3, LP3 |
| 65 | HIGH | DO_NOT_INSTALL | 3 | `fable-safe-prompt` | AR3, P1, YR4 |
| 65 | HIGH | DO_NOT_INSTALL | 2 | `huggingface-tool-builder` | LP3, TT3 |
| 65 | HIGH | DO_NOT_INSTALL | 5 | `videodb` | LP1×2, PE3×2, RA2 |
| 64 | HIGH | DO_NOT_INSTALL | 20 | `scanning-tools` | PE2×15, RP1×2, YR4×2, TM1 |
| 64 | HIGH | DO_NOT_INSTALL | 9 | `train-sentence-transformers` | AE1×5, RA2×3, LP3 |
| 64 | HIGH | DO_NOT_INSTALL | 18 | `typescript-expert` | RP1×14, TM1×2, AST4, LP3 |
| 64 | HIGH | DO_NOT_INSTALL | 5 | `webapp-testing` | AST4×2, TM1×2, LP3 |
| 62 | HIGH | DO_NOT_INSTALL | 6 | `edr-bypass-re` | AE1×5, YR1 |
| 62 | HIGH | DO_NOT_INSTALL | 6 | `frontend-architecture` | AE1×2, RP1×2, EA2, P9 |
| 62 | HIGH | DO_NOT_INSTALL | 9 | `inventory-demand-planning` | AE4×4, AR2×2, EA2, EA3, P9 |
| 62 | HIGH | DO_NOT_INSTALL | 10 | `linux-shell-scripting` | PE2×4, RA2×4, PE3, TM1 |
| 62 | HIGH | DO_NOT_INSTALL | 4 | `skill-writer` | RA1×3, AE1 |
| 61 | HIGH | DO_NOT_INSTALL | 6 | `agents-sdk` | AE1×3, RP1×2, EA2 |
| 61 | HIGH | DO_NOT_INSTALL | 3 | `git-pr-review` | P1, P6, YR4 |
| 61 | HIGH | DO_NOT_INSTALL | 5 | `n8n-agents` | EA2×2, P6×2, AR1 |
| 60 | HIGH | DO_NOT_INSTALL | 5 | `api-security` | PE3×3, SSRF1×2 |
| 60 | HIGH | DO_NOT_INSTALL | 3 | `skill-security-audit` | AE1×2, RA1 |
| 60 | HIGH | DO_NOT_INSTALL | 5 | `wellally-tech` | PE3×3, E1, P3 |
| 59 | HIGH | DO_NOT_INSTALL | 18 | `cloudflare-email-service` | E1×9, RP1×7, AE1×2 |
| 58 | HIGH | DO_NOT_INSTALL | 7 | `agy-delegate` | EA2×4, AE1×3 |
| 58 | HIGH | DO_NOT_INSTALL | 6 | `client-secret-exposure-audit` | PE3×3, P2×2, E1 |
| 58 | HIGH | DO_NOT_INSTALL | 7 | `opencode-delegate` | EA2×4, AE1×3 |
| 58 | HIGH | DO_NOT_INSTALL | 6 | `xss-html-injection` | E1×2, P2×2, EA3, YR4 |
| 57 | HIGH | DO_NOT_INSTALL | 11 | `claimable-postgres` | RP1×4, EA2×3, PE3×3, E1 |
| 57 | HIGH | DO_NOT_INSTALL | 4 | `dotnet-reverse` | YR4×2, AS2, PE2 |
| 57 | HIGH | DO_NOT_INSTALL | 5 | `omp-delegate` | AE1×3, EA2, RA2 |
| 57 | HIGH | DO_NOT_INSTALL | 3 | `security-compliance-compliance-check` | AE1×2, YR4 |
| 56 | HIGH | DO_NOT_INSTALL | 5 | `cron-doctor` | AE1×3, RA2×2 |
| 56 | HIGH | DO_NOT_INSTALL | 4 | `frontend-seo` | OH1×2, AE1, RP1 |
| 56 | HIGH | DO_NOT_INSTALL | 9 | `weaviate-cookbooks` | PE3×3, RP1×3, P9×2, PE2 |
| 56 | HIGH | DO_NOT_INSTALL | 8 | `wp-site-health-auditor` | PE2×5, AE1×3 |
| 55 | HIGH | DO_NOT_INSTALL | 6 | `cursor-delegate` | AE1×4, EA2×2 |
| 55 | HIGH | DO_NOT_INSTALL | 5 | `frontend-optimistic-mutations` | AE1×2, P9×2, RP1 |
| 55 | HIGH | DO_NOT_INSTALL | 3 | `hig-inputs` | AE1, EA2, P1 |
| 55 | HIGH | DO_NOT_INSTALL | 3 | `n8n-error-handling` | AE1×2, PE3 |
| 55 | HIGH | DO_NOT_INSTALL | 4 | `ui-update` | AS3×2, AS1, RA1 |
| 54 | HIGH | DO_NOT_INSTALL | 5 | `codebase-cleanup-deps-audit` | AE1×2, E1×2, RP1 |
| 54 | HIGH | DO_NOT_INSTALL | 5 | `dependency-management-deps-audit` | AE1×2, E1×2, RP1 |
| 54 | HIGH | DO_NOT_INSTALL | 7 | `monorepo-management` | RP1×4, PE3, RA2, TM2 |
| 54 | HIGH | DO_NOT_INSTALL | 15 | `workers-best-practices` | E1×12, AE1×3 |
| 53 | HIGH | DO_NOT_INSTALL | 7 | `turborepo-caching` | RP1×4, PE3×2, TM2 |
| 52 | HIGH | DO_NOT_INSTALL | 25 | `cline-delegate` | EA2×23, AE1×2 |
| 51 | HIGH | DO_NOT_INSTALL | 4 | `commandcode-delegate` | AE1×3, EA2 |
| 50 | MEDIUM | CAUTION | 8 | `agentflow` | EA5×6, RA2×2 |
| 50 | MEDIUM | CAUTION | 3 | `claude-code-guide` | MP3×2, P1 |
| 50 | MEDIUM | CAUTION | 5 | `hugging-face-vision-trainer` | AE1×4, LP3 |
| 50 | MEDIUM | CAUTION | 25 | `junta-leiloeiros` | TM3×8, SC1×7, SC4×6, E1×2, AST4 |
| 50 | MEDIUM | CAUTION | 2 | `security-scanning-security-hardening` | EA2, YR1 |
| 49 | MEDIUM | CAUTION | 6 | `apify-actor-development` | E1×3, SC2×2, RP1 |
| 49 | MEDIUM | CAUTION | 5 | `frontend-lighthouse` | RP1×3, AE1×2 |
| 49 | MEDIUM | CAUTION | 3 | `logic-fix-all` | AE1, EA2, TM1 |
| 49 | MEDIUM | CAUTION | 6 | `react-modernization` | RP1×4, AE1×2 |
| 49 | MEDIUM | CAUTION | 6 | `react-native-architecture` | RP1×4, AE1×2 |
| 49 | MEDIUM | CAUTION | 3 | `ste-writing` | AE1, LP3, PE3 |
| 48 | MEDIUM | CAUTION | 4 | `agent-self-scheduling` | EA5×2, EA2, RA2 |
| 48 | MEDIUM | CAUTION | 4 | `ai-md` | EA2×2, AS1, PE3 |
| 48 | MEDIUM | CAUTION | 4 | `api-fuzzing-bug-bounty` | PE3×2, E1, TM1 |
| 48 | MEDIUM | CAUTION | 3 | `cc-skill-continuous-learning` | AS1, AS3, EA2 |
| 48 | MEDIUM | CAUTION | 21 | `fedora-hyprland-installer` | PE2×16, RA2×4, AE1 |
| 48 | MEDIUM | CAUTION | 4 | `hugging-face-cli` | PE3×3, TM1 |
| 47 | MEDIUM | CAUTION | 5 | `aws-sst-development` | RP1×3, P2, YR4 |
| 47 | MEDIUM | CAUTION | 7 | `javascript-testing-patterns` | E1×5, AE1×2 |
| 47 | MEDIUM | CAUTION | 7 | `neon-postgres` | RP1×5, PE3, TM1 |
| 47 | MEDIUM | CAUTION | 3 | `supabase` | AS2, EA2, PE3 |
| 47 | MEDIUM | CAUTION | 4 | `user-thoughts` | P2×2, PE3, RA2 |
| 47 | MEDIUM | CAUTION | 6 | `warp-delegate` | EA2×4, AE1, AS3 |
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
| 46 | MEDIUM | CAUTION | 3 | `hig-foundations` | AE1, OH3, P2 |
| 46 | MEDIUM | CAUTION | 5 | `os-scripting` | P1×3, PE2, RA2 |
| 45 | MEDIUM | CAUTION | 5 | `agent-orchestrator` | AE1, AST4, LP3, SC1, SC4 |
| 45 | MEDIUM | CAUTION | 7 | `agy-auto` | AS1×6, RA2 |
| 45 | MEDIUM | CAUTION | 3 | `aws-serverless` | E1, MP3, TM1 |
| 45 | MEDIUM | CAUTION | 4 | `codex-subagent` | EA5×3, RA2 |
| 45 | MEDIUM | CAUTION | 3 | `error-handling-patterns` | AE1×2, OH3 |
| 45 | MEDIUM | CAUTION | 12 | `git-hooks-automation` | RP1×9, TM1×3 |
| 45 | MEDIUM | CAUTION | 6 | `huggingface-lora-space-builder` | E5×2, PE3×2, EA2, EA3 |
| 45 | MEDIUM | CAUTION | 3 | `windows-ad` | YR4×2, YR1 |
| 44 | MEDIUM | CAUTION | 3 | `api-testing-observability-api-mock` | AE1×2, SSRF2 |
| 44 | MEDIUM | CAUTION | 3 | `frontend-data-contracts` | AE1×2, RP1 |
| 44 | MEDIUM | CAUTION | 14 | `instagram` | SC1×5, SC4×4, E1×3, LP3, TM1 |
| 44 | MEDIUM | CAUTION | 4 | `matematico-tao` | AE4×2, AE1, LP3 |
| 44 | MEDIUM | CAUTION | 4 | `prompt-engineering-patterns` | P6×3, LP3 |
| 44 | MEDIUM | CAUTION | 4 | `skill-creator-ms` | RA1×3, RP1 |
| 44 | MEDIUM | CAUTION | 4 | `weaviate` | AE1, AST7, LP3, PE2 |
| 43 | MEDIUM | CAUTION | 6 | `algorithmic-art` | AE1×6 |
| 43 | MEDIUM | CAUTION | 2 | `azure-servicebus-ts` | E4, P3 |
| 43 | MEDIUM | CAUTION | 2 | `claude-settings-audit` | AS1, AS2 |
| 43 | MEDIUM | CAUTION | 5 | `clean-code-guard` | AE1×5 |
| 43 | MEDIUM | CAUTION | 3 | `kimi-delegate` | AE1×3 |
| 43 | MEDIUM | CAUTION | 46 | `linear-claude-skill` | RP1×42, PE3×2, RA2×2 |
| 43 | MEDIUM | CAUTION | 7 | `mobile-reverse` | RA2×4, PE3×3 |
| 43 | MEDIUM | CAUTION | 3 | `pi-delegate` | AE1×3 |
| 43 | MEDIUM | CAUTION | 3 | `review-animations` | AE1×3 |
| 43 | MEDIUM | CAUTION | 9 | `transformers-js` | AE1×9 |
| 43 | MEDIUM | CAUTION | 4 | `uv-package-manager` | RA2, SC2, TM2, YR1 |
| 43 | MEDIUM | CAUTION | 4 | `zcode-delegate` | AE1, E1, RA2, RP1 |
| 42 | MEDIUM | CAUTION | 3 | `backend-dev-guidelines` | PE3×2, TM1 |
| 42 | MEDIUM | CAUTION | 2 | `beautiful-prose` | AR2, P6 |
| 42 | MEDIUM | CAUTION | 3 | `code-documentation-doc-generate` | AE1×2, E1 |
| 42 | MEDIUM | CAUTION | 2 | `delegate-setup` | AE1, PE3 |
| 42 | MEDIUM | CAUTION | 4 | `deploy-to-vercel` | PE3×2, LP3, RA2 |
| 42 | MEDIUM | CAUTION | 3 | `documentation-generation-doc-generate` | AE1×2, E1 |
| 42 | MEDIUM | CAUTION | 2 | `maintain-codex-wiki` | AR3, YR4 |
| 42 | MEDIUM | CAUTION | 3 | `nextjs-app-router-patterns` | AE1×2, E1 |
| 42 | MEDIUM | CAUTION | 4 | `pwn-chain` | PE2×2, YR4×2 |
| 42 | MEDIUM | CAUTION | 3 | `team-collaboration-issue` | AE1×2, E1 |
| 42 | MEDIUM | CAUTION | 3 | `temporal-python-testing` | AE1×2, E1 |
| 41 | MEDIUM | CAUTION | 2 | `api-analyzer` | P6, TM1 |
| 41 | MEDIUM | CAUTION | 5 | `break-ai-fix-loops` | AST4×3, LP3, YR1 |
| 41 | MEDIUM | CAUTION | 2 | `create-plugin` | MP3, RA1 |
| 41 | MEDIUM | CAUTION | 7 | `paypal-integration` | E1×4, EA2×2, PE3 |
| 40 | MEDIUM | CAUTION | 10 | `hubspot-integration` | PE3×6, E1×4 |
| 40 | MEDIUM | CAUTION | 2 | `linkerd-patterns` | SC2, TM2 |
| 40 | MEDIUM | CAUTION | 2 | `task-intelligence` | AE1, PE3 |
| 39 | MEDIUM | CAUTION | 3 | `distribute-skill-to-all-agents` | AE1, AS3, E3 |
| 39 | MEDIUM | CAUTION | 6 | `vibe-delegate` | EA2×5, AE1 |
| 38 | MEDIUM | CAUTION | 6 | `api-design-principles` | E1×4, TM1×2 |
| 38 | MEDIUM | CAUTION | 4 | `autonomous-agents` | EA2×2, AR3, OH3 |
| 38 | MEDIUM | CAUTION | 11 | `cred-omega` | PE3×9, PE2×2 |
| 38 | MEDIUM | CAUTION | 4 | `odoo-backup-strategy` | E5×2, RA2, TM1 |
| 37 | MEDIUM | CAUTION | 2 | `accessibility-compliance-accessibility-audit` | AE1×2 |
| 37 | MEDIUM | CAUTION | 2 | `antigravity-maintainer-batch-release` | AE1×2 |
| 37 | MEDIUM | CAUTION | 4 | `browser-harness` | RA2×2, YR1×2 |
| 37 | MEDIUM | CAUTION | 2 | `code-review-excellence` | AE1×2 |
| 37 | MEDIUM | CAUTION | 21 | `convex` | RP1×16, E1×4, PE3 |
| 37 | MEDIUM | CAUTION | 2 | `copilot-delegate` | AE1×2 |
| 37 | MEDIUM | CAUTION | 7 | `debugging-code` | E1×2, PE2×2, RA2×2, LP3 |
| 37 | MEDIUM | CAUTION | 2 | `debugging-strategies` | AE1×2 |
| 37 | MEDIUM | CAUTION | 5 | `e2e-testing-patterns` | RP1×4, AE1 |
| 37 | MEDIUM | CAUTION | 2 | `error-debugging-error-trace` | AE1×2 |
| 37 | MEDIUM | CAUTION | 2 | `error-diagnostics-error-trace` | AE1×2 |
| 37 | MEDIUM | CAUTION | 2 | `file-uploads` | AR3, PE3 |
| 37 | MEDIUM | CAUTION | 2 | `framework-migration-code-migrate` | AE1×2 |
| 37 | MEDIUM | CAUTION | 4 | `frontend-slides` | E1, EA2, LP3, P2 |
| 37 | MEDIUM | CAUTION | 2 | `git-pr-workflows-pr-enhance` | AE1×2 |
| 37 | MEDIUM | CAUTION | 3 | `grok-delegate` | EA2×2, AE1 |
| 37 | MEDIUM | CAUTION | 2 | `incident-response-smart-fix` | AE1×2 |
| 37 | MEDIUM | CAUTION | 2 | `modern-javascript-patterns` | AE1×2 |
| 37 | MEDIUM | CAUTION | 2 | `nodejs-backend-patterns` | AE1×2 |
| 37 | MEDIUM | CAUTION | 2 | `obsidian-bases` | AE1×2 |
| 37 | MEDIUM | CAUTION | 2 | `project-skill-audit` | AE1×2 |
| 37 | MEDIUM | CAUTION | 2 | `rust-async-patterns` | AE1×2 |
| 37 | MEDIUM | CAUTION | 2 | `tailwind-design-system` | AE1×2 |
| 37 | MEDIUM | CAUTION | 2 | `theme-factory` | AE1×2 |
| 37 | MEDIUM | CAUTION | 2 | `typescript-advanced-types` | AE1×2 |
| 37 | MEDIUM | CAUTION | 2 | `web-artifacts-builder` | AE1×2 |
| 37 | MEDIUM | CAUTION | 6 | `web-performance-optimization` | RP1×3, E1×2, P2 |
| 37 | MEDIUM | CAUTION | 2 | `wgm` | AE1×2 |
| 36 | MEDIUM | CAUTION | 4 | `codebase-audit-pre-push` | PE3×3, EA4 |
| 36 | MEDIUM | CAUTION | 7 | `html-injection-testing` | P2×6, E1 |
| 36 | MEDIUM | CAUTION | 10 | `native-data-fetching` | PE3×7, E1×3 |
| 36 | MEDIUM | CAUTION | 3 | `pipecat-friday-agent` | PE3×2, LP3 |
| 36 | MEDIUM | CAUTION | 5 | `skill-sentinel` | E1, LP3, PE3, SC1, SC4 |
| 36 | MEDIUM | CAUTION | 4 | `wcag-audit-patterns` | P2×2, RP1×2 |
| 35 | MEDIUM | CAUTION | 5 | `atlas-contract` | EA2×4, P1 |
| 35 | MEDIUM | CAUTION | 16 | `expo-module` | RP1×8, P9×6, RA2×2 |
| 35 | MEDIUM | CAUTION | 4 | `papers-skill` | E1×2, AR2, LP3 |
| 35 | MEDIUM | CAUTION | 3 | `sdk-dx` | RP1×2, AE1 |
| 34 | MEDIUM | CAUTION | 3 | `hf-cloud-aws-context-discovery` | EA2×2, PE3 |
| 34 | MEDIUM | CAUTION | 4 | `react-best-practices` | OH1×2, RP1×2 |
| 34 | MEDIUM | CAUTION | 7 | `vibe-code-cleanup` | RP1×5, PE3×2 |
| 33 | MEDIUM | CAUTION | 6 | `aws-mcp-setup` | RP1×5, AS2 |
| 33 | MEDIUM | CAUTION | 3 | `bats-testing-patterns` | PE2×2, TM1 |
| 33 | MEDIUM | CAUTION | 2 | `cloud-k8s` | SSRF1×2 |
| 33 | MEDIUM | CAUTION | 4 | `context-engineering` | EA2×2, PE3, RP1 |
| 33 | MEDIUM | CAUTION | 2 | `discord-automation` | P3×2 |
| 33 | MEDIUM | CAUTION | 6 | `huggingface-spaces` | SC1×2, AR2, E1, SC2, SC4 |
| 33 | MEDIUM | CAUTION | 5 | `youtube-notetaker` | AST4×2, TT2×2, LP3 |
| 32 | MEDIUM | CAUTION | 3 | `autonomous-agent-patterns` | EA2×2, TM1 |
| 32 | MEDIUM | CAUTION | 3 | `developer-onboarding` | AR2, E1, RP1 |
| 32 | MEDIUM | CAUTION | 2 | `i18n-localization` | AE1, LP3 |
| 32 | MEDIUM | CAUTION | 3 | `mmx-cli` | EA2, PE3, RA2 |
| 32 | MEDIUM | CAUTION | 2 | `open-dynamic-workflows` | AE1, RP1 |
| 32 | MEDIUM | CAUTION | 2 | `skill-porter` | AE1, LP3 |
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
| 30 | MEDIUM | CAUTION | 2 | `apify-actorization` | AE1, E1 |
| 30 | MEDIUM | CAUTION | 13 | `atlas-cloud-media` | E1×9, PE2×3, EA2 |
| 30 | MEDIUM | CAUTION | 2 | `atlas-ledger` | EA2, P1 |
| 30 | MEDIUM | CAUTION | 2 | `auri-core` | AE3, AS3 |
| 30 | MEDIUM | CAUTION | 7 | `azd-deployment` | PE3×7 |
| 30 | MEDIUM | CAUTION | 4 | `copilot-sdk` | E1, EA1, EA2, MP2 |
| 30 | MEDIUM | CAUTION | 3 | `dbos-python` | E1×2, P3 |
| 30 | MEDIUM | CAUTION | 9 | `gemini-omni-flash-api` | AST4×7, AS3, LP3 |
| 30 | MEDIUM | CAUTION | 3 | `github-presence` | P2×3 |
| 30 | MEDIUM | CAUTION | 3 | `helm-chart-scaffolding` | E5, LP3, PE3 |
| 30 | MEDIUM | CAUTION | 8 | `plaid-fintech` | PE3×8 |
| 30 | MEDIUM | CAUTION | 4 | `planning-with-files` | P2×4 |
| 30 | MEDIUM | CAUTION | 3 | `playwright-java` | P2, P4, RA2 |
| 30 | MEDIUM | CAUTION | 2 | `project-state-governor` | MP3×2 |
| 30 | MEDIUM | CAUTION | 2 | `re-create` | AR1×2 |
| 30 | MEDIUM | CAUTION | 3 | `remotion` | RP1×2, AS2 |
| 29 | MEDIUM | CAUTION | 6 | `astro` | RP1×5, P2 |
| 29 | MEDIUM | CAUTION | 4 | `azure-microsoft-playwright-testing-ts` | RP1×3, PE3 |
| 29 | MEDIUM | CAUTION | 1 | `cc-skill-strategic-compact` | AS1 |
| 29 | MEDIUM | CAUTION | 5 | `git-advanced-workflows` | TM1×5 |
| 29 | MEDIUM | CAUTION | 2 | `n8n-validation-expert` | EA4, MP3 |
| 29 | MEDIUM | CAUTION | 5 | `smtp-penetration-testing` | PE2×4, YR4 |
| 28 | MEDIUM | CAUTION | 8 | `api-documentation-generator` | E1×7, PE3 |
| 28 | MEDIUM | CAUTION | 2 | `architecture-decision-records` | E4×2 |
| 28 | MEDIUM | CAUTION | 2 | `bulletmind` | P6, P9 |
| 28 | MEDIUM | CAUTION | 2 | `deployment-procedures` | AR2, EA2 |
| 28 | MEDIUM | CAUTION | 44 | `hasdata` | E1×43, TM1 |
| 28 | MEDIUM | CAUTION | 2 | `huggingface-local-models` | E1, EA5 |
| 28 | MEDIUM | CAUTION | 6 | `lint-and-validate` | RP1×4, AST4, LP3 |
| 28 | MEDIUM | CAUTION | 3 | `pentest-checklist` | PE2×2, YR4 |
| 28 | MEDIUM | CAUTION | 2 | `spec-driven-loop` | AE1, EA3 |
| 28 | MEDIUM | CAUTION | 4 | `unified-ai-gateway` | RP1×3, PE3 |
| 27 | MEDIUM | CAUTION | 12 | `app-builder` | RP1×11, PE3 |
| 27 | MEDIUM | CAUTION | 2 | `bash-linux` | E1, TM1 |
| 27 | MEDIUM | CAUTION | 8 | `ci-cd-and-automation` | RP1×7, PE3 |
| 27 | MEDIUM | CAUTION | 1 | `diagnosing-bugs` | P6 |
| 27 | MEDIUM | CAUTION | 2 | `gdpr-data-handling` | AR3, EA2 |
| 27 | MEDIUM | CAUTION | 2 | `manifest` | AS1, RA2 |
| 27 | MEDIUM | CAUTION | 6 | `postgres-readonly-queries` | PE2×4, LP3, RA2 |
| 27 | MEDIUM | CAUTION | 2 | `security-scanning-security-sast` | EA2, TM1 |
| 27 | MEDIUM | CAUTION | 2 | `shipping-and-launch` | AR2, RP1 |
| 26 | MEDIUM | CAUTION | 2 | `ai-wrapper-product` | AR1×2 |
| 26 | MEDIUM | CAUTION | 2 | `angular-best-practices` | P2×2 |
| 26 | MEDIUM | CAUTION | 2 | `azure-communication-common-java` | PE3×2 |
| 26 | MEDIUM | CAUTION | 2 | `azure-monitor-opentelemetry-exporter-java` | PE3×2 |
| 26 | MEDIUM | CAUTION | 2 | `azure-speech-to-text-rest-py` | PE3×2 |
| 26 | MEDIUM | CAUTION | 4 | `conductor-setup` | PE3×4 |
| 26 | MEDIUM | CAUTION | 2 | `developer-sandbox` | P2×2 |
| 26 | MEDIUM | CAUTION | 5 | `discord-bot-architect` | PE3×5 |
| 26 | MEDIUM | CAUTION | 2 | `docs-generator` | P2×2 |
| 26 | MEDIUM | CAUTION | 2 | `famulor-skill` | PE3×2 |
| 26 | MEDIUM | CAUTION | 5 | `hugging-face-evaluation` | PE3×5 |
| 26 | MEDIUM | CAUTION | 5 | `kubestellar-console` | PE3×5 |
| 26 | MEDIUM | CAUTION | 9 | `mailtrap-sending-emails` | P9×7, E1, MP2 |
| 26 | MEDIUM | CAUTION | 4 | `quality-nonconformance` | AE4×2, EA2, P9 |
| 26 | MEDIUM | CAUTION | 11 | `vercel-cli-with-tokens` | PE3×11 |
| 26 | MEDIUM | CAUTION | 2 | `voice-ai-engine-development` | PE3×2 |
| 25 | MEDIUM | CAUTION | 1 | `agent-creator` | AE1 |
| 25 | MEDIUM | CAUTION | 1 | `agent-qa-result-triage` | AE1 |
| 25 | MEDIUM | CAUTION | 4 | `app-store-optimization` | AS3×2, LP3, RA2 |
| 25 | MEDIUM | CAUTION | 1 | `boost-asio-pro` | AE1 |
| 25 | MEDIUM | CAUTION | 2 | `broken-authentication` | EA2, YR4 |
| 25 | MEDIUM | CAUTION | 2 | `burpsuite-project-parser` | MP2, YR4 |
| 25 | MEDIUM | CAUTION | 2 | `clarity-gate` | EA2, P2 |
| 25 | MEDIUM | CAUTION | 1 | `comprehensive-review-pr-enhance` | AE1 |
| 25 | MEDIUM | CAUTION | 2 | `conductor-revert` | TM1×2 |
| 25 | MEDIUM | CAUTION | 1 | `durable-objects` | AE1 |
| 25 | MEDIUM | CAUTION | 3 | `firmware-analyst` | PE2×2, PE3 |
| 25 | MEDIUM | CAUTION | 1 | `fsi-compliance-checker` | AE1 |
| 25 | MEDIUM | CAUTION | 1 | `logic-review` | AE1 |
| 25 | MEDIUM | CAUTION | 3 | `model-authoring` | EA3×2, MP3 |
| 25 | MEDIUM | CAUTION | 1 | `offers` | AE1 |
| 25 | MEDIUM | CAUTION | 1 | `plugin-validator` | AE1 |
| 25 | MEDIUM | CAUTION | 1 | `power-user-cultivation` | AE1 |
| 25 | MEDIUM | CAUTION | 1 | `qoder-delegate` | AE1 |
| 25 | MEDIUM | CAUTION | 2 | `red-team-tactics` | PE2, TM2 |
| 25 | MEDIUM | CAUTION | 1 | `tdd-workflows-tdd-green` | AE1 |
| 25 | MEDIUM | CAUTION | 2 | `usage-based-pricing` | AR2, E1 |
| 24 | MEDIUM | CAUTION | 2 | `humanize-chinese` | P6, TR1 |
| 23 | MEDIUM | CAUTION | 4 | `cmux` | RA2×2, PE2, RP1 |
| 23 | MEDIUM | CAUTION | 3 | `docs-as-marketing` | E1×2, PE3 |
| 23 | MEDIUM | CAUTION | 5 | `electron-development` | RA2×3, RP1×2 |
| 23 | MEDIUM | CAUTION | 2 | `fastapi-templates` | PE3×2 |
| 23 | MEDIUM | CAUTION | 5 | `frontend-slides-frontend-slides` | RP1×3, EA2×2 |
| 23 | MEDIUM | CAUTION | 2 | `git-workflow-and-versioning` | RP1, TM1 |
| 23 | MEDIUM | CAUTION | 2 | `landing-page-generator` | LP3, OH1 |
| 23 | MEDIUM | CAUTION | 2 | `llm-application-dev-prompt-optimize` | AR2, EA3 |
| 23 | MEDIUM | CAUTION | 5 | `makepad-deployment` | RA2×3, PE2×2 |
| 22 | MEDIUM | CAUTION | 56 | `agentphone` | E1×51, P9×5 |
| 22 | MEDIUM | CAUTION | 2 | `azure-monitor-query-java` | E1, PE3 |
| 22 | MEDIUM | CAUTION | 1 | `basecamp-automation` | P3 |
| 22 | MEDIUM | CAUTION | 2 | `burp-suite-testing` | PE3×2 |
| 22 | MEDIUM | CAUTION | 4 | `claude-monitor` | AST4×3, LP3 |
| 22 | MEDIUM | CAUTION | 1 | `deepapi` | RA1 |
| 22 | MEDIUM | CAUTION | 1 | `doubt-driven-development` | EA5 |
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
| 22 | MEDIUM | CAUTION | 3 | `polis-protocol-a-self-optimizing-city-of-agents` | AS3, EA2, RP1 |
| 22 | MEDIUM | CAUTION | 2 | `senior-architect` | LP3, PE3 |
| 22 | MEDIUM | CAUTION | 2 | `senior-fullstack` | LP3, PE3 |
| 22 | MEDIUM | CAUTION | 1 | `slack-automation` | P3 |
| 21 | MEDIUM | CAUTION | 1 | `analyze-project` | AR2 |
| 21 | MEDIUM | CAUTION | 1 | `azure-servicebus-dotnet` | E4 |
| 21 | MEDIUM | CAUTION | 1 | `brooks-harness` | RA1 |
| 21 | MEDIUM | CAUTION | 1 | `brooks-review` | P6 |
| 21 | MEDIUM | CAUTION | 1 | `browser-act` | RA1 |
| 21 | MEDIUM | CAUTION | 1 | `claude-win11-speckit-update-skill` | RA1 |
| 21 | MEDIUM | CAUTION | 2 | `code-simplification` | EA3, RA1 |
| 21 | MEDIUM | CAUTION | 1 | `database-cloud-optimization-cost-optimize` | P6 |
| 21 | MEDIUM | CAUTION | 1 | `design-md` | P6 |
| 21 | MEDIUM | CAUTION | 1 | `ditto` | E4 |
| 21 | MEDIUM | CAUTION | 1 | `gdb-cli` | YR1 |
| 21 | MEDIUM | CAUTION | 1 | `hig-components-menus` | P6 |
| 21 | MEDIUM | CAUTION | 1 | `ida-reverse` | YR1 |
| 21 | MEDIUM | CAUTION | 2 | `javascript-typescript-typescript-scaffold` | PE3, TM3 |
| 21 | MEDIUM | CAUTION | 1 | `keyword-extractor` | P6 |
| 21 | MEDIUM | CAUTION | 1 | `lemmaly` | RA1 |
| 21 | MEDIUM | CAUTION | 8 | `llm-council` | E1×6, RA2×2 |
| 21 | MEDIUM | CAUTION | 1 | `microsoft-teams-automation` | E4 |
| 21 | MEDIUM | CAUTION | 1 | `n8n-binary-and-data` | E4 |
| 21 | MEDIUM | CAUTION | 1 | `paywall-upgrade-cro` | P6 |
| 21 | MEDIUM | CAUTION | 1 | `pre-release-review` | P6 |
| 21 | MEDIUM | CAUTION | 1 | `professional-proofreader` | P6 |
| 21 | MEDIUM | CAUTION | 1 | `quit-sponsor` | AR2 |
| 21 | MEDIUM | CAUTION | 4 | `spec-driven-development` | AS3×3, EA2 |
| 21 | MEDIUM | CAUTION | 1 | `time-ledger` | AR2 |
| 21 | MEDIUM | CAUTION | 4 | `upstash-qstash` | E1×2, RA2, SSRF2 |
| 20 | LOW | CAUTION | 5 | `add-app-clip` | RA2×4, RP1 |
| 20 | LOW | CAUTION | 1 | `agenttrace-session-audit` | MP3 |
| 20 | LOW | CAUTION | 1 | `api-and-interface-design` | TM1 |
| 20 | LOW | SAFE | 1 | `api-endpoint-builder` | TM1 |
| 20 | LOW | CAUTION | 1 | `api-integration` | TM1 |
| 20 | LOW | SAFE | 1 | `architecture` | MP3 |
| 20 | LOW | CAUTION | 1 | `ask-matt` | MP3 |
| 20 | LOW | SAFE | 1 | `audit-context-building` | MP3 |
| 20 | LOW | CAUTION | 1 | `c-pro` | MP3 |
| 20 | LOW | SAFE | 1 | `carrier-relationship-management` | AR2 |
| 20 | LOW | CAUTION | 1 | `cc-skill-backend-patterns` | TM1 |
| 20 | LOW | CAUTION | 1 | `cc-skill-coding-standards` | TM1 |
| 20 | LOW | SAFE | 1 | `free-tier-strategy` | AR2 |
| 20 | LOW | CAUTION | 2 | `huggingface-zerogpu` | AR2, SC2 |
| 20 | LOW | CAUTION | 1 | `incident-response-incident-response` | MP3 |
| 20 | LOW | SAFE | 1 | `linkedin-profile-optimizer` | MP3 |
| 20 | LOW | CAUTION | 1 | `neon-postgres-branches` | MP3 |
| 20 | LOW | SAFE | 4 | `nextjs-on-cloudflare` | RP1×3, AS3 |
| 20 | LOW | CAUTION | 1 | `personal-tool-builder` | MP3 |
| 20 | LOW | CAUTION | 1 | `privacy-mask` | AR2 |
| 20 | LOW | CAUTION | 1 | `public-relations` | AR2 |
| 20 | LOW | CAUTION | 3 | `revops` | RA2×2, EA2 |
| 20 | LOW | SAFE | 1 | `sql-pro` | AR3 |
| 20 | LOW | CAUTION | 1 | `voice-agents` | MP3 |
| 20 | LOW | CAUTION | 1 | `wp-guard` | AR2 |
| 19 | LOW | CAUTION | 10 | `smartui-skill` | RP1×9, EA2 |
| 19 | LOW | SAFE | 3 | `youtube-summarizer` | PE2×2, RA2 |
| 18 | LOW | SAFE | 1 | `anti-reversing-techniques` | YR1 |
| 18 | LOW | CAUTION | 1 | `context-management-context-save` | E4 |
| 18 | LOW | SAFE | 1 | `ddd-strategic-design` | E4 |
| 18 | LOW | CAUTION | 7 | `dependency-upgrade` | RP1×6, E1 |
| 18 | LOW | CAUTION | 5 | `entropy-box` | E1×4, EA2 |
| 18 | LOW | CAUTION | 2 | `evolution` | P2, SC2 |
| 18 | LOW | CAUTION | 1 | `go-playwright` | AR3 |
| 18 | LOW | CAUTION | 8 | `incident-runbook-templates` | E1×7, EA2 |
| 18 | LOW | CAUTION | 4 | `patch-diff-exploit` | E1×2, PE2×2 |
| 18 | LOW | SAFE | 3 | `security-scanning-security-dependencies` | EA2×2, RP1 |
| 18 | LOW | CAUTION | 1 | `semgrep-rule-creator` | YR2 |
| 18 | LOW | SAFE | 1 | `team-collaboration-standup-notes` | E4 |
| 17 | LOW | CAUTION | 1 | `ai-native-cli` | PE3 |
| 17 | LOW | CAUTION | 1 | `angular` | P2 |
| 17 | LOW | SAFE | 1 | `angular-ui-patterns` | P2 |
| 17 | LOW | CAUTION | 4 | `apk-reverse` | E1×3, PE2 |
| 17 | LOW | SAFE | 1 | `azure-ai-agents-persistent-java` | PE3 |
| 17 | LOW | CAUTION | 1 | `azure-appconfiguration-java` | PE3 |
| 17 | LOW | SAFE | 1 | `azure-communication-chat-java` | PE3 |
| 17 | LOW | CAUTION | 1 | `azure-compute-batch-java` | PE3 |
| 17 | LOW | SAFE | 1 | `azure-cosmos-java` | PE3 |
| 17 | LOW | CAUTION | 1 | `azure-messaging-webpubsub-java` | PE3 |
| 17 | LOW | CAUTION | 1 | `azure-messaging-webpubsubservice-py` | PE3 |
| 17 | LOW | SAFE | 1 | `azure-monitor-ingestion-java` | PE3 |
| 17 | LOW | CAUTION | 1 | `azure-postgres-ts` | PE3 |
| 17 | LOW | CAUTION | 1 | `azure-resource-manager-playwright-dotnet` | PE3 |
| 17 | LOW | CAUTION | 1 | `azure-web-pubsub-ts` | PE3 |
| 17 | LOW | CAUTION | 3 | `bumblebee` | PE2×2, LP3 |
| 17 | LOW | CAUTION | 1 | `cold-email` | AR1 |
| 17 | LOW | SAFE | 1 | `competitor-tracking` | AR1 |
| 17 | LOW | CAUTION | 1 | `content-strategy` | PE3 |
| 17 | LOW | CAUTION | 5 | `expo-api-routes` | E1×4, RP1 |
| 17 | LOW | CAUTION | 1 | `git-pr-workflows-git-workflow` | TM1 |
| 17 | LOW | CAUTION | 1 | `github-workflow-automation` | TM1 |
| 17 | LOW | CAUTION | 1 | `google-docs-automation` | PE3 |
| 17 | LOW | CAUTION | 1 | `hugging-face-datasets` | PE3 |
| 17 | LOW | CAUTION | 1 | `monte-carlo-storage-cost-analysis` | P2 |
| 17 | LOW | CAUTION | 10 | `muapi-media` | E1×9, EA2 |
| 17 | LOW | CAUTION | 1 | `odoo-performance-tuner` | P1 |
| 17 | LOW | CAUTION | 5 | `outreachagent` | E1×4, EA2 |
| 17 | LOW | SAFE | 1 | `production-scheduling` | AR1 |
| 17 | LOW | CAUTION | 1 | `salesforce-development` | PE3 |
| 17 | LOW | CAUTION | 1 | `sveltekit` | P2 |
| 17 | LOW | SAFE | 1 | `thick-client` | PE3 |
| 17 | LOW | CAUTION | 3 | `using-git-worktrees` | EA2×2, RA2 |
| 16 | LOW | SAFE | 3 | `api-onboarding` | E1×2, EA2 |
| 16 | LOW | CAUTION | 1 | `cc-skill-security-review` | OH1 |
| 16 | LOW | CAUTION | 1 | `frontend-mobile-security-xss-scan` | OH1 |
| 16 | LOW | CAUTION | 4 | `image-generator` | E1×3, RA2 |
| 16 | LOW | CAUTION | 2 | `ingest-youtube` | AST4, LP3 |
| 16 | LOW | SAFE | 3 | `mailtrap-managing-contacts` | P9×2, E1 |
| 16 | LOW | CAUTION | 3 | `malware-analysis` | PE2×2, E1 |
| 16 | LOW | CAUTION | 2 | `monte-carlo-validation-notebook` | AST4, LP3 |
| 16 | LOW | SAFE | 2 | `oss-hunter` | AST4, LP3 |
| 16 | LOW | SAFE | 2 | `performance-profiling` | AST4, LP3 |
| 16 | LOW | CAUTION | 5 | `pptx-deck-creation` | E1×4, EA2 |
| 16 | LOW | CAUTION | 1 | `schema-markup-generator` | OH1 |
| 16 | LOW | SAFE | 5 | `xvary-stock-research` | E1×4, LP3 |
| 15 | LOW | CAUTION | 1 | `aegisops-ai` | PE3 |
| 15 | LOW | CAUTION | 2 | `design-spatial` | AE4, RP1 |
| 15 | LOW | CAUTION | 1 | `geminiignore-finops` | PE3 |
| 15 | LOW | CAUTION | 1 | `neon-object-storage` | PE3 |
| 15 | LOW | SAFE | 1 | `nestjs-expert` | PE3 |
| 15 | LOW | SAFE | 1 | `news-sentiment-engine` | PE3 |
| 15 | LOW | CAUTION | 1 | `posix-shell-pro` | PE3 |
| 15 | LOW | SAFE | 3 | `python-testing-patterns` | E1×2, RA2 |
| 15 | LOW | CAUTION | 1 | `saas-mvp-launcher` | PE3 |
| 15 | LOW | CAUTION | 2 | `sast-configuration` | EA2, RP1 |
| 15 | LOW | CAUTION | 4 | `shodan-reconnaissance` | E1×3, PE2 |
| 15 | LOW | CAUTION | 1 | `technical-tutorials` | PE3 |
| 15 | LOW | CAUTION | 1 | `telegram-bot-builder` | PE3 |
| 15 | LOW | SAFE | 1 | `x402-express-wrapper` | PE3 |
| 15 | LOW | SAFE | 3 | `yield-intelligence` | E1×2, EA2 |
| 14 | LOW | SAFE | 2 | `blueprint` | AS3, RA2 |
| 14 | LOW | CAUTION | 4 | `context-compression` | MP2×4 |
| 14 | LOW | CAUTION | 2 | `pilot-protocol` | E1, EA2 |
| 14 | LOW | CAUTION | 2 | `react-native-skills` | P4, RP1 |
| 14 | LOW | CAUTION | 5 | `returns-reverse-logistics` | EA2×5 |
| 14 | LOW | CAUTION | 2 | `sankhya-dashboard-html-jsp-custom-best-pratices` | AS3, RA2 |
| 14 | LOW | SAFE | 3 | `skill-suggester` | P7×3 |
| 13 | LOW | SAFE | 2 | `anti-sycophancy` | RA2, TR2 |
| 13 | LOW | CAUTION | 2 | `constant-time-analysis` | RA2×2 |
| 13 | LOW | CAUTION | 2 | `docker-expert` | RP1, TM3 |
| 13 | LOW | CAUTION | 3 | `ffuf-web-fuzzing` | E1×2, RA2 |
| 13 | LOW | CAUTION | 2 | `seo-image-gen` | P7, RA2 |
| 13 | LOW | SAFE | 5 | `supply-chain-security` | RP1×4, TM1 |
| 13 | LOW | CAUTION | 2 | `tmux` | EA2, RA2 |
| 13 | LOW | SAFE | 3 | `verification-before-completion` | EA2×3 |
| 12 | LOW | CAUTION | 6 | `accesslint-diff` | RP1×6 |
| 12 | LOW | SAFE | 3 | `accesslint-scan` | RP1×3 |
| 12 | LOW | SAFE | 2 | `airflow-dag-patterns` | E1, EA2 |
| 12 | LOW | SAFE | 3 | `awt-e2e-testing` | RP1×3 |
| 12 | LOW | CAUTION | 4 | `browser-automation` | RP1×4 |
| 12 | LOW | CAUTION | 3 | `building-native-ui` | RP1×3 |
| 12 | LOW | SAFE | 3 | `changelog-automation` | RP1×3 |
| 12 | LOW | CAUTION | 8 | `cypress-skill` | RP1×8 |
| 12 | LOW | CAUTION | 4 | `database-migration` | RP1×4 |
| 12 | LOW | CAUTION | 3 | `database-migrations-migration-observability` | E1×3 |
| 12 | LOW | CAUTION | 5 | `drizzle-orm-expert` | RP1×5 |
| 12 | LOW | SAFE | 2 | `error-debugging-error-analysis` | E1, EA2 |
| 12 | LOW | SAFE | 2 | `error-diagnostics-error-analysis` | E1, EA2 |
| 12 | LOW | CAUTION | 4 | `expo-examples` | RP1×4 |
| 12 | LOW | SAFE | 5 | `expo-observe` | RP1×5 |
| 12 | LOW | CAUTION | 2 | `expo-ui` | RP1×2 |
| 12 | LOW | CAUTION | 2 | `filesystem-context` | AS3×2 |
| 12 | LOW | SAFE | 3 | `framework-migration-deps-upgrade` | RP1×3 |
| 12 | LOW | CAUTION | 2 | `grok-build` | EA2×2 |
| 12 | LOW | CAUTION | 5 | `hugging-face-dataset-viewer` | RP1×5 |
| 12 | LOW | CAUTION | 6 | `ii-commons` | RP1×6 |
| 12 | LOW | CAUTION | 5 | `jest-skill` | RP1×5 |
| 12 | LOW | SAFE | 3 | `jobgpt` | RP1×3 |
| 12 | LOW | CAUTION | 15 | `linkedin-cli` | P9×15 |
| 12 | LOW | CAUTION | 3 | `mailtrap-testing-with-sandbox` | P9×3 |
| 12 | LOW | CAUTION | 2 | `mcp-builder-ms` | E1, RP1 |
| 12 | LOW | CAUTION | 2 | `monte-carlo-monitoring-advisor` | EA2×2 |
| 12 | LOW | CAUTION | 4 | `nx-workspace-patterns` | RP1×4 |
| 12 | LOW | CAUTION | 9 | `prisma-expert` | RP1×9 |
| 12 | LOW | CAUTION | 2 | `production-audit` | E1, EA2 |
| 12 | LOW | CAUTION | 11 | `protect-mcp-governance` | RP1×11 |
| 12 | LOW | CAUTION | 2 | `segment-cdp` | E1, EA2 |
| 12 | LOW | SAFE | 2 | `skill-check` | AS3×2 |
| 12 | LOW | CAUTION | 2 | `smart-git-automation` | EA2×2 |
| 12 | LOW | CAUTION | 9 | `trigger-dev` | RP1×9 |
| 12 | LOW | SAFE | 5 | `ui-skills-root` | RP1×5 |
| 12 | LOW | CAUTION | 7 | `unslop-file` | P9×7 |
| 12 | LOW | CAUTION | 5 | `upgrading-expo` | RP1×5 |
| 12 | LOW | CAUTION | 6 | `vitest-skill` | RP1×6 |
| 12 | LOW | CAUTION | 5 | `web3-testing` | RP1×5 |
| 12 | LOW | CAUTION | 3 | `webdriverio-skill` | RP1×3 |
| 11 | LOW | CAUTION | 2 | `azure-cosmos-db-py` | TM3×2 |
| 11 | LOW | CAUTION | 2 | `email-systems` | EA2×2 |
| 11 | LOW | CAUTION | 2 | `finishing-a-development-branch` | EA2×2 |
| 11 | LOW | CAUTION | 9 | `hf-mem` | RP1×9 |
| 11 | LOW | SAFE | 2 | `privacy-by-design` | EA2×2 |
| 11 | LOW | CAUTION | 2 | `production-code-audit` | EA2×2 |
| 11 | LOW | CAUTION | 2 | `python-pptx-generator` | EA2×2 |
| 10 | LOW | CAUTION | 2 | `ejentum-reasoning-harness` | RP1×2 |
| 10 | LOW | CAUTION | 2 | `expo-dev-client` | RP1×2 |
| 10 | LOW | CAUTION | 2 | `expo-ui-jetpack-compose` | RP1×2 |
| 10 | LOW | SAFE | 2 | `expo-ui-swift-ui` | RP1×2 |
| 10 | LOW | CAUTION | 4 | `generate-nanobanana` | E1×4 |
| 10 | LOW | CAUTION | 2 | `github-actions-advanced` | RP1×2 |
| 10 | LOW | CAUTION | 3 | `liuguang-banlan-ui` | SC4×2, LP3 |
| 10 | LOW | CAUTION | 2 | `neon-ai-gateway` | P9×2 |
| 10 | LOW | CAUTION | 2 | `orca-replay` | RP1×2 |
| 10 | LOW | CAUTION | 2 | `performance-optimization` | RP1×2 |
| 10 | LOW | CAUTION | 2 | `radix-ui-design-system` | RP1×2 |
| 10 | LOW | CAUTION | 2 | `reverse-browser-automation` | RP1×2 |
| 10 | LOW | CAUTION | 2 | `vercel-deployment` | RP1×2 |
| 10 | LOW | CAUTION | 2 | `vscode-extension-guide-en` | RP1×2 |
| 9 | LOW | SAFE | 8 | `agentmail` | E1×8 |
| 9 | LOW | CAUTION | 5 | `azure-storage-blob-py` | E5×5 |
| 9 | LOW | CAUTION | 4 | `azure-storage-file-share-py` | E5×4 |
| 9 | LOW | SAFE | 2 | `prompt-engineer` | EA3, RA2 |
| 9 | LOW | CAUTION | 2 | `red-team-tools` | E1×2 |
| 9 | LOW | CAUTION | 1 | `subagent-orchestrator` | RP1 |
| 8 | LOW | CAUTION | 1 | `agent-memory-systems` | MP2 |
| 8 | LOW | SAFE | 1 | `agent-squad` | EA4 |
| 8 | LOW | CAUTION | 1 | `asana-automation` | RA2 |
| 8 | LOW | SAFE | 3 | `async-python-patterns` | E1×3 |
| 8 | LOW | CAUTION | 1 | `aws-agentic-ai` | EA2 |
| 8 | LOW | SAFE | 1 | `bamboohr-automation` | EA2 |
| 8 | LOW | CAUTION | 3 | `binary-diff` | E1×3 |
| 8 | LOW | CAUTION | 5 | `calendly-automation` | E1×5 |
| 8 | LOW | CAUTION | 1 | `ckw-design` | AE4 |
| 8 | LOW | SAFE | 1 | `commit` | EA2 |
| 8 | LOW | CAUTION | 1 | `conductor-implement` | EA2 |
| 8 | LOW | CAUTION | 1 | `context-fundamentals` | MP2 |
| 8 | LOW | CAUTION | 1 | `design-taste-frontend` | EA2 |
| 8 | LOW | CAUTION | 4 | `efficient-web-research` | E1×4 |
| 8 | LOW | CAUTION | 1 | `elon-musk` | AE4 |
| 8 | LOW | SAFE | 1 | `executing-plans` | EA2 |
| 8 | LOW | SAFE | 2 | `expo-cicd-workflows` | E1, TR1 |
| 8 | LOW | CAUTION | 1 | `food-database-query` | AE4 |
| 8 | LOW | CAUTION | 1 | `gitlab-ci-patterns` | EA2 |
| 8 | LOW | SAFE | 1 | `glasser` | EA2 |
| 8 | LOW | CAUTION | 1 | `hf-mcp` | RA2 |
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
| 8 | LOW | CAUTION | 1 | `radare2` | TM3 |
| 8 | LOW | SAFE | 1 | `rag-engineer` | MP2 |
| 8 | LOW | CAUTION | 1 | `scientific-writing` | AE4 |
| 8 | LOW | CAUTION | 1 | `seaborn` | AE4 |
| 8 | LOW | CAUTION | 2 | `secrets-management` | RP1, TM1 |
| 8 | LOW | SAFE | 1 | `seo-aeo-blog-writer` | AS3 |
| 8 | LOW | SAFE | 1 | `seo-aeo-content-cluster` | AS3 |
| 8 | LOW | SAFE | 1 | `seo-aeo-content-quality-auditor` | AS3 |
| 8 | LOW | SAFE | 1 | `seo-aeo-internal-linking` | AS3 |
| 8 | LOW | SAFE | 1 | `seo-aeo-keyword-research` | AS3 |
| 8 | LOW | SAFE | 1 | `seo-aeo-landing-page-writer` | AS3 |
| 8 | LOW | SAFE | 1 | `seo-aeo-meta-description-generator` | AS3 |
| 8 | LOW | SAFE | 1 | `seo-aeo-schema-generator` | AS3 |
| 8 | LOW | SAFE | 1 | `server-management` | PE2 |
| 8 | LOW | SAFE | 1 | `skill-optimizer` | AS3 |
| 8 | LOW | CAUTION | 1 | `skill-recommender` | AS3 |
| 8 | LOW | CAUTION | 1 | `slideops` | AS3 |
| 8 | LOW | SAFE | 1 | `talivia-agent-kit` | EA2 |
| 8 | LOW | SAFE | 1 | `track-management` | RA2 |
| 8 | LOW | CAUTION | 1 | `unslop-review` | EA2 |
| 7 | LOW | SAFE | 1 | `ad-campaign-analyzer` | EA2 |
| 7 | LOW | CAUTION | 1 | `adhx` | P4 |
| 7 | LOW | CAUTION | 1 | `ai-engineer` | EA2 |
| 7 | LOW | SAFE | 1 | `anti-ui-slop` | RP1 |
| 7 | LOW | SAFE | 1 | `api-patterns` | LP3 |
| 7 | LOW | CAUTION | 2 | `api-sdk-generator` | E1×2 |
| 7 | LOW | SAFE | 1 | `application-performance-performance-optimization` | EA2 |
| 7 | LOW | CAUTION | 1 | `azure-servicebus-rust` | P9 |
| 7 | LOW | CAUTION | 1 | `azure-storage-queue-rust` | P9 |
| 7 | LOW | SAFE | 1 | `backend-development-feature-development` | EA2 |
| 7 | LOW | CAUTION | 1 | `bash-pro` | PE2 |
| 7 | LOW | CAUTION | 1 | `behavioral-modes` | RA2 |
| 7 | LOW | CAUTION | 1 | `brooks-lint` | RP1 |
| 7 | LOW | SAFE | 2 | `changelog-updates` | E1×2 |
| 7 | LOW | CAUTION | 1 | `churn-prevention` | EA2 |
| 7 | LOW | CAUTION | 2 | `citation-management` | E1×2 |
| 7 | LOW | CAUTION | 1 | `cloudflare-workers-expert` | RP1 |
| 7 | LOW | SAFE | 1 | `code-polish` | EA2 |
| 7 | LOW | SAFE | 1 | `codex-review` | RP1 |
| 7 | LOW | CAUTION | 1 | `cohesivity` | EA2 |
| 7 | LOW | CAUTION | 1 | `competitor-profiling` | EA2 |
| 7 | LOW | SAFE | 1 | `content-creator` | LP3 |
| 7 | LOW | CAUTION | 1 | `context-agent` | LP3 |
| 7 | LOW | CAUTION | 1 | `context-guardian` | LP3 |
| 7 | LOW | SAFE | 1 | `context7-auto-research` | RP1 |
| 7 | LOW | CAUTION | 1 | `cowork-to-code-bridge` | TM3 |
| 7 | LOW | CAUTION | 1 | `cro` | EA2 |
| 7 | LOW | CAUTION | 1 | `cucumber-skill` | RP1 |
| 7 | LOW | SAFE | 1 | `customs-trade-compliance` | EA2 |
| 7 | LOW | SAFE | 1 | `database-design` | LP3 |
| 7 | LOW | SAFE | 1 | `deployment-engineer` | EA2 |
| 7 | LOW | SAFE | 1 | `deprecation-and-migration` | RP1 |
| 7 | LOW | SAFE | 1 | `emblemai-crypto-wallet` | RP1 |
| 7 | LOW | SAFE | 1 | `energy-procurement` | P9 |
| 7 | LOW | SAFE | 1 | `exa-search` | RP1 |
| 7 | LOW | CAUTION | 1 | `faf-wizard` | RP1 |
| 7 | LOW | CAUTION | 1 | `favicon` | PE2 |
| 7 | LOW | SAFE | 1 | `firecrawl-scraper` | RP1 |
| 7 | LOW | SAFE | 1 | `flowhunt-skill` | RP1 |
| 7 | LOW | SAFE | 1 | `form-cro` | EA2 |
| 7 | LOW | CAUTION | 1 | `frontend-ui-dark-ts` | RP1 |
| 7 | LOW | CAUTION | 1 | `gemini-interactions-api` | EA2 |
| 7 | LOW | SAFE | 1 | `geo-fundamentals` | LP3 |
| 7 | LOW | CAUTION | 1 | `global-chat-agent-discovery` | RP1 |
| 7 | LOW | CAUTION | 1 | `graphql` | RP1 |
| 7 | LOW | CAUTION | 1 | `grpc-golang` | P9 |
| 7 | LOW | CAUTION | 1 | `hig-platforms` | EA2 |
| 7 | LOW | CAUTION | 1 | `hig-project-context` | RA2 |
| 7 | LOW | CAUTION | 1 | `hugo-to-markdown` | LP3 |
| 7 | LOW | CAUTION | 1 | `incremental-implementation` | RP1 |
| 7 | LOW | CAUTION | 1 | `infinity` | EA2 |
| 7 | LOW | CAUTION | 1 | `instructree` | RP1 |
| 7 | LOW | CAUTION | 1 | `interview-coach` | RP1 |
| 7 | LOW | SAFE | 1 | `kubernetes-architect` | EA2 |
| 7 | LOW | CAUTION | 1 | `leiloeiro-avaliacao` | LP3 |
| 7 | LOW | CAUTION | 1 | `leiloeiro-edital` | LP3 |
| 7 | LOW | CAUTION | 1 | `leiloeiro-ia` | LP3 |
| 7 | LOW | CAUTION | 1 | `leiloeiro-juridico` | LP3 |
| 7 | LOW | CAUTION | 1 | `leiloeiro-mercado` | LP3 |
| 7 | LOW | CAUTION | 1 | `leiloeiro-risco` | LP3 |
| 7 | LOW | CAUTION | 1 | `logic-lens` | RP1 |
| 7 | LOW | CAUTION | 1 | `logistics-exception-management` | EA2 |
| 7 | LOW | SAFE | 1 | `longbridge` | RP1 |
| 7 | LOW | CAUTION | 1 | `macos-menubar-tuist-app` | RA2 |
| 7 | LOW | CAUTION | 2 | `makepad-splash` | E1×2 |
| 7 | LOW | SAFE | 2 | `mercury-mcp` | E1×2 |
| 7 | LOW | CAUTION | 1 | `monte-carlo-monitor-creation` | P9 |
| 7 | LOW | SAFE | 1 | `moyu` | EA2 |
| 7 | LOW | SAFE | 1 | `multi-source-search` | LP3 |
| 7 | LOW | CAUTION | 2 | `n8n-code-javascript` | E1×2 |
| 7 | LOW | CAUTION | 1 | `n8n-subworkflows` | EA4 |
| 7 | LOW | SAFE | 1 | `not-a-vibe-coder` | EA2 |
| 7 | LOW | CAUTION | 1 | `pdf` | LP3 |
| 7 | LOW | CAUTION | 1 | `pdf-official` | LP3 |
| 7 | LOW | SAFE | 1 | `performance-engineer` | EA2 |
| 7 | LOW | CAUTION | 1 | `plan-writing` | RP1 |
| 7 | LOW | CAUTION | 1 | `planning-and-task-breakdown` | EA2 |
| 7 | LOW | SAFE | 1 | `product-decision-agent` | LP3 |
| 7 | LOW | CAUTION | 2 | `pytest-skill` | E1×2 |
| 7 | LOW | SAFE | 1 | `recallmax` | RP1 |
| 7 | LOW | CAUTION | 1 | `recsys-pipeline-architect` | RP1 |
| 7 | LOW | CAUTION | 1 | `requesting-code-review` | EA2 |
| 7 | LOW | SAFE | 1 | `rich-elicitation` | EA2 |
| 7 | LOW | CAUTION | 1 | `sales-enablement` | EA2 |
| 7 | LOW | SAFE | 1 | `sandbox-migrate-to-next` | RP1 |
| 7 | LOW | CAUTION | 1 | `screenshots` | RP1 |
| 7 | LOW | SAFE | 1 | `seo` | RP1 |
| 7 | LOW | SAFE | 1 | `seo-fundamentals` | LP3 |
| 7 | LOW | SAFE | 1 | `skill-issue` | RP1 |
| 7 | LOW | CAUTION | 1 | `skill-rails-upgrade` | EA2 |
| 7 | LOW | CAUTION | 1 | `slack-bot-builder` | EA2 |
| 7 | LOW | CAUTION | 6 | `slack-gif-creator` | SC1×4, SC4×2 |
| 7 | LOW | SAFE | 1 | `socialclaw` | RP1 |
| 7 | LOW | CAUTION | 1 | `source-driven-development` | EA2 |
| 7 | LOW | CAUTION | 1 | `squirrel` | RP1 |
| 7 | LOW | CAUTION | 1 | `stitch-loop` | RP1 |
| 7 | LOW | SAFE | 1 | `tavily-web` | RP1 |
| 7 | LOW | CAUTION | 1 | `telegram-mini-app` | EA2 |
| 7 | LOW | CAUTION | 1 | `threejs-animation` | EA4 |
| 7 | LOW | SAFE | 1 | `tool-use-guardian` | RP1 |
| 7 | LOW | CAUTION | 1 | `ui-score` | TR2 |
| 7 | LOW | CAUTION | 1 | `unship` | RP1 |
| 7 | LOW | SAFE | 1 | `uxui-principles` | RP1 |
| 7 | LOW | SAFE | 1 | `videodb-skills` | RP1 |
| 7 | LOW | CAUTION | 1 | `wiki-onboarding` | TR2 |
| 7 | LOW | SAFE | 1 | `x-twitter-scraper` | RP1 |
| 7 | LOW | CAUTION | 1 | `youtube-full` | RP1 |
| 6 | LOW | SAFE | 1 | `ai-engineering-toolkit` | RA2 |
| 6 | LOW | CAUTION | 1 | `analytics` | TM3 |
| 6 | LOW | CAUTION | 1 | `anywrite` | RA2 |
| 6 | LOW | CAUTION | 1 | `appdeploy` | E1 |
| 6 | LOW | CAUTION | 1 | `aws-cdk-development` | RP1 |
| 6 | LOW | CAUTION | 1 | `context-kit` | RA2 |
| 6 | LOW | SAFE | 1 | `delegating-to-agents` | RA2 |
| 6 | LOW | CAUTION | 1 | `deployment-pipeline-design` | E1 |
| 6 | LOW | CAUTION | 1 | `find-matching-tenders` | E1 |
| 6 | LOW | CAUTION | 1 | `hugging-face-papers` | E1 |
| 6 | LOW | SAFE | 1 | `maxia` | E1 |
| 6 | LOW | CAUTION | 1 | `moodle-external-api-development` | E1 |
| 6 | LOW | CAUTION | 1 | `odoo-rpc-api` | E1 |
| 6 | LOW | CAUTION | 1 | `pi-web-search` | E1 |
| 6 | LOW | CAUTION | 1 | `postgresql` | OH3 |
| 6 | LOW | SAFE | 1 | `python-packaging` | RA2 |
| 6 | LOW | CAUTION | 1 | `shopify-apps` | SSRF3 |
| 6 | LOW | SAFE | 1 | `speed` | RA2 |
| 6 | LOW | CAUTION | 1 | `subagent-driven-development` | RA2 |
| 6 | LOW | CAUTION | 1 | `vibers-code-review` | E1 |
| 6 | LOW | CAUTION | 1 | `youtube-transcript` | E1 |
| 5 | LOW | CAUTION | 1 | `api-rate-limit-handler` | E1 |
| 5 | LOW | CAUTION | 1 | `applicationinsights-web-ts` | E1 |
| 5 | LOW | CAUTION | 1 | `azure-functions` | E1 |
| 5 | LOW | CAUTION | 1 | `azure-mgmt-apicenter-dotnet` | E1 |
| 5 | LOW | CAUTION | 1 | `buywhere-product-catalog` | E1 |
| 5 | LOW | CAUTION | 1 | `jq` | E1 |
| 5 | LOW | CAUTION | 1 | `kaizen` | E1 |
| 5 | LOW | CAUTION | 1 | `m365-agents-dotnet` | E1 |
| 5 | LOW | CAUTION | 1 | `m365-agents-py` | E1 |
| 5 | LOW | CAUTION | 1 | `microsoft-azure-webjobs-extensions-authentication-events-dotnet` | E1 |
| 5 | LOW | CAUTION | 2 | `model-compression-exploration` | EA3×2 |
| 5 | LOW | CAUTION | 1 | `molykit` | E1 |
| 5 | LOW | CAUTION | 1 | `n8n-expression-syntax` | E1 |
| 5 | LOW | CAUTION | 1 | `openapi-spec-generator` | E1 |
| 5 | LOW | CAUTION | 1 | `pagespeed-enhancer` | E1 |
| 5 | LOW | CAUTION | 1 | `postman-newman-automation` | E1 |
| 5 | LOW | CAUTION | 1 | `robius-app-architecture` | RA2 |
| 5 | LOW | CAUTION | 1 | `us-property-data` | E1 |
| 5 | LOW | CAUTION | 2 | `working-with-coreai` | EA3×2 |
| 3 | LOW | SAFE | 1 | `employment-contract-templates` | EA3 |
| 3 | LOW | CAUTION | 1 | `hig-components-controls` | EA3 |
| 3 | LOW | CAUTION | 1 | `hig-components-system` | EA3 |
| 3 | LOW | SAFE | 1 | `loopy` | EA3 |
| 3 | LOW | SAFE | 1 | `multi-agent-brainstorming` | EA3 |
| 3 | LOW | SAFE | 1 | `odoo-upgrade-advisor` | EA3 |
| 3 | LOW | CAUTION | 1 | `odw` | TR1 |
| 3 | LOW | CAUTION | 1 | `sql-injection-testing` | EA3 |
| 0 | LOW | CAUTION | 0 | `00-andruia-consultant` | — |
| 0 | LOW | CAUTION | 0 | `10-andruia-skill-smith` | — |
| 0 | LOW | CAUTION | 0 | `20-andruia-niche-intelligence` | — |
| 0 | LOW | CAUTION | 0 | `3d-web-experience` | — |
| 0 | LOW | SAFE | 0 | `ab-test-setup` | — |
| 0 | LOW | CAUTION | 0 | `ab-testing` | — |
| 0 | LOW | SAFE | 0 | `acceptance-orchestrator` | — |
| 0 | LOW | SAFE | 0 | `accesslint-audit` | — |
| 0 | LOW | SAFE | 0 | `accint-commitments` | — |
| 0 | LOW | SAFE | 0 | `accint-frames` | — |
| 0 | LOW | CAUTION | 0 | `accint-solve` | — |
| 0 | LOW | CAUTION | 0 | `activecampaign-automation` | — |
| 0 | LOW | SAFE | 0 | `address-github-comments` | — |
| 0 | LOW | SAFE | 0 | `advanced-evaluation` | — |
| 0 | LOW | CAUTION | 0 | `advogado-criminal` | — |
| 0 | LOW | CAUTION | 0 | `advogado-especialista` | — |
| 0 | LOW | CAUTION | 0 | `agent-evaluation-reporting` | — |
| 0 | LOW | CAUTION | 0 | `agent-framework-azure-ai-py` | — |
| 0 | LOW | CAUTION | 0 | `agent-harness-fault-injection` | — |
| 0 | LOW | CAUTION | 0 | `agent-manager-skill` | — |
| 0 | LOW | SAFE | 0 | `agent-memory` | — |
| 0 | LOW | SAFE | 0 | `agent-memory-mcp` | — |
| 0 | LOW | SAFE | 0 | `agent-orchestration-improve-agent` | — |
| 0 | LOW | SAFE | 0 | `agent-orchestration-multi-agent-optimize` | — |
| 0 | LOW | CAUTION | 0 | `agent-qa-authoring` | — |
| 0 | LOW | SAFE | 0 | `agent-qa-debug-fix` | — |
| 0 | LOW | CAUTION | 0 | `agent-tool-builder` | — |
| 0 | LOW | SAFE | 0 | `agentfolio` | — |
| 0 | LOW | CAUTION | 0 | `agentic-actions-auditor` | — |
| 0 | LOW | CAUTION | 0 | `agents-md` | — |
| 0 | LOW | CAUTION | 0 | `agents-v2-py` | — |
| 0 | LOW | SAFE | 0 | `ai-agent-development` | — |
| 0 | LOW | SAFE | 0 | `ai-agents-architect` | — |
| 0 | LOW | CAUTION | 0 | `ai-analyzer` | — |
| 0 | LOW | SAFE | 0 | `ai-dev-jobs-mcp` | — |
| 0 | LOW | CAUTION | 0 | `ai-loop` | — |
| 0 | LOW | SAFE | 0 | `ai-ml` | — |
| 0 | LOW | CAUTION | 0 | `ai-seo` | — |
| 0 | LOW | SAFE | 0 | `airtable-automation` | — |
| 0 | LOW | SAFE | 0 | `akf-trust-metadata` | — |
| 0 | LOW | CAUTION | 0 | `algolia-search` | — |
| 0 | LOW | SAFE | 0 | `alpha-vantage` | — |
| 0 | LOW | SAFE | 0 | `alternatives-pages` | — |
| 0 | LOW | CAUTION | 0 | `amazon-alexa` | — |
| 0 | LOW | SAFE | 0 | `amplitude-automation` | — |
| 0 | LOW | SAFE | 0 | `analytics-product` | — |
| 0 | LOW | SAFE | 0 | `analytics-tracking` | — |
| 0 | LOW | CAUTION | 0 | `andrej-karpathy` | — |
| 0 | LOW | CAUTION | 0 | `android-cli` | — |
| 0 | LOW | CAUTION | 0 | `android-jetpack-compose-expert` | — |
| 0 | LOW | CAUTION | 0 | `android-ui-journey-testing` | — |
| 0 | LOW | CAUTION | 0 | `android_ui_verification` | — |
| 0 | LOW | CAUTION | 0 | `angular-migration` | — |
| 0 | LOW | CAUTION | 0 | `angular-state-management` | — |
| 0 | LOW | SAFE | 0 | `animejs-animation` | — |
| 0 | LOW | SAFE | 0 | `anti-deception` | — |
| 0 | LOW | SAFE | 0 | `anti-sleep` | — |
| 0 | LOW | CAUTION | 0 | `antigravity-agent-manager` | — |
| 0 | LOW | CAUTION | 0 | `antigravity-design-expert` | — |
| 0 | LOW | CAUTION | 0 | `antigravity-skill-orchestrator` | — |
| 0 | LOW | CAUTION | 0 | `antigravity-workflows` | — |
| 0 | LOW | CAUTION | 0 | `aomi-transact` | — |
| 0 | LOW | CAUTION | 0 | `api-designer` | — |
| 0 | LOW | SAFE | 0 | `api-documentation` | — |
| 0 | LOW | SAFE | 0 | `api-documenter` | — |
| 0 | LOW | SAFE | 0 | `api-security-testing` | — |
| 0 | LOW | SAFE | 0 | `app-store-changelog` | — |
| 0 | LOW | CAUTION | 0 | `appium-skill` | — |
| 0 | LOW | CAUTION | 0 | `apple-notes-search` | — |
| 0 | LOW | SAFE | 0 | `architect-review` | — |
| 0 | LOW | SAFE | 0 | `architecture-patterns` | — |
| 0 | LOW | CAUTION | 0 | `arm-cortex-expert` | — |
| 0 | LOW | SAFE | 0 | `arrowspace` | — |
| 0 | LOW | SAFE | 0 | `article-illustrations` | — |
| 0 | LOW | CAUTION | 0 | `ask-copilot` | — |
| 0 | LOW | SAFE | 0 | `ask-questions-if-underspecified` | — |
| 0 | LOW | CAUTION | 0 | `astropy` | — |
| 0 | LOW | SAFE | 0 | `attack-tree-construction` | — |
| 0 | LOW | CAUTION | 0 | `audit-agent-run-evidence` | — |
| 0 | LOW | SAFE | 0 | `auto-research` | — |
| 0 | LOW | CAUTION | 0 | `automated-triage` | — |
| 0 | LOW | CAUTION | 0 | `avalonia-layout-zafiro` | — |
| 0 | LOW | CAUTION | 0 | `avalonia-viewmodels-zafiro` | — |
| 0 | LOW | SAFE | 0 | `avalonia-zafiro-development` | — |
| 0 | LOW | SAFE | 0 | `avoid-ai-writing` | — |
| 0 | LOW | SAFE | 0 | `awareness-stage-mapper` | — |
| 0 | LOW | CAUTION | 0 | `aws-cost-cleanup` | — |
| 0 | LOW | CAUTION | 0 | `aws-cost-operations` | — |
| 0 | LOW | SAFE | 0 | `aws-cost-optimizer` | — |
| 0 | LOW | CAUTION | 0 | `aws-serverless-eda` | — |
| 0 | LOW | SAFE | 0 | `aws-skills` | — |
| 0 | LOW | SAFE | 0 | `ax-extract-workflow` | — |
| 0 | LOW | SAFE | 0 | `axiom` | — |
| 0 | LOW | CAUTION | 0 | `azure-ai-agents-persistent-dotnet` | — |
| 0 | LOW | SAFE | 0 | `azure-ai-anomalydetector-java` | — |
| 0 | LOW | CAUTION | 0 | `azure-ai-contentsafety-java` | — |
| 0 | LOW | CAUTION | 0 | `azure-ai-contentsafety-py` | — |
| 0 | LOW | CAUTION | 0 | `azure-ai-contentsafety-ts` | — |
| 0 | LOW | CAUTION | 0 | `azure-ai-contentunderstanding-py` | — |
| 0 | LOW | CAUTION | 0 | `azure-ai-document-intelligence-dotnet` | — |
| 0 | LOW | CAUTION | 0 | `azure-ai-document-intelligence-ts` | — |
| 0 | LOW | CAUTION | 0 | `azure-ai-formrecognizer-java` | — |
| 0 | LOW | CAUTION | 0 | `azure-ai-language-conversations-py` | — |
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
| 0 | LOW | SAFE | 0 | `azure-communication-callingserver-java` | — |
| 0 | LOW | SAFE | 0 | `azure-communication-sms-java` | — |
| 0 | LOW | CAUTION | 0 | `azure-containerregistry-py` | — |
| 0 | LOW | CAUTION | 0 | `azure-cosmos-py` | — |
| 0 | LOW | SAFE | 0 | `azure-cosmos-rust` | — |
| 0 | LOW | CAUTION | 0 | `azure-cosmos-ts` | — |
| 0 | LOW | SAFE | 0 | `azure-data-tables-java` | — |
| 0 | LOW | SAFE | 0 | `azure-data-tables-py` | — |
| 0 | LOW | CAUTION | 0 | `azure-eventgrid-dotnet` | — |
| 0 | LOW | CAUTION | 0 | `azure-eventgrid-java` | — |
| 0 | LOW | CAUTION | 0 | `azure-eventgrid-py` | — |
| 0 | LOW | CAUTION | 0 | `azure-eventhub-dotnet` | — |
| 0 | LOW | SAFE | 0 | `azure-eventhub-java` | — |
| 0 | LOW | CAUTION | 0 | `azure-eventhub-py` | — |
| 0 | LOW | SAFE | 0 | `azure-eventhub-rust` | — |
| 0 | LOW | CAUTION | 0 | `azure-eventhub-ts` | — |
| 0 | LOW | CAUTION | 0 | `azure-identity-dotnet` | — |
| 0 | LOW | SAFE | 0 | `azure-identity-java` | — |
| 0 | LOW | SAFE | 0 | `azure-identity-py` | — |
| 0 | LOW | SAFE | 0 | `azure-identity-rust` | — |
| 0 | LOW | SAFE | 0 | `azure-identity-ts` | — |
| 0 | LOW | SAFE | 0 | `azure-keyvault-certificates-rust` | — |
| 0 | LOW | SAFE | 0 | `azure-keyvault-keys-rust` | — |
| 0 | LOW | CAUTION | 0 | `azure-keyvault-keys-ts` | — |
| 0 | LOW | SAFE | 0 | `azure-keyvault-py` | — |
| 0 | LOW | SAFE | 0 | `azure-keyvault-secrets-rust` | — |
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
| 0 | LOW | SAFE | 0 | `azure-monitor-opentelemetry-exporter-py` | — |
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
| 0 | LOW | SAFE | 0 | `azure-storage-blob-rust` | — |
| 0 | LOW | CAUTION | 0 | `azure-storage-blob-ts` | — |
| 0 | LOW | CAUTION | 0 | `azure-storage-file-datalake-py` | — |
| 0 | LOW | CAUTION | 0 | `azure-storage-file-share-ts` | — |
| 0 | LOW | SAFE | 0 | `azure-storage-queue-py` | — |
| 0 | LOW | CAUTION | 0 | `azure-storage-queue-ts` | — |
| 0 | LOW | CAUTION | 0 | `babysit-pr` | — |
| 0 | LOW | SAFE | 0 | `backend-architect` | — |
| 0 | LOW | CAUTION | 0 | `backend-security-coder` | — |
| 0 | LOW | SAFE | 0 | `backtesting-frameworks` | — |
| 0 | LOW | SAFE | 0 | `baseline-ui` | — |
| 0 | LOW | CAUTION | 0 | `bash-scripting` | — |
| 0 | LOW | CAUTION | 0 | `bazel-build-optimization` | — |
| 0 | LOW | CAUTION | 0 | `bdi-mental-states` | — |
| 0 | LOW | SAFE | 0 | `bdistill-behavioral-xray` | — |
| 0 | LOW | SAFE | 0 | `bdistill-knowledge-extraction` | — |
| 0 | LOW | SAFE | 0 | `before-you-build` | — |
| 0 | LOW | CAUTION | 0 | `bevy-ecs-expert` | — |
| 0 | LOW | CAUTION | 0 | `bilig-workpaper` | — |
| 0 | LOW | SAFE | 0 | `bill-gates` | — |
| 0 | LOW | SAFE | 0 | `billing-automation` | — |
| 0 | LOW | CAUTION | 0 | `binary-analysis-patterns` | — |
| 0 | LOW | CAUTION | 0 | `biopython` | — |
| 0 | LOW | CAUTION | 0 | `bitbucket-automation` | — |
| 0 | LOW | CAUTION | 0 | `blockchain-developer` | — |
| 0 | LOW | CAUTION | 0 | `blockrun` | — |
| 0 | LOW | SAFE | 0 | `blog-writing-guide` | — |
| 0 | LOW | CAUTION | 0 | `box-automation` | — |
| 0 | LOW | CAUTION | 0 | `brain-to-docs` | — |
| 0 | LOW | SAFE | 0 | `brainstorming` | — |
| 0 | LOW | SAFE | 0 | `brand-guidelines` | — |
| 0 | LOW | SAFE | 0 | `brand-guidelines-anthropic` | — |
| 0 | LOW | SAFE | 0 | `brand-guidelines-community` | — |
| 0 | LOW | SAFE | 0 | `brand-perception-psychologist` | — |
| 0 | LOW | CAUTION | 0 | `brave-man` | — |
| 0 | LOW | CAUTION | 0 | `brendangregg-use-tsa` | — |
| 0 | LOW | CAUTION | 0 | `brevo-automation` | — |
| 0 | LOW | SAFE | 0 | `brooks-audit` | — |
| 0 | LOW | SAFE | 0 | `brooks-debt` | — |
| 0 | LOW | SAFE | 0 | `brooks-sweep` | — |
| 0 | LOW | SAFE | 0 | `brooks-test` | — |
| 0 | LOW | CAUTION | 0 | `browser-extension-builder` | — |
| 0 | LOW | SAFE | 0 | `browser-extension-reverse` | — |
| 0 | LOW | CAUTION | 0 | `bug-hunt-swarm` | — |
| 0 | LOW | CAUTION | 0 | `bug-hunter` | — |
| 0 | LOW | CAUTION | 0 | `bugs-are-annoying` | — |
| 0 | LOW | CAUTION | 0 | `build` | — |
| 0 | LOW | SAFE | 0 | `bullmq-specialist` | — |
| 0 | LOW | CAUTION | 0 | `business-analyst` | — |
| 0 | LOW | CAUTION | 0 | `busybox-on-windows` | — |
| 0 | LOW | CAUTION | 0 | `c4-architecture-c4-architecture` | — |
| 0 | LOW | CAUTION | 0 | `c4-code` | — |
| 0 | LOW | CAUTION | 0 | `c4-component` | — |
| 0 | LOW | CAUTION | 0 | `c4-container` | — |
| 0 | LOW | CAUTION | 0 | `c4-context` | — |
| 0 | LOW | SAFE | 0 | `cal-com-automation` | — |
| 0 | LOW | SAFE | 0 | `canva-automation` | — |
| 0 | LOW | CAUTION | 0 | `canvas-design` | — |
| 0 | LOW | CAUTION | 0 | `case-review` | — |
| 0 | LOW | CAUTION | 0 | `cc-skill-clickhouse-io` | — |
| 0 | LOW | CAUTION | 0 | `cc-skill-frontend-patterns` | — |
| 0 | LOW | CAUTION | 0 | `cc-skill-project-guidelines-example` | — |
| 0 | LOW | CAUTION | 0 | `cdk-patterns` | — |
| 0 | LOW | CAUTION | 0 | `chat-widget` | — |
| 0 | LOW | CAUTION | 0 | `check-identity-pack` | — |
| 0 | LOW | CAUTION | 0 | `chrome-extension-developer` | — |
| 0 | LOW | CAUTION | 0 | `circleci-automation` | — |
| 0 | LOW | CAUTION | 0 | `cirq` | — |
| 0 | LOW | SAFE | 0 | `clarvia-aeo-check` | — |
| 0 | LOW | SAFE | 0 | `claude-ally-health` | — |
| 0 | LOW | CAUTION | 0 | `claude-d3js-skill` | — |
| 0 | LOW | SAFE | 0 | `claude-scientific-skills` | — |
| 0 | LOW | SAFE | 0 | `claude-speed-reader` | — |
| 0 | LOW | SAFE | 0 | `clean-code` | — |
| 0 | LOW | CAUTION | 0 | `clerk-auth` | — |
| 0 | LOW | SAFE | 0 | `clickup-automation` | — |
| 0 | LOW | SAFE | 0 | `close-automation` | — |
| 0 | LOW | SAFE | 0 | `closed-loop-delivery` | — |
| 0 | LOW | CAUTION | 0 | `cloud-architect` | — |
| 0 | LOW | SAFE | 0 | `cloud-devops` | — |
| 0 | LOW | CAUTION | 0 | `cloudflare-one` | — |
| 0 | LOW | SAFE | 0 | `cloudflare-one-migrations` | — |
| 0 | LOW | SAFE | 0 | `cloudformation-best-practices` | — |
| 0 | LOW | CAUTION | 0 | `co-marketing` | — |
| 0 | LOW | SAFE | 0 | `coda-automation` | — |
| 0 | LOW | CAUTION | 0 | `code-audit` | — |
| 0 | LOW | SAFE | 0 | `code-documentation-code-explain` | — |
| 0 | LOW | CAUTION | 0 | `code-refactoring-context-restore` | — |
| 0 | LOW | SAFE | 0 | `code-refactoring-refactor-clean` | — |
| 0 | LOW | SAFE | 0 | `code-refactoring-tech-debt` | — |
| 0 | LOW | CAUTION | 0 | `code-review-ai-ai-review` | — |
| 0 | LOW | CAUTION | 0 | `code-review-and-quality` | — |
| 0 | LOW | SAFE | 0 | `code-review-checklist` | — |
| 0 | LOW | CAUTION | 0 | `code-reviewer` | — |
| 0 | LOW | CAUTION | 0 | `code-showcase-core-components` | — |
| 0 | LOW | SAFE | 0 | `code-showcase-react-ui-patterns` | — |
| 0 | LOW | SAFE | 0 | `code-showcase-systematic-debugging` | — |
| 0 | LOW | CAUTION | 0 | `code-showcase-testing-patterns` | — |
| 0 | LOW | SAFE | 0 | `code-simplifier` | — |
| 0 | LOW | SAFE | 0 | `codebase-cleanup-refactor-clean` | — |
| 0 | LOW | SAFE | 0 | `codebase-cleanup-tech-debt` | — |
| 0 | LOW | SAFE | 0 | `codebase-design` | — |
| 0 | LOW | CAUTION | 0 | `codebase-to-wordpress-converter` | — |
| 0 | LOW | CAUTION | 0 | `codex-fable5` | — |
| 0 | LOW | CAUTION | 0 | `codex-profiles` | — |
| 0 | LOW | CAUTION | 0 | `community-building` | — |
| 0 | LOW | SAFE | 0 | `competitive-landscape` | — |
| 0 | LOW | CAUTION | 0 | `competitor-ad-intelligence` | — |
| 0 | LOW | SAFE | 0 | `competitor-alternatives` | — |
| 0 | LOW | CAUTION | 0 | `compile-knowledge` | — |
| 0 | LOW | CAUTION | 0 | `complexity-cuts` | — |
| 0 | LOW | CAUTION | 0 | `composition-patterns` | — |
| 0 | LOW | CAUTION | 0 | `comprehensive-review-full-review` | — |
| 0 | LOW | SAFE | 0 | `computer-vision-expert` | — |
| 0 | LOW | CAUTION | 0 | `concise-planning` | — |
| 0 | LOW | CAUTION | 0 | `conductor-new-track` | — |
| 0 | LOW | CAUTION | 0 | `conductor-status` | — |
| 0 | LOW | CAUTION | 0 | `conductor-validator` | — |
| 0 | LOW | CAUTION | 0 | `confluence-automation` | — |
| 0 | LOW | CAUTION | 0 | `content-marketer` | — |
| 0 | LOW | SAFE | 0 | `context-degradation` | — |
| 0 | LOW | CAUTION | 0 | `context-driven-development` | — |
| 0 | LOW | CAUTION | 0 | `context-management-context-restore` | — |
| 0 | LOW | CAUTION | 0 | `context-manager` | — |
| 0 | LOW | SAFE | 0 | `context-optimization` | — |
| 0 | LOW | CAUTION | 0 | `context-window-management` | — |
| 0 | LOW | CAUTION | 0 | `conversation-memory` | — |
| 0 | LOW | CAUTION | 0 | `convertkit-automation` | — |
| 0 | LOW | SAFE | 0 | `copy-editing` | — |
| 0 | LOW | SAFE | 0 | `copywriting` | — |
| 0 | LOW | SAFE | 0 | `copywriting-psychologist` | — |
| 0 | LOW | CAUTION | 0 | `core-components` | — |
| 0 | LOW | CAUTION | 0 | `cost-optimization` | — |
| 0 | LOW | SAFE | 0 | `cpp-pro` | — |
| 0 | LOW | SAFE | 0 | `cqrs-implementation` | — |
| 0 | LOW | SAFE | 0 | `create-branch` | — |
| 0 | LOW | SAFE | 0 | `create-issue-gate` | — |
| 0 | LOW | SAFE | 0 | `create-pr` | — |
| 0 | LOW | CAUTION | 0 | `crewai` | — |
| 0 | LOW | SAFE | 0 | `cross-platform-contract-propagation-audit` | — |
| 0 | LOW | SAFE | 0 | `crossframe` | — |
| 0 | LOW | SAFE | 0 | `crossframe-casebook` | — |
| 0 | LOW | SAFE | 0 | `crossframe-critical` | — |
| 0 | LOW | SAFE | 0 | `crossframe-debate` | — |
| 0 | LOW | SAFE | 0 | `crossframe-dialogue` | — |
| 0 | LOW | SAFE | 0 | `crossframe-essay` | — |
| 0 | LOW | SAFE | 0 | `crossframe-notebook` | — |
| 0 | LOW | SAFE | 0 | `crossframe-org` | — |
| 0 | LOW | SAFE | 0 | `crossframe-public` | — |
| 0 | LOW | CAUTION | 0 | `crossframe-review` | — |
| 0 | LOW | CAUTION | 0 | `crossframe-suite` | — |
| 0 | LOW | SAFE | 0 | `crossframe-teach` | — |
| 0 | LOW | SAFE | 0 | `crypto-bd-agent` | — |
| 0 | LOW | CAUTION | 0 | `csharp-pro` | — |
| 0 | LOW | SAFE | 0 | `customer-psychographic-profiler` | — |
| 0 | LOW | CAUTION | 0 | `customer-research` | — |
| 0 | LOW | CAUTION | 0 | `customer-support` | — |
| 0 | LOW | CAUTION | 0 | `cv-generator` | — |
| 0 | LOW | CAUTION | 0 | `cyber-audit` | — |
| 0 | LOW | CAUTION | 0 | `daily` | — |
| 0 | LOW | SAFE | 0 | `daily-gift` | — |
| 0 | LOW | SAFE | 0 | `daily-news-report` | — |
| 0 | LOW | SAFE | 0 | `data-engineer` | — |
| 0 | LOW | CAUTION | 0 | `data-engineering-data-driven-feature` | — |
| 0 | LOW | SAFE | 0 | `data-engineering-data-pipeline` | — |
| 0 | LOW | SAFE | 0 | `data-quality-frameworks` | — |
| 0 | LOW | SAFE | 0 | `data-scientist` | — |
| 0 | LOW | CAUTION | 0 | `data-storytelling` | — |
| 0 | LOW | CAUTION | 0 | `data-structure-protocol` | — |
| 0 | LOW | SAFE | 0 | `database` | — |
| 0 | LOW | CAUTION | 0 | `database-admin` | — |
| 0 | LOW | SAFE | 0 | `database-architect` | — |
| 0 | LOW | CAUTION | 0 | `database-migrations-sql-migrations` | — |
| 0 | LOW | CAUTION | 0 | `database-optimizer` | — |
| 0 | LOW | SAFE | 0 | `database-security` | — |
| 0 | LOW | SAFE | 0 | `datadog-automation` | — |
| 0 | LOW | SAFE | 0 | `dbt-transformation-patterns` | — |
| 0 | LOW | SAFE | 0 | `ddd-context-mapping` | — |
| 0 | LOW | SAFE | 0 | `ddd-tactical-patterns` | — |
| 0 | LOW | CAUTION | 0 | `debate-review` | — |
| 0 | LOW | CAUTION | 0 | `debug-buttercup` | — |
| 0 | LOW | CAUTION | 0 | `debugger` | — |
| 0 | LOW | CAUTION | 0 | `debugging-and-error-recovery` | — |
| 0 | LOW | CAUTION | 0 | `debugging-toolkit` | — |
| 0 | LOW | CAUTION | 0 | `debugging-toolkit-smart-debug` | — |
| 0 | LOW | CAUTION | 0 | `deep-research` | — |
| 0 | LOW | CAUTION | 0 | `defi-protocol-templates` | — |
| 0 | LOW | SAFE | 0 | `defuddle` | — |
| 0 | LOW | CAUTION | 0 | `deployment-validation-config-validate` | — |
| 0 | LOW | SAFE | 0 | `design-it` | — |
| 0 | LOW | SAFE | 0 | `design-orchestration` | — |
| 0 | LOW | SAFE | 0 | `design-philosophy` | — |
| 0 | LOW | SAFE | 0 | `design-spells` | — |
| 0 | LOW | CAUTION | 0 | `design-system` | — |
| 0 | LOW | CAUTION | 0 | `design-thinking` | — |
| 0 | LOW | SAFE | 0 | `design-ux` | — |
| 0 | LOW | CAUTION | 0 | `detect-ai-text` | — |
| 0 | LOW | CAUTION | 0 | `deterministic-design` | — |
| 0 | LOW | CAUTION | 0 | `dev-to-hashnode` | — |
| 0 | LOW | CAUTION | 0 | `devcontainer-setup` | — |
| 0 | LOW | CAUTION | 0 | `developer-advocacy` | — |
| 0 | LOW | CAUTION | 0 | `developer-audience-context` | — |
| 0 | LOW | SAFE | 0 | `developer-churn` | — |
| 0 | LOW | SAFE | 0 | `developer-listening` | — |
| 0 | LOW | CAUTION | 0 | `developer-newsletter` | — |
| 0 | LOW | SAFE | 0 | `developer-seo` | — |
| 0 | LOW | SAFE | 0 | `developer-signup-flow` | — |
| 0 | LOW | CAUTION | 0 | `development` | — |
| 0 | LOW | CAUTION | 0 | `devops-troubleshooter` | — |
| 0 | LOW | CAUTION | 0 | `devrel-content` | — |
| 0 | LOW | SAFE | 0 | `diagnose-android-overheating` | — |
| 0 | LOW | CAUTION | 0 | `diagram-generator` | — |
| 0 | LOW | SAFE | 0 | `differential-review` | — |
| 0 | LOW | SAFE | 0 | `digital-forensics` | — |
| 0 | LOW | SAFE | 0 | `dispatch` | — |
| 0 | LOW | CAUTION | 0 | `dispatching-parallel-agents` | — |
| 0 | LOW | CAUTION | 0 | `distributed-tracing` | — |
| 0 | LOW | CAUTION | 0 | `django-access-review` | — |
| 0 | LOW | CAUTION | 0 | `django-perf-review` | — |
| 0 | LOW | CAUTION | 0 | `django-pro` | — |
| 0 | LOW | CAUTION | 0 | `doc-coauthoring` | — |
| 0 | LOW | CAUTION | 0 | `doc2math` | — |
| 0 | LOW | CAUTION | 0 | `docs-architect` | — |
| 0 | LOW | CAUTION | 0 | `docs-guard` | — |
| 0 | LOW | SAFE | 0 | `documentation` | — |
| 0 | LOW | SAFE | 0 | `documentation-and-adrs` | — |
| 0 | LOW | CAUTION | 0 | `documentation-templates` | — |
| 0 | LOW | SAFE | 0 | `docusign-automation` | — |
| 0 | LOW | SAFE | 0 | `domain-driven-design` | — |
| 0 | LOW | CAUTION | 0 | `domain-modeling` | — |
| 0 | LOW | CAUTION | 0 | `dos-verify-done-claims` | — |
| 0 | LOW | CAUTION | 0 | `dotnet-architect` | — |
| 0 | LOW | CAUTION | 0 | `dotnet-backend` | — |
| 0 | LOW | SAFE | 0 | `dotnet-backend-patterns` | — |
| 0 | LOW | CAUTION | 0 | `dropbox-automation` | — |
| 0 | LOW | SAFE | 0 | `dsh-deepread` | — |
| 0 | LOW | CAUTION | 0 | `dwarf-expert` | — |
| 0 | LOW | CAUTION | 0 | `dx-optimizer` | — |
| 0 | LOW | SAFE | 0 | `e2e-testing` | — |
| 0 | LOW | CAUTION | 0 | `earllm-build` | — |
| 0 | LOW | CAUTION | 0 | `eas-update-insights` | — |
| 0 | LOW | CAUTION | 0 | `elixir-pro` | — |
| 0 | LOW | SAFE | 0 | `email-issue-fixer` | — |
| 0 | LOW | SAFE | 0 | `email-security` | — |
| 0 | LOW | SAFE | 0 | `email-sequence` | — |
| 0 | LOW | CAUTION | 0 | `embedding-strategies` | — |
| 0 | LOW | CAUTION | 0 | `emergency-card` | — |
| 0 | LOW | CAUTION | 0 | `emil-design-eng` | — |
| 0 | LOW | SAFE | 0 | `emotional-arc-designer` | — |
| 0 | LOW | CAUTION | 0 | `enhance-prompt` | — |
| 0 | LOW | CAUTION | 0 | `error-debugging-multi-agent-review` | — |
| 0 | LOW | CAUTION | 0 | `error-detective` | — |
| 0 | LOW | CAUTION | 0 | `error-diagnostics-smart-debug` | — |
| 0 | LOW | SAFE | 0 | `evaluation` | — |
| 0 | LOW | SAFE | 0 | `event-sourcing-architect` | — |
| 0 | LOW | SAFE | 0 | `event-staffing-compliance` | — |
| 0 | LOW | SAFE | 0 | `event-staffing-ordering` | — |
| 0 | LOW | SAFE | 0 | `event-store-design` | — |
| 0 | LOW | SAFE | 0 | `examprep-ai` | — |
| 0 | LOW | SAFE | 0 | `explain-like-socrates` | — |
| 0 | LOW | SAFE | 0 | `expo-deployment` | — |
| 0 | LOW | CAUTION | 0 | `expo-tailwind-setup` | — |
| 0 | LOW | CAUTION | 0 | `extract-document-data` | — |
| 0 | LOW | SAFE | 0 | `fact-check-x-complete` | — |
| 0 | LOW | CAUTION | 0 | `faf-context` | — |
| 0 | LOW | CAUTION | 0 | `faf-go` | — |
| 0 | LOW | SAFE | 0 | `fal-audio` | — |
| 0 | LOW | SAFE | 0 | `fal-generate` | — |
| 0 | LOW | SAFE | 0 | `fal-image-edit` | — |
| 0 | LOW | SAFE | 0 | `fal-platform` | — |
| 0 | LOW | SAFE | 0 | `fal-upscale` | — |
| 0 | LOW | SAFE | 0 | `fal-workflow` | — |
| 0 | LOW | SAFE | 0 | `falsify` | — |
| 0 | LOW | CAUTION | 0 | `family-health-analyzer` | — |
| 0 | LOW | CAUTION | 0 | `fastapi-pro` | — |
| 0 | LOW | CAUTION | 0 | `fastapi-router-py` | — |
| 0 | LOW | SAFE | 0 | `fda-food-safety-auditor` | — |
| 0 | LOW | SAFE | 0 | `fda-medtech-compliance-auditor` | — |
| 0 | LOW | SAFE | 0 | `ffuf-claude-skill` | — |
| 0 | LOW | SAFE | 0 | `figma-automation` | — |
| 0 | LOW | CAUTION | 0 | `file-organizer` | — |
| 0 | LOW | CAUTION | 0 | `find-bugs` | — |
| 0 | LOW | CAUTION | 0 | `firebase` | — |
| 0 | LOW | CAUTION | 0 | `fitness-analyzer` | — |
| 0 | LOW | SAFE | 0 | `fix-review` | — |
| 0 | LOW | SAFE | 0 | `fixing-accessibility` | — |
| 0 | LOW | SAFE | 0 | `fixing-metadata` | — |
| 0 | LOW | SAFE | 0 | `fixing-motion-performance` | — |
| 0 | LOW | CAUTION | 0 | `flutter-expert` | — |
| 0 | LOW | CAUTION | 0 | `folder-specific-claude-and-agents-md` | — |
| 0 | LOW | SAFE | 0 | `formik-patterns` | — |
| 0 | LOW | CAUTION | 0 | `fp-async` | — |
| 0 | LOW | CAUTION | 0 | `fp-backend` | — |
| 0 | LOW | CAUTION | 0 | `fp-data-transforms` | — |
| 0 | LOW | SAFE | 0 | `fp-either-ref` | — |
| 0 | LOW | CAUTION | 0 | `fp-errors` | — |
| 0 | LOW | SAFE | 0 | `fp-option-ref` | — |
| 0 | LOW | SAFE | 0 | `fp-pipe-ref` | — |
| 0 | LOW | CAUTION | 0 | `fp-pragmatic` | — |
| 0 | LOW | CAUTION | 0 | `fp-react` | — |
| 0 | LOW | CAUTION | 0 | `fp-refactor` | — |
| 0 | LOW | SAFE | 0 | `fp-taskeither-ref` | — |
| 0 | LOW | CAUTION | 0 | `fp-ts-errors` | — |
| 0 | LOW | CAUTION | 0 | `fp-ts-pragmatic` | — |
| 0 | LOW | CAUTION | 0 | `fp-ts-react` | — |
| 0 | LOW | CAUTION | 0 | `fp-types-ref` | — |
| 0 | LOW | CAUTION | 0 | `framework-migration-legacy-modernize` | — |
| 0 | LOW | SAFE | 0 | `free-tool-strategy` | — |
| 0 | LOW | SAFE | 0 | `freshdesk-automation` | — |
| 0 | LOW | CAUTION | 0 | `freshservice-automation` | — |
| 0 | LOW | SAFE | 0 | `frontend-api-integration-patterns` | — |
| 0 | LOW | SAFE | 0 | `frontend-design` | — |
| 0 | LOW | CAUTION | 0 | `frontend-dev-guidelines` | — |
| 0 | LOW | CAUTION | 0 | `frontend-developer` | — |
| 0 | LOW | CAUTION | 0 | `frontend-mobile-development-component-scaffold` | — |
| 0 | LOW | CAUTION | 0 | `frontend-security-coder` | — |
| 0 | LOW | CAUTION | 0 | `frontend-ui-engineering` | — |
| 0 | LOW | SAFE | 0 | `full-output-enforcement` | — |
| 0 | LOW | CAUTION | 0 | `full-stack-orchestration-full-stack-feature` | — |
| 0 | LOW | SAFE | 0 | `game-development` | — |
| 0 | LOW | CAUTION | 0 | `gemini-api-dev` | — |
| 0 | LOW | CAUTION | 0 | `gemini-live-api-dev` | — |
| 0 | LOW | SAFE | 0 | `geoffrey-hinton` | — |
| 0 | LOW | SAFE | 0 | `gh-attach` | — |
| 0 | LOW | CAUTION | 0 | `gh-image` | — |
| 0 | LOW | SAFE | 0 | `gh-review-requests` | — |
| 0 | LOW | CAUTION | 0 | `gha-security-review` | — |
| 0 | LOW | SAFE | 0 | `ghidra-reverse` | — |
| 0 | LOW | CAUTION | 0 | `git-pr-workflows-onboard` | — |
| 0 | LOW | CAUTION | 0 | `git-pushing` | — |
| 0 | LOW | SAFE | 0 | `github` | — |
| 0 | LOW | SAFE | 0 | `github-actions-debugger` | — |
| 0 | LOW | CAUTION | 0 | `github-automation` | — |
| 0 | LOW | CAUTION | 0 | `github-issue-creator` | — |
| 0 | LOW | CAUTION | 0 | `gitlab-automation` | — |
| 0 | LOW | CAUTION | 0 | `gmail-automation` | — |
| 0 | LOW | SAFE | 0 | `go-concurrency-patterns` | — |
| 0 | LOW | SAFE | 0 | `go-in-depth` | — |
| 0 | LOW | CAUTION | 0 | `go-rust-reverse` | — |
| 0 | LOW | CAUTION | 0 | `goal-analyzer` | — |
| 0 | LOW | CAUTION | 0 | `goal-loop` | — |
| 0 | LOW | SAFE | 0 | `godot-4-migration` | — |
| 0 | LOW | SAFE | 0 | `godot-gdscript-patterns` | — |
| 0 | LOW | SAFE | 0 | `golang-pro` | — |
| 0 | LOW | SAFE | 0 | `google-analytics-automation` | — |
| 0 | LOW | CAUTION | 0 | `google-calendar-automation` | — |
| 0 | LOW | CAUTION | 0 | `google-drive-automation` | — |
| 0 | LOW | CAUTION | 0 | `google-sheets-automation` | — |
| 0 | LOW | CAUTION | 0 | `google-slides-automation` | — |
| 0 | LOW | CAUTION | 0 | `googlesheets-automation` | — |
| 0 | LOW | SAFE | 0 | `gpt-taste` | — |
| 0 | LOW | CAUTION | 0 | `graceful-shutdown` | — |
| 0 | LOW | CAUTION | 0 | `grafana-dashboards` | — |
| 0 | LOW | CAUTION | 0 | `graphql-architect` | — |
| 0 | LOW | CAUTION | 0 | `graphql-schema` | — |
| 0 | LOW | SAFE | 0 | `grill-me` | — |
| 0 | LOW | SAFE | 0 | `grill-with-docs` | — |
| 0 | LOW | SAFE | 0 | `grilling` | — |
| 0 | LOW | CAUTION | 0 | `growth-engine` | — |
| 0 | LOW | SAFE | 0 | `handoff` | — |
| 0 | LOW | SAFE | 0 | `hardware-security` | — |
| 0 | LOW | CAUTION | 0 | `haskell-pro` | — |
| 0 | LOW | SAFE | 0 | `headline-psychologist` | — |
| 0 | LOW | CAUTION | 0 | `health-trend-analyzer` | — |
| 0 | LOW | SAFE | 0 | `helium-mcp` | — |
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
| 0 | LOW | SAFE | 0 | `hugging-face-trackio` | — |
| 0 | LOW | CAUTION | 0 | `huggingface-best` | — |
| 0 | LOW | CAUTION | 0 | `hybrid-cloud-architect` | — |
| 0 | LOW | CAUTION | 0 | `hybrid-cloud-networking` | — |
| 0 | LOW | SAFE | 0 | `hybrid-search-implementation` | — |
| 0 | LOW | CAUTION | 0 | `hyperexecute-skill` | — |
| 0 | LOW | SAFE | 0 | `iconsax-library` | — |
| 0 | LOW | CAUTION | 0 | `idea-autopsy` | — |
| 0 | LOW | CAUTION | 0 | `idea-darwin` | — |
| 0 | LOW | CAUTION | 0 | `idea-os` | — |
| 0 | LOW | CAUTION | 0 | `idea-refine` | — |
| 0 | LOW | SAFE | 0 | `identity-federation` | — |
| 0 | LOW | SAFE | 0 | `identity-mirror` | — |
| 0 | LOW | CAUTION | 0 | `idor-testing` | — |
| 0 | LOW | SAFE | 0 | `ilya-sutskever` | — |
| 0 | LOW | SAFE | 0 | `image-studio` | — |
| 0 | LOW | CAUTION | 0 | `imagen` | — |
| 0 | LOW | SAFE | 0 | `implement` | — |
| 0 | LOW | CAUTION | 0 | `improve-codebase-architecture` | — |
| 0 | LOW | CAUTION | 0 | `incident-responder` | — |
| 0 | LOW | CAUTION | 0 | `indexing-issue-auditor` | — |
| 0 | LOW | CAUTION | 0 | `industrial-brutalist-ui` | — |
| 0 | LOW | SAFE | 0 | `infinite-gratitude` | — |
| 0 | LOW | CAUTION | 0 | `inngest` | — |
| 0 | LOW | SAFE | 0 | `instagram-automation` | — |
| 0 | LOW | CAUTION | 0 | `interactive-portfolio` | — |
| 0 | LOW | CAUTION | 0 | `intercom-automation` | — |
| 0 | LOW | SAFE | 0 | `internal-comms` | — |
| 0 | LOW | SAFE | 0 | `internal-comms-anthropic` | — |
| 0 | LOW | CAUTION | 0 | `internal-comms-community` | — |
| 0 | LOW | SAFE | 0 | `interview-style-doc-building` | — |
| 0 | LOW | SAFE | 0 | `ios-debugger-agent` | — |
| 0 | LOW | CAUTION | 0 | `ios-developer` | — |
| 0 | LOW | CAUTION | 0 | `issues` | — |
| 0 | LOW | CAUTION | 0 | `istio-traffic-management` | — |
| 0 | LOW | SAFE | 0 | `it-manager-hospital` | — |
| 0 | LOW | SAFE | 0 | `it-manager-pro` | — |
| 0 | LOW | CAUTION | 0 | `iterate-pr` | — |
| 0 | LOW | SAFE | 0 | `itil-expert` | — |
| 0 | LOW | CAUTION | 0 | `java-pro` | — |
| 0 | LOW | CAUTION | 0 | `javascript-mastery` | — |
| 0 | LOW | SAFE | 0 | `javascript-pro` | — |
| 0 | LOW | SAFE | 0 | `jira-automation` | — |
| 0 | LOW | SAFE | 0 | `jobs-to-be-done-analyst` | — |
| 0 | LOW | CAUTION | 0 | `js-reverse` | — |
| 0 | LOW | CAUTION | 0 | `json-canvas` | — |
| 0 | LOW | CAUTION | 0 | `julia-pro` | — |
| 0 | LOW | CAUTION | 0 | `junit-5-skill` | — |
| 0 | LOW | CAUTION | 0 | `k8s-security-policies` | — |
| 0 | LOW | CAUTION | 0 | `klaviyo-automation` | — |
| 0 | LOW | SAFE | 0 | `kotler-macro-analyzer` | — |
| 0 | LOW | CAUTION | 0 | `kotlin-coroutines-expert` | — |
| 0 | LOW | CAUTION | 0 | `kpi-dashboard-design` | — |
| 0 | LOW | SAFE | 0 | `kubernetes-deployment` | — |
| 0 | LOW | SAFE | 0 | `lambda-lang` | — |
| 0 | LOW | CAUTION | 0 | `lambdatest-agent-skills` | — |
| 0 | LOW | CAUTION | 0 | `langchain-architecture` | — |
| 0 | LOW | SAFE | 0 | `langfuse` | — |
| 0 | LOW | CAUTION | 0 | `langgraph` | — |
| 0 | LOW | SAFE | 0 | `laravel-development-workflow` | — |
| 0 | LOW | SAFE | 0 | `laravel-expert` | — |
| 0 | LOW | CAUTION | 0 | `latex-paper-conversion` | — |
| 0 | LOW | SAFE | 0 | `launch-strategy` | — |
| 0 | LOW | CAUTION | 0 | `lead-magnets` | — |
| 0 | LOW | CAUTION | 0 | `legacy-modernizer` | — |
| 0 | LOW | CAUTION | 0 | `legal-advisor` | — |
| 0 | LOW | CAUTION | 0 | `lesson-generator` | — |
| 0 | LOW | SAFE | 0 | `lex` | — |
| 0 | LOW | SAFE | 0 | `lightning-architecture-review` | — |
| 0 | LOW | SAFE | 0 | `lightning-channel-factories` | — |
| 0 | LOW | SAFE | 0 | `lightning-factory-explainer` | — |
| 0 | LOW | SAFE | 0 | `linear-automation` | — |
| 0 | LOW | SAFE | 0 | `linkedin-automation` | — |
| 0 | LOW | SAFE | 0 | `linkedin-post-writer` | — |
| 0 | LOW | SAFE | 0 | `linux-troubleshooting` | — |
| 0 | LOW | CAUTION | 0 | `llm-app-patterns` | — |
| 0 | LOW | SAFE | 0 | `llm-application-dev-ai-assistant` | — |
| 0 | LOW | CAUTION | 0 | `llm-application-dev-langchain-agent` | — |
| 0 | LOW | CAUTION | 0 | `llm-evaluation` | — |
| 0 | LOW | CAUTION | 0 | `llm-ops` | — |
| 0 | LOW | SAFE | 0 | `llm-prompt-optimizer` | — |
| 0 | LOW | CAUTION | 0 | `llm-structured-output` | — |
| 0 | LOW | SAFE | 0 | `local-legal-seo-audit` | — |
| 0 | LOW | SAFE | 0 | `local-llm-expert` | — |
| 0 | LOW | CAUTION | 0 | `logic-diff` | — |
| 0 | LOW | CAUTION | 0 | `logic-explain` | — |
| 0 | LOW | CAUTION | 0 | `logic-locate` | — |
| 0 | LOW | CAUTION | 0 | `longbridge-content` | — |
| 0 | LOW | CAUTION | 0 | `longbridge-fundamentals` | — |
| 0 | LOW | CAUTION | 0 | `longbridge-market-data` | — |
| 0 | LOW | CAUTION | 0 | `lookdev-auto` | — |
| 0 | LOW | SAFE | 0 | `loop-library` | — |
| 0 | LOW | SAFE | 0 | `loss-aversion-designer` | — |
| 0 | LOW | CAUTION | 0 | `m365-agents-ts` | — |
| 0 | LOW | CAUTION | 0 | `machine-learning-ops-ml-pipeline` | — |
| 0 | LOW | SAFE | 0 | `macos-reverse` | — |
| 0 | LOW | CAUTION | 0 | `macos-screen-recorder` | — |
| 0 | LOW | SAFE | 0 | `magic-animator` | — |
| 0 | LOW | SAFE | 0 | `magic-ui-generator` | — |
| 0 | LOW | CAUTION | 0 | `mailchimp-automation` | — |
| 0 | LOW | CAUTION | 0 | `mailtrap-setting-up-sending-domain` | — |
| 0 | LOW | SAFE | 0 | `make-automation` | — |
| 0 | LOW | CAUTION | 0 | `makepad-animation` | — |
| 0 | LOW | CAUTION | 0 | `makepad-basics` | — |
| 0 | LOW | CAUTION | 0 | `makepad-dsl` | — |
| 0 | LOW | CAUTION | 0 | `makepad-event-action` | — |
| 0 | LOW | CAUTION | 0 | `makepad-font` | — |
| 0 | LOW | CAUTION | 0 | `makepad-layout` | — |
| 0 | LOW | SAFE | 0 | `makepad-reference` | — |
| 0 | LOW | CAUTION | 0 | `makepad-shaders` | — |
| 0 | LOW | SAFE | 0 | `makepad-skills` | — |
| 0 | LOW | CAUTION | 0 | `makepad-widgets` | — |
| 0 | LOW | CAUTION | 0 | `malware-analyst` | — |
| 0 | LOW | SAFE | 0 | `markdown-rendering` | — |
| 0 | LOW | CAUTION | 0 | `market-sizing-analysis` | — |
| 0 | LOW | SAFE | 0 | `marketing-ideas` | — |
| 0 | LOW | SAFE | 0 | `marketing-psychology` | — |
| 0 | LOW | SAFE | 0 | `marketplace-rbac-audit` | — |
| 0 | LOW | CAUTION | 0 | `markstream-angular` | — |
| 0 | LOW | CAUTION | 0 | `markstream-custom-components` | — |
| 0 | LOW | CAUTION | 0 | `markstream-install` | — |
| 0 | LOW | CAUTION | 0 | `markstream-migration` | — |
| 0 | LOW | CAUTION | 0 | `markstream-nuxt` | — |
| 0 | LOW | CAUTION | 0 | `markstream-react` | — |
| 0 | LOW | CAUTION | 0 | `markstream-svelte` | — |
| 0 | LOW | CAUTION | 0 | `markstream-vue` | — |
| 0 | LOW | CAUTION | 0 | `markstream-vue2` | — |
| 0 | LOW | CAUTION | 0 | `markstream-vue2-cli` | — |
| 0 | LOW | CAUTION | 0 | `markstream-vue2-vite` | — |
| 0 | LOW | CAUTION | 0 | `matplotlib` | — |
| 0 | LOW | CAUTION | 0 | `mcp-tool-developer` | — |
| 0 | LOW | CAUTION | 0 | `md2video-audio` | — |
| 0 | LOW | CAUTION | 0 | `mdpr-skill` | — |
| 0 | LOW | SAFE | 0 | `memory-safety-patterns` | — |
| 0 | LOW | SAFE | 0 | `memory-systems` | — |
| 0 | LOW | CAUTION | 0 | `mental-health-analyzer` | — |
| 0 | LOW | CAUTION | 0 | `mermaid-expert` | — |
| 0 | LOW | CAUTION | 0 | `mesh-memory` | — |
| 0 | LOW | SAFE | 0 | `micro-saas-launcher` | — |
| 0 | LOW | SAFE | 0 | `microservices-patterns` | — |
| 0 | LOW | CAUTION | 0 | `minecraft-bukkit-pro` | — |
| 0 | LOW | CAUTION | 0 | `minimalist-ui` | — |
| 0 | LOW | CAUTION | 0 | `miro-automation` | — |
| 0 | LOW | CAUTION | 0 | `mise-configurator` | — |
| 0 | LOW | SAFE | 0 | `mixpanel-automation` | — |
| 0 | LOW | CAUTION | 0 | `ml-engineer` | — |
| 0 | LOW | CAUTION | 0 | `ml-pipeline-workflow` | — |
| 0 | LOW | CAUTION | 0 | `mlops-engineer` | — |
| 0 | LOW | SAFE | 0 | `moatmri` | — |
| 0 | LOW | CAUTION | 0 | `mobile-developer` | — |
| 0 | LOW | CAUTION | 0 | `mobile-security-coder` | — |
| 0 | LOW | CAUTION | 0 | `mock-hunter` | — |
| 0 | LOW | CAUTION | 0 | `modellix` | — |
| 0 | LOW | SAFE | 0 | `monday-automation` | — |
| 0 | LOW | CAUTION | 0 | `monetization` | — |
| 0 | LOW | CAUTION | 0 | `monopoly` | — |
| 0 | LOW | CAUTION | 0 | `monorepo-architect` | — |
| 0 | LOW | CAUTION | 0 | `monte-carlo-analyze-root-cause` | — |
| 0 | LOW | CAUTION | 0 | `monte-carlo-asset-health` | — |
| 0 | LOW | CAUTION | 0 | `monte-carlo-performance-diagnosis` | — |
| 0 | LOW | CAUTION | 0 | `monte-carlo-remediation` | — |
| 0 | LOW | CAUTION | 0 | `multi-advisor` | — |
| 0 | LOW | CAUTION | 0 | `multi-agent-architect` | — |
| 0 | LOW | SAFE | 0 | `multi-agent-patterns` | — |
| 0 | LOW | CAUTION | 0 | `multi-agent-task-orchestrator` | — |
| 0 | LOW | CAUTION | 0 | `multi-cloud-architecture` | — |
| 0 | LOW | CAUTION | 0 | `multi-platform-apps-multi-platform` | — |
| 0 | LOW | CAUTION | 0 | `n8n-code-python` | — |
| 0 | LOW | CAUTION | 0 | `n8n-code-tool` | — |
| 0 | LOW | CAUTION | 0 | `n8n-multi-instance` | — |
| 0 | LOW | SAFE | 0 | `nanobanana-ppt-skills` | — |
| 0 | LOW | CAUTION | 0 | `neon-postgres-egress-optimizer` | — |
| 0 | LOW | SAFE | 0 | `nerdzao-elite` | — |
| 0 | LOW | SAFE | 0 | `nerdzao-elite-gemini-high` | — |
| 0 | LOW | CAUTION | 0 | `network-engineer` | — |
| 0 | LOW | CAUTION | 0 | `new-rails-project` | — |
| 0 | LOW | CAUTION | 0 | `newman-cicd-integration` | — |
| 0 | LOW | CAUTION | 0 | `nextjs-best-practices` | — |
| 0 | LOW | CAUTION | 0 | `nextjs-seo-indexing` | — |
| 0 | LOW | CAUTION | 0 | `nextjs-supabase-auth` | — |
| 0 | LOW | CAUTION | 0 | `nft-standards` | — |
| 0 | LOW | CAUTION | 0 | `nika` | — |
| 0 | LOW | CAUTION | 0 | `nodejs-best-practices` | — |
| 0 | LOW | SAFE | 0 | `nosql-expert` | — |
| 0 | LOW | CAUTION | 0 | `not-human-search-mcp` | — |
| 0 | LOW | CAUTION | 0 | `notion-automation` | — |
| 0 | LOW | SAFE | 0 | `notion-template-business` | — |
| 0 | LOW | SAFE | 0 | `objection-preemptor` | — |
| 0 | LOW | CAUTION | 0 | `observability-and-instrumentation` | — |
| 0 | LOW | SAFE | 0 | `observability-engineer` | — |
| 0 | LOW | SAFE | 0 | `observability-monitoring-monitor-setup` | — |
| 0 | LOW | SAFE | 0 | `observability-monitoring-slo-implement` | — |
| 0 | LOW | CAUTION | 0 | `obsidian-cli` | — |
| 0 | LOW | CAUTION | 0 | `obsidian-clipper-template-creator` | — |
| 0 | LOW | SAFE | 0 | `obsidian-markdown` | — |
| 0 | LOW | CAUTION | 0 | `occupational-health-analyzer` | — |
| 0 | LOW | SAFE | 0 | `odoo-accounting-setup` | — |
| 0 | LOW | CAUTION | 0 | `odoo-automated-tests` | — |
| 0 | LOW | SAFE | 0 | `odoo-ecommerce-configurator` | — |
| 0 | LOW | CAUTION | 0 | `odoo-edi-connector` | — |
| 0 | LOW | CAUTION | 0 | `odoo-hr-payroll-setup` | — |
| 0 | LOW | SAFE | 0 | `odoo-inventory-optimizer` | — |
| 0 | LOW | CAUTION | 0 | `odoo-l10n-compliance` | — |
| 0 | LOW | SAFE | 0 | `odoo-manufacturing-advisor` | — |
| 0 | LOW | CAUTION | 0 | `odoo-migration-helper` | — |
| 0 | LOW | CAUTION | 0 | `odoo-module-developer` | — |
| 0 | LOW | CAUTION | 0 | `odoo-orm-expert` | — |
| 0 | LOW | SAFE | 0 | `odoo-project-timesheet` | — |
| 0 | LOW | SAFE | 0 | `odoo-purchase-workflow` | — |
| 0 | LOW | CAUTION | 0 | `odoo-qweb-templates` | — |
| 0 | LOW | SAFE | 0 | `odoo-sales-crm-expert` | — |
| 0 | LOW | CAUTION | 0 | `odoo-security-rules` | — |
| 0 | LOW | CAUTION | 0 | `odoo-woocommerce-bridge` | — |
| 0 | LOW | CAUTION | 0 | `odoo-xml-views-builder` | — |
| 0 | LOW | SAFE | 0 | `office-productivity` | — |
| 0 | LOW | CAUTION | 0 | `on-call-handoff-patterns` | — |
| 0 | LOW | CAUTION | 0 | `onboarding` | — |
| 0 | LOW | SAFE | 0 | `onboarding-cro` | — |
| 0 | LOW | SAFE | 0 | `onboarding-psychologist` | — |
| 0 | LOW | SAFE | 0 | `one-drive-automation` | — |
| 0 | LOW | CAUTION | 0 | `ontoly-software-graph` | — |
| 0 | LOW | CAUTION | 0 | `open-source-marketing` | — |
| 0 | LOW | CAUTION | 0 | `openclaw-github-repo-commander` | — |
| 0 | LOW | SAFE | 0 | `optim-agent` | — |
| 0 | LOW | SAFE | 0 | `options-flow-analyzer` | — |
| 0 | LOW | SAFE | 0 | `oral-health-analyzer` | — |
| 0 | LOW | SAFE | 0 | `orchestrate` | — |
| 0 | LOW | SAFE | 0 | `orchestrate-batch-refactor` | — |
| 0 | LOW | SAFE | 0 | `osterwalder-canvas-architect` | — |
| 0 | LOW | SAFE | 0 | `ot-ics` | — |
| 0 | LOW | SAFE | 0 | `outlook-automation` | — |
| 0 | LOW | SAFE | 0 | `outlook-calendar-automation` | — |
| 0 | LOW | SAFE | 0 | `page-cro` | — |
| 0 | LOW | CAUTION | 0 | `pagerduty-automation` | — |
| 0 | LOW | SAFE | 0 | `paid-ads` | — |
| 0 | LOW | CAUTION | 0 | `pakistan-payments-stack` | — |
| 0 | LOW | CAUTION | 0 | `parallel-agents` | — |
| 0 | LOW | SAFE | 0 | `parallel-search-mcp` | — |
| 0 | LOW | CAUTION | 0 | `payment-integration` | — |
| 0 | LOW | CAUTION | 0 | `pci-compliance` | — |
| 0 | LOW | SAFE | 0 | `pdf-conversion-router` | — |
| 0 | LOW | SAFE | 0 | `people-data` | — |
| 0 | LOW | CAUTION | 0 | `performance-optimizer` | — |
| 0 | LOW | CAUTION | 0 | `performance-testing-review-ai-review` | — |
| 0 | LOW | CAUTION | 0 | `performance-testing-review-multi-agent-review` | — |
| 0 | LOW | CAUTION | 0 | `permission-manager` | — |
| 0 | LOW | SAFE | 0 | `phase-gated-debugging` | — |
| 0 | LOW | CAUTION | 0 | `photopea-embedded-editor` | — |
| 0 | LOW | CAUTION | 0 | `php-pro` | — |
| 0 | LOW | CAUTION | 0 | `pi-custom-model` | — |
| 0 | LOW | CAUTION | 0 | `pipedrive-automation` | — |
| 0 | LOW | SAFE | 0 | `pitch-psychologist` | — |
| 0 | LOW | CAUTION | 0 | `plotly` | — |
| 0 | LOW | CAUTION | 0 | `podcast-generation` | — |
| 0 | LOW | SAFE | 0 | `poka-yoke` | — |
| 0 | LOW | CAUTION | 0 | `polars` | — |
| 0 | LOW | SAFE | 0 | `popup-cro` | — |
| 0 | LOW | CAUTION | 0 | `postgres-best-practices` | — |
| 0 | LOW | SAFE | 0 | `postgresql-optimization` | — |
| 0 | LOW | SAFE | 0 | `posthog-automation` | — |
| 0 | LOW | CAUTION | 0 | `postman-collection-generator` | — |
| 0 | LOW | CAUTION | 0 | `postman-openapi-converter` | — |
| 0 | LOW | CAUTION | 0 | `postmark-automation` | — |
| 0 | LOW | CAUTION | 0 | `postmortem-writing` | — |
| 0 | LOW | CAUTION | 0 | `powershell-windows` | — |
| 0 | LOW | CAUTION | 0 | `pr-merge-champion` | — |
| 0 | LOW | CAUTION | 0 | `pr-writer` | — |
| 0 | LOW | CAUTION | 0 | `pre-ship-gate` | — |
| 0 | LOW | SAFE | 0 | `premium-3d-website` | — |
| 0 | LOW | SAFE | 0 | `price-psychology-strategist` | — |
| 0 | LOW | CAUTION | 0 | `pricing` | — |
| 0 | LOW | SAFE | 0 | `pricing-strategy` | — |
| 0 | LOW | CAUTION | 0 | `product-design` | — |
| 0 | LOW | CAUTION | 0 | `product-inventor` | — |
| 0 | LOW | CAUTION | 0 | `product-manager` | — |
| 0 | LOW | CAUTION | 0 | `product-marketing` | — |
| 0 | LOW | CAUTION | 0 | `product-marketing-context` | — |
| 0 | LOW | SAFE | 0 | `production-runtime-certification` | — |
| 0 | LOW | SAFE | 0 | `programmatic-seo` | — |
| 0 | LOW | SAFE | 0 | `progressive-estimation` | — |
| 0 | LOW | CAUTION | 0 | `progressive-web-app` | — |
| 0 | LOW | SAFE | 0 | `project-development` | — |
| 0 | LOW | SAFE | 0 | `projection-patterns` | — |
| 0 | LOW | CAUTION | 0 | `prometheus-configuration` | — |
| 0 | LOW | CAUTION | 0 | `prompt-caching` | — |
| 0 | LOW | SAFE | 0 | `prompt-engineering` | — |
| 0 | LOW | SAFE | 0 | `prompt-library` | — |
| 0 | LOW | CAUTION | 0 | `protocol-reverse` | — |
| 0 | LOW | SAFE | 0 | `protocol-reverse-engineering` | — |
| 0 | LOW | CAUTION | 0 | `prototype` | — |
| 0 | LOW | CAUTION | 0 | `pubmed-database` | — |
| 0 | LOW | CAUTION | 0 | `puppeteer-skill` | — |
| 0 | LOW | SAFE | 0 | `push-skill-to-github` | — |
| 0 | LOW | SAFE | 0 | `puzzle-activity-planner` | — |
| 0 | LOW | SAFE | 0 | `pydantic-ai` | — |
| 0 | LOW | CAUTION | 0 | `pydantic-models-py` | — |
| 0 | LOW | SAFE | 0 | `pypict-skill` | — |
| 0 | LOW | CAUTION | 0 | `python-development` | — |
| 0 | LOW | CAUTION | 0 | `python-development-python-scaffold` | — |
| 0 | LOW | SAFE | 0 | `python-fastapi-development` | — |
| 0 | LOW | SAFE | 0 | `python-patterns` | — |
| 0 | LOW | SAFE | 0 | `python-performance-optimization` | — |
| 0 | LOW | SAFE | 0 | `python-pro` | — |
| 0 | LOW | CAUTION | 0 | `qiskit` | — |
| 0 | LOW | CAUTION | 0 | `quant-analyst` | — |
| 0 | LOW | SAFE | 0 | `radio-sdr` | — |
| 0 | LOW | SAFE | 0 | `rag-implementation` | — |
| 0 | LOW | SAFE | 0 | `rayden-code` | — |
| 0 | LOW | SAFE | 0 | `rayden-use` | — |
| 0 | LOW | SAFE | 0 | `react-component-performance` | — |
| 0 | LOW | CAUTION | 0 | `react-flow-architect` | — |
| 0 | LOW | CAUTION | 0 | `react-flow-node-ts` | — |
| 0 | LOW | CAUTION | 0 | `react-nextjs-development` | — |
| 0 | LOW | SAFE | 0 | `react-patterns` | — |
| 0 | LOW | CAUTION | 0 | `react-state-management` | — |
| 0 | LOW | SAFE | 0 | `react-ui-patterns` | — |
| 0 | LOW | SAFE | 0 | `read-all-adrs` | — |
| 0 | LOW | SAFE | 0 | `receiving-code-review` | — |
| 0 | LOW | SAFE | 0 | `recursive-context-pruning-token-budgeting` | — |
| 0 | LOW | SAFE | 0 | `reddit-automation` | — |
| 0 | LOW | CAUTION | 0 | `redesign-existing-projects` | — |
| 0 | LOW | CAUTION | 0 | `reference-builder` | — |
| 0 | LOW | SAFE | 0 | `referral-program` | — |
| 0 | LOW | CAUTION | 0 | `rehabilitation-analyzer` | — |
| 0 | LOW | SAFE | 0 | `render-automation` | — |
| 0 | LOW | CAUTION | 0 | `repo-maintainer` | — |
| 0 | LOW | SAFE | 0 | `research-prompt` | — |
| 0 | LOW | SAFE | 0 | `resolving-merge-conflicts` | — |
| 0 | LOW | SAFE | 0 | `resume-ats-review` | — |
| 0 | LOW | CAUTION | 0 | `reverse-engineer` | — |
| 0 | LOW | CAUTION | 0 | `review-and-simplify-changes` | — |
| 0 | LOW | SAFE | 0 | `review-multi-agent-orchestration` | — |
| 0 | LOW | CAUTION | 0 | `review-swarm` | — |
| 0 | LOW | SAFE | 0 | `riffkit` | — |
| 0 | LOW | CAUTION | 0 | `risk-manager` | — |
| 0 | LOW | SAFE | 0 | `risk-metrics-calculation` | — |
| 0 | LOW | CAUTION | 0 | `robius-event-action` | — |
| 0 | LOW | CAUTION | 0 | `robius-matrix-integration` | — |
| 0 | LOW | CAUTION | 0 | `robius-state-management` | — |
| 0 | LOW | CAUTION | 0 | `robius-widget-patterns` | — |
| 0 | LOW | CAUTION | 0 | `robot-framework-skill` | — |
| 0 | LOW | SAFE | 0 | `routerbase-model-gateway` | — |
| 0 | LOW | CAUTION | 0 | `ruby-pro` | — |
| 0 | LOW | SAFE | 0 | `run-deep-swe` | — |
| 0 | LOW | CAUTION | 0 | `runapi-cli` | — |
| 0 | LOW | CAUTION | 0 | `runaway-guard` | — |
| 0 | LOW | SAFE | 0 | `rust-pro` | — |
| 0 | LOW | CAUTION | 0 | `saas-multi-tenant` | — |
| 0 | LOW | CAUTION | 0 | `saga-orchestration` | — |
| 0 | LOW | CAUTION | 0 | `sales-automator` | — |
| 0 | LOW | CAUTION | 0 | `salesforce-automation` | — |
| 0 | LOW | SAFE | 0 | `sam-altman` | — |
| 0 | LOW | CAUTION | 1 | `sandbase-mcp` | SC2 |
| 0 | LOW | CAUTION | 0 | `sandbox-next` | — |
| 0 | LOW | SAFE | 0 | `sandbox-stable` | — |
| 0 | LOW | SAFE | 0 | `satori` | — |
| 0 | LOW | CAUTION | 0 | `scala-pro` | — |
| 0 | LOW | CAUTION | 0 | `scanpy` | — |
| 0 | LOW | SAFE | 0 | `scarcity-urgency-psychologist` | — |
| 0 | LOW | SAFE | 0 | `schema-markup` | — |
| 0 | LOW | CAUTION | 0 | `scikit-learn` | — |
| 0 | LOW | CAUTION | 0 | `screen-adverse-media` | — |
| 0 | LOW | SAFE | 0 | `screen-reader-testing` | — |
| 0 | LOW | CAUTION | 0 | `screenstudio-alt` | — |
| 0 | LOW | CAUTION | 0 | `scroll-experience` | — |
| 0 | LOW | CAUTION | 0 | `search-specialist` | — |
| 0 | LOW | SAFE | 0 | `security-audit` | — |
| 0 | LOW | CAUTION | 0 | `security-auditor` | — |
| 0 | LOW | CAUTION | 0 | `security-bluebook-builder` | — |
| 0 | LOW | SAFE | 0 | `security-requirement-extraction` | — |
| 0 | LOW | SAFE | 0 | `seek-and-analyze-video` | — |
| 0 | LOW | SAFE | 0 | `segment-automation` | — |
| 0 | LOW | CAUTION | 0 | `selenium-skill` | — |
| 0 | LOW | SAFE | 0 | `semgrep-rule-variant-creator` | — |
| 0 | LOW | SAFE | 0 | `sendgrid-automation` | — |
| 0 | LOW | CAUTION | 0 | `sentry-automation` | — |
| 0 | LOW | SAFE | 0 | `seo-audit` | — |
| 0 | LOW | CAUTION | 0 | `seo-authority-builder` | — |
| 0 | LOW | CAUTION | 0 | `seo-cannibalization-detector` | — |
| 0 | LOW | CAUTION | 0 | `seo-competitor-pages` | — |
| 0 | LOW | CAUTION | 0 | `seo-content` | — |
| 0 | LOW | CAUTION | 0 | `seo-content-auditor` | — |
| 0 | LOW | CAUTION | 0 | `seo-content-planner` | — |
| 0 | LOW | CAUTION | 0 | `seo-content-refresher` | — |
| 0 | LOW | CAUTION | 0 | `seo-content-writer` | — |
| 0 | LOW | CAUTION | 0 | `seo-dataforseo` | — |
| 0 | LOW | SAFE | 0 | `seo-drift` | — |
| 0 | LOW | SAFE | 0 | `seo-forensic-incident-response` | — |
| 0 | LOW | CAUTION | 0 | `seo-geo` | — |
| 0 | LOW | CAUTION | 0 | `seo-hreflang` | — |
| 0 | LOW | CAUTION | 0 | `seo-images` | — |
| 0 | LOW | CAUTION | 0 | `seo-keyword-strategist` | — |
| 0 | LOW | CAUTION | 0 | `seo-meta-optimizer` | — |
| 0 | LOW | SAFE | 0 | `seo-page` | — |
| 0 | LOW | CAUTION | 0 | `seo-plan` | — |
| 0 | LOW | SAFE | 0 | `seo-programmatic` | — |
| 0 | LOW | CAUTION | 0 | `seo-schema` | — |
| 0 | LOW | CAUTION | 0 | `seo-sitemap` | — |
| 0 | LOW | CAUTION | 0 | `seo-snippet-hunter` | — |
| 0 | LOW | CAUTION | 0 | `seo-structure-architect` | — |
| 0 | LOW | SAFE | 0 | `seo-technical` | — |
| 0 | LOW | SAFE | 0 | `sequence-psychologist` | — |
| 0 | LOW | CAUTION | 0 | `service-mesh-expert` | — |
| 0 | LOW | CAUTION | 0 | `service-mesh-observability` | — |
| 0 | LOW | SAFE | 0 | `setup-help` | — |
| 0 | LOW | CAUTION | 0 | `setup-matt-pocock-skills` | — |
| 0 | LOW | SAFE | 0 | `sexual-health-analyzer` | — |
| 0 | LOW | CAUTION | 0 | `shader-programming-glsl` | — |
| 0 | LOW | SAFE | 0 | `sharp-coder` | — |
| 0 | LOW | SAFE | 0 | `shopify-automation` | — |
| 0 | LOW | SAFE | 0 | `shopify-review-triage` | — |
| 0 | LOW | SAFE | 0 | `short` | — |
| 0 | LOW | SAFE | 0 | `signup-flow-cro` | — |
| 0 | LOW | SAFE | 0 | `similarity-search-patterns` | — |
| 0 | LOW | CAUTION | 0 | `simplify-code` | — |
| 0 | LOW | CAUTION | 0 | `site-architecture` | — |
| 0 | LOW | SAFE | 0 | `skill-improver` | — |
| 0 | LOW | SAFE | 0 | `skill-reviewer` | — |
| 0 | LOW | SAFE | 0 | `skill-router` | — |
| 0 | LOW | SAFE | 0 | `skill-seekers` | — |
| 0 | LOW | SAFE | 0 | `skin-health-analyzer` | — |
| 0 | LOW | CAUTION | 0 | `skyvern-browser-automation` | — |
| 0 | LOW | CAUTION | 0 | `sleep-analyzer` | — |
| 0 | LOW | CAUTION | 0 | `slo-implementation` | — |
| 0 | LOW | CAUTION | 0 | `snowflake-development` | — |
| 0 | LOW | SAFE | 0 | `social-content` | — |
| 0 | LOW | CAUTION | 0 | `social-metadata-hardening` | — |
| 0 | LOW | SAFE | 0 | `social-orchestrator` | — |
| 0 | LOW | SAFE | 0 | `social-post-writer-seo` | — |
| 0 | LOW | SAFE | 0 | `social-proof-architect` | — |
| 0 | LOW | CAUTION | 0 | `software-architecture` | — |
| 0 | LOW | SAFE | 0 | `solidity-security` | — |
| 0 | LOW | CAUTION | 0 | `spark-optimization` | — |
| 0 | LOW | CAUTION | 0 | `spec-kit` | — |
| 0 | LOW | CAUTION | 0 | `spec-to-code-compliance` | — |
| 0 | LOW | CAUTION | 0 | `speckit-updater` | — |
| 0 | LOW | SAFE | 0 | `sql-optimization-patterns` | — |
| 0 | LOW | CAUTION | 0 | `sql-sentinel` | — |
| 0 | LOW | SAFE | 0 | `square-automation` | — |
| 0 | LOW | CAUTION | 0 | `sred-project-organizer` | — |
| 0 | LOW | SAFE | 0 | `sred-work-summary` | — |
| 0 | LOW | CAUTION | 0 | `sshepherd` | — |
| 0 | LOW | CAUTION | 0 | `startup-analyst` | — |
| 0 | LOW | CAUTION | 0 | `startup-business-analyst-business-case` | — |
| 0 | LOW | CAUTION | 0 | `startup-business-analyst-financial-projections` | — |
| 0 | LOW | CAUTION | 0 | `startup-business-analyst-market-opportunity` | — |
| 0 | LOW | CAUTION | 0 | `startup-financial-modeling` | — |
| 0 | LOW | SAFE | 0 | `startup-metrics-framework` | — |
| 0 | LOW | CAUTION | 0 | `statsmodels` | — |
| 0 | LOW | SAFE | 0 | `steve-jobs` | — |
| 0 | LOW | CAUTION | 0 | `stitch-design-taste` | — |
| 0 | LOW | SAFE | 0 | `stitch-ui-design` | — |
| 0 | LOW | SAFE | 0 | `stride-analysis-patterns` | — |
| 0 | LOW | SAFE | 0 | `stripe-automation` | — |
| 0 | LOW | CAUTION | 0 | `stripe-integration` | — |
| 0 | LOW | CAUTION | 0 | `styleseed-design-review` | — |
| 0 | LOW | SAFE | 0 | `subject-line-psychologist` | — |
| 0 | LOW | CAUTION | 0 | `supabase-automation` | — |
| 0 | LOW | SAFE | 0 | `supabase-postgres-best-practices` | — |
| 0 | LOW | SAFE | 0 | `superpowers-lab` | — |
| 0 | LOW | CAUTION | 0 | `supply-chain-risk-auditor` | — |
| 0 | LOW | SAFE | 0 | `swift-concurrency-expert` | — |
| 0 | LOW | CAUTION | 0 | `swiftui-expert-skill` | — |
| 0 | LOW | CAUTION | 0 | `swiftui-liquid-glass` | — |
| 0 | LOW | SAFE | 0 | `swiftui-performance-audit` | — |
| 0 | LOW | SAFE | 0 | `swiftui-ui-patterns` | — |
| 0 | LOW | SAFE | 0 | `swiftui-view-refactor` | — |
| 0 | LOW | CAUTION | 0 | `sympy` | — |
| 0 | LOW | CAUTION | 0 | `systems-programming-rust-project` | — |
| 0 | LOW | CAUTION | 0 | `tailwind-patterns` | — |
| 0 | LOW | CAUTION | 0 | `taisly-social-media-posting` | — |
| 0 | LOW | CAUTION | 0 | `tanstack-query-expert` | — |
| 0 | LOW | CAUTION | 0 | `tcm-constitution-analyzer` | — |
| 0 | LOW | CAUTION | 0 | `tdd` | — |
| 0 | LOW | CAUTION | 0 | `tdd-orchestrator` | — |
| 0 | LOW | SAFE | 0 | `tdd-workflow` | — |
| 0 | LOW | CAUTION | 0 | `tdd-workflows` | — |
| 0 | LOW | CAUTION | 0 | `tdd-workflows-tdd-cycle` | — |
| 0 | LOW | SAFE | 0 | `tdd-workflows-tdd-red` | — |
| 0 | LOW | CAUTION | 0 | `tdd-workflows-tdd-refactor` | — |
| 0 | LOW | CAUTION | 0 | `teach` | — |
| 0 | LOW | CAUTION | 0 | `team-composition-analysis` | — |
| 0 | LOW | SAFE | 0 | `technical-change-tracker` | — |
| 0 | LOW | SAFE | 0 | `telegram-automation` | — |
| 0 | LOW | CAUTION | 0 | `temporal-golang-pro` | — |
| 0 | LOW | CAUTION | 0 | `temporal-python-pro` | — |
| 0 | LOW | CAUTION | 0 | `terraform-aws-modules` | — |
| 0 | LOW | SAFE | 0 | `terraform-infrastructure` | — |
| 0 | LOW | CAUTION | 0 | `terraform-module-library` | — |
| 0 | LOW | CAUTION | 0 | `terraform-skill` | — |
| 0 | LOW | SAFE | 0 | `terraform-specialist` | — |
| 0 | LOW | CAUTION | 0 | `test-automator` | — |
| 0 | LOW | CAUTION | 0 | `test-driven-development` | — |
| 0 | LOW | CAUTION | 0 | `test-fixing` | — |
| 0 | LOW | CAUTION | 0 | `test-framework-migration-skill` | — |
| 0 | LOW | CAUTION | 0 | `test-guard` | — |
| 0 | LOW | CAUTION | 0 | `testing-patterns` | — |
| 0 | LOW | SAFE | 0 | `testing-qa` | — |
| 0 | LOW | CAUTION | 0 | `testng-skill` | — |
| 0 | LOW | CAUTION | 0 | `the-honoured-one` | — |
| 0 | LOW | SAFE | 0 | `threat-hunting` | — |
| 0 | LOW | CAUTION | 0 | `threat-intelligence` | — |
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
| 0 | LOW | SAFE | 0 | `to-issues` | — |
| 0 | LOW | SAFE | 0 | `to-prd` | — |
| 0 | LOW | SAFE | 0 | `todoist-automation` | — |
| 0 | LOW | CAUTION | 0 | `tokenwise` | — |
| 0 | LOW | SAFE | 0 | `tool-design` | — |
| 0 | LOW | SAFE | 0 | `top-web-vulnerabilities` | — |
| 0 | LOW | SAFE | 0 | `trading-ledger` | — |
| 0 | LOW | CAUTION | 0 | `travel-health-analyzer` | — |
| 0 | LOW | SAFE | 0 | `travel-planner` | — |
| 0 | LOW | CAUTION | 0 | `tree-ring-memory` | — |
| 0 | LOW | SAFE | 0 | `trello-automation` | — |
| 0 | LOW | CAUTION | 0 | `triage` | — |
| 0 | LOW | CAUTION | 0 | `trl-training` | — |
| 0 | LOW | CAUTION | 0 | `trpc-fullstack` | — |
| 0 | LOW | SAFE | 0 | `trust-calibrator` | — |
| 0 | LOW | CAUTION | 0 | `tune-monitor` | — |
| 0 | LOW | CAUTION | 0 | `tutorial-engineer` | — |
| 0 | LOW | SAFE | 0 | `twilio-communications` | — |
| 0 | LOW | SAFE | 0 | `twitter-automation` | — |
| 0 | LOW | SAFE | 0 | `typescript-pro` | — |
| 0 | LOW | SAFE | 0 | `ui-a11y` | — |
| 0 | LOW | CAUTION | 0 | `ui-component` | — |
| 0 | LOW | SAFE | 0 | `ui-lint` | — |
| 0 | LOW | CAUTION | 0 | `ui-motion` | — |
| 0 | LOW | SAFE | 0 | `ui-page` | — |
| 0 | LOW | SAFE | 0 | `ui-pattern` | — |
| 0 | LOW | SAFE | 0 | `ui-review` | — |
| 0 | LOW | CAUTION | 0 | `ui-setup` | — |
| 0 | LOW | SAFE | 0 | `ui-skills` | — |
| 0 | LOW | CAUTION | 0 | `ui-tokens` | — |
| 0 | LOW | CAUTION | 0 | `ui-ux-designer` | — |
| 0 | LOW | CAUTION | 0 | `ui-visual-validator` | — |
| 0 | LOW | SAFE | 0 | `uncle-bob-craft` | — |
| 0 | LOW | CAUTION | 0 | `uniprot-database` | — |
| 0 | LOW | CAUTION | 0 | `unit-testing-test-generate` | — |
| 0 | LOW | SAFE | 0 | `unity-ai-game-creator` | — |
| 0 | LOW | CAUTION | 0 | `unity-developer` | — |
| 0 | LOW | SAFE | 0 | `unity-ecs-patterns` | — |
| 0 | LOW | SAFE | 0 | `unreal-engine-cpp-pro` | — |
| 0 | LOW | CAUTION | 0 | `unslop` | — |
| 0 | LOW | SAFE | 0 | `unslop-commit` | — |
| 0 | LOW | CAUTION | 0 | `unsloth-finetuning` | — |
| 0 | LOW | SAFE | 0 | `unsplash-integration` | — |
| 0 | LOW | CAUTION | 0 | `update-swiftui-apis` | — |
| 0 | LOW | SAFE | 0 | `upstash-ratelimit` | — |
| 0 | LOW | CAUTION | 0 | `upstash-redis` | — |
| 0 | LOW | CAUTION | 0 | `use-dom` | — |
| 0 | LOW | CAUTION | 0 | `using-n8n-mcp-skills` | — |
| 0 | LOW | CAUTION | 0 | `using-neon` | — |
| 0 | LOW | SAFE | 0 | `using-superpowers` | — |
| 0 | LOW | SAFE | 0 | `ux-audit` | — |
| 0 | LOW | SAFE | 0 | `ux-copy` | — |
| 0 | LOW | SAFE | 0 | `ux-feedback` | — |
| 0 | LOW | SAFE | 0 | `ux-flow` | — |
| 0 | LOW | SAFE | 0 | `ux-persuasion-engineer` | — |
| 0 | LOW | CAUTION | 0 | `variant-analysis` | — |
| 0 | LOW | SAFE | 0 | `varlock-claude-skill` | — |
| 0 | LOW | CAUTION | 0 | `vector-database-engineer` | — |
| 0 | LOW | SAFE | 0 | `vector-index-tuning` | — |
| 0 | LOW | CAUTION | 0 | `vercel-ai-sdk-expert` | — |
| 0 | LOW | CAUTION | 0 | `vercel-automation` | — |
| 0 | LOW | CAUTION | 0 | `vercel-react-view-transitions` | — |
| 0 | LOW | CAUTION | 0 | `verify-citations` | — |
| 0 | LOW | CAUTION | 0 | `verify-document` | — |
| 0 | LOW | SAFE | 0 | `vexor` | — |
| 0 | LOW | SAFE | 0 | `vexor-cli` | — |
| 0 | LOW | CAUTION | 0 | `vibe-code-auditor` | — |
| 0 | LOW | SAFE | 0 | `viboscope` | — |
| 0 | LOW | CAUTION | 0 | `video-content-extractor` | — |
| 0 | LOW | SAFE | 0 | `video-router` | — |
| 0 | LOW | CAUTION | 0 | `viral-generator-builder` | — |
| 0 | LOW | SAFE | 0 | `visual-emotion-engineer` | — |
| 0 | LOW | SAFE | 0 | `vizcom` | — |
| 0 | LOW | CAUTION | 0 | `voice-ai-development` | — |
| 0 | LOW | CAUTION | 0 | `vps-server-management` | — |
| 0 | LOW | SAFE | 0 | `warehouse` | — |
| 0 | LOW | SAFE | 0 | `warren-buffett` | — |
| 0 | LOW | SAFE | 0 | `web-design-guidelines` | — |
| 0 | LOW | CAUTION | 0 | `web-media-getter` | — |
| 0 | LOW | CAUTION | 0 | `web-perf` | — |
| 0 | LOW | SAFE | 0 | `web-project-brainstorming` | — |
| 0 | LOW | SAFE | 0 | `web-security-testing` | — |
| 0 | LOW | CAUTION | 0 | `webflow-automation` | — |
| 0 | LOW | SAFE | 0 | `wechat-official-account-strategist` | — |
| 0 | LOW | CAUTION | 0 | `weightloss-analyzer` | — |
| 0 | LOW | SAFE | 0 | `whatsapp-automation` | — |
| 0 | LOW | SAFE | 0 | `wifi-wireless` | — |
| 0 | LOW | SAFE | 0 | `wiki-architect` | — |
| 0 | LOW | CAUTION | 0 | `wiki-builder` | — |
| 0 | LOW | SAFE | 0 | `wiki-changelog` | — |
| 0 | LOW | SAFE | 0 | `wiki-page-writer` | — |
| 0 | LOW | CAUTION | 0 | `wiki-qa` | — |
| 0 | LOW | SAFE | 0 | `wiki-researcher` | — |
| 0 | LOW | CAUTION | 0 | `wiki-vitepress` | — |
| 0 | LOW | CAUTION | 0 | `windows-shell-reliability` | — |
| 0 | LOW | CAUTION | 0 | `wireshark-analysis` | — |
| 0 | LOW | CAUTION | 0 | `wjttc-builder` | — |
| 0 | LOW | CAUTION | 0 | `wjttc-tester` | — |
| 0 | LOW | CAUTION | 0 | `woo-guard` | — |
| 0 | LOW | CAUTION | 0 | `wordpress` | — |
| 0 | LOW | SAFE | 0 | `wordpress-centric-high-seo-optimized-blogwriting-skill` | — |
| 0 | LOW | CAUTION | 0 | `wordpress-plugin-development` | — |
| 0 | LOW | CAUTION | 0 | `wordpress-theme-development` | — |
| 0 | LOW | CAUTION | 0 | `wordpress-woocommerce-development` | — |
| 0 | LOW | CAUTION | 0 | `workflow-automation` | — |
| 0 | LOW | CAUTION | 0 | `workflow-orchestration-patterns` | — |
| 0 | LOW | SAFE | 0 | `workflow-patterns` | — |
| 0 | LOW | SAFE | 0 | `workorai` | — |
| 0 | LOW | CAUTION | 0 | `wrangler` | — |
| 0 | LOW | SAFE | 0 | `wrike-automation` | — |
| 0 | LOW | SAFE | 0 | `writing-great-skills` | — |
| 0 | LOW | CAUTION | 0 | `writing-plans` | — |
| 0 | LOW | SAFE | 0 | `x-article-publisher-skill` | — |
| 0 | LOW | SAFE | 0 | `xiaohongshu-content-strategist` | — |
| 0 | LOW | CAUTION | 0 | `yann-lecun` | — |
| 0 | LOW | SAFE | 0 | `yann-lecun-debate` | — |
| 0 | LOW | SAFE | 0 | `yann-lecun-filosofia` | — |
| 0 | LOW | CAUTION | 0 | `yann-lecun-tecnico` | — |
| 0 | LOW | SAFE | 0 | `yes-md` | — |
| 0 | LOW | SAFE | 0 | `youtube-automation` | — |
| 0 | LOW | SAFE | 0 | `youtube-seo-optimizer` | — |
| 0 | LOW | SAFE | 0 | `zapier-make-patterns` | — |
| 0 | LOW | SAFE | 0 | `zendesk-automation` | — |
| 0 | LOW | CAUTION | 0 | `zeroize-audit` | — |
| 0 | LOW | CAUTION | 0 | `zipai-optimizer` | — |
| 0 | LOW | CAUTION | 0 | `zod-validation-expert` | — |
| 0 | LOW | SAFE | 0 | `zoho-crm-automation` | — |
| 0 | LOW | SAFE | 0 | `zoom-automation` | — |
| 0 | LOW | CAUTION | 0 | `zustand-store-ts` | — |

## High / Critical skills

- `007` — score=100, severity=CRITICAL, max_issue=HIGH, rules=PE3×26, AR3×5, P1×4, P6×3, YR4×3
- `2slides-ppt-generator` — score=100, severity=CRITICAL, max_issue=CRITICAL, rules=TT3×7, PE3×6, E1×5, SC1×3, SC4×3
- `agents-generator` — score=100, severity=CRITICAL, max_issue=HIGH, rules=P9×13, RP1×7, AE1×2, AR2, MP3
- `apple-container` — score=100, severity=CRITICAL, max_issue=HIGH, rules=AE1×12, PE2×12, TM1×10, RA2×4, PE3×3
- `attack-chain` — score=100, severity=CRITICAL, max_issue=HIGH, rules=PE2×5, YR4×5, PE3×4, RA2×4, YR1×4
- `aws-penetration-testing` — score=100, severity=CRITICAL, max_issue=HIGH, rules=SSRF1×8, PE2×2, AE1, E5, EA2
- `claude-code-expert` — score=100, severity=CRITICAL, max_issue=HIGH, rules=AS1×7, EA5×5, PE2, SC2, TM1
- `cloud-penetration-testing` — score=100, severity=CRITICAL, max_issue=HIGH, rules=SSRF1×14, PE3×6, E5×3, PE2×3, SC2×2
- `cloudflare` — score=100, severity=CRITICAL, max_issue=HIGH, rules=E1×124, RP1×32, TM1×11, PE3×8, EA2×3
- `cloudflare-security-audit` — score=100, severity=CRITICAL, max_issue=HIGH, rules=TM3×4, EA2×2, AE1, P1, PE1
- `comfyui-gateway` — score=100, severity=CRITICAL, max_issue=HIGH, rules=PE3×22, RP1×14, E1×10, TM3×8, PE2×5
- `command-development` — score=100, severity=CRITICAL, max_issue=HIGH, rules=AS1×17, P2×6, TM1×6, AE1×4, RA2×3
- `competitor-analysis` — score=100, severity=CRITICAL, max_issue=HIGH, rules=AE1×9, TM1×3, AS1, LP1, TM2
- `computer-use-agents` — score=100, severity=CRITICAL, max_issue=HIGH, rules=EA2×17, RP1×3, TM1×3, AR1, E1
- `container-security-hardening` — score=100, severity=CRITICAL, max_issue=HIGH, rules=RP1×10, TM1×7, PE2×3, PE5×2, AR2
- `diary` — score=100, severity=CRITICAL, max_issue=HIGH, rules=AST4×2, EA2×2, TT2×2, AST7, E1
- `ecl-harness-engineer` — score=100, severity=CRITICAL, max_issue=HIGH, rules=RP1×8, PE3×7, TM1×6, AE1×5, EA2×2
- `environment-setup-guide` — score=100, severity=CRITICAL, max_issue=HIGH, rules=PE2×12, PE3×8, TM3×3, E1, RA2
- `ethical-hacking-methodology` — score=100, severity=CRITICAL, max_issue=CRITICAL, rules=YR4×3, PE3×2, PE2, YR1
- `expo-brownfield` — score=100, severity=CRITICAL, max_issue=HIGH, rules=RP1×21, RA2×3, TM1×3, AE1×2, P9×2
- `hig-patterns` — score=100, severity=CRITICAL, max_issue=HIGH, rules=EA2×3, AE1×2, RA2×2, AR2, EA3
- `hook-development` — score=100, severity=CRITICAL, max_issue=HIGH, rules=AE1×6, PE3×3, TM1×2, E1, LP3
- `hugging-face-jobs` — score=100, severity=CRITICAL, max_issue=HIGH, rules=E5×11, E1×4, PE1×4, AE1×2, EA2×2
- `hugging-face-model-trainer` — score=100, severity=CRITICAL, max_issue=HIGH, rules=PE2×9, AST4×4, E5×3, TM2×3, PE1×2
- `last30days` — score=100, severity=CRITICAL, max_issue=HIGH, rules=PE3×16, E1×4, PE2×3, RA2×2, EA4
- `linkedin-content-generator` — score=100, severity=CRITICAL, max_issue=HIGH, rules=AE1×3, MP3×3, LP3, P6, RA2
- `linux-privilege-escalation` — score=100, severity=CRITICAL, max_issue=CRITICAL, rules=PE2×24, PE3×8, TM2×2, YR1×2, YR4×2
- `llm-security` — score=100, severity=CRITICAL, max_issue=HIGH, rules=P2×5, P7×4, AR3×3, P1×3, YR4×3
- `loki-mode` — score=100, severity=CRITICAL, max_issue=HIGH, rules=TM1×27, EA2×19, SC1×19, RP1×14, RA1×12
- `lore` — score=100, severity=CRITICAL, max_issue=HIGH, rules=AE1×14, P2×8, AST4×6, P1×3, AR3×2
- `macos-spm-app-packaging` — score=100, severity=CRITICAL, max_issue=HIGH, rules=RA2×17, AE1×5, PE3×4, TM1×2, LP3
- `make-me-an-expert` — score=100, severity=CRITICAL, max_issue=HIGH, rules=AS3×4, RA2×4, AE1×3, AR2, AST4
- `manage-skills` — score=100, severity=CRITICAL, max_issue=HIGH, rules=AS3×11, AS1×3, TM1×2, AE1, RA2
- `mcp-builder` — score=100, severity=CRITICAL, max_issue=HIGH, rules=AE1×6, E1×2, SC1×2, SC4×2, EA1
- `metasploit-framework` — score=100, severity=CRITICAL, max_issue=CRITICAL, rules=YR4×2, P1, PE2, YR1
- `monte-carlo-push-ingestion` — score=100, severity=CRITICAL, max_issue=HIGH, rules=AST7×29, E1×13, AE1×3, PE3×2, LP3
- `network-101` — score=100, severity=CRITICAL, max_issue=HIGH, rules=PE2×34, TM2×4, TM1×2, YR4×2, RA2
- `notebooklm` — score=100, severity=CRITICAL, max_issue=HIGH, rules=AST4×8, AS3×4, EA2×2, PE3×2, RA2×2
- `pentest-tools` — score=100, severity=CRITICAL, max_issue=CRITICAL, rules=PE3×588, SSRF1×178, E1×144, P2×61, YR4×59
- `plugin-structure` — score=100, severity=CRITICAL, max_issue=HIGH, rules=AE1×4, AS3×2, PE3×2, RA1, RA2
- `privilege-escalation-methods` — score=100, severity=CRITICAL, max_issue=HIGH, rules=PE2×18, TM2×3, PE3×2, YR4×2, YR1
- `rclone-cli` — score=100, severity=CRITICAL, max_issue=HIGH, rules=PE3×94, PE2×70, P2×38, TM1×29, RA1×19
- `remote-gpu-trainer` — score=100, severity=CRITICAL, max_issue=HIGH, rules=RA2×40, PE3×26, PE2×14, AE1×10, AR2×3
- `reverse-engineering` — score=100, severity=CRITICAL, max_issue=HIGH, rules=RA1×20, AE1×7, YR1×7, PE2×6, PE3×5
- `senior-frontend` — score=100, severity=CRITICAL, max_issue=HIGH, rules=AE1×12, E1×6, PE3×2, LP3, OH1
- `shadcn` — score=100, severity=CRITICAL, max_issue=HIGH, rules=RP1×73, P9×10, AE1×2, EA2×2, RA1×2
- `sharp-edges` — score=100, severity=CRITICAL, max_issue=HIGH, rules=P1×2, AR2, EA2, EA4, RA1
- `skill-developer` — score=100, severity=CRITICAL, max_issue=HIGH, rules=RP1×16, TM3×8, AS1×6, P3, RA2
- `skill-installer` — score=100, severity=CRITICAL, max_issue=HIGH, rules=PE3×8, AS3×5, AST4, LP3, RA1
- `stability-ai` — score=100, severity=CRITICAL, max_issue=HIGH, rules=AE1×13, PE3×5, E1×2, P6×2, LP3
- `survey-generator` — score=100, severity=CRITICAL, max_issue=CRITICAL, rules=AE1×4, EA2×2, E1, LP1, TT3
- `telegram` — score=100, severity=CRITICAL, max_issue=CRITICAL, rules=E1×23, SC1×12, PE3×9, SC4×4, AE1×3
- `turnstile-spin` — score=100, severity=CRITICAL, max_issue=HIGH, rules=E1×21, AE1×12, EA2×4, P9×4, SC2×3
- `ui-ux-pro-max` — score=100, severity=CRITICAL, max_issue=HIGH, rules=E1×15, EA2×7, PE3×5, RP1×4, P6×3
- `varlock` — score=100, severity=CRITICAL, max_issue=HIGH, rules=PE3×12, AS3×2, E2×2, SC2×2, RA2
- `vercel-optimize` — score=100, severity=CRITICAL, max_issue=HIGH, rules=AE1×17, EA2×3, YR1×2, LP3, P6
- `vulnerability-scanner` — score=100, severity=CRITICAL, max_issue=HIGH, rules=PE3×3, AR3×2, TM3×2, AST4, EA4
- `whatsapp-cloud-api` — score=100, severity=CRITICAL, max_issue=CRITICAL, rules=PE3×17, SC1×11, AE1×10, SC4×6, E1×4
- `wordpress-penetration-testing` — score=100, severity=CRITICAL, max_issue=CRITICAL, rules=E1×2, YR2×2, YR4×2, P1, YR1
- `shopify-development` — score=99, severity=CRITICAL, max_issue=HIGH, rules=PE3×41, SC1×3, AE1×2, SSRF3×2, AST4
- `active-directory-attacks` — score=98, severity=CRITICAL, max_issue=HIGH, rules=TM1×2, YR1×2, YR4×2, EA2, PE2
- `feature-tracking` — score=98, severity=CRITICAL, max_issue=HIGH, rules=P1×2, AR3, RA1, YR4
- `android-dev` — score=96, severity=CRITICAL, max_issue=HIGH, rules=PE3×5, AE1×2, RP1×2, P2
- `hig-technologies` — score=95, severity=CRITICAL, max_issue=HIGH, rules=EA2×6, P6×3, AE1, MP3
- `hugging-face-paper-publisher` — score=94, severity=CRITICAL, max_issue=HIGH, rules=AE1×45, PE3×5, AE4, E5, LP3
- `security-and-hardening` — score=94, severity=CRITICAL, max_issue=HIGH, rules=PE3×5, EA1, P2, SSRF1, YR4
- `ssh-penetration-testing` — score=94, severity=CRITICAL, max_issue=HIGH, rules=PE3×9, E1, E3, PE2, YR1
- `file-path-traversal` — score=93, severity=CRITICAL, max_issue=CRITICAL, rules=PE3×35, E1, PE2, YR2
- `bash-defensive-patterns` — score=92, severity=CRITICAL, max_issue=HIGH, rules=AE1×2, EA2, RA2, TM1, TM2
- `readme` — score=92, severity=CRITICAL, max_issue=HIGH, rules=PE3×3, PE2×2, RP1×2, TM1×2, EA2
- `gcp-cloud-run` — score=90, severity=CRITICAL, max_issue=HIGH, rules=TM1×2, AR1, E1, PE2, RA2
- `bun-development` — score=89, severity=CRITICAL, max_issue=HIGH, rules=PE3×2, SC2×2, TM2×2, RP1
- `vibecode-production-qa-validator` — score=89, severity=CRITICAL, max_issue=HIGH, rules=RP1×9, SC2×2, TM2×2, PE3
- `web-scraper` — score=89, severity=CRITICAL, max_issue=HIGH, rules=AE1×2, AR1, EA2, PE1, SC2
- `devops-deploy` — score=88, severity=CRITICAL, max_issue=CRITICAL, rules=E1×2, EA2×2, TM1×2, YR1
- `super-code` — score=88, severity=CRITICAL, max_issue=HIGH, rules=AE1×4, TM1×3, EA2
- `gitops-workflow` — score=86, severity=CRITICAL, max_issue=HIGH, rules=PE3×3, EA2, PE2, SC2, TM2
- `claude-in-chrome-troubleshooting` — score=85, severity=CRITICAL, max_issue=HIGH, rules=AS1×3, TM1×3, RA2
- `effective-agent-skills` — score=85, severity=CRITICAL, max_issue=HIGH, rules=AE1×2, EA1, P1, YR4
- `mcp-integration` — score=85, severity=CRITICAL, max_issue=HIGH, rules=E1×13, EA1×2, PE3×2, AE1, P1
- `hugging-face-community-evals` — score=84, severity=CRITICAL, max_issue=HIGH, rules=AST4×5, AE1×4, E2, LP3
- `plugin-settings` — score=84, severity=CRITICAL, max_issue=HIGH, rules=AS1×2, AE1, PE2, PE3
- `postgresql-cli` — score=84, severity=CRITICAL, max_issue=HIGH, rules=P9×20, PE2×5, AE1, EA2, OH1
- `cicd-automation-workflow-automate` — score=83, severity=CRITICAL, max_issue=HIGH, rules=PE3×8, RP1×3, AE1×2, EA2
- `conductor-manage` — score=83, severity=CRITICAL, max_issue=HIGH, rules=RA2×3, AE1×2, TM1×2
- `writing-skills` — score=82, severity=CRITICAL, max_issue=HIGH, rules=RA1×8, AS3×3, AE1, RA2
- `distributed-debugging-debug-trace` — score=81, severity=CRITICAL, max_issue=HIGH, rules=AE1×2, AR3, P1, TM3
- `skill-audit` — score=80, severity=HIGH, max_issue=HIGH, rules=P1×2, PE3×2, YR4
- `mobile-design` — score=79, severity=HIGH, max_issue=HIGH, rules=PE3×10, LP3, MP2, MP3, RA2
- `pptx` — score=79, severity=HIGH, max_issue=HIGH, rules=AST4×5, PE2×2, AE1, AST7, LP3
- `pptx-official` — score=79, severity=HIGH, max_issue=HIGH, rules=AST4×5, PE2×2, AE1, AST7, LP3
- `firmware-pentest` — score=78, severity=HIGH, max_issue=HIGH, rules=PE2×29, TM2×4, YR4×3
- `skill-scanner` — score=78, severity=HIGH, max_issue=HIGH, rules=AE1, E1, EA2, P3, PE3
- `claude-api` — score=77, severity=HIGH, max_issue=HIGH, rules=E1×6, E4×3, P9×3, EA2×2, MP2
- `claude-delegate` — score=77, severity=HIGH, max_issue=HIGH, rules=EA2×2, AE1, EA5, PE3
- `gemini-deep-research` — score=77, severity=HIGH, max_issue=HIGH, rules=PE3×4, SC1×2, SC4×2, EA4, LP3
- `systematic-debugging` — score=77, severity=HIGH, max_issue=HIGH, rules=PE3×2, AE1, E4, EA4
- `agent-evaluation` — score=76, severity=HIGH, max_issue=HIGH, rules=P1×2, AE4, P6, YR4
- `telegram-bot-messaging` — score=76, severity=HIGH, max_issue=HIGH, rules=AE1×9, EA4, LP3, PE2, RA2
- `spline-3d-integration` — score=74, severity=HIGH, max_issue=HIGH, rules=AE1×3, P2×3
- `using-lwc` — score=74, severity=HIGH, max_issue=HIGH, rules=RA2×2, RP1×2, AE1, LP3, P1
- `lovable-cleanup` — score=73, severity=HIGH, max_issue=HIGH, rules=P2×3, PE3×2, YR4
- `audit-skills` — score=72, severity=HIGH, max_issue=HIGH, rules=TM1×3, RA2×2, SC2
- `marketing-plan` — score=72, severity=HIGH, max_issue=HIGH, rules=AE4×4, AR1, AS3, EA2, RA1
- `aider-delegate` — score=71, severity=HIGH, max_issue=HIGH, rules=EA2×4, TM1×2, AE1, EA3
- `yao-meta-skill` — score=71, severity=HIGH, max_issue=HIGH, rules=AE1×2, EA2×2, RA1
- `k6-load-testing` — score=70, severity=HIGH, max_issue=HIGH, rules=E1×12, PE3×6, PE2×5, TM2
- `pentest-commands` — score=70, severity=HIGH, max_issue=CRITICAL, rules=YR4×2, YR1
- `playwright-skill` — score=70, severity=HIGH, max_issue=HIGH, rules=RP1×13, AE1×4, EA3, LP3, SC1
- `redis-cli` — score=70, severity=HIGH, max_issue=HIGH, rules=AE1×2, PE2×2, PE3, RP1
- `skill-development` — score=70, severity=HIGH, max_issue=HIGH, rules=RA1×3, AE1, AS3
- `ai-studio-image` — score=69, severity=HIGH, max_issue=HIGH, rules=PE3×10, SC1×3, SC4×2, LP3, P6
- `neon-functions` — score=69, severity=HIGH, max_issue=HIGH, rules=AE1×2, P9, PE3, RP1
- `skill-creator` — score=69, severity=HIGH, max_issue=HIGH, rules=AS3×5, E3×3, RA2×2, LP3, RA1
- `ai-product` — score=68, severity=HIGH, max_issue=HIGH, rules=EA2, P1, P6, YR4
- `audio-transcriber` — score=68, severity=HIGH, max_issue=MEDIUM, rules=SC1×15, AST4×6, PE2×2, AS3, EA2
- `auth-implementation-patterns` — score=68, severity=HIGH, max_issue=HIGH, rules=PE3×3, AE1×2
- `frontend-observability` — score=68, severity=HIGH, max_issue=HIGH, rules=P9×3, AE1×2, MP2×2, RP1
- `go-rod-master` — score=68, severity=HIGH, max_issue=HIGH, rules=AE1×3, LP3, PE3
- `remotion-best-practices` — score=68, severity=HIGH, max_issue=HIGH, rules=RP1×12, AE1×3, E1, EA4
- `ad-creative` — score=67, severity=HIGH, max_issue=HIGH, rules=E1×3, RP1×3, AE1, AR2
- `drizzle-migration-conflict` — score=67, severity=HIGH, max_issue=HIGH, rules=AE1, AS3, LP3, P6, RA2
- `xlsx` — score=67, severity=HIGH, max_issue=HIGH, rules=AST4×3, AE1×2, LP3, P4
- `xlsx-official` — score=67, severity=HIGH, max_issue=HIGH, rules=AST4×3, AE1×2, LP3, P4
- `codex-delegate` — score=66, severity=HIGH, max_issue=HIGH, rules=EA5×2, AE1, EA2
- `find-complementary-founders` — score=66, severity=HIGH, max_issue=HIGH, rules=AE1×7, AE4, EA2, LP3
- `browser-testing-with-devtools` — score=65, severity=HIGH, max_issue=HIGH, rules=P1, RP1, YR1, YR4
- `docx` — score=65, severity=HIGH, max_issue=HIGH, rules=AST4×3, P2×3, PE2×3, LP3
- `docx-official` — score=65, severity=HIGH, max_issue=HIGH, rules=AST4×3, P2×3, PE2×3, LP3
- `fable-safe-prompt` — score=65, severity=HIGH, max_issue=HIGH, rules=AR3, P1, YR4
- `huggingface-tool-builder` — score=65, severity=HIGH, max_issue=CRITICAL, rules=LP3, TT3
- `videodb` — score=65, severity=HIGH, max_issue=HIGH, rules=LP1×2, PE3×2, RA2
- `scanning-tools` — score=64, severity=HIGH, max_issue=HIGH, rules=PE2×15, RP1×2, YR4×2, TM1
- `train-sentence-transformers` — score=64, severity=HIGH, max_issue=HIGH, rules=AE1×5, RA2×3, LP3
- `typescript-expert` — score=64, severity=HIGH, max_issue=HIGH, rules=RP1×14, TM1×2, AST4, LP3
- `webapp-testing` — score=64, severity=HIGH, max_issue=HIGH, rules=AST4×2, TM1×2, LP3
- `edr-bypass-re` — score=62, severity=HIGH, max_issue=HIGH, rules=AE1×5, YR1
- `frontend-architecture` — score=62, severity=HIGH, max_issue=HIGH, rules=AE1×2, RP1×2, EA2, P9
- `inventory-demand-planning` — score=62, severity=HIGH, max_issue=HIGH, rules=AE4×4, AR2×2, EA2, EA3, P9
- `linux-shell-scripting` — score=62, severity=HIGH, max_issue=HIGH, rules=PE2×4, RA2×4, PE3, TM1
- `skill-writer` — score=62, severity=HIGH, max_issue=HIGH, rules=RA1×3, AE1
- `agents-sdk` — score=61, severity=HIGH, max_issue=HIGH, rules=AE1×3, RP1×2, EA2
- `git-pr-review` — score=61, severity=HIGH, max_issue=HIGH, rules=P1, P6, YR4
- `n8n-agents` — score=61, severity=HIGH, max_issue=HIGH, rules=EA2×2, P6×2, AR1
- `api-security` — score=60, severity=HIGH, max_issue=HIGH, rules=PE3×3, SSRF1×2
- `skill-security-audit` — score=60, severity=HIGH, max_issue=HIGH, rules=AE1×2, RA1
- `wellally-tech` — score=60, severity=HIGH, max_issue=HIGH, rules=PE3×3, E1, P3
- `cloudflare-email-service` — score=59, severity=HIGH, max_issue=HIGH, rules=E1×9, RP1×7, AE1×2
- `agy-delegate` — score=58, severity=HIGH, max_issue=HIGH, rules=EA2×4, AE1×3
- `client-secret-exposure-audit` — score=58, severity=HIGH, max_issue=HIGH, rules=PE3×3, P2×2, E1
- `opencode-delegate` — score=58, severity=HIGH, max_issue=HIGH, rules=EA2×4, AE1×3
- `xss-html-injection` — score=58, severity=HIGH, max_issue=HIGH, rules=E1×2, P2×2, EA3, YR4
- `claimable-postgres` — score=57, severity=HIGH, max_issue=HIGH, rules=RP1×4, EA2×3, PE3×3, E1
- `dotnet-reverse` — score=57, severity=HIGH, max_issue=HIGH, rules=YR4×2, AS2, PE2
- `omp-delegate` — score=57, severity=HIGH, max_issue=HIGH, rules=AE1×3, EA2, RA2
- `security-compliance-compliance-check` — score=57, severity=HIGH, max_issue=HIGH, rules=AE1×2, YR4
- `cron-doctor` — score=56, severity=HIGH, max_issue=HIGH, rules=AE1×3, RA2×2
- `frontend-seo` — score=56, severity=HIGH, max_issue=HIGH, rules=OH1×2, AE1, RP1
- `weaviate-cookbooks` — score=56, severity=HIGH, max_issue=HIGH, rules=PE3×3, RP1×3, P9×2, PE2
- `wp-site-health-auditor` — score=56, severity=HIGH, max_issue=HIGH, rules=PE2×5, AE1×3
- `cursor-delegate` — score=55, severity=HIGH, max_issue=HIGH, rules=AE1×4, EA2×2
- `frontend-optimistic-mutations` — score=55, severity=HIGH, max_issue=HIGH, rules=AE1×2, P9×2, RP1
- `hig-inputs` — score=55, severity=HIGH, max_issue=HIGH, rules=AE1, EA2, P1
- `n8n-error-handling` — score=55, severity=HIGH, max_issue=HIGH, rules=AE1×2, PE3
- `ui-update` — score=55, severity=HIGH, max_issue=HIGH, rules=AS3×2, AS1, RA1
- `codebase-cleanup-deps-audit` — score=54, severity=HIGH, max_issue=HIGH, rules=AE1×2, E1×2, RP1
- `dependency-management-deps-audit` — score=54, severity=HIGH, max_issue=HIGH, rules=AE1×2, E1×2, RP1
- `monorepo-management` — score=54, severity=HIGH, max_issue=HIGH, rules=RP1×4, PE3, RA2, TM2
- `workers-best-practices` — score=54, severity=HIGH, max_issue=HIGH, rules=E1×12, AE1×3
- `turborepo-caching` — score=53, severity=HIGH, max_issue=HIGH, rules=RP1×4, PE3×2, TM2
- `cline-delegate` — score=52, severity=HIGH, max_issue=HIGH, rules=EA2×23, AE1×2
- `commandcode-delegate` — score=51, severity=HIGH, max_issue=HIGH, rules=AE1×3, EA2
