---
description: Attribution for the spec-kit Plan Mode skill. Distilled from GitHub Spec Kit (MIT).
metadata:
  tags: [source, attribution, spec-kit]
  source: github-spec-kit
---

# Source

Plan Mode adaptation of [GitHub Spec Kit](https://github.com/github/spec-kit) Spec-Driven Development.

- Upstream: https://github.com/github/spec-kit
- Docs: https://github.github.io/spec-kit/
- License: MIT (github/spec-kit)
- Official Cursor integration: `specify init --integration cursor-agent` (per-project `.cursor/skills/speckit-*/SKILL.md` + `.specify/`)

This library skill distills specify → clarify → plan → tasks → analyze for Cursor Plan Mode. It is **not** a wrapper around `specify-cli` and does **not** copy the official command prompts or extension-hook machinery.

Templates and quality rules follow Spec Kit's published outlines:

- `templates/spec-template.md`
- `templates/plan-template.md`
- `templates/tasks-template.md`
- Agentic SDD command order in Spec Kit docs

`disable-model-invocation: true` is added by this repo's lazy-load policy.
