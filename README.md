# tecnologia-morelos-workflow

![version](https://img.shields.io/badge/version-0.1.0-blue)
![license](https://img.shields.io/badge/license-MIT-green)

Plugin de Claude Code para documentar y planear proyectos de tecnología del Gobierno del Estado de Morelos.

Publica documentación estructurada en [tecnologia.morelos.gob.mx](https://tecnologia.morelos.gob.mx) y organiza el trabajo en Linear. Sigue el framework **AI Fluency (4Ds)** — la AI propone, el humano aprueba.

## Pipeline

Cada proyecto pasa por 3 gates con aprobación humana obligatoria:

```
GATE 0 (Autorización)
  → charter: Project Charter, SOW, Acerca de
  → governance: Stakeholder Register, RACI, Communication Plan, Normatividad
  → Humano aprueba ✓

GATE 1 (Discovery aprobado)
  → discover: Discovery Report, Glosario
  → spec: PRD, Functional Spec, Quality Requirements, Privacy Impact, DoD
  → Humano aprueba ✓

GATE 2 (Plan aprobado)
  → document: Architecture, Security, Testing, Risks, KPIs
  → visualize: C4, ERD (Mermaid), User Flows, Wireframes (Excalidraw)
  → plan: Linear Product Structure, Projects, Milestones, Epics
  → Humano aprueba ✓
```

## Skills

| Skill | Fase | Qué genera |
|-------|------|------------|
| **charter** | Gate 0 | Project Charter, SOW, Acerca de |
| **governance** | Gate 0 | Stakeholder Register, RACI, Communication Plan, Normatividad |
| **discover** | Phase 1 | Discovery Report, Glosario |
| **spec** | Phase 1 | PRD, Functional Spec, Quality Requirements, Privacy Impact, DoD |
| **document** | Phase 2 | Architecture, Crosscutting, Security, Testing, Risks, KPIs, API Ref |
| **visualize** | Phase 2 | C4, ERD (Mermaid), User Flows, Wireframes, Sequences (Excalidraw) |
| **plan** | Phase 2 | Product Structure, Project Config, Milestones, Epics, User Stories |
| **adr** | Transversal | Architecture Decision Records |
| **kb-read** | Transversal | Buscar y leer documentos en TM |
| **kb-publish** | Transversal | Crear y editar documentos en TM |
| **review** | Transversal | Revisión guiada de documentos con AI Fluency |

## Requisitos

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) con soporte de plugins
- Acceso a los MCP servers configurados (ver sección MCP Servers)

## Instalación

```bash
git clone https://github.com/ATD-Morelos/tecnologia-morelos-workflow.git
```

Usar el plugin con Claude Code:

```bash
claude --plugin-dir /path/to/tecnologia-morelos-workflow
```

## Uso

El plugin funciona como un agente conversacional. Ejemplos:

```
"Inicia un nuevo proyecto llamado Trámites Digitales"
→ Ejecuta charter + governance (Gate 0)

"Necesito el discovery report del proyecto X"
→ Verifica si existe con kb-read, luego ejecuta discover

"Documenta la arquitectura"
→ Ejecuta document + visualize (Phase 2)

"Configura Linear para este proyecto"
→ Ejecuta plan (Phase 2)
```

## Estructura del proyecto

```
tecnologia-morelos-workflow/
├── .claude-plugin/plugin.json     ← Metadata del plugin
├── CLAUDE.md                      ← Agent principal (dispatch, reglas, pipeline)
├── kb-structure.md                ← Estructura canónica de KB en TM
├── .mcp.json                      ← Configuración de MCP servers
├── skills/
│   ├── charter/                   ← Gate 0: Project Charter, SOW, About
│   ├── governance/                ← Gate 0: Stakeholders, RACI, Comms
│   ├── discover/                  ← Phase 1: Discovery Report, Glossary
│   ├── spec/                      ← Phase 1: PRD, Specs, DoD
│   ├── document/                  ← Phase 2: Architecture, Security, Testing
│   ├── visualize/                 ← Phase 2: C4, ERD, Flows, Wireframes
│   ├── plan/                      ← Phase 2: Linear setup
│   ├── adr/                       ← Transversal: Decision Records
│   ├── kb-read/                   ← Transversal: Leer KB en TM
│   ├── kb-publish/                ← Transversal: Publicar en TM
│   └── review/                    ← Transversal: Revisión con 4Ds
├── hooks/hooks.json
└── settings.json
```

## MCP Servers

| Server | Propósito |
|--------|-----------|
| **tecnologia-morelos** | Knowledge Base y datos en tecnologia.morelos.gob.mx |
| **linear** | Gestión de proyectos, equipos e issues |
| **excalidraw** | Diagramas interactivos (User Flows, Wireframes, Sequences) |

## AI Fluency (4Ds)

Este plugin implementa el framework AI Fluency:

- **Delegation** — Los gates son puntos de delegación. La AI produce borradores, el humano aprueba.
- **Description** — Cada skill es una tarea descompuesta con input/output claro.
- **Discernment** — El skill `review` ayuda a evaluar la calidad del output de la AI.
- **Diligence** — Change Log y ADRs rastrean qué fue generado por AI vs decidido por humanos.

## Licencia

[MIT](LICENSE)

## Autor

**ATDEM** — Agencia de Tecnología Digital del Estado de Morelos
