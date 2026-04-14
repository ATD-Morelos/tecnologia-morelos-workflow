# User Stories — [Nombre del Producto] / [Nombre del Epic]

User stories derivadas del PRD y Functional Spec para implementación en Linear.

## Formato

Cada user story sigue el formato estándar:

> **Como** [rol/persona], **quiero** [capacidad], **para** [beneficio].

## Stories

| ID | Story | Prioridad (MoSCoW) | Criterios de aceptación | Epic | Estimación |
|----|-------|--------------------|------------------------|------|------------|
| US-001 | Como [rol], quiero [capacidad], para [beneficio] | Must | - [Criterio 1]\n- [Criterio 2] | [Epic padre] | [1-13 pts] |
| US-002 | Como [rol], quiero [capacidad], para [beneficio] | Should | - [Criterio 1] | [Epic padre] | [1-13 pts] |

## Convenciones

- **Prioridad**: MoSCoW (Must, Should, Could, Won't para esta iteración)
- **Estimación**: Fibonacci (1, 2, 3, 5, 8, 13). Si >13, descomponer.
- **Criterios de aceptación**: Formato Given/When/Then o checklist simple.
- **Trazabilidad**: Cada story debe referenciar el requerimiento del PRD que implementa.

## Mapeo a Linear

- Cada user story → 1 issue en Linear (sub-issue del epic padre)
- Labels: `Phase: plan`, `Type: Feature` (o `Chore`), `MoSCoW: [prioridad]`
- Si una story tiene >1 tarea ejecutable → crear sub-issues adicionales (ADR-007)

## Notas

- Documentar primero aquí, luego crear en Linear.
- El usuario debe aprobar las stories antes de crearlas en Linear.
- Stories que no caben en esta iteración se marcan como `Won't` con nota de por qué.
