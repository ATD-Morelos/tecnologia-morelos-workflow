# Review Checklist — 4Ds de AI Fluency

Checklist genérico para revisar cualquier documento generado por AI.
Adaptar las preguntas al tipo de documento específico.

## 1. Delegation — ¿Se delegó correctamente?

- [ ] ¿La tarea era apropiada para generación con AI?
- [ ] ¿El alcance del documento es correcto (ni muy amplio ni muy limitado)?
- [ ] ¿Hay secciones que requieren conocimiento experto humano que no se debe delegar?
- [ ] ¿Se proporcionó contexto suficiente al AI para generar esto?

## 2. Description — ¿Se describió bien la tarea?

- [ ] ¿El documento responde a lo que se pidió?
- [ ] ¿Los inputs (nombre del proyecto, contexto, requisitos) fueron suficientes?
- [ ] ¿Faltan datos que mejorarían significativamente el resultado?
- [ ] ¿El formato y estructura son los esperados?

## 3. Discernment — ¿Se evaluó la calidad del output?

### Precisión
- [ ] ¿La información es factualmente correcta?
- [ ] ¿Los datos, cifras y fechas son precisos?
- [ ] ¿No hay "alucinaciones" (información inventada que parece real)?

### Completitud
- [ ] ¿Están todas las secciones requeridas?
- [ ] ¿Falta información crítica?
- [ ] ¿Los stakeholders, riesgos o dependencias relevantes están incluidos?

### Contexto
- [ ] ¿El contenido refleja la realidad del proyecto y del gobierno de Morelos?
- [ ] ¿Los supuestos del AI son correctos?
- [ ] ¿Las referencias a normatividad, procesos o sistemas son válidas?

### Calidad
- [ ] ¿El lenguaje es claro y apropiado para la audiencia?
- [ ] ¿Los objetivos son SMART (si aplica)?
- [ ] ¿Los entregables son medibles y verificables?

## 4. Diligence — ¿Se documentó la trazabilidad?

- [ ] ¿El footer de AI transparency está presente?
- [ ] ¿Queda claro qué fue generado por AI y qué fue decidido por humanos?
- [ ] ¿Las decisiones importantes están documentadas (o se registrarán como ADR)?
- [ ] ¿El documento será publicado en TM como fuente única de verdad?

## Resultado de la revisión

- **Aprobado** → Proceder a publicar en TM con `kb-publish`
- **Requiere cambios** → Listar cambios específicos, regenerar/editar, volver a revisar
- **Rechazado** → Replantear el enfoque, revisar inputs, volver a generar desde cero
