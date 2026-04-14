---
name: governance
description: >
  Gate 0 skill. Generates four governance documents for a project: Stakeholder
  Register, RACI Matrix, Communication Plan, and Applicable Regulations
  (Normatividad Aplicable). Checks TM for existing documents before creating,
  presents drafts for human review, and publishes to TM after approval.
allowed-tools: mcp__tecnologia-morelos__get_knowledge_node mcp__tecnologia-morelos__list_knowledge_nodes mcp__tecnologia-morelos__hybrid_search mcp__tecnologia-morelos__create_knowledge_node mcp__tecnologia-morelos__update_knowledge_node mcp__tecnologia-morelos__create_knowledge_base
---

# Governance — Gate 0 Governance Documents

## When to use

- Starting a new project (Gate 0), after charter documents are created
- User says "set up governance", "who are the stakeholders", "create the RACI"
- As part of the dispatch: `kb-read → charter → governance`

## Documents produced

1. **Stakeholder Register** — Who is involved and how to engage them
2. **RACI Matrix** — Who is Responsible, Accountable, Consulted, Informed
3. **Communication Plan** — How, when, and to whom to communicate
4. **Normatividad Aplicable** — Laws and regulations that apply to the project

Templates are in `templates/` as reference. Generate content adapted to the
specific project — do not copy templates verbatim.

## Workflow

### 1. Check existing documents
```
kb-read: search for "[Project Name]" in TM
  → If governance docs already exist, inform user and ask how to proceed
  → Verify that charter documents exist (prerequisite)
```

### 2. Gather governance information

Ask the user for (if not already provided):
- Lista de stakeholders conocidos
- Estructura organizacional del proyecto
- Canales de comunicación preferidos
- Normatividad específica que aplica al proyecto

Use the Project Charter and SOW as input — they contain scope, team, and
objectives that inform governance documents.

### 3. Generate documents

Generate each document using the templates as structure reference:
1. Stakeholder Register (see `templates/stakeholder-register.md`)
2. RACI Matrix (see `templates/raci.md`)
3. Communication Plan (see `templates/communication-plan.md`)
4. Normatividad Aplicable (see `templates/applicable-regulations.md`)

Present each document to the user for review before publishing.

### 4. Review

Use the `review` skill mentally — present relevant 4Ds questions.
Wait for explicit approval on each document.

### 5. Publish to TM

After approval, use `kb-publish` conventions to create nodes in TM:
- All four documents go at the KB root level (see [kb-structure.md](../../kb-structure.md))
- Document type: `PAGE` for all four
- Include AI transparency footer

## KB structure reference

```
📚 [Project Name]
├── 📄 Stakeholder Register       (PAGE)
├── 📄 RACI                       (PAGE)
├── 📄 Communication Plan         (PAGE)
└── 📄 Normatividad Aplicable     (PAGE)
```

## Rules

- **Charter first** — Governance documents depend on charter info. If charter
  doesn't exist, inform the user and suggest creating it first.
- **Never publish without approval** — Always present drafts first
- **Check before creating** — Use kb-read to avoid duplicates
- **Regulations must be current** — Verify that referenced laws and norms are
  still in effect. When in doubt, flag for the user to verify.
- **AI transparency footer** — Required on every document
