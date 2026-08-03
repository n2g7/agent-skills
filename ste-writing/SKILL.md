---
disable-model-invocation: true
name: ste-writing
description: Rewrite prose (docs, READMEs, PR descriptions, error messages, release notes, comments — never code) into ASD-STE100 Simplified Technical English to remove "AI slop". Use when asked to make writing not sound like AI, make docs clear or plain, enforce a controlled writing style, write technical documentation that reads human, or explain technical information in STE. Two modes — strict (procedures/safety) and STE-flavored (general prose).
category: writing
risk: safe
source: local
date_added: "2026-08-03"
---

# ste-writing

Write prose in ASD-STE100 Simplified Technical English. This applies to documentation, READMEs, pull-request text, error messages, release notes, and comments. It does not apply to code, identifiers, or command syntax. It is not for marketing copy, essays, or anything that needs a voice — STE strips voice on purpose.

Aligned with ASD-STE100 Issue 9 (2025-01-15). Do not copy the copyrighted Part 2 dictionary into outputs or files. For strict dictionary checks, consult the user's local PDF if available (for example `~/Downloads/ASD-STE100_ISSUE9.pdf`).

## Agent workflow

1. **Scope** — Prose only. Never rewrite code, identifiers, CLI flags, or command syntax. Not for marketing voice or essays.
2. **Pick mode**
   - **strict** — procedures, runbooks, safety text, error messages: apply every rule and both length caps (20 words instruction, 25 words descriptive).
   - **STE-flavored** (default for explanations, READMEs, PR text, general docs) — apply sentence, paragraph, active-voice, and no-phrasal-verb discipline; relax the ~900-word dictionary lockdown so the text keeps enough range to read naturally.
3. **Rewrite or explain**
   - If source text is given → rewrite it in STE.
   - If the user asks to explain a concept or system → write a clear STE explanation (short paragraphs, one topic each; numbered steps when procedural).
4. **House rules** — No semicolons. No em dashes. American spelling. Write only the requested text. No preamble, no summary, no closing remarks.
5. **Self-lint** — Run the checklist below before returning. Optionally run `scripts/ste_lint.py` on the draft for mechanical fails (`--mode strict|flavored`, `--json` for counts).

Load on demand:

- [references/ste-rule-index.md](references/ste-rule-index.md) — Part 1 rule map
- [references/word-swaps.md](references/word-swaps.md) — common slop → STE swaps
- [references/examples.md](references/examples.md) — before/after samples

## Rules

WORDS
- Use one name for one thing. Do not call the same item by two different names.
- Use the short common word: start (not begin/commence/initiate), use (not utilize/leverage), help (not facilitate), make sure (not ensure), before (not prior to), after (not subsequent to), about (not regarding/concerning), get (not obtain/acquire), show (not demonstrate), also (not additionally/furthermore/moreover).
- Give each word one meaning. "fall" means to move down, not to decrease.
- No marketing adjectives: seamless, robust, powerful, cutting-edge, effortless, world-class, next-generation, revolutionary.
- American spelling.

VERBS
- Active voice. "the parser reads the file", not "the file is read by the parser".
- Use a verb for an action. "analyze the log", not "perform an analysis of the log".
- No stacked auxiliaries. Not "it is important to note that this may help to improve". Write "this improves X".
- No "-ing" main verb where a simple tense works.

SENTENCES
- One instruction per sentence. Max 20 words (instruction), max 25 (descriptive).
- No contractions. Use articles: a, an, the, this, these.

PUNCTUATION
- No semicolons. Write two sentences.
- No em dashes.

STRUCTURE
- One topic per paragraph, max six sentences. For steps, use a numbered vertical list, one action per item, imperative form. Put a condition before its command.

Write only the requested text. No preamble, no summary, no closing remarks.

## Modes

- **strict** — procedures, runbooks, safety text, error messages: apply every rule and both length caps.
- **STE-flavored** — general prose (READMEs, PR descriptions, docs): apply the sentence, paragraph, active-voice, and no-phrasal-verb discipline; relax the ~900-word dictionary lockdown so the text keeps enough range to read naturally.

## Self-lint (run before returning text)

1. Any sentence over 20 words? Split it. (Descriptive in STE-flavored / descriptive writing: max 25.)
2. Any semicolon? Replace with a period.
3. Any em dash? Replace with a period or rephrase.
4. Any contraction? Expand it.
5. Any passive voice with a known actor? Make it active.
6. Any "-ing" main verb, nominalization ("perform an analysis"), or phrasal verb ("spin up")? Replace with a plain verb.
7. Same thing named two ways? Pick one name.

The mechanical rules above are lintable and are what removes slop. Full STE also needs human judgment (the right technical noun, whether a sentence "makes good sense") — a checker cannot certify that, and slop is not about that. This skill fixes the FORM of slop. It cannot make a hollow paragraph true.
