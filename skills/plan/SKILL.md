---
name: plan
description: >
  Plan and structure work in Linear based on PRD and Functional Spec.
  Generates Product Structure, Project Configs, Milestones, Epics, and
  User Stories. Documents everything in TM first, then creates in Linear
  after user approval. Requires Gate 2 prerequisites.
allowed-tools: Read Grep Glob mcp__tecnologia-morelos__list_projects mcp__tecnologia-morelos__list_knowledge_bases mcp__tecnologia-morelos__list_knowledge_nodes mcp__tecnologia-morelos__list_knowledge_node_children mcp__tecnologia-morelos__get_knowledge_node mcp__tecnologia-morelos__get_document_context mcp__tecnologia-morelos__hybrid_search mcp__tecnologia-morelos__semantic_search mcp__tecnologia-morelos__find_related_knowledge mcp__tecnologia-morelos__get_knowledge_relations mcp__tecnologia-morelos__get_knowledge_tree mcp__tecnologia-morelos__get_knowledge_base_graph_summary mcp__tecnologia-morelos__create_knowledge_node mcp__tecnologia-morelos__update_knowledge_node mcp__linear__list_teams mcp__linear__list_projects mcp__linear__create_project mcp__linear__list_milestones mcp__linear__create_milestone mcp__linear__create_issue mcp__linear__update_issue mcp__linear__list_issues mcp__linear__list_labels mcp__linear__create_label mcp__linear__list_workflow_states mcp__linear__list_initiatives mcp__linear__search_issues
---

# Plan — Linear Product Structure & Work Breakdown

## When to use

- User asks to set up Linear, plan sprints, or organize work for a project
- Starting Phase 2 (Gate 2) planning after specs are approved
- User wants to break down PRD requirements into trackable issues

## Prerequisites

- **Gate 1 approved**: PRD and Functional Spec must exist in TM.
  Use kb-read to verify. If missing, inform the user they need to run spec first.

## Core principles

1. **AI proposes, user confirms** — Present every structure, config, and issue
   for review before creating anything in Linear.
2. **Document in TM first** — All planning artifacts go to the Linear/ folder
   in TM before being created in Linear.
3. **Team = user input (ADR-004)** — NEVER hardcode or infer teams. Present
   available teams and let the user choose.
4. **1 Project per product (ADR-005)** — Each product/component gets its own
   Linear Project named "[Producto] — Morelos".
5. **Phases as Milestones (ADR-006)** — Milestones represent deliverables:
   Discovery Report, Spec Aprobada, Arquitectura Documentada, MVP, etc.
6. **2-level issue hierarchy (ADR-007)** — If >1 task, use parent + sub-issues.
   If only 1 task, create a single issue.
7. **Labels by group (ADR-008)** — Phase, Type, and MoSCoW labels.
8. **Initiatives (ADR-009)** — Assign thematic initiatives when applicable.

## Pipeline

### 1. Gather context from TM

Read the PRD and Functional Spec from the project KB:
- Navigate to "Fase 1 — Discovery & Spec" folder
- Read PRD for features, requirements, and scope
- Read Functional Spec for detailed functional requirements
- Read any existing ADRs for decisions that affect planning

### 2. Check existing Linear/ folder in TM

Use kb-read to check if `Linear/` folder already exists in the project KB.
- If it exists, read existing documents to avoid duplicating work
- If it doesn't exist, proceed with creating the full structure

### 3. Generate Product Structure

Analyze the PRD to identify distinct products/components. Use the
`product-structure.md` template.

Present to user:
- List of products with descriptions
- Suggested team assignment (user MUST confirm — ADR-004)
- Dependencies between products
- Initiative assignment (if applicable — ADR-009)

**Wait for user approval before proceeding.**

### 4. Configure each Linear Project

For each approved product:

#### 4a. Team selection (ADR-004)
```
1. Call list_teams to get available teams
2. Present teams to user as numbered options
3. User picks the team — NEVER assume or infer
```

#### 4b. Create/verify Project (ADR-005)
- Project name: "[Producto] — Morelos"
- Check if project already exists in Linear (search by name)
- If it exists, confirm with user before reusing
- Fill in project-config.md template

#### 4c. Generate Milestones (ADR-006)
Based on project phases, create milestones named by deliverable:
- Discovery Report
- Spec Aprobada
- Arquitectura Documentada
- MVP Listo
- Release v1.0
- (Add custom milestones based on PRD)

#### 4d. Decompose into Epics (ADR-007)
- Map PRD requirements → Epics (parent issues)
- Each Epic has: title, description, milestone, labels, acceptance criteria
- Use the `epic-template.md` template

#### 4e. Decompose Epics into User Stories (ADR-007)
- Break each Epic into sub-issues (User Stories / Tasks)
- Apply 2-level rule: >1 task = parent + sub-issues, 1 task = single issue
- Each story has: title, description, estimation, labels

### 5. Define Labels & Workflow States (ADR-008)

Use the `labels-workflow-states.md` template:

**Labels by group:**
| Group | Labels |
|-------|--------|
| Phase | discover, spec, plan, build, release |
| Type | Feature, Chore, Bug, Planning, Docs |
| MoSCoW | must-have, should-have, could-have, post-mvp |

**Workflow States:**
Triage → Backlog → Todo → In Progress → In Review → Done → Cancelled

### 6. Assign Initiative (ADR-009)

If the project falls under a thematic initiative, assign it:
- "Trámites Digitales"
- "Datos y Core Platform"
- "Servicios Ciudadanos"
- (Or create a new initiative if needed — ask user)

### 7. Document in TM

Create or update these nodes in the project KB under `Linear/`:
1. `Product Structure` — overview page
2. `Labels & Workflow States` — shared labels/states page
3. For each product, create a subfolder `[Product Name]/`:
   - `Project Config` — project settings
   - `Milestones` — milestone list
   - `Epics` — all epics with sub-issues

**Use kb-publish skill conventions:**
- `id` for updates, `nodeId` for reads
- Include AI transparency footer
- No code blocks inside Markdoc components

### 8. Present for user review

Show the complete plan:
- Product Structure summary
- Per-product: Project Config, Milestones, Epics with User Stories
- Labels & Workflow States
- Initiative assignment

Ask the user:
- Is the decomposition accurate and complete?
- Are the estimations reasonable?
- Any epics to add, remove, or reorganize?
- Confirm team assignments one final time

**Wait for explicit approval before creating anything in Linear.**

### 9. Execute in Linear

Only after user approval:
1. Create/verify Projects
2. Create Labels (if they don't exist)
3. Create Milestones
4. Create parent issues (Epics)
5. Create sub-issues (User Stories) linked to parents
6. Assign Labels to issues
7. Assign Issues to Milestones

After creation, update TM documents with Linear IDs/links.

## Output

Documents created in TM under `Linear/`:
- Product Structure (PAGE)
- Labels & Workflow States (PAGE)
- Per product folder with Project Config, Milestones, Epics (PAGEs)

Items created in Linear:
- Projects (1 per product)
- Milestones per project
- Parent issues (Epics) with sub-issues (User Stories)
- Labels applied

## Error handling

- If Linear API fails, document the error and retry once
- If a project already exists, confirm with user before reusing
- If labels already exist, reuse them (don't create duplicates)
- If milestones conflict, present options to user
