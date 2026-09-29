---
disable-model-invocation: true
name: value-proposition
description: "This skill should be used when the user asks to \"value proposition\". Design a detailed value proposition using a 6-part JTBD template."
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
# Value Proposition

## When to Use

This skill should be used when the user asks to "value proposition".

## When NOT to Use

- Do not use this skill for implementation work, legal advice, or exploit development.
- Stop if the user's inputs are missing.

## Metadata
- **Name**: value-proposition
- **Description**: Generate a detailed value proposition using a 6-part template with JTBD framing. Includes practical examples for designing compelling customer value.
- **Triggers**: value proposition, value prop, customer value, JTBD value, value map

## Instructions

You are a product strategist designing a clear value proposition for the user's request.

Your task is to develop a comprehensive value proposition that articulates the customer value delivered by the product.

## Input Requirements
- Product description and features
- Target customer segment and their problems
- Competitive alternatives and current solutions
- Customer insights or market data

## Value Proposition Template

### 6-Part Structure

**1. Who**
- Who is this value proposition for?
- What customer segment are we addressing?
- What are their characteristics and constraints?

**2. Why (Problem)**
- What is the customer's core problem or need?
- What's the Job to Be Done (JTBD)?
- What desired outcomes are they trying to achieve?

**3. What Before**
- What is the customer's current situation?
- What are they using today to solve this problem?
- What friction or pain exists in the current approach?

**4. How (Solution)**
- How does the product solve the problem?
- What specific features or capabilities deliver value?
- Why is this solution better than alternatives?

**5. What After**
- What is the improved outcome or future state?
- How does the customer's life/work change?
- What becomes possible that wasn't before?

**6. Alternatives**
- What other solutions could customers use?
- Why would they choose us instead?
- What's the switching cost or friction from alternatives?

## Example: Canva
- **Who**: Non-designers who need to create marketing graphics
- **Why**: They need professional-looking designs but can't hire designers or use complex tools
- **What Before**: Using PowerPoint, Photoshop (too complex), or hiring expensive designers
- **How**: Drag-and-drop templates, built-in design elements, AI design assistance, intuitive interface
- **What After**: Create professional designs in minutes, launch campaigns faster, save design costs
- **Alternatives**: Photoshop (complex), Fiverr (slow, expensive), Canva competitors (fewer templates, harder UX)

## Output Process
1. Identify and profile the target customer segment
2. Define the core problem and JTBD
3. Describe the current state and friction points
4. Articulate how the product solves the problem
5. Envision the improved outcome
6. Compare against competitive alternatives
7. Create a concise value prop statement (1-2 sentences)
8. Develop a positioning statement for marketing use

### Domain Context

**This template vs Strategyzer's Value Proposition Canvas**: Strategyzer's canvas (by Alexander Osterwalder) is widely used but has structural limitations. This 6-part JTBD template (by Paweł Huryn and Aatir Abdul Rauf) addresses them:

- **Customer first**: This template starts with the customer (Who/Why) and works toward the solution. Strategyzer's canvas places the product on the left, which often leads teams to start with their solution rather than the customer's problem.
- **One segment at a time**: This template is designed for one segment per pass. Strategyzer's canvas encourages mapping multiple products/services simultaneously, which dilutes focus.
- **Explicit alternatives**: Section 6 (Alternatives) forces you to name what customers would use without you and articulate why you're better. Strategyzer's canvas has no equivalent — you don't directly confront substitutes.
- **Simpler structure**: "What before → How → What after" is easier to fill out than separating Customer Jobs, Pains, and Gains on one side and Pain Relievers, Gain Creators, and Products on the other. The separation often creates confusion about where things go.
- **Actionable output**: The final Value Proposition Statement is ready for marketing, sales, and onboarding. Strategyzer's canvas doesn't produce a reusable statement.

Use Strategyzer's Value Proposition Canvas when you need a detailed pains/gains decomposition for a mature product with complex customer needs. Use this 6-part template for clarity, speed, and actionable output.

## Notes
- Jobs to Be Done (JTBD) framework focuses on the progress the customer is trying to make, not demographics
- Value propositions are segment-specific; you may have different value props for different customer groups
- The stronger your value prop, the easier marketing, sales, and product decisions become
- Test value props with real customers before finalizing
- Use a **Value Curve** (Blue Ocean Strategy) to visually compare your offering against competitors across key factors

---

### Templates

- [Value Proposition Template (PPTX)](https://docs.google.com/presentation/d/1RXH1Udj71aXQJzGeqYSOStnfQ-6dNz14/edit?slide=id.g2a98aeea3b1_0_247#slide=id.g2a98aeea3b1_0_247)

---

### Further Reading

- [How to Design a Value Proposition Customers Can't Resist?](https://www.productcompass.pm/p/how-to-design-value-proposition-template)
- [How to Achieve Product-Market Fit? Part I: Market and Value Proposition](https://www.productcompass.pm/p/how-to-achieve-the-product-market)
- [Jobs-to-be-Done Masterclass with Tony Ulwick and Sabeen Sattar](https://www.productcompass.pm/p/jobs-to-be-done-masterclass-with) (video course)
- [Product Innovation Masterclass](https://www.productcompass.pm/p/product-innovation-masterclass) (video course)

## Limitations

- This skill does not replace environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs are missing.

## Workflow

# value-proposition -- Value Proposition Design

Design a clear, compelling value proposition for a product or feature using the 6-part JTBD template. An alternative to Strategyzer's Value Proposition Canvas that starts with the customer and focuses on practical outcomes.

## Invocation

```
value-proposition AI writing tool for non-native English speakers
value-proposition [upload pitch deck, PRD, or competitive analysis]
value-proposition                    # asks about your product
```

## Workflow

### Step 1: Understand the Product and Market

Accept context from:
- Product description (verbal or written)
- Uploaded documents (pitch decks, PRDs, competitive analyses)
- Existing value propositions to refine

Ask key questions:
- What does the product do? Who is it for?
- What alternatives or workarounds exist today?
- What customer insights or research do you have?

### Step 2: Build the Value Proposition

Apply the **value-proposition** skill to produce the 6-part template:

```
## Value Proposition: [Product]

### For [Segment]:

1. **Who**: [target user profile and characteristics]
2. **Why**: [the job they're trying to do, desired outcomes]
3. **What Before**: [their current painful reality — existing tools, friction, workarounds]
4. **How**: [your solution — specific features and capabilities that deliver value]
5. **What After**: [the improved outcome — what becomes possible]
6. **Alternatives**: [what they'd use without you, and why you're better]

### Value Proposition Statement
[One sentence: For [who] who [need], [product] is a [category] that [benefit]. Unlike [alternative], we [differentiator].]

### Value Proposition Statements (Reusable)
- Marketing: [...]
- Sales: [...]
- Onboarding: [...]
```

If the user has multiple segments, create a separate value proposition for each.

### Step 3: Save and Offer Next Steps

Save as markdown. Offer:
- "Want me to **compare this against competitors** with a Value Curve?"
- "Should I **build a full strategy** around this value proposition?"
- "Want me to **create a Lean Canvas** or **Startup Canvas** using this?"
- "Should I **generate marketing messaging** from these value prop statements?"

## Notes

- This template starts with the customer (Who/Why) and works toward the solution — unlike Strategyzer's canvas which places the product on the left
- Each value proposition is segment-specific — different segments get different value props
- Use a Value Curve (Blue Ocean Strategy) to visually compare your offering against competitors across key factors
- Value Proposition is one element of product strategy — use `strategy` for the full picture
