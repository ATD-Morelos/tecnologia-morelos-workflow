---
name: discover
description: >
  Investigate a project to produce a Discovery Report and draft Glossary.
  Researches context, stakeholders, systems, and risks. Outputs go into
  the "Fase 1 — Discovery & Spec" folder in TM.
when_to_use: "User says 'investigate project', 'discovery report', 'research project', 'what is this project about'"
argument-hint: "[project-name]"
allowed-tools: Read Grep Glob WebSearch mcp__tecnologia-morelos__list_projects mcp__tecnologia-morelos__list_knowledge_bases mcp__tecnologia-morelos__list_knowledge_nodes mcp__tecnologia-morelos__list_knowledge_node_children mcp__tecnologia-morelos__get_knowledge_node mcp__tecnologia-morelos__get_document_context mcp__tecnologia-morelos__hybrid_search mcp__tecnologia-morelos__semantic_search mcp__tecnologia-morelos__find_related_knowledge mcp__tecnologia-morelos__get_knowledge_relations mcp__tecnologia-morelos__get_knowledge_tree mcp__tecnologia-morelos__get_knowledge_base_graph_summary
---

# Discover — Discovery Report & Glossary

## When to use

- User asks to investigate, discover, or research a project
- Starting Phase 1 (Gate 1) for a project
- User wants to understand what a project is about before writing specs

## Prerequisites

- **Gate 0 approved**: Project Charter and SOW must exist in TM.
  Use kb-read to verify. If missing, inform the user and stop.

## Pipeline

### 1. Receive project input

Get the project name and description from the user. Clarify scope if ambiguous.

### 2. Check existing KB (kb-read)

Use kb-read to verify:
- Does a KB for this project exist?
- Does a "Fase 1 — Discovery & Spec" folder exist?
- Does a Discovery Report already exist?

If the Discovery Report already exists, ask the user if they want to update it
or start fresh.

### 3. Read existing context

If Gate 0 docs exist, read them for context:
- Project Charter → objectives, scope, constraints
- SOW → deliverables, timeline
- Stakeholder Register → known stakeholders
- Glosario → existing terminology

### 4. Research

Gather information from multiple sources:

- **TM MCP**: Search for related projects, existing documentation, regulations
- **Codebase** (if exists): Use Glob/Grep/Read to explore project structure,
  tech stack, existing patterns
- **Web** (if needed): Use WebSearch for regulatory context, best practices,
  technology references

Focus on answering:
- What problem does this project solve?
- Who are the stakeholders?
- What systems are involved?
- What data flows exist or will exist?
- What risks are apparent?

### 5. Generate Discovery Report

Use the template at [templates/discovery-report.md](templates/discovery-report.md) as a
structural reference. Generate real content based on research findings.

Every section must contain substantive findings, not placeholders.

### 6. Generate Glossary draft

Use the template at [templates/glossary.md](templates/glossary.md) as a structural
reference. Extract domain terms found during research.

Include terms from:
- Existing Glosario (if found in Gate 0 docs)
- Technical terms from codebase exploration
- Domain terms from stakeholder documents
- Regulatory/legal terms

### 7. Present for review (AI Fluency — Discernment)

Present both documents to the user. Ask:
- Is the information accurate and complete?
- Are there assumptions the AI made that are incorrect?
- What would you change or add?
- Are any stakeholders or systems missing?

**Do NOT publish until the user explicitly approves.**

### 8. Publish to TM

After approval, delegate publishing to the kb-publish skill:
1. Ensure the "Fase 1 — Discovery & Spec" folder exists (create if needed)
2. Create/update the Discovery Report node in TM
3. Update the Glosario node at the KB root level (per kb-structure.md)
4. Add the AI transparency footer to both documents

For the full KB structure, see [kb-structure.md](../../kb-structure.md).

## Output

| Document | Location in TM | Type |
|----------|----------------|------|
| Discovery Report | `[KB]/Fase 1 — Discovery & Spec/Discovery Report` | PAGE |
| Glosario | `[KB]/Glosario` | PAGE |

## Notes

- The Glossary lives at the KB root, not inside Phase 1, because it spans all phases.
- If the user provides existing documents (PDFs, links), incorporate them into the research.
- Keep findings factual. Flag assumptions explicitly.
