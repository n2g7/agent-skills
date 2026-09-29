---
disable-model-invocation: true
name: pre-mortem
description: "This skill should be used when the user asks to \"pre mortem\". Run a pre-mortem risk analysis on a PRD or launch plan."
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
# Pre-Mortem: Risk Analysis for Product Launch

## When to Use

This skill should be used when the user asks to "pre mortem".

## When NOT to Use

- Do not use this skill for implementation work, legal advice, or exploit development.
- Stop if the user's inputs are missing.

## Purpose

You are a veteran product manager conducting a pre-mortem analysis on the user's request. This skill imagines launch failure and works backward to identify real risks, distinguish them from perceived worries, and create action plans to mitigate launch-blocking issues.

## Context

A pre-mortem is a structured risk-identification exercise that forces teams to think critically about what could go wrong before launch, when there's still time to act. By assuming failure, we surface hidden concerns and separate legitimate threats from overblown worries.

## Instructions

1. **Gather the PRD**: If the user provides a PRD or product plan file, read it thoroughly. Understand the product, target market, key assumptions, and timeline. If relevant, use web search to research competitive landscape or market conditions.

2. **Think Step by Step**:
   - Imagine the product launches in 14 days
   - Now imagine it fails—customers don't adopt it, revenue targets miss, reputation takes a hit
   - What went wrong?
   - What did we miss or not execute well?
   - What were we overconfident about?

3. **Categorize Risks**: Classify each potential failure as one of three types:

   **Tigers**: Real problems you personally see that could derail the project
   - Based on evidence, past experience, or clear logic
   - Should keep you awake at night
   - Require action

   **Paper Tigers**: Problems others might worry about, but you don't believe in them
   - Valid concerns on the surface, but unlikely or overblown
   - Not worth significant resource investment
   - Worth documenting to align stakeholders

   **Elephants**: Something you're not sure is a problem, but the team isn't discussing it enough
   - Unspoken concerns or assumptions nobody is validating
   - Could be real; you're unsure
   - Deserve investigation before launch

4. **Classify Tigers by Urgency**:

   **Launch-Blocking**: Must be solved before launch
   - Example: Core feature broken, regulatory blocker, key customer dependency unmet

   **Fast-Follow**: Must be solved within 30 days post-launch
   - Example: Performance issues, secondary features incomplete

   **Track**: Monitor post-launch; solve if it becomes an issue
   - Example: Nice-to-have features, edge cases

5. **Create Action Plans**: For every Launch-Blocking Tiger:
   - Describe the risk clearly
   - Suggest a concrete mitigation action
   - Identify the best owner (function/person)
   - Set a decision/completion date

6. **Structure Output**: Present the analysis as:

   ```
   ## Pre-Mortem Analysis: [Product Name]

   ### Tigers (Real Risks)
   [List each real risk with category and mitigation plan]

   ### Paper Tigers (Overblown Concerns)
   [List each, explain why it's not a true risk]

   ### Elephants (Unspoken Worries)
   [List each, recommend investigation approach]

   ### Action Plans for Launch-Blocking Tigers
   [For each, include: Risk, Mitigation, Owner, Due Date]
   ```

7. **Save the Output**: Save as a markdown document: `PreMortem-[product-name]-[date].md`

## Notes

- Be honest and constructive—the goal is to improve launch readiness, not assign blame
- Default to "Tiger" if unsure; it's better to address risks early
- Involve cross-functional perspectives (engineering, design, go-to-market) in your analysis
- Revisit the pre-mortem 2-3 weeks before launch to verify mitigations are on track

---

### Further Reading

- [How Meta and Instagram Use Pre-Mortems to Avoid Post-Mortems](https://www.productcompass.pm/p/how-to-run-pre-mortem-template)
- [How to Manage Risks as a Product Manager](https://www.productcompass.pm/p/how-to-manage-risks-as-a-product-manager)

## Limitations

- This skill does not replace environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs are missing.

## Workflow

# pre-mortem -- Pre-Launch Risk Analysis

Imagine your launch has failed. Now work backward to figure out why. This command applies the Tigers/Paper Tigers/Elephants framework to surface real risks and create mitigation plans.

## Invocation

```
pre-mortem [paste or upload a PRD, launch plan, or feature spec]
pre-mortem We're launching a self-serve billing portal next month
```

## Workflow

### Step 1: Accept the Plan

Accept in any format: PRD, feature spec, launch plan, project brief, or verbal description. The more detail provided, the sharper the risk analysis.

### Step 2: Risk Identification

Apply the **pre-mortem** skill:

Imagine the product has launched and failed. Generate risks across categories:
- **Technical**: Performance, scalability, integration failures, data issues
- **User**: Adoption barriers, usability problems, unmet expectations
- **Business**: Revenue impact, competitive response, market timing
- **Operational**: Support load, documentation gaps, training needs
- **Dependencies**: Third-party services, cross-team handoffs, regulatory

### Step 3: Classify Risks

Categorize each risk:

**Tigers** — Real, substantive risks that could cause failure
- Assess severity: Launch-blocking / Fast-follow / Track
- For launch-blocking Tigers: immediate mitigation required
- For fast-follow Tigers: plan to address within first sprint post-launch
- For track Tigers: monitor but don't delay launch

**Paper Tigers** — Risks that feel scary but are overblown
- Explain why the concern is manageable
- Note what would need to change for this to become a real Tiger

**Elephants** — Unspoken risks the team knows about but avoids discussing
- Surface political, organizational, or uncomfortable risks
- Frame constructively with suggested conversation starters

### Step 4: Generate Pre-Mortem Report

```
## Pre-Mortem: [Feature/Launch]

**Date**: [today]
**Status**: [Draft / Reviewed]

### Risk Summary
- **Tigers**: [count] ([launch-blocking], [fast-follow], [track])
- **Paper Tigers**: [count]
- **Elephants**: [count]

### Launch-Blocking Tigers
| # | Risk | Likelihood | Impact | Mitigation | Owner | Deadline |
|---|------|-----------|--------|-----------|-------|----------|

### Fast-Follow Tigers
| # | Risk | Likelihood | Impact | Planned Response | Owner |
|---|------|-----------|--------|-----------------|-------|

### Track Tigers
[Risks to monitor post-launch with trigger conditions]

### Paper Tigers
[Concerns that seem big but are manageable — with reasoning]

### Elephants in the Room
[Uncomfortable truths the team should discuss]

### Go/No-Go Checklist
- [ ] All launch-blocking Tigers mitigated
- [ ] Fast-follow plan documented and assigned
- [ ] Monitoring in place for Track Tigers
- [ ] Rollback plan defined
- [ ] Support team briefed
```

Save as markdown.

### Step 5: Offer Next Steps

- "Want me to **update the PRD** with risk mitigations?"
- "Should I **create test scenarios** for the riskiest areas?"
- "Want me to **draft a launch checklist** from these findings?"

## Notes

- The best pre-mortems happen when the plan is 80% done — early enough to change course, late enough to have substance
- Push past the obvious risks — the most dangerous risks are the ones nobody mentions
- Elephants are the highest-value output — surfacing what the team avoids discussing
- For each Tiger, the mitigation should be specific and assignable, not "be careful"
- If the pre-mortem reveals too many launch-blocking Tigers, recommend delaying or phasing the launch
