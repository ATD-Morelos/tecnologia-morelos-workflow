---
name: document
description: >
  Gate 2 skill. Generates architecture and technical documentation based on
  Phase 1 outputs (PRD, Functional Spec). Uses arc42 as framework. Produces:
  Architecture Overview, Crosscutting Concepts, Security/Threat Model,
  Testing Strategy, Risks & Technical Debt, Measurement/KPIs, API Reference,
  and Definition of Done (final). Publishes to TM after approval.
allowed-tools: Read Grep Glob WebSearch mcp__tecnologia-morelos__list_projects mcp__tecnologia-morelos__list_knowledge_bases mcp__tecnologia-morelos__list_knowledge_nodes mcp__tecnologia-morelos__list_knowledge_node_children mcp__tecnologia-morelos__get_knowledge_node mcp__tecnologia-morelos__get_document_context mcp__tecnologia-morelos__hybrid_search mcp__tecnologia-morelos__semantic_search mcp__tecnologia-morelos__find_related_knowledge mcp__tecnologia-morelos__get_knowledge_relations mcp__tecnologia-morelos__get_knowledge_tree mcp__tecnologia-morelos__create_knowledge_node mcp__tecnologia-morelos__update_knowledge_node
---

# Document — Architecture & Technical Documentation

## When to use

- User asks to document the architecture of a project
- Starting Phase 2 (Gate 2) documentation
- User says "document architecture", "write technical docs", "create the design docs"
- As part of the dispatch: `kb-read → document`

## Prerequisites

- **Gate 1 approved**: PRD and Functional Spec must exist in TM.
  Use kb-read to verify. If missing, inform the user and stop.
- Discovery Report and Glossary should exist for context.

## Documents produced

1. **Architecture Overview** — arc42 full architecture document
2. **Crosscutting Concepts** — Domain model, patterns, security strategy, logging
3. **Security / Threat Model** — STRIDE threat analysis and controls
4. **Testing Strategy** — Test levels, tools, coverage, environments
5. **Risks & Technical Debt** — Risk register and tech debt tracker
6. **Measurement / KPIs** — Project objectives mapped to measurable indicators
7. **API Reference** — Initial API definition (endpoints, auth, errors)
8. **Definition of Done (final)** — Finalized DoD based on architecture decisions

Templates are in `templates/` as reference. Generate content adapted to the
specific project — do not copy templates verbatim.

## Workflow

### 1. Verify Phase 1 documents exist

```
kb-read: search for "[Project Name]" in TM
  → Verify "Fase 1 — Discovery & Spec" folder exists
  → Verify PRD and Functional Spec exist
  → If missing, inform user and stop
```

### 2. Read Phase 1 context

Read these documents from TM for context:
- **PRD** → objectives, features, user stories, success metrics
- **Functional Spec** → detailed requirements, data model, integrations
- **Discovery Report** → research findings, stakeholders, systems
- **Quality Requirements** → NFRs that drive architecture decisions
- **Privacy Impact Assessment** → data handling constraints (if exists)
- **Glossary** → domain terminology
- **Project Charter / SOW** → scope, constraints, timeline

### 3. Generate architecture documents

Generate each document using the corresponding template as structure reference.
Order matters — later documents reference earlier ones:

1. **Architecture Overview** (`templates/architecture-overview.md`)
   - Use arc42 as framework (12 sections)
   - Reference Phase 1 requirements for quality attributes
   - Document key architectural decisions

2. **Crosscutting Concepts** (`templates/crosscutting-concepts.md`)
   - Extract domain model from Functional Spec
   - Define patterns based on Architecture Overview
   - Document strategies for security, logging, errors, i18n

3. **Security / Threat Model** (`templates/security-threat-model.md`)
   - Identify assets from PRD and data model
   - Apply STRIDE to each attack surface
   - Propose controls with priority levels

4. **Testing Strategy** (`templates/testing-strategy.md`)
   - Define test levels based on architecture
   - Map quality requirements to test types
   - Set coverage targets aligned with KPIs

5. **Risks & Technical Debt** (`templates/risks-technical-debt.md`)
   - Extract risks from Discovery Report and architecture decisions
   - Identify tech debt from design trade-offs
   - Assign owners and mitigation strategies

6. **Measurement / KPIs** (`templates/measurement-kpis.md`)
   - Map PRD objectives to measurable KPIs
   - Define technical and adoption metrics
   - Propose dashboard and review cadence

7. **API Reference** (`templates/api-reference.md`)
   - Define endpoints from Functional Spec
   - Document auth, errors, rate limiting
   - Note: this is the initial definition — live docs auto-generate from code

8. **Definition of Done (final)** (base template: `../spec/templates/definition-of-done.md`)
   - Read the DoD draft from Phase 1
   - Incorporate architecture decisions, testing criteria, security requirements
   - Finalize acceptance criteria per deliverable

### 4. Present for review (AI Fluency — Discernment)

Present all documents to the user. Ask:
- Is the information accurate and complete?
- Are there assumptions the AI made that are incorrect?
- What would you change or add?
- Do the architecture decisions align with organizational constraints?
- Are the KPI targets realistic?

**Do NOT publish until the user explicitly approves.**

### 5. Publish to TM (kb-publish)

After approval:
1. Ensure the "Fase 2 — Design & Plan" folder exists (create if needed)
2. Create/update each document node in TM
3. Add the AI transparency footer to all documents
4. Document type: `PAGE` for all except API Reference (`API_REFERENCE`)

## Output

| Document | Location in TM | Type |
|----------|----------------|------|
| Architecture Overview | `[KB]/Fase 2 — Design & Plan/Architecture Overview` | PAGE |
| Crosscutting Concepts | `[KB]/Fase 2 — Design & Plan/Crosscutting Concepts` | PAGE |
| Security / Threat Model | `[KB]/Fase 2 — Design & Plan/Security / Threat Model` | PAGE |
| Testing Strategy | `[KB]/Fase 2 — Design & Plan/Testing Strategy` | PAGE |
| Risks & Technical Debt | `[KB]/Fase 2 — Design & Plan/Risks & Technical Debt` | PAGE |
| Measurement / KPIs | `[KB]/Fase 2 — Design & Plan/Measurement / KPIs` | PAGE |
| API Reference | `[KB]/Fase 2 — Design & Plan/API Reference` | API_REFERENCE |
| Definition of Done (final) | `[KB]/Fase 2 — Design & Plan/Definition of Done (final)` | PAGE |

## Notes

- arc42 is the framework, not a rigid template. Adapt sections to the project.
- Architecture decisions should reference or create ADRs when significant.
- The API Reference is an initial definition. It will be superseded by auto-generated docs once code exists.
- Cross-reference between documents: Architecture Overview links to Crosscutting, Risks, and Glossary.
- Every section must contain substantive content, not placeholders.
