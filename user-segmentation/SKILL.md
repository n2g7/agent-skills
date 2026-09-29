---
disable-model-invocation: true
name: user-segmentation
description: "This skill should be used when the user asks to \"user segmentation\". Segment users from feedback data based on behavior, JTBD, and needs."
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
# User Segmentation

## When to Use

This skill should be used when the user asks to "user segmentation".

## When NOT to Use

- Do not use this skill for implementation work, legal advice, or exploit development.
- Stop if the user's inputs are missing.

## Purpose
Analyze diverse user feedback to identify at least 3 distinct behavioral and needs-based user segments. This skill surfaces hidden customer groups based on jobs-to-be-done, behaviors, and motivations rather than demographics alone, enabling targeted product strategy.

## Instructions

You are an expert behavioral researcher and data analyst specializing in user segmentation and behavioral clustering.

### Input
Your task is to segment users for **the user's request** based on behavior, jobs-to-be-done, and unmet needs.

If the user provides feedback data, interviews, support tickets, product usage logs, surveys, or other user data, read and analyze them directly. Extract behavioral patterns, motivations, and needs across the user base.

### Analysis Steps (Think Step by Step)

1. **Data Preparation**: Read and organize all provided user feedback and data
2. **Behavior Extraction**: Identify key behavioral patterns, usage modes, and user journeys
3. **Needs Analysis**: Map jobs-to-be-done, desired outcomes, and pain points for each user
4. **Clustering**: Group users into distinct segments based on behavior and needs similarity
5. **Validation**: Ensure segments are coherent, non-overlapping, and actionable
6. **Characterization**: Develop rich profiles for each segment with representative quotes

### Output Structure

For each identified segment (minimum 3):

**Segment Name & Overview**
- Clear, descriptive segment identifier
- Size: estimated number or percentage of user base
- Brief one-sentence characterization

**Behavioral Characteristics**
- How this segment uses the user's request (primary use cases, frequency, depth)
- Typical user journey and key touchpoints
- Technical proficiency or sophistication level
- Integration with other tools or workflows

**Jobs-to-be-Done & Motivations**
- Core job(s) this segment is trying to accomplish
- Underlying motivations and desired outcomes
- Context and frequency of the job
- What success looks like for this segment

**Key Needs & Pain Points**
- Unmet needs specific to this segment's behavior
- Obstacles preventing effective job completion
- Current workarounds or alternative solutions they employ
- Severity and frequency of pain points

**Current Product Fit**
- How well the user's request currently serves this segment
- Features or capabilities this segment values most
- Gaps or limitations most frustrating to this segment
- Likelihood to continue using vs. churn risk

**Differentiated Value Proposition**
- What unique value could be unlocked for this segment
- Feature or experience improvements that would maximize fit
- Messaging and positioning most resonant with this segment

**Segment Prioritization**
- Strategic importance: growth potential, revenue impact, alignment with vision
- Implementation difficulty: ease of serving this segment's needs
- Recommendation: invest, maintain, or de-prioritize

## Best Practices

- Ground segmentation in behavioral and motivational data, not just demographics
- Use representative quotes and examples from actual user feedback
- Ensure segments are distinct and serve different core needs
- Consider interdependencies between segments and prioritization tradeoffs
- Flag any segments that may be underrepresented in feedback data
- Validate emerging segments against product usage or customer data when available
- Consider adjacent behaviors and cross-segment patterns

---

### Further Reading

- [Market Research: Advanced Techniques](https://www.productcompass.pm/p/market-research-advanced-techniques)
- [User Interviews: The Ultimate Guide to Research Interviews](https://www.productcompass.pm/p/interviewing-customers-the-ultimate)
- [Jobs-to-be-Done Masterclass with Tony Ulwick and Sabeen Sattar](https://www.productcompass.pm/p/jobs-to-be-done-masterclass-with) (video course)

## Limitations

- This skill does not replace environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs are missing.
