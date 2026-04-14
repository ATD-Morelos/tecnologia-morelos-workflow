---
name: review
description: >
  Transversal skill for reviewing AI-generated documents using the AI Fluency
  Framework (4Ds: Delegation, Description, Discernment, Diligence). Guides the
  human reviewer with structured questions to evaluate quality, accuracy, and
  completeness of any document produced by this plugin.
allowed-tools: []
---

# Review — AI Fluency Document Review

## When to use

- After ANY skill generates a document, before publishing to TM
- When the user asks to review or validate existing documentation
- As part of gate approval (Gate 0, 1, 2) — each gate requires human review

## How it works

This skill is purely instructional — it does not call any tools. It provides a
structured framework for the human to evaluate AI-generated content before
approval.

Present the review checklist (see `review-checklist.md`) adapted to the specific
document type being reviewed.

## Review flow

1. **Present the document** — Show the generated content to the user
2. **Apply the 4Ds checklist** — Walk through each dimension with the user
3. **Collect feedback** — Record what needs to change
4. **Iterate** — Regenerate or edit based on feedback
5. **Get approval** — Explicit "approved" from the user before publishing

## The 4Ds applied to document review

### Delegation (¿Se delegó bien?)
- Was the right task given to the AI?
- Is the scope appropriate for AI generation?
- Are there parts that should have been written by a human instead?

### Description (¿Se describió bien?)
- Was the input/context sufficient for a good output?
- Did the AI have enough information about the project?
- Are there missing inputs that would improve the result?

### Discernment (¿Se evaluó bien?)
- Is the information accurate and complete?
- Are there incorrect assumptions?
- Does the content match the project's real context?
- Are there hallucinated details?

### Diligence (¿Se documentó bien?)
- Is it clear what was AI-generated vs human-decided?
- Does the AI transparency footer exist?
- Are decisions and rationale properly recorded?

## Adapting to document type

| Document | Focus areas |
|----------|-------------|
| Project Charter | Objectives are SMART, scope is realistic, budget is accurate |
| SOW | Deliverables are measurable, timeline is feasible |
| Stakeholder Register | All key stakeholders included, influence levels accurate |
| RACI | No missing roles, no tasks without a Responsible |
| Discovery Report | Problem statement accurate, user research reflects reality |
| Architecture | Components are correct, integrations exist, no fantasy APIs |
| PRD | Requirements are testable, priorities reflect real needs |

## Output

This skill produces no artifacts. Its output is the user's approval or feedback
on the document being reviewed.
