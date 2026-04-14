# Labels & Workflow States — [Nombre del Proyecto]

## Labels (ADR-008)

### Phase Labels

| Label | Descripción | Color sugerido |
|-------|-------------|----------------|
| `phase:discover` | Trabajo de discovery e investigación | 🔵 Blue |
| `phase:spec` | Especificaciones y requerimientos | 🟣 Purple |
| `phase:plan` | Planificación y diseño | 🟡 Yellow |
| `phase:build` | Desarrollo e implementación | 🟢 Green |
| `phase:release` | Release y deployment | 🔴 Red |

### Type Labels

| Label | Descripción | Color sugerido |
|-------|-------------|----------------|
| `type:feature` | Nueva funcionalidad | 🟢 Green |
| `type:chore` | Tarea técnica sin impacto visible al usuario | ⚪ Gray |
| `type:bug` | Corrección de defecto | 🔴 Red |
| `type:planning` | Tarea de planificación o coordinación | 🟡 Yellow |
| `type:docs` | Documentación | 🔵 Blue |

### MoSCoW Labels

| Label | Descripción | Color sugerido |
|-------|-------------|----------------|
| `must-have` | Requerimiento esencial para MVP | 🔴 Red |
| `should-have` | Importante pero no bloqueante para MVP | 🟠 Orange |
| `could-have` | Deseable si hay tiempo/recursos | 🟡 Yellow |
| `post-mvp` | Para versiones futuras | ⚪ Gray |

## Workflow States

| # | Estado | Descripción | Criterio de entrada | Criterio de salida |
|---|--------|-------------|---------------------|--------------------|
| 1 | **Triage** | Issue recién creado, necesita clasificación | Issue creado | Labels asignados, estimación definida |
| 2 | **Backlog** | Clasificado, esperando priorización | Triaged | Priorizado para un ciclo |
| 3 | **Todo** | Priorizado para el ciclo actual | En ciclo activo | Asignado a alguien |
| 4 | **In Progress** | En desarrollo activo | Alguien está trabajando | PR listo para review |
| 5 | **In Review** | En revisión de código o QA | PR enviado | Review aprobado, QA pasado |
| 6 | **Done** | Completado y desplegado | Merged, deployed | N/A |
| 7 | **Cancelled** | Descartado o ya no aplica | Decisión del equipo | N/A |

## Estimation Convention

[Definir la convención de estimación del equipo. Opciones comunes:]

- **Story Points (Fibonacci):** 1, 2, 3, 5, 8, 13
  - 1 = trivial (< 1 hora)
  - 2 = pequeño (medio día)
  - 3 = mediano (1 día)
  - 5 = grande (2-3 días)
  - 8 = muy grande (1 semana)
  - 13 = demasiado grande, descomponer

[O bien T-shirt sizing: XS, S, M, L, XL]

## Notas

- Los labels se crean una vez por team en Linear y se reutilizan entre proyectos
- Verificar labels existentes antes de crear nuevos para evitar duplicados
- Los workflow states son configuración del team, no del proyecto

---
Generado con AI (tecnologia-morelos-workflow v0.1.0), revisado por [nombre]
