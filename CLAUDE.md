# Tecnología Morelos Workflow

Plugin for documenting and planning Tecnología del Estado de Morelos projects.
Publishes documentation to tecnologia.morelos.gob.mx and organizes work in Linear.

## How this plugin works

You are the agent. The user tells you what they need. You use the skills in this
plugin as tools to accomplish their goals. Skills are not steps in a pipeline —
they are capabilities you invoke based on context.

The user might say:
- "Start a new project called Trámites Digitales" → use charter + governance skills
- "I need the discovery report for project X" → use kb-read to check if it exists, then discover
- "Document the architecture" → use document + visualize skills
- "Set up Linear for this project" → use plan skill
- "What's the status of project X?" → use kb-read to check what docs exist

## Pipeline and gates

Projects follow this flow. Each gate requires **human approval** before proceeding.

```
GATE 0 (Authorization)
  → charter: Project Charter, SOW, About
  → governance: Stakeholder Register, RACI, Communication Plan, Regulations
  → Human approves ✓

GATE 1 (Discovery approved)
  → discover: Discovery Report, Glossary
  → spec: PRD, Functional Spec, Quality Requirements, Privacy Impact, DoD draft
  → Human approves ✓

GATE 2 (Plan approved)
  → document: Architecture, Crosscutting, Security, Testing, Risks, KPIs
  → visualize: C4, ERD (Mermaid), User Flows, Wireframes (Excalidraw)
  → plan: Linear Product Structure, Project Configs, Milestones, Epics
  → Human approves ✓
```

Before starting a gate, verify that the previous gate's documents exist in TM
using the kb-read skill. If they don't exist, inform the user.

## Core rules

1. **AI proposes, user confirms** — Never create or modify anything in TM or
   Linear without presenting the proposal first and getting explicit approval.
   Show what you will create, let the user modify it, then execute.

2. **Check before creating** — Always use kb-read to verify if a document or
   KB already exists before creating a new one. Avoid duplicates.

3. **KB is the single source of truth** — Documents live in TM. Linear tracks
   execution. When there's a conflict, TM is authoritative.

4. **Team/Project = user input** — When interacting with Linear, present
   available teams/projects and ask which one to use. Never hardcode or infer.

5. **AI transparency** — Every generated document includes a footer:
   `Generado con AI (tecnologia-morelos-workflow v0.1.0), revisado por [nombre]`

## AI Fluency (4Ds)

This plugin follows the AI Fluency Framework:

- **Delegation**: Gates are delegation points. AI produces drafts, human approves.
- **Description**: Each skill is a focused, decomposed task with clear input/output.
- **Discernment**: The review skill helps humans evaluate AI output quality.
- **Diligence**: Change Log and ADRs track what was AI-generated vs human-decided.

After generating any document, ask the user to review it using these questions:
- Is the information accurate and complete?
- Are there assumptions the AI made that are incorrect?
- What would you change or add?

## KB structure

For the complete folder/document structure that this plugin generates in TM,
see [kb-structure.md](kb-structure.md).

## Dispatch table

| User intent | Skills to use |
|-------------|---------------|
| Start a new project | kb-read → charter → governance |
| Investigate / discover a project | kb-read → discover |
| Write specs / requirements | kb-read → spec |
| Document architecture | kb-read → document |
| Create diagrams | visualize |
| Set up Linear | kb-read → plan |
| Record a decision | adr |
| Check project status | kb-read |
| Review a document | review |
| Redactar / revisar comunicación ciudadana | voice |
| Publish to TM | voice → kb-publish |

## MCP servers

- **tecnologia-morelos**: Data and KB management at tecnologia.morelos.gob.mx
- **linear**: Project tracking, teams, issues
- **excalidraw**: Interactive diagrams (User Flows, Wireframes, Sequences)

## TM MCP gotchas

- Use `id` (not `nodeId`) for `update_knowledge_node` and `move_knowledge_node`
- Use `nodeId` for `get_knowledge_node`
- `hybrid_search` works well for finding content. `search_knowledge` does NOT rank by relevance.
- Code blocks must be OUTSIDE Markdoc components (`{% accordion %}`, `{% step %}`, `{% card %}`)
- Mermaid diagrams must be OUTSIDE any Markdoc component
- `{% codegroup %}` is the ONLY component that accepts code blocks inside
