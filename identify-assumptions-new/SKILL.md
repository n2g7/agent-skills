---
disable-model-invocation: true
name: identify-assumptions-new
description: "This skill should be used when the user asks to \"identify assumptions new\". Identify risky assumptions for a new product idea across 8 risk categories including Go-to-Market, Strategy, and Team."
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

This skill should be used when the user asks to "identify assumptions new".

## When NOT to Use

- Do not use this skill for implementation work, legal advice, or exploit development.
- Stop if the user's inputs are missing.

## Identify Assumptions (New Product)

Comprehensive risk identification across 8 categories — extending the 4 core product risks (Teresa Torres, *Continuous Discovery Habits*) with Ethics, Go-to-Market, Strategy & Objectives, and Team risks that are critical for new products.

### Context

You are evaluating assumptions for a new product: **the user's request**.

If the user provides files (business plans, research), read them first.

### Domain Context

**The 4 core product risks** (Teresa Torres, *Continuous Discovery Habits*): Value, Usability, Viability, Feasibility.

**For new products, extend to 8 risk categories.** Good teams assume at least three-quarters of their ideas won't perform as they hope.

### Instructions

The user will describe the product concept, target segment, and feature idea. Work through these steps:

1. **Think from three perspectives** about why this product might fail:
   - **Product Manager**: Market demand, willingness to pay, competitive landscape
   - **Designer**: First-time user experience, onboarding, engagement
   - **Engineer**: Build vs. buy decisions, scalability, technical debt

2. **Identify assumptions across 8 risk categories**:

   - **Value**: Will it create value for customers? Will they keep using it?
   - **Usability**: Will people figure out how to use it? Can we onboard them fast enough? Will it increase cognitive load?
   - **Viability**: Can we sell/monetize/finance it? Is it worth the cost? Can we support customers and help them succeed? Can we scale? Will it be compliant?
   - **Feasibility**: Can we do it with the current technology? Is this integration possible? Can it be efficient? Can we scale it?
   - **Ethics**: Should we do it at all? Are there any ethical considerations? Will it pose a risk for our customers?
   - **Go-to-Market** (especially critical for new products): Can we market it? Do we have the required channels? Can we convince customers to try it? Is this the right messaging for this channel? Is this the right time? Is this the right way to launch it?
   - **Strategy & Objectives**: What are our assumptions? Can others copy our strategy? Have we considered political, economic, legal, technological, and environmental factors? Are those the best problems to solve?
   - **Team**: How well will the team work together? Do we have the right people? Do we have the right tools? Will the entire team stay with us long enough?

3. **For each assumption**, rate confidence and suggest a test.

Think step by step. Save as markdown.

---

### Further Reading

- [Assumption Prioritization Canvas: How to Identify And Test The Right Assumptions](https://www.productcompass.pm/p/assumption-prioritization-canvas)
- [What Is Product Discovery? The Ultimate Guide Step-by-Step](https://www.productcompass.pm/p/what-exactly-is-product-discovery)
- [Continuous Product Discovery Masterclass (CPDM)](https://www.productcompass.pm/p/cpdm) (video course)

## Limitations

- This skill does not replace environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs are missing.
