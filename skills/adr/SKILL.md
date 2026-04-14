---
name: adr
description: >
  Create Architecture Decision Records (ADRs) for any project decision.
  Can be invoked at any gate or phase. Assigns sequential numbers,
  categorizes decisions, and publishes to TM under the ADRs/ folder.
allowed-tools: Read Grep Glob mcp__tecnologia-morelos__list_projects mcp__tecnologia-morelos__list_knowledge_bases mcp__tecnologia-morelos__list_knowledge_nodes mcp__tecnologia-morelos__list_knowledge_node_children mcp__tecnologia-morelos__get_knowledge_node mcp__tecnologia-morelos__get_document_context mcp__tecnologia-morelos__hybrid_search mcp__tecnologia-morelos__semantic_search mcp__tecnologia-morelos__find_related_knowledge mcp__tecnologia-morelos__get_knowledge_relations mcp__tecnologia-morelos__get_knowledge_tree mcp__tecnologia-morelos__get_knowledge_base_graph_summary mcp__tecnologia-morelos__create_knowledge_node mcp__tecnologia-morelos__update_knowledge_node
---

# ADR — Architecture Decision Records

## When to use

- User wants to record an important decision about the project
- A technical, architectural, business, security, or process decision needs documentation
- During any gate or phase — ADRs are not restricted to a specific stage
- When a previous ADR needs to be superseded

## Prerequisites

- A project KB must exist in TM with an `ADRs/` folder (or it will be created)
- No gate prerequisite — ADRs can be created at any point

## Categories

| Category | When to use |
|----------|-------------|
| `[negocio]` | Business decisions, scope, priorities, stakeholder agreements |
| `[arquitectura]` | Technical architecture, patterns, technology choices |
| `[seguridad]` | Security decisions, auth, encryption, compliance |
| `[proceso]` | Process decisions, workflow, team conventions |

## Pipeline

### 1. Gather decision context

Ask the user:
- What decision needs to be recorded?
- What problem or question prompted this decision?
- What options were considered?
- What was decided and why?

If the user provides only a brief description, ask clarifying questions to
fill in the template completely.

### 2. Determine ADR number

Read the `ADRs/` folder in the project KB to find existing ADRs:
```
1. Navigate to project KB
2. Find or create the ADRs/ folder
3. List children to see existing ADR numbers
4. Assign next sequential number (ADR-001, ADR-002, etc.)
```

If no `ADRs/` folder exists, create it and start with ADR-001.

### 3. Categorize the decision

Based on the content, assign one of the categories:
- `[negocio]` — business decisions
- `[arquitectura]` — technical decisions
- `[seguridad]` — security decisions
- `[proceso]` — process decisions

Present the category to the user for confirmation.

### 4. Generate ADR

Use the `adr-template.md` template to generate the ADR content:
- Fill in all sections with the gathered context
- List all options considered with pros/cons
- State the decision clearly
- Document consequences (positive and negative)
- Link to related ADRs or documents

### 5. Present for review

Show the complete ADR to the user:
- Is the context accurately described?
- Are all options fairly represented?
- Is the decision statement clear?
- Are the consequences complete?

**Wait for user approval before publishing.**

### 6. Publish to TM

After approval:
1. Create the ADR page in the `ADRs/` folder:
   ```
   create_knowledge_node({
     knowledgeBaseId: "<kb_id>",
     title: "ADR-NNN: [Título]",
     documentType: "PAGE",
     content: "<adr_content>",
     parentId: "<adrs_folder_id>"
   })
   ```
2. Include the AI transparency footer

### 7. Update ADR Index (if exists)

If an ADR Index page exists in the KB, update it with the new entry:
- ADR number, title, status, category, date
- If no index exists, consider creating one after 3+ ADRs

## Superseding an ADR

When a new decision replaces an old one:
1. Create the new ADR with status `accepted`
2. Update the old ADR's status to `superseded by ADR-NNN`
3. Add a link between both ADRs

## Output

- 1 ADR page in TM under `ADRs/` folder
- Updated ADR Index (if it exists)
- Status: `proposed` (default) or `accepted` (if user confirms)
