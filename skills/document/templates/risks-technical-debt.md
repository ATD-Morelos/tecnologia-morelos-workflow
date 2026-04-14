# Risks & Technical Debt — [Nombre del Proyecto]

## Registro de riesgos

### Matriz de evaluación

| | Impacto bajo | Impacto medio | Impacto alto | Impacto critico |
|---|---|---|---|---|
| **Probabilidad alta** | Medio | Alto | Crítico | Crítico |
| **Probabilidad media** | Bajo | Medio | Alto | Crítico |
| **Probabilidad baja** | Bajo | Bajo | Medio | Alto |

### Riesgos identificados

| ID | Descripción | Categoría | Probabilidad | Impacto | Riesgo | Estrategia | Owner | Estado | Fecha |
|----|-------------|-----------|--------------|---------|--------|------------|-------|--------|-------|
| R01 | [Descripción del riesgo] | [Técnico / Organizacional / Externo / Legal] | [Alta/Media/Baja] | [Crítico/Alto/Medio/Bajo] | [Crítico/Alto/Medio/Bajo] | [Mitigar] | [Nombre] | [Abierto] | [Fecha] |
| R02 | [Descripción del riesgo] | [Categoría] | [Probabilidad] | [Impacto] | [Riesgo] | [Aceptar] | [Nombre] | [Abierto] | [Fecha] |
| R03 | [Descripción del riesgo] | [Categoría] | [Probabilidad] | [Impacto] | [Riesgo] | [Transferir] | [Nombre] | [Abierto] | [Fecha] |
| R04 | [Descripción del riesgo] | [Categoría] | [Probabilidad] | [Impacto] | [Riesgo] | [Evitar] | [Nombre] | [Abierto] | [Fecha] |

### Detalle de riesgos criticos y altos

#### R01 — [Titulo del riesgo]

- **Descripción**: [Descripción detallada del riesgo]
- **Causa raiz**: [Que origina este riesgo]
- **Impacto si se materializa**: [Que pasa si ocurre]
- **Estrategia de mitigación**:
  1. [Accion 1]
  2. [Accion 2]
  3. [Accion 3]
- **Indicadores de alerta temprana**: [Senales de que el riesgo se esta materializando]
- **Plan de contingencia**: [Que hacer si el riesgo se materializa]

### Estrategias de manejo

| Estrategia | Cuando usar | Ejemplo |
|------------|-------------|---------|
| **Mitigar** | Se puede reducir probabilidad o impacto | Implementar redundancia para reducir riesgo de downtime |
| **Aceptar** | Costo de mitigación supera el impacto | Aceptar riesgo de baja probabilidad con plan de contingencia |
| **Transferir** | Otro puede manejar mejor el riesgo | Contratar seguro, usar servicio managed |
| **Evitar** | Se puede eliminar cambiando el enfoque | Cambiar tecnologia para evitar dependencia riesgosa |

## Registro de deuda tecnica

### Deuda identificada

| ID | Descripción | Origen | Impacto | Esfuerzo estimado | Prioridad | Sprint tentativo |
|----|-------------|--------|---------|-------------------|-----------|------------------|
| TD01 | [Descripción de la deuda] | [Decision de diseño / Shortcut / Legacy] | [Alto/Medio/Bajo] | [XS/S/M/L/XL] | [P1/P2/P3] | [Sprint N] |
| TD02 | [Descripción de la deuda] | [Origen] | [Impacto] | [Esfuerzo] | [Prioridad] | [Sprint N] |
| TD03 | [Descripción de la deuda] | [Origen] | [Impacto] | [Esfuerzo] | [Prioridad] | [Backlog] |

### Detalle de deuda de alta prioridad

#### TD01 — [Titulo de la deuda]

- **Descripción**: [Que es la deuda y por que existe]
- **Impacto en el proyecto**:
  - [Afecta velocidad de desarrollo en X%]
  - [Aumenta riesgo de bugs en modulo Y]
  - [Dificulta onboarding de nuevos desarrolladores]
- **Plan de remediacion**:
  1. [Paso 1]
  2. [Paso 2]
  3. [Paso 3]
- **Costo de no remediar**: [Que pasa si se deja la deuda]

### Clasificacion de esfuerzo

| Tamano | Estimacion | Ejemplo |
|--------|-----------|---------|
| XS | < 2 horas | Renombrar variable, fix typo en config |
| S | 2-8 horas | Refactor de un modulo pequeno |
| M | 1-3 dias | Refactor de un servicio, agregar tests |
| L | 1-2 semanas | Migrar a nueva libreria, redisenar componente |
| XL | > 2 semanas | Reescritura de modulo, cambio de arquitectura |

## Revision periodica

- **Frecuencia**: [Quincenal / Al inicio de cada sprint]
- **Participantes**: [Tech Lead, Product Owner, QA Lead]
- **Proceso**:
  1. Revisar riesgos existentes — actualizar estado y probabilidad
  2. Identificar nuevos riesgos
  3. Revisar deuda tecnica — repriorizar segun impacto actual
  4. Decidir que deuda abordar en el siguiente sprint
  5. Actualizar este documento

---
Generado con AI (tecnologia-morelos-workflow v0.1.0), revisado por [nombre]
