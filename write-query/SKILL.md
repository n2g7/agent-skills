---
disable-model-invocation: true
name: write-query
description: "This skill should be used when the user asks to \"write query\". Generate SQL queries from natural language."
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
# write-query -- SQL Query Generator

## When to Use

This skill should be used when the user asks to "write query".

## When NOT to Use

- Do not use this skill for implementation work, legal advice, or exploit development.
- Stop if the user's inputs are missing.

Describe what data you need in plain English and get an optimized SQL query. Supports multiple dialects and can read your schema from uploaded files.

## Invocation

```
write-query Show me daily active users for the last 30 days, broken down by plan tier
write-query Find users who signed up last month but never completed onboarding
write-query [upload a schema diagram] What's the conversion rate from trial to paid by cohort?
```

## Workflow

### Step 1: Understand the Question

Parse the user's natural language request to identify:
- What data is being requested (metrics, dimensions, filters)
- Time range and granularity
- Grouping and ordering preferences
- Output expectations (raw data, aggregated, ranked)

### Step 2: Determine Schema

If a schema is available (uploaded diagram, DDL, or description):
- Map the request to specific tables and columns
- Identify necessary joins

If no schema is provided:
- Ask for the database type (BigQuery, PostgreSQL, MySQL, etc.)
- Infer a reasonable schema from the question and ask the user to confirm
- Use common SaaS data model conventions as defaults

### Step 3: Generate Query

Apply the **sql-queries** skill:

- Write the SQL query in the correct dialect
- Optimize for readability and performance
- Include comments explaining key logic
- Add CTEs for complex queries to improve readability
- Handle edge cases (NULLs, timezone considerations, duplicate handling)

### Step 4: Present and Iterate

```
## SQL Query: [What It Does]

**Dialect**: [BigQuery / PostgreSQL / MySQL / etc.]
**Tables used**: [list]

### Query
[SQL code block with comments]

### What This Returns
[Description of the output: columns, rows, expected result shape]

### Assumptions
- [Schema assumptions made]
- [Business logic assumptions]

### Notes
- [Performance considerations for large datasets]
- [Edge cases handled or flagged]
```

Offer:
- "Want me to **modify this** — add filters, change grouping, extend the time range?"
- "Should I **create a companion query** for a related metric?"
- "Want me to **build a dashboard** around this query?"
- "Need a **cohort analysis** version of this?"

## Notes

- Always include comments in the SQL — PMs share queries with analysts who need to understand intent
- Default to readable over clever — CTEs over nested subqueries
- Flag queries that might be slow on large datasets and suggest optimization
- If the request is ambiguous (e.g., "active users"), ask the user to define the metric precisely
- Offer to generate the query in multiple dialects if the user is unsure which database they're using

## Limitations

- This skill does not replace environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs are missing.
