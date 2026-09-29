---
disable-model-invocation: true
name: stakeholder-map
description: "This skill should be used when the user asks to \"stakeholder map\". Build a stakeholder map using a power/interest grid, identify communication strategies per quadrant, and generate a communication."
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

This skill should be used when the user asks to "stakeholder map".

## When NOT to Use

- Do not use this skill for implementation work, legal advice, or exploit development.
- Stop if the user's inputs are missing.

## Stakeholder Mapping & Communication Plan

Map stakeholders on a Power × Interest grid and create a tailored communication plan for each group.

### Context

You are helping build a stakeholder map for **the user's request**.

If the user provides files (org charts, project briefs, team rosters), read them first. If they describe the product or initiative, use that context to infer likely stakeholders.

### Instructions

1. **Identify stakeholders**: List all relevant individuals and groups — executives, engineering leads, designers, marketing, sales, support, legal, finance, external partners, and end users.

2. **Classify each stakeholder** on two dimensions:
   - **Power** (High/Low): Their ability to influence decisions, resources, or outcomes
   - **Interest** (High/Low): How much the project directly affects them or how engaged they are

3. **Place stakeholders in the Power × Interest grid**:

   | | High Interest | Low Interest |
   |---|---|---|
   | **High Power** | **Manage Closely** — Regular 1:1s, involve in decisions, seek their input early | **Keep Satisfied** — Periodic updates, escalate only critical issues |
   | **Low Power** | **Keep Informed** — Regular status updates, invite to demos, gather feedback | **Monitor** — Light-touch updates, available on request |

4. **For each quadrant**, recommend:
   - Communication frequency (daily, weekly, bi-weekly, monthly)
   - Communication format (1:1, email, Slack, meeting, dashboard)
   - Key messages and framing
   - Potential risks if this stakeholder is neglected

5. **Create a communication plan table**:

   | Stakeholder | Role | Power | Interest | Strategy | Frequency | Channel | Key Message |
   |---|---|---|---|---|---|---|---|

6. **Flag potential conflicts**: Identify stakeholders with competing interests and suggest alignment strategies.

Think step by step. Save the stakeholder map as a markdown document.

---

### Further Reading

- [The Product Management Frameworks Compendium + Templates](https://www.productcompass.pm/p/the-product-frameworks-compendium)
- [Team Topologies: A Handbook to Set and Scale Product Teams](https://www.productcompass.pm/p/team-topologies-a-handbook-to-set)

## Limitations

- This skill does not replace environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs are missing.

## Workflow

# stakeholder-map -- Stakeholder Mapping & Communication Plan

Identify all stakeholders for a project, map them by influence and interest, and generate a communication plan that ensures the right people get the right information at the right time.

## Invocation

```
stakeholder-map New analytics platform launch
stakeholder-map Pricing model change affecting all customers
stakeholder-map [upload a project brief or org chart]
```

## Workflow

### Step 1: Understand the Initiative

Ask:
- What is the project or initiative?
- What phase is it in? (planning, building, launching, post-launch)
- Who are the obvious stakeholders you already know about?
- Are there any politically sensitive dynamics to be aware of?

### Step 2: Identify Stakeholders

Brainstorm stakeholders the user might not have considered:
- **Internal**: Engineering, Design, QA, Data, Legal, Finance, Marketing, Sales, Support, Leadership
- **External**: Customers, partners, vendors, regulators, board members
- **Often missed**: Adjacent teams, on-call engineers, customer success, documentation team

### Step 3: Map to Power × Interest Grid

Apply the **stakeholder-map** skill:

Place each stakeholder in a quadrant:

```
                    HIGH INTEREST
                         │
    KEEP SATISFIED       │      MANAGE CLOSELY
    (High Power,         │      (High Power,
     Low Interest)       │       High Interest)
                         │
   ──────────────────────┼──────────────────────
                         │
    MONITOR              │      KEEP INFORMED
    (Low Power,          │      (Low Power,
     Low Interest)       │       High Interest)
                         │
                    LOW INTEREST
```

### Step 4: Generate Communication Plan

```
## Stakeholder Map: [Initiative]

### Stakeholder Grid
| Stakeholder | Role | Power | Interest | Quadrant | Stance |
|------------|------|-------|----------|----------|--------|

### Communication Plan

#### Manage Closely (High Power, High Interest)
| Stakeholder | Channel | Frequency | Content | Owner |
|------------|---------|-----------|---------|-------|

#### Keep Satisfied (High Power, Low Interest)
| Stakeholder | Channel | Frequency | Content | Owner |
|------------|---------|-----------|---------|-------|

#### Keep Informed (Low Power, High Interest)
| Stakeholder | Channel | Frequency | Content | Owner |
|------------|---------|-----------|---------|-------|

#### Monitor (Low Power, Low Interest)
[Minimal communication — include in broad updates only]

### Potential Conflicts
[Where stakeholder interests may clash — with mitigation strategies]

### Escalation Path
[Who to go to when decisions are blocked]

### RACI Matrix
| Decision Area | Responsible | Accountable | Consulted | Informed |
|--------------|-------------|-------------|-----------|----------|
```

Save as markdown.

### Step 5: Offer Next Steps

- "Want me to **draft the first stakeholder update** for the 'Manage Closely' group?"
- "Should I **create a meeting prep brief** for key stakeholder conversations?"
- "Want me to **set up a communication cadence** as a recurring checklist?"

## Notes

- The "Manage Closely" quadrant is where PMs spend most of their political capital — get these relationships right
- "Stance" (supportive, neutral, resistant) helps prioritize where to invest relationship-building effort
- Don't forget downstream stakeholders: support, docs, and sales enablement teams are often surprised by launches
- Update the map as the project evolves — stakeholder interest shifts with project phase
