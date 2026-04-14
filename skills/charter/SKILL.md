---
name: charter
description: >
  Gate 0 skill. Generates the three foundational documents for a new project:
  Project Charter, Statement of Work (SOW), and Acerca de (About page).
  Checks TM for existing documents before creating, presents drafts for
  human review, and publishes to TM after approval.
when_to_use: "User says 'start a new project', 'create project charter', 'write SOW', 'initialize project'"
argument-hint: "[project-name]"
allowed-tools: mcp__tecnologia-morelos__get_knowledge_node mcp__tecnologia-morelos__list_knowledge_nodes mcp__tecnologia-morelos__hybrid_search mcp__tecnologia-morelos__create_knowledge_node mcp__tecnologia-morelos__update_knowledge_node mcp__tecnologia-morelos__create_knowledge_base
---

# Charter — Gate 0 Project Foundation Documents

## When to use

- Starting a new project (Gate 0)
- User says "create a project charter", "start a new project", "write the SOW"
- As part of the dispatch: `kb-read → charter → governance`

## Documents produced

1. **Project Charter** — Authorization and scope definition
2. **SOW (Statement of Work)** — Internal work agreement with deliverables
3. **Acerca de** — Public-facing overview page for the project

Templates are in `templates/` as reference. Generate content adapted to the
specific project — do not copy templates verbatim.

## Workflow

### 1. Check existing documents
```
kb-read: search for "[Project Name]" in TM
  → If KB exists, list existing nodes
  → If charter/SOW/about already exist, inform user and ask how to proceed
```

### 2. Gather project information

Ask the user for (if not already provided):
- Nombre del proyecto
- Sponsor / Owner
- Problema que resuelve
- Objetivos principales
- Alcance esperado
- Presupuesto estimado (si aplica)
- Timeline esperado

### 3. Generate documents

Generate each document using the templates as structure reference:
1. Project Charter (see `templates/project-charter.md`)
2. SOW (see `templates/sow.md`)
3. Acerca de (see `templates/about.md`)

Present each document to the user for review before publishing.

### 4. Review

Use the `review` skill mentally — present the 4Ds questions relevant to each
document type. Wait for explicit approval.

### 5. Publish to TM

After approval, use `kb-publish` conventions to create nodes in TM:
- All three documents go at the KB root level (see [kb-structure.md](../../kb-structure.md))
- Document type: `PAGE` for all three
- Include AI transparency footer

## KB structure reference

```
📚 [Project Name]
├── 📄 Acerca de          (PAGE)
├── 📄 Project Charter    (PAGE)
└── 📄 SOW                (PAGE)
```

## Rules

- **Never publish without approval** — Always present drafts first
- **Check before creating** — Use kb-read to avoid duplicates
- **Objectives must be SMART** — Specific, Measurable, Achievable, Relevant, Time-bound
- **AI transparency footer** — Required on every document
