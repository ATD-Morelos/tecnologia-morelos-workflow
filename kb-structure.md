# KB Structure — Tecnología Morelos

This is the canonical folder/document structure that this plugin generates
in tecnologia.morelos.gob.mx for each project.

Every skill references this file to know what nodes to create in TM.

## Structure

```
📚 [Project Name] (Knowledge Base in TM)
│
│── ── GATE 0: Authorization ── ──
│
├── 📄 Acerca de                        (PAGE)
├── 📄 Project Charter                  (PAGE)
├── 📄 SOW                              (PAGE)
├── 📄 Glosario                         (PAGE)
├── 📄 Stakeholder Register             (PAGE)
├── 📄 RACI                             (PAGE)
├── 📄 Communication Plan               (PAGE)
├── 📄 Normatividad Aplicable           (PAGE)
│
│── ── GATE 1: Discovery approved ── ──
│
├── 📁 Fase 1 — Discovery & Spec/      (FOLDER)
│   ├── 📄 Discovery Report             (PAGE)
│   ├── 📄 PRD                          (PAGE)
│   ├── 📄 Functional Spec              (PAGE)
│   ├── 📄 Quality Requirements         (PAGE)
│   ├── 📄 Privacy Impact Assessment    (PAGE) — if personal data
│   └── 📄 Definition of Done (draft)   (PAGE)
│
│── ── GATE 2: Plan approved ── ──
│
├── 📁 Fase 2 — Design & Plan/         (FOLDER)
│   ├── 📄 Architecture Overview        (PAGE)
│   ├── 📄 Crosscutting Concepts        (PAGE)
│   ├── 📄 Definition of Done (final)   (PAGE)
│   ├── 📄 Risks & Technical Debt       (PAGE)
│   ├── 📄 Security / Threat Model      (PAGE)
│   ├── 📄 Testing Strategy             (PAGE)
│   ├── 📄 Measurement / KPIs           (PAGE)
│   ├── 📁 Diagramas/                   (FOLDER)
│   │   ├── 📄 C4 Context              (PAGE) — Mermaid
│   │   ├── 📄 C4 Container            (PAGE) — Mermaid
│   │   ├── 📄 ERD                     (PAGE) — Mermaid
│   │   ├── 📄 User Flows             (PAGE) — Excalidraw
│   │   ├── 📄 Sequences              (PAGE) — Excalidraw
│   │   ├── 📄 Wireframes             (PAGE) — Excalidraw
│   │   └── 📄 Deployment Architecture (PAGE) — Mermaid
│   └── 📄 API Reference               (API_REFERENCE)
│
├── 📁 ADRs/                            (FOLDER)
│   ├── 📄 ADR-001                      (PAGE)
│   ├── 📄 ADR-002                      (PAGE)
│   └── 📄 ...
│
├── 📁 Linear/                          (FOLDER)
│   ├── 📄 Product Structure            (PAGE)
│   ├── 📄 Labels & Workflow States     (PAGE)
│   └── 📁 [Product Name]/             (FOLDER)
│       ├── 📄 Project Config           (PAGE)
│       ├── 📄 Milestones               (PAGE)
│       ├── 📄 Epics                    (PAGE)
│       └── 📄 User Stories             (PAGE)
│
└── 📄 Change Log                       (PAGE)
```

## Node types in TM

- `FOLDER` — container node, no documentType
- `DOCUMENT` with `documentType`:
  - `PAGE` — general content (most common)
  - `GUIDE` — step-by-step guide
  - `API_REFERENCE` — OpenAPI / technical reference

## Gates

- **Gate 0**: Project Charter and SOW must exist and be approved before Phase 1.
- **Gate 1**: Discovery Report must exist and be approved before Phase 2.
- **Gate 2**: Architecture Overview and Linear Product Structure must exist and be approved before execution.

## Diagram tools

| Diagram | Tool | Why |
|---------|------|-----|
| C4 Context, C4 Container, ERD, Deployment | **Mermaid** | Structured, code-generatable, version-controllable |
| User Flows, Sequences, Wireframes | **Excalidraw** | Freeform, visual communication, hand-drawn style |

## Markdoc rules (TM renderer)

- Code blocks (triple backtick) must be OUTSIDE `{% accordion %}`, `{% step %}`, `{% card %}`
- `{% codegroup %}` is the ONLY component that accepts code blocks inside
- Mermaid diagrams must be OUTSIDE any Markdoc component
- Use `id` (not `nodeId`) for `update_knowledge_node`
- Use `nodeId` for `get_knowledge_node`
