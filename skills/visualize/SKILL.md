---
name: visualize
description: >
  Gate 2 skill. Generates architecture and design diagrams using Mermaid
  (C4 Context, C4 Container, ERD, Deployment) and Excalidraw (User Flows,
  Sequences, Wireframes). Reads Architecture Overview for context.
  Publishes to TM after approval.
allowed-tools: Read Grep mermaid_validate mcp__tecnologia-morelos__list_knowledge_nodes mcp__tecnologia-morelos__list_knowledge_node_children mcp__tecnologia-morelos__get_knowledge_node mcp__tecnologia-morelos__get_document_context mcp__tecnologia-morelos__hybrid_search mcp__tecnologia-morelos__create_knowledge_node mcp__tecnologia-morelos__update_knowledge_node mcp__excalidraw__create-element mcp__excalidraw__get-all-elements mcp__excalidraw__update-element mcp__excalidraw__delete-element mcp__excalidraw__export-scene mcp__excalidraw__get-scene-info
---

# Visualize — Architecture & Design Diagrams

## When to use

- User asks to create diagrams for a project
- After architecture documentation is written (or in parallel)
- User says "create diagrams", "visualize the architecture", "draw the flows"
- As part of the dispatch: `visualize`

## Prerequisites

- **Architecture Overview should exist** (or be in progress) for context.
  Use kb-read to check. If missing, can generate diagrams from PRD/Functional Spec
  but warn the user that diagrams may need updating after architecture is documented.

## Diagrams produced

### Mermaid (structured, code-generatable)

| Diagram | Purpose | Guide |
|---------|---------|-------|
| C4 Context | System and external actors | `diagram-guides/c4-mermaid-guide.md` |
| C4 Container | Internal containers/services | `diagram-guides/c4-mermaid-guide.md` |
| ERD | Data model relationships | `diagram-guides/erd-mermaid-guide.md` |
| Deployment Architecture | Infrastructure layout | Flowchart with deployment nodes |

### Excalidraw (freeform, visual communication)

| Diagram | Purpose | Guide |
|---------|---------|-------|
| User Flows | Step-by-step user journeys | `diagram-guides/excalidraw-guide.md` |
| Sequences | Actor-system interactions | `diagram-guides/excalidraw-guide.md` |
| Wireframes | Basic screen layouts | `diagram-guides/excalidraw-guide.md` |

## Workflow

### 1. Read context

Read from TM:
- **Architecture Overview** → system context, building blocks, deployment
- **Functional Spec** → user flows, data model
- **PRD** → user stories, key features
- **Crosscutting Concepts** → domain model, patterns

### 2. Determine which diagrams to generate

If the user requests specific diagrams, generate those.
If the user says "create all diagrams", generate all seven.
Recommend an order based on dependencies:

1. C4 Context → C4 Container (structural, top-down)
2. ERD (data model)
3. Deployment Architecture (infrastructure)
4. User Flows (behavioral)
5. Sequences (detailed interactions)
6. Wireframes (UI)

### 3. Generate Mermaid diagrams

For each Mermaid diagram:
1. Read the corresponding guide in `diagram-guides/`
2. Generate the Mermaid code following the guide conventions
3. Validate with `mermaid_validate` before presenting
4. Present the rendered diagram to the user

**Important Mermaid rules for TM**:
- Mermaid code blocks must be OUTSIDE any Markdoc component
- Use ```` ```mermaid ```` code fence
- Keep diagrams focused — split large diagrams into multiple smaller ones
- Include a title and brief description above each diagram

### 4. Generate Excalidraw diagrams

For each Excalidraw diagram:
1. Read the guide at `diagram-guides/excalidraw-guide.md`
2. Use the Excalidraw MCP tools to create elements
3. Follow the patterns described in the guide
4. Export and present to the user

### 5. Present for review

Present all diagrams to the user. Ask:
- Do the diagrams accurately represent the architecture?
- Are any components or flows missing?
- Is the level of detail appropriate?

**Do NOT publish until the user explicitly approves.**

### 6. Publish to TM (kb-publish)

After approval:
1. Ensure "Fase 2 — Design & Plan/Diagramas" folder exists
2. Create a PAGE for each diagram in TM
3. Mermaid diagrams: include the code block directly in the page content
4. Excalidraw diagrams: export and embed or link

## Output

| Document | Location in TM | Type | Tool |
|----------|----------------|------|------|
| C4 Context | `[KB]/Fase 2 — Design & Plan/Diagramas/C4 Context` | PAGE | Mermaid |
| C4 Container | `[KB]/Fase 2 — Design & Plan/Diagramas/C4 Container` | PAGE | Mermaid |
| ERD | `[KB]/Fase 2 — Design & Plan/Diagramas/ERD` | PAGE | Mermaid |
| Deployment Architecture | `[KB]/Fase 2 — Design & Plan/Diagramas/Deployment Architecture` | PAGE | Mermaid |
| User Flows | `[KB]/Fase 2 — Design & Plan/Diagramas/User Flows` | PAGE | Excalidraw |
| Sequences | `[KB]/Fase 2 — Design & Plan/Diagramas/Sequences` | PAGE | Excalidraw |
| Wireframes | `[KB]/Fase 2 — Design & Plan/Diagramas/Wireframes` | PAGE | Excalidraw |

## Notes

- Prefer Mermaid for structural diagrams (architecture, data, deployment) — they are version-controllable and auto-renderable.
- Prefer Excalidraw for behavioral and UI diagrams (flows, wireframes) — the hand-drawn style communicates "this is a draft" effectively.
- Each diagram should be self-contained with a title and brief legend if needed.
- For government projects, always include the citizen as an external actor in C4 Context.
- ERDs should reflect the domain model from Crosscutting Concepts.
