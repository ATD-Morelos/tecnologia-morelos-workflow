---
name: manual-ciudadano
description: >
  Convierte una ficha técnica de un trámite o servicio en un Manual de Uso
  ciudadano publicable en Tecnología Morelos. Aplica automáticamente la voz
  institucional (Clara, Cercana, Confiable) y genera Markdoc con los
  componentes nativos de TM: steps, accordion, cardgroup y video embed.
  El output va a la sección de manuales del proyecto en TM.
argument-hint: "[nombre-tramite]"
allowed-tools: Read Glob mcp__tecnologia-morelos__list_projects mcp__tecnologia-morelos__list_knowledge_bases mcp__tecnologia-morelos__list_knowledge_nodes mcp__tecnologia-morelos__list_knowledge_node_children mcp__tecnologia-morelos__get_knowledge_node mcp__tecnologia-morelos__hybrid_search mcp__tecnologia-morelos__create_knowledge_node mcp__tecnologia-morelos__update_knowledge_node
---

# manual-ciudadano — Generador de Manuales de Uso para Ciudadanía

## Cuándo usar este skill

- Usuario quiere crear o actualizar un manual de uso de un trámite o servicio
- Se cuenta con una ficha técnica (información estructurada del trámite)
- El output va a la sección **Manuales** del KB del proyecto en TM

## Estructura del manual generado

Cada manual sigue esta estructura fija en el orden indicado. No omitir secciones,
no reordenar:

| # | Sección | Componente TM |
|---|---------|---------------|
| 1 | Introducción | Markdown estándar (párrafo + lista) |
| 2 | Antes de iniciar | Checklist `- [ ]` + bloque `> ` para avisos |
| 3 | Paso a Paso | `{% steps %}` + `{% step title="..." %}` |
| 4 | Video Tutorial | `{% video src="URL" title="TITLE" /%}` *(ver nota)* |
| 5 | Preguntas Frecuentes | `{% accordion title="¿Pregunta?" %}` por cada Q&A |
| 6 | CTA + Artículos relacionados | `{% cardgroup %}` + `{% card %}` |

> **Nota Video**: El componente `{% video %}` está pendiente de implementación
> en `kb-publish`. Si aún no está disponible, usar un `{% card %}` con el link
> al video como placeholder hasta que se active el componente.

## Flujo

### 1. Recibir la ficha técnica

Leer `ficha-tecnica-schema.md` para saber qué campos son obligatorios.
Si el usuario no proporcionó la ficha completa, preguntar los campos faltantes
**antes** de generar el manual. No inventar datos del trámite.

Campos mínimos obligatorios:
- Nombre del trámite
- Dependencia responsable
- URL del trámite
- Audiencia (persona física / moral / ambas)
- Requisitos previos (al menos 3)
- Pasos del proceso (al menos 3)
- Al menos 3 preguntas frecuentes con respuesta

### 2. Aplicar voz institucional

Leer estos archivos del skill `voice` antes de redactar:
- `../voice/principios.md` — pilares Clara / Cercana / Confiable
- `../voice/patrones.md` — burocratismos prohibidos y equivalentes
- `../voice/checklist.md` — lista de verificación

Reglas de voz que aplican siempre en manuales ciudadanos:
- Tutear al ciudadano: "Verifica que...", "Descarga tu...", "Ingresa a..."
- Fechas absolutas, no relativas: ❌ "próximamente" → ✅ "antes del 31 de marzo"
- Sin tecnicismos sin definir: ❌ "AMIS" → ✅ "AMIS (Asociación Mexicana de Instituciones de Seguros)"
- Verbos de acción al inicio de cada paso: "Ingresa", "Captura", "Selecciona", "Descarga"
- Los pasos van numerados con verbo imperativo en el `title` del `{% step %}`

### 3. Generar el manual en Markdoc

Usar `templates/manual-base.md` como estructura base. Sustituir todos los
placeholders `[...]` con el contenido real de la ficha técnica.

Reglas críticas de Markdoc (ver `../kb-publish/markdoc-reference.md`):
- **NO** poner bloques de código dentro de `{% step %}`, `{% accordion %}` o `{% card %}`
- **NO** poner diagramas Mermaid dentro de ningún componente
- Cada `{% accordion %}` contiene solo texto e inline code
- Los links dentro de steps y accordions usan sintaxis Markdown estándar: `[texto](url)`

### 4. Verificar checklist de voz

Antes de presentar el borrador, recorrer `../voice/checklist.md` punto por punto.
Marcar mentalmente cada item. Si hay incumplimientos, corregirlos antes de mostrar.

### 5. Presentar borrador al usuario

Mostrar el manual completo en Markdoc. Indicar:
- Qué campos se completaron con la ficha
- Qué supuestos se hicieron (si alguno)
- Si el componente `{% video %}` está disponible o se usó `{% card %}` como fallback

Esperar aprobación explícita antes de publicar.

### 6. Publicar en TM

Después de aprobación:

1. Usar `kb-read` para localizar el KB del proyecto en TM
2. Navegar a la sección `Manuales/` (o crearla si no existe)
3. Crear el nodo con `create_knowledge_node`:
   - `type`: `PAGE`
   - `title`: `MANUAL DE USO — [Nombre del Trámite]`
   - `content`: el Markdoc generado
4. Confirmar al usuario con el link directo al nodo publicado

## Reglas

- **Nunca publicar sin aprobación** — siempre mostrar el borrador primero
- **Nunca inventar datos del trámite** — URLs, fechas, requisitos vienen de la ficha
- **Respetar el orden de secciones** — no reordenar ni fusionar
- **Un manual por trámite** — si hay variantes (física/moral), generar un manual por cada una
- **Footer obligatorio al publicar**:
  ```
  ---
  Generado con AI (tecnologia-morelos-workflow v0.1.0), revisado por [nombre]
  ```

## Archivos de referencia

- [ficha-tecnica-schema.md](ficha-tecnica-schema.md) — campos de entrada del manual
- [templates/manual-base.md](templates/manual-base.md) — plantilla Markdoc completa
- [ejemplos/refrendo-fisico.md](ejemplos/refrendo-fisico.md) — ejemplo real en formato TM
- [../voice/principios.md](../voice/principios.md) — pilares de voz institucional
- [../voice/patrones.md](../voice/patrones.md) — burocratismos prohibidos
- [../voice/checklist.md](../voice/checklist.md) — checklist pre-publicación
- [../kb-publish/markdoc-reference.md](../kb-publish/markdoc-reference.md) — componentes TM
- [../kb-publish/gotchas.md](../kb-publish/gotchas.md) — errores comunes en TM
