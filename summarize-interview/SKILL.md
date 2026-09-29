---
disable-model-invocation: true
name: summarize-interview
description: "This skill should be used when the user asks to \"summarize interview\". Summarize a customer interview transcript into a structured template with JTBD, satisfaction signals, and action items."
risk: none
source: community
source_repo: phuryn/pm-skills
source_type: community
license: MIT
license_source: "https://github.com/phuryn/pm-skills/blob/main/LICENSE"
author: "Pawel Huryn"
date_added: "2026-09-29"
catalog_category: "Product Management"
---
## When to Use

This skill should be used when the user asks to "summarize interview".

## When NOT to Use

- Do not use this skill for implementation work, legal advice, or exploit development.
- Stop if the user's inputs are missing.

## Summarize Customer Interview

Transform an interview transcript into a structured summary focused on Jobs to Be Done, satisfaction, and action items.

### Context

You are summarizing a customer interview for the product discovery of **the user's request**.

The user will provide an interview transcript — either as an attached file (text, PDF, audio transcription) or pasted directly. Read any attached files first.

### Instructions

1. **Read the full transcript** carefully before summarizing.

2. **Fill in the summary template** below. Use "-" if information is unavailable. Replace numeric values with qualitative descriptions if needed (e.g., "not satisfied").

3. **Use clear, simple language** — a primary school graduate should be able to understand the summary.

### Output Template

```
**Date**: [Date and time of the interview]
**Participants**: [Full names and roles]
**Background**: [Background information about the customer]

**Current Solution**: [What solution they currently use]

**What They Like About Current Solution**:
- [Job to be done, desired outcome, importance, and satisfaction level]

**Problems With Current Solution**:
- [Job to be done, desired outcome, importance, and satisfaction level]

**Key Insights**:
- [Unexpected findings or notable quotes]

**Action Items**:
- [Date, Owner, Action — e.g., "2025-01-15, Paweł Huryn, Follow up with customer about pricing"]
```

Save the summary as a markdown document in the user's workspace.

---

### Further Reading

- [User Interviews: The Ultimate Guide to Research Interviews](https://www.productcompass.pm/p/interviewing-customers-the-ultimate)
- [Continuous Product Discovery Masterclass (CPDM)](https://www.productcompass.pm/p/cpdm) (video course)

## Limitations

- This skill does not replace environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs are missing.
