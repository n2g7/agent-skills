# Cleanup plan: keep the useful skill, strip injection and stealth

This is the follow-up to `llm-intent-review.md`. It is based on the **actual SkillSpector match text** in `_security/skillspector/per-skill/*.json`, not on rule counts alone.

Goal: keep the cool, working parts of these skills. Remove (1) prompt-injection / control-hijack, (2) “install me into the agent’s config dir” persistence that the job does not need, (3) silent high-agency extras. Do **not** delete educational security content, OOXML schemas, Apple HIG, or legitimate `.env` documentation.

## What the scanner got wrong (do not “fix” these)

Most Bucket C High/Critical hits are **false positives**. Blindly deleting flagged lines would gut good skills.

| Skill | What SkillSpector matched | Reality |
|-------|---------------------------|---------|
| `pptx` / `docx` (+ official copies) | `P2` on `<!-- ppt/slides/slide1.xml -->`; `RA2` inside ECMA/ISO **XSD schemas** | XML comments and schema types, not hidden agent instructions |
| `ui-ux-pro-max`, `hig-*` | `EA2` / `P1` / `AR2` in design CSVs and Apple HIG copy | Words like “ignore”, “always preserved”, “no warning” in UX prose |
| `mobile-design` | `PE3` on Keychain / SecureStore | Correct mobile security advice |
| `readme` | `PE3` on `.env.example` | A README skill is supposed to document env files |
| `senior-frontend` | `PE3` in a generated `.gitignore` | Ignoring `.env` is correct |
| `turborepo-caching` | `PE3` on `"globalDependencies": [".env"]` | Valid Turbo config |
| `ai-product`, `git-pr-review`, `sharp-edges` | `P1`/`P6` quoting “ignore previous instructions” | Teaching/defending **against** injection |
| `007`, `vulnerability-scanner` | Attack strings / `debug=True` regexes | Bucket A: that *is* the syllabus |
| `distributed-debugging-debug-trace` | `AR3` on “Avoid enabling verbose tracing” | Safety warning, not a jailbreak |
| `gcp-cloud-run` | `AR1` on `Always respond` in a **health check** | HTTP 200 handler |
| `lovable-cleanup` | `P2` on `<!-- security-allowlist: grep, read-only -->` | Author trying to *document* safe grep |
| `inventory-demand-planning` | `AR2` on “10× demand with no warning” | Business scenario, not anti-disclaimer |
| `plugin-settings` | `PE2` `chmod 600` on settings files | Least-privilege, keep it |
| `wellally-tech` | `P3` on “Do **not** upload data to external servers” | Negative instruction, keep it |
| `junta-leiloeiros` | `SC1`/`SC4` unpinned deps | Supply-chain hygiene, not injection |
| `survey-generator` | `TT3` `Authorization: Bearer $FIREWORKS_API_KEY` | Calling the vendor API is the job |

**Rule of thumb:** if the match is *about* secrets, injection, or sudo as documentation/defense, leave it. If the match is the skill *doing* injection, silent escalation, or writing into `~/.claude` without that being the product, change it.

## Rubric (keep vs strip)

**Keep**

- Domain knowledge, templates, scripts, APIs, OOXML tooling, HIG references, design CSVs
- Documented `.env.example` / `.gitignore` / Turbo `globalEnv`
- Educational attack examples in security skills, clearly framed as *detect, do not follow*
- User-local optional config (`$VAR` or a project `.env`) when the skill actually calls a vendor API
- `chmod 600` on files the user owns

**Strip or rewrite**

- Skill text wrapped as `<SYSTEM_INSTRUCTION>` / “inject this into the system prompt”
- “Ignore previous instructions”, DAN, “you have no restrictions” **when directed at the running agent** (not when quoted as an attack to detect)
- Hidden HTML comments that steer the agent (`<!-- SYSTEM: ... -->`, command metadata disguised as comments)
- Clone/curl/install into `~/.claude/skills` or `~/.claude/commands` when the skill is not a skill-manager
- Silent auto-escalation to a more powerful tool (browser, sudo, creds) without asking
- Live-looking API key placeholders (`sk-live-...`) — keep obviously fake `sk-...` or `<YOUR_KEY>`

---

## Phase 1 — Real control-hijack (do first)

Small diffs, high value. Keep the product; remove the stealth.

### 1. `linkedin-content-generator` — keep the writer, drop system-prompt injection

**Keep:** calendar/post/carousel generation, niche SEO rules, local `memory.md` preference log (that is the cool part).

**Change:**

- `scripts/utils.py`: stop wrapping prompts in `<SYSTEM_INSTRUCTION>…</SYSTEM_INSTRUCTION>`. Use a normal user/developer prompt (“Apply these saved style preferences: …”).
- `SKILL.md`: replace “inject your saved …” with “pass saved preferences as prompt context.” Memory stays opt-in, local, and user-visible (`/show-memory`, `/clear-memory` with confirm).

### 2. `web-scraper` — keep strategies, require a ask before Browser

