---
disable-model-invocation: true
name: test-scenarios
description: "This skill should be used when the user asks to \"test scenarios\". Create comprehensive test scenarios from user stories with test objectives, starting conditions, user roles, step-by-step actions."
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
# Test Scenarios

## When to Use

This skill should be used when the user asks to "test scenarios".

## When NOT to Use

- Do not use this skill for implementation work, legal advice, or exploit development.
- Stop if the user's inputs are missing.

Create comprehensive test scenarios from user stories with test objectives, starting conditions, user roles, step-by-step test actions, and expected outcomes.

**Use when:** Writing QA test cases, creating test plans, defining acceptance test scenarios, or validating user story implementations.

**Arguments:**
- `$PRODUCT`: The product or system name
- `$USER_STORY`: The user story to test (title and acceptance criteria)
- `$CONTEXT`: Additional testing context or constraints

## Step-by-Step Process

1. **Review the user story** and acceptance criteria
2. **Define test objectives** - What specific behavior to validate
3. **Establish starting conditions** - System state, data setup, configurations
4. **Identify user roles** - Who performs the test actions
5. **Create test steps** - Break down interactions step-by-step
6. **Define expected outcomes** - Observable results after each step
7. **Consider edge cases** - Invalid inputs, boundary conditions
8. **Output detailed test scenarios** - Ready for QA execution

## Scenario Template

**Test Scenario:** [Clear scenario name]

**Test Objective:** [What this test validates]

**Starting Conditions:**
- [System state required]
- [Data or configuration needed]
- [User setup or permissions]

**User Role:** [Who performs the test]

**Test Steps:**
1. [First action and its expected result]
2. [Second action and observable outcome]
3. [Third action and system behavior]
4. [Completion action and final state]

**Expected Outcomes:**
- [Observable result 1]
- [Observable result 2]
- [Observable result 3]

## Example Test Scenario

**Test Scenario:** View Recently Viewed Products on Product Page

**Test Objective:** Verify that the 'Recently viewed' section displays correctly and excludes the current product.

**Starting Conditions:**
- User is logged in or has browser history enabled
- User has viewed at least 2 products in the current session
- User is now on a product page different from previously viewed items

**User Role:** Online Shopper

**Test Steps:**
1. Navigate to any product page → Section should appear at bottom with previously viewed items
2. Scroll to bottom of page → "Recently viewed" section is visible with product cards
3. Verify product thumbnails → Images, titles, and prices are displayed correctly
4. Check current product → Current product is NOT in the recently viewed list
5. Click on a product card → User navigates to the corresponding product page

**Expected Outcomes:**
- Recently viewed section appears only after viewing at least 1 prior product
- Section displays 4-8 product cards with complete information
- Current product is excluded from the list
- Each card shows "Viewed X minutes/hours ago" timestamp
- Clicking cards navigates to correct product pages
- Performance: Section loads within 2 seconds

## Output Deliverables

- Comprehensive test scenarios for each acceptance criterion
- Clear test objectives aligned with user story intent
- Detailed step-by-step test actions
- Observable expected outcomes after each step
- Edge case and error scenario coverage
- Ready for QA team execution and documentation

## Limitations

- This skill does not replace environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs are missing.

## Workflow

# test-scenarios -- Test Scenario Generator

Turn user stories or feature descriptions into comprehensive test scenarios that QA can execute immediately. Covers happy paths, edge cases, error handling, and cross-browser/device considerations.

## Invocation

```
test-scenarios [paste user stories or acceptance criteria]
test-scenarios [upload a PRD or feature spec]
test-scenarios User can reset their password via email link
```

## Workflow

### Step 1: Accept Input

Accept: user stories, acceptance criteria, PRD sections, feature descriptions, or any specification of expected behavior.

### Step 2: Generate Test Scenarios

Apply the **test-scenarios** skill:

For each user story or requirement, generate:

**Happy Path Scenarios**: The expected user flow works correctly
**Edge Cases**: Boundary conditions, unusual inputs, concurrent operations
**Error Scenarios**: What happens when things go wrong
**Security Scenarios**: If applicable (auth, permissions, data access)
**Performance Scenarios**: If applicable (load, timeout, large data)

### Step 3: Structure Output

```
## Test Scenarios: [Feature]

**Source**: [user stories / PRD / description]
**Total scenarios**: [count]
**Coverage**: [happy path / edge cases / errors / security / performance]

### Scenario 1: [Title]
**Tests**: [which story or requirement]
**Preconditions**: [setup needed]
**User role**: [who is performing this]

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | [user action] | [expected system response] |
| 2 | [user action] | [expected system response] |

**Postconditions**: [state after completion]
**Priority**: [Critical / High / Medium / Low]

---
[Repeat for each scenario]

### Coverage Matrix
| Requirement | Happy Path | Edge Cases | Error Handling | Notes |
|------------|-----------|-----------|---------------|-------|

### Test Data Requirements
[What test data is needed to execute these scenarios]
```

Save as markdown.

### Step 4: Offer Next Steps

- "Want me to **generate the test data** for these scenarios?"
- "Should I **add more edge cases** for any specific scenario?"
- "Want me to **create the user stories** that these scenarios test?"

## Notes

- Happy paths first, then layer in edge cases — ensure basic flows work before testing boundaries
- Every acceptance criterion from the original story should map to at least one test scenario
- Include both positive tests (it works) and negative tests (it fails gracefully)
- For APIs, include scenarios for rate limiting, timeout, malformed requests, and auth failures
- Flag scenarios that require specific test environments or third-party service mocking
