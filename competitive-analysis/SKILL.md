---
disable-model-invocation: true
name: competitive-analysis
description: "This skill should be used when the user asks to \"competitive analysis\". Analyze the competitive landscape."
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
# competitive-analysis -- Competitive Landscape Analysis

## When to Use

This skill should be used when the user asks to "competitive analysis".

## When NOT to Use

- Do not use this skill for implementation work, legal advice, or exploit development.
- Stop if the user's inputs are missing.

Research and analyze your competitive landscape. Identifies direct and indirect competitors, maps positioning, and surfaces differentiation opportunities.

## Invocation

```
competitive-analysis AI-powered project management tools
competitive-analysis Our product vs Notion, Asana, and Monday.com
competitive-analysis [upload a competitor list or market brief]
```

## Workflow

### Step 1: Understand the Competitive Context

Ask:
- What is your product? What category does it compete in?
- Any specific competitors you want analyzed? Or should I identify them?
- What's the lens? (feature comparison, positioning, pricing, go-to-market)
- What will you use this analysis for? (strategy, sales enablement, investor pitch, product roadmap)

### Step 2: Identify Competitors

Apply the **pm-competitor-analysis** skill:

- Identify 5 direct competitors (same category, same buyer)
- Identify 2-3 indirect competitors (different approach, same job-to-be-done)
- Note emerging/disruptive players if relevant
- Use web research to gather current information

### Step 3: Analyze Each Competitor

For each competitor:
- **Positioning**: How they describe themselves, target audience, key messaging
- **Strengths**: What they do well, where they win
- **Weaknesses**: Where they fall short, common complaints
- **Pricing**: Model and price points (if public)
- **Market traction**: Funding, team size, customer base signals
- **Recent moves**: New features, partnerships, pivots

### Step 4: Generate Competitive Analysis

```
## Competitive Analysis: [Your Product/Market]

**Date**: [today]
**Analyzed**: [count] competitors

### Market Overview
[2-3 sentences on market dynamics, trends, and where it's heading]

### Competitive Landscape
| Competitor | Category | Target | Positioning | Strength | Weakness |
|-----------|----------|--------|------------|----------|----------|

### Feature Comparison Matrix
| Capability | Your Product | Competitor A | Competitor B | Competitor C |
|-----------|-------------|-------------|-------------|-------------|

### Positioning Map
[2x2 matrix showing competitive positioning on key dimensions]

### Differentiation Opportunities
1. **[Opportunity]** — [why it's defensible and valuable]
2. ...

### Competitive Threats
1. **[Threat]** — [what to watch for, recommended response]
2. ...

### Recommendations
- **Double down on**: [your unique advantages]
- **Close the gap on**: [table-stakes features you're missing]
- **Ignore**: [competitor moves that aren't worth responding to]
```

Save as markdown.

### Step 5: Offer Next Steps

- "Want me to **create a battlecard** for sales against a specific competitor?"
- "Should I **develop positioning** that differentiates from the top competitors?"
- "Want me to **identify feature gaps** to close and add to the roadmap?"

## Notes

- Web research is used for current competitor data — results are as fresh as available sources
- Distinguish between "table stakes" (must-have to compete) and "differentiators" (must-have to win)
- Don't just list features — analyze *why* competitors make the choices they make
- Pricing intelligence should note whether pricing is public, usage-based, or requires sales contact
- Update this analysis quarterly — competitive landscapes shift fast

## Limitations

- This skill does not replace environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs are missing.