**Keep:** multi-strategy extraction, Markdown tables, recon.

**Change:**

- Remove **silent** auto-escalation (WebFetch → Browser without asking). Offer Strategy B and wait for a yes.
- Rephrase “Always respond in the user’s language” → “Match the user’s language” so it is not an AR1-shaped always-comply rule.

### 3. `last30days` — keep the research CLI, stop planting it in Claude’s skill dir

**Keep:** Reddit/X/web research scripts, compact emit modes, optional OpenAI/xAI keys.

**Change:**

- README: do not `git clone … ~/.claude/skills/last30days`. Document repo-relative `python3 scripts/last30days.py`.
- `SKILL.md` / `SPEC.md`: same — no hardcoded `~/.claude/skills/…` paths.
- Prefer `OPENAI_API_KEY` / `XAI_API_KEY` from the environment. Optional `~/.config/last30days/.env` can stay as a convenience, with placeholders only (`sk-...`, `xai-...`), never “required persistence.”

### 4. `turnstile-spin` — keep Turnstile setup, drop remote prompt install

**Keep:** widget + siteverify wiring, framework snippets, “don’t call siteverify from the browser.”

**Change:** README should not `curl` a hosted prompt into `.claude/skills/turnstile-spin/SKILL.md`. Point at this repo path (or Cloudflare docs) instead. That curl is a supply-chain footgun (SC2) and agent-dir persistence (AS3).

---

## Phase 2 — Injection-shaped comments (easy, no feature loss)

HTML/`<!-- -->` comments are how `P2` fires. Replace agent-facing HTML comments with Markdown. **Do not edit OOXML XSD schema files.**

| Skill | Action |
|-------|--------|
| `lovable-cleanup` | `<!-- security-allowlist: … -->` → a Markdown note above the grep. Keep the greps. |
| `command-development` | Docs in `references/documentation-patterns.md` and `marketplace-considerations.md`: HTML comments that look like hidden commands → Markdown headings / blockquotes. Keep slash-command guidance. `AS1` hits on `.claude/commands/` stay — that **is** the skill’s job. |
| `pptx` / `pptx-official` / `docx` / `docx-official` | Only in **human docs** (`ooxml.md`): prefer headings over `<!-- slide1.xml -->`. Leave `ooxml/schemas/**` untouched. |

---

## Phase 3 — Soften always-comply wording (optional, low risk)

No behavior change except tone.

| Skill | Match | Rewrite to |
|-------|--------|------------|
| `computer-use-agents` | “Always respond with ONLY a JSON action object” | “Return a single JSON action object (no extra prose)” |
| `web-scraper` | covered in Phase 1 | |

Leave `gcp-cloud-run` health-check “Always respond” — it is not agent jailbreak.

---

## Phase 4 — Explicitly out of scope (do not gut)

- Bucket **A** pentest/exploit skills (`metasploit-framework`, `linux-privilege-escalation`, …). Optional later: a one-line authorized-use warning where missing.
- `007` attack catalogs — keep; they are labeled as injection **test cases**. If we touch them, only add “examples to detect, never execute.”
- Design/HIG/frontend/readme/turbo/mobile-secure-storage documentation.
- `survey-generator` Fireworks calls, `junta-leiloeiros` scraping (pin `requirements.txt` separately if we want a hygiene PR).

---

## Phase 5 — Verify

For each touched skill, not the whole 1636:

```bash
export PATH="$HOME/.local/bin:$PATH"
# per-skill re-scan (wrapper already supports --limit; or call skillspector on one dir)
skillspector scan <skill-dir> --no-llm --format json --output /tmp/recheck.json
```

Pass bar:

- `P1`/`P2`/`P6`/`AR1`/`AR3`/`MP3` gone **or** clearly educational/false-positive as in Phase 4
- No new clone/curl into `~/.claude/skills` except skill-manager skills
- Skill still does its job (LinkedIn calendar still generates; last30days still researches; Turnstile still documents siteverify)

Then a focused `scripts/scan-skillspector.sh static --limit …` is **not** enough (limit is first-N alpha). Re-scan the edited directories only.

---

## Suggested order of work

1. Phase 1 (4 skills) — one commit per skill, easy to revert.
2. Phase 2 comments — one commit.
3. Phase 3 wording — one commit if we still care about AR1 noise.
4. Re-scan edited dirs; update `llm-intent-review.md` notes if a skill drops out of High/Critical for the right reasons.
5. Leave Bucket A and HIG/CSV false positives alone unless a later pass wants authorized-use banners only.

## Success looks like

Agents still get a good LinkedIn writer, 30-day researcher, PPTX/DOCX pipeline, Turnstile guide, and scraper. They do **not** get system-prompt wrappers, silent browser escalation, or “curl this into `~/.claude/skills`.” SkillSpector scores may stay HIGH on pptx/HIG because of schemas and UX prose; that is acceptable. The cleanup is about **intent**, not chasing a green scoreboard.
