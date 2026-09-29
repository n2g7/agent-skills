---
disable-model-invocation: true
name: business-model
description: "Generate a Business Model Canvas with all 9 building blocks. Use when creating a business model, documenting how a business creates value, or analyzing an existing business model."
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
# Business Model Canvas

## When to Use

This skill should be used when the user asks to "business model".

## When NOT to Use

- Use `osterwalder-canvas-architect` for an iterative 9-block Business Model Canvas.
- Do not use this skill for implementation work, legal advice, or exploit development.
- Stop if the user's inputs are missing.

## Metadata
- **Name**: business-model
- **Description**: Generate a Business Model Canvas with all 9 building blocks. Use when creating a business model, documenting how a business creates value, or analyzing an existing business model.
- **Triggers**: business model canvas, BMC, business model, how we make money

## Instructions

You are a business model strategist designing a Business Model Canvas for the user's request.

Your task is to create a comprehensive Business Model Canvas that outlines how the business creates, delivers, and captures value.

## Input Requirements
- Product or service description
- Target customer(s) and market
- Current business operations or assumptions
- Competitive context or industry dynamics

## Business Model Canvas Template

### Left Side: Creating Value

**1. Key Partners**
- Who are the key strategic partners and suppliers?
- What partnerships enable our business model?
- Which activities do partners handle?
- Are there joint ventures or co-creation opportunities?

**2. Key Activities**
- What key activities does the business perform?
- What processes are critical to delivering value?
- Are these activities in-house or outsourced?
- Production, problem-solving, platform/network activities?

**3. Key Resources**
- What resources are necessary to create value?
- Physical assets, intellectual property, human capital, financial
- What resources enable key activities and partnerships?
- What's the minimum viable resource set?

### Center: The Value Proposition

**4. Value Propositions**
- What value do we deliver to customers?
- Which customer problems do we solve?
- What needs are satisfied?
- What products/services address each segment?
- Quantitative (price, speed, quality) vs. qualitative (design, status)

### Right Side: Delivering Value

**5. Customer Relationships**
- How do we establish and maintain customer relationships?
- Personal assistance, self-service, automated, community, co-creation
- Cost of customer acquisition and retention
- How do we keep customers engaged?

**6. Channels**
- How do customers discover and access the value?
- Awareness: How do customers learn about us?
- Purchase: How do they buy?
- Delivery: How is value delivered?
- After-sales: How do we support customers?
- Direct vs. indirect, owned vs. partner channels

**7. Customer Segments**
- Who are the key customer segments?
- Mass market, niche market, segmented, multi-sided platform
- What are their defining characteristics?
- Distinct needs, channels, relationships, or profitability

### Bottom: Financial Viability

**8. Cost Structure**
- What are the most important costs?
- Fixed vs. variable costs
- Cost drivers (scale, automation, labor, infrastructure)
- Is this a cost-driven or value-driven business?

**9. Revenue Streams**
- How does the business make money?
- Per customer, per transaction, subscription, licensing, rents
- Pricing mechanisms (fixed, dynamic, value-based)
- Customer lifetime value and unit economics

## Output Process
1. Identify and profile customer segments
2. Define the core value proposition(s)
3. Map customer relationships and channels
4. List key activities and resources
5. Identify key partners
6. Outline cost structure
7. Define revenue streams
8. Ensure all 9 blocks align and support each other
9. Test economic viability (LTV > 3x CAC)
10. Identify key assumptions and risks

### Domain Context

**Business Model Canvas vs Lean Canvas vs Startup Canvas**:

Business Model Canvas (Strategyzer, Alexander Osterwalder) is the most widely used canvas framework. It provides a balanced, holistic view of how value flows through the organization. However, it has known limitations for product strategy:

- **No vision**: Why should your team wake up every day? BMC doesn't address motivation or aspiration.
- **No Can't/Won't test**: What stops competitors from copying you? BMC lacks a defensibility section that goes beyond listing resources.
- **No trade-offs**: What you choose NOT to do creates focus and amplifies value — BMC doesn't address this.
- **No key metrics**: How do you know the strategy is working? BMC has no metrics section.
- **Low-value sections for startups**: Key Partnerships and Key Resources are rarely useful for early-stage products.

**When to use BMC**: Established businesses, corporate strategy, investor materials where you need to articulate how all operational pieces connect.

**Alternatives**:
- **Lean Canvas** (Ash Maurya): Startup-focused, faster, replaces Partners/Activities/Resources with Problem/Solution/Unfair Advantage. Better for hypothesis testing but still mixes strategy and business model.
- **Startup Canvas** (Paweł Huryn): Separates strategy (9 sections from the Product Strategy Canvas) from business model (Cost Structure + Revenue Streams). Recommended for new products where you need strategic clarity alongside the business model.

## Notes
- The Business Model Canvas provides a holistic view of how value flows through the organization
- Each block should reinforce and support the others
- Strong business models have clear, defensible value propositions
- Financial sustainability requires revenue to exceed costs at scale
- Use this to identify opportunities for innovation and optimization

---

### Further Reading

