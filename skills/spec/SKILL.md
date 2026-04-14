---
name: spec
description: >
  Generate specification documents for a project: PRD, Functional Spec,
  Quality Requirements, Privacy Impact Assessment, and Definition of Done (draft).
  Requires an approved Discovery Report (Gate 1 prerequisite).
when_to_use: "User says 'write specs', 'create PRD', 'requirements document', 'functional spec'"
argument-hint: "[project-name]"
allowed-tools: Read Grep Glob mcp__tecnologia-morelos__list_projects mcp__tecnologia-morelos__list_knowledge_bases mcp__tecnologia-morelos__list_knowledge_nodes mcp__tecnologia-morelos__list_knowledge_node_children mcp__tecnologia-morelos__get_knowledge_node mcp__tecnologia-morelos__get_document_context mcp__tecnologia-morelos__hybrid_search mcp__tecnologia-morelos__semantic_search mcp__tecnologia-morelos__find_related_knowledge mcp__tecnologia-morelos__get_knowledge_relations mcp__tecnologia-morelos__get_knowledge_tree mcp__tecnologia-morelos__get_knowledge_base_graph_summary
---

# Spec — Specification Documents

## When to use

- User asks to write specs, requirements, or PRD for a project
- Continuing Phase 1 after Discovery Report is approved
- User needs functional specification, quality requirements, or privacy assessment

## Prerequisites

- **Gate 1 prerequisite**: Discovery Report must exist and be approved in TM.
  Use kb-read to verify. If missing, inform the user they need to run discover first.

## Pipeline

### 1. Verify Discovery Report exists

Use kb-read to:
- Find the project KB
- Navigate to "Fase 1 — Discovery & Spec" folder
- Confirm the Discovery Report exists

If it doesn't exist, inform the user:
> "The Discovery Report for [project] doesn't exist yet. Run the discover
> skill first to complete Gate 1 prerequisites."

### 2. Read Discovery Report and context

Read the Discovery Report to extract:
- Problem statement and objectives
- Stakeholders and their needs
- Systems and dependencies
- Identified risks
- Key findings

Also read:
- Project Charter (scope, constraints)
- Glosario (domain terms)
- Stakeholder Register (if exists)

### 3. Generate documents

Generate each document using the corresponding template as structural
reference. All content must be derived from the Discovery Report findings.

#### 3a. PRD (Product Requirements Document)

Template: [templates/prd.md](templates/prd.md)

Translate discovery findings into product requirements. Each requirement
must trace back to a finding or stakeholder need.

#### 3b. Functional Specification

Template: [templates/functional-spec.md](templates/functional-spec.md)

Detail how the system will behave. Use cases must cover the scope defined
in the PRD. Include error scenarios.

#### 3c. Quality Requirements

Template: [templates/quality-requirements.md](templates/quality-requirements.md)

Define non-functional requirements based on the project context. Be specific
with measurable targets (e.g., "response time < 2s for 95th percentile").

#### 3d. Privacy Impact Assessment

Template: [templates/privacy-impact-assessment.md](templates/privacy-impact-assessment.md)

**Only generate if the project handles personal data.** If it doesn't,
note this in the output and skip.

Must reference LGPDPPSO (Ley General de Protección de Datos Personales
en Posesión de Sujetos Obligados) and applicable state regulations.

#### 3e. Definition of Done (draft)

Template: [templates/definition-of-done.md](templates/definition-of-done.md)

Generate a draft DoD. This will be finalized in Phase 2 after architecture
decisions are made.

### 4. Present for review (AI Fluency — Discernment)

Present all generated documents to the user. For each document, ask:
- Is the information accurate and complete?
- Are there assumptions the AI made that are incorrect?
- What would you change or add?

Present documents one at a time or as a batch, based on user preference.

**Do NOT publish until the user explicitly approves.**

### 5. Publish to TM

After approval, delegate publishing to the kb-publish skill:
1. Ensure the "Fase 1 — Discovery & Spec" folder exists
2. Create/update each document node in TM
3. Add the AI transparency footer to all documents

## Output

| Document | Location in TM | Type |
|----------|----------------|------|
| PRD | `[KB]/Fase 1 — Discovery & Spec/PRD` | PAGE |
| Functional Spec | `[KB]/Fase 1 — Discovery & Spec/Functional Spec` | PAGE |
| Quality Requirements | `[KB]/Fase 1 — Discovery & Spec/Quality Requirements` | PAGE |
| Privacy Impact Assessment | `[KB]/Fase 1 — Discovery & Spec/Privacy Impact Assessment` | PAGE |
| Definition of Done (draft) | `[KB]/Fase 1 — Discovery & Spec/Definition of Done (draft)` | PAGE |

## Notes

- The Privacy Impact Assessment is conditional — only create if personal data is involved.
- Definition of Done is a draft; it gets finalized in Phase 2 (document skill).
- Requirements must be specific and measurable. Avoid vague statements like "the system should be fast".
- Use MoSCoW prioritization for functional requirements (Must, Should, Could, Won't).