- [Business Model Canvas Examples: Google Maps, Airbnb, Uber](https://www.productcompass.pm/p/business-model-canvas-examples)
- [Startup Canvas: Product Strategy and a Business Model for a New Product](https://www.productcompass.pm/p/startup-canvas)

## Limitations

- This skill does not replace environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs are missing.

## Workflow

# business-model -- Business Model Exploration

Build and analyze business models using four complementary frameworks. Choose one or run all for a complete picture.

## Invocation

```
business-model lean Marketplace connecting freelance PMs with startups
business-model full Enterprise analytics platform
business-model startup AI writing tool for non-native English speakers
business-model value-prop SaaS onboarding tool
business-model all SaaS onboarding tool        # runs all four
business-model                                   # asks what you need
```

## Modes

---

### Lean Canvas Mode

Best for: Early-stage ideas, startups, new product lines.

Apply the **lean-canvas** skill to produce a complete Lean Canvas:

```
## Lean Canvas: [Product]

| Problem (Top 3) | Solution | Unique Value Proposition |
|-----------------|----------|------------------------|
| 1. [problem]    | [solution to each] | [single clear message] |
| 2. [problem]    |          |                        |
| 3. [problem]    |          |                        |

| Key Metrics | Unfair Advantage |
|------------|-----------------|
| [what you measure] | [what can't be copied] |

| Channels | Customer Segments |
|---------|------------------|
| [how you reach them] | [who, early adopters first] |

| Cost Structure | Revenue Streams |
|---------------|----------------|
| [fixed + variable] | [how you make money] |

### Riskiest Assumptions
[What must be true for this to work — prioritized by risk]

### Experiments to Run
[How to validate the riskiest assumptions cheaply]
```

---

### Full Business Model Canvas Mode

Best for: Established products, strategic planning, investor materials.

Apply the **business-model** skill to produce all 9 building blocks:

```
## Business Model Canvas: [Product]

| Key Partners | Key Activities | Value Propositions | Customer Relationships | Customer Segments |
|-------------|---------------|-------------------|----------------------|------------------|
| [who helps you] | [core actions] | [why customers choose you] | [how you interact] | [who you serve] |

| Key Resources | | Channels | |
|-------------|---|---------|---|
| [what you need] | | [how you deliver] | |

| Cost Structure | Revenue Streams |
|---------------|----------------|
| [your costs] | [your revenue] |

### Analysis
[Strengths and weaknesses of this model]
[How the pieces reinforce each other]
[Vulnerabilities and dependencies]
```

---

### Startup Canvas Mode

Best for: New products and startups that need both strategy and business model in one artifact. Recommended over Lean Canvas and BMC for new products.

Apply the **startup-canvas** skill to produce a Startup Canvas with 9 strategy sections + business model:

```
## Startup Canvas: [Product]

### Part 1: Product Strategy

| Vision | Market Segments | Relative Costs |
|--------|----------------|---------------|
| [inspiring why] | [JTBD, first segment] | [low cost vs unique value] |

| Value Proposition | Trade-offs | Key Metrics |
|------------------|-----------|------------|
| [What before → How → What after → Alternatives] | [what you won't do] | [North Star + OMTM] |

| Growth | Capabilities | Can't/Won't |
|--------|-------------|------------|
| [PLG vs Sales-Led, channels] | [build vs partner] | [why competitors can't copy] |

### Part 2: Business Model

| Cost Structure | Revenue Streams |
|---------------|----------------|
| [fixed + variable, how they scale] | [pricing model, revenue per channel] |

### Strategy Coherence Check
[Do all elements reinforce each other?]

### Riskiest Assumptions
[What must be true — and how to test it]
```

---

### Value Proposition Mode

Best for: Refining messaging, understanding user value, product-market fit analysis.

Apply the **value-proposition** skill to produce a JTBD-framed value proposition:

```
## Value Proposition: [Product]

### For [Segment]:
1. **Who**: [target user profile]
2. **Why**: [the job they're trying to do]
3. **What Before**: [their current painful reality]
4. **How**: [your solution approach]
5. **What After**: [their improved reality]
6. **Alternatives**: [what they'd use without you, and why you're better]

### Value Proposition Statement
[One sentence: For [who] who [need], [product] is a [category] that [benefit]. Unlike [alternative], we [differentiator].]
```

---

### All Mode

Runs all four frameworks and adds a synthesis section comparing insights across frameworks.

## Workflow (All Modes)

### Step 1: Gather Context

Ask:
- What is the product or business idea?
- What stage? (idea, validated, scaling)
- Any existing business model to refine?
- Who is the target customer?

### Step 2: Generate the Selected Framework(s)

Apply the relevant skill(s) as described above.

### Step 3: Save and Iterate

Save as markdown. Offer:
- "Want me to **stress-test this model** with a SWOT or PESTLE analysis?"
- "Should I **design a pricing strategy** for the revenue streams?"
- "Want me to **build a strategy canvas** around this model?"
- "Should I **identify the beachhead segment**?"

## Notes

- **Startup Canvas** is the recommended starting point for new products — it separates strategy from business model and covers what BMC and Lean Canvas miss (vision, trade-offs, metrics, Can't/Won't)
- **Lean Canvas** is best for speed and hypothesis testing — don't overthink it, but be aware it mixes strategy and business model into one artifact
- **BMC** is better for mature businesses that need to articulate how everything connects, but lacks strategic sections (vision, trade-offs, metrics)
- **Value Proposition** is the sharpest tool for product-market fit conversations
- In "all" mode, highlight where frameworks agree (strong signal) and where they diverge (needs investigation)
