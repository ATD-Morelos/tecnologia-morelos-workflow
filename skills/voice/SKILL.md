---
name: voice
description: >
  Aplica y valida la guía de voz y tono institucional del Gobierno del Estado
  de Morelos (Clara, Cercana, Confiable) a cualquier texto dirigido a la
  ciudadanía: comunicados, notificaciones, páginas en TM, respuestas y
  mensajes cortos. Redacta desde cero o audita texto existente.
allowed-tools: []
---

# Voice — Voz y Tono Institucional de Morelos

## Promesa de marca

> La comunicación gubernamental que el ciudadano merece.

Todo texto dirigido a ciudadanía debe sostenerse en tres pilares:

- **Clara** — Sin tecnicismos ni ambigüedades.
- **Cercana** — Habla de tú, sin burocracia.
- **Confiable** — Compromisos con fecha real.

## Cuándo usar este skill

- Al redactar comunicados, avisos, notificaciones, FAQs, respuestas ciudadanas o mensajes cortos (push/SMS/banner).
- Al revisar o auditar cualquier texto que se publicará en TM o en canales públicos.
- Como paso previo obligatorio antes de `kb-publish` cuando el documento es dirigido a ciudadanía.
- Como complemento del skill `review` para documentos con audiencia externa.

## Flujo

### A. Redactar desde cero
1. Leer [principios.md](principios.md) para fijar los tres pilares.
2. Elegir una plantilla en [templates/](templates/) según el canal.
3. Rellenar con los datos que aporte el usuario. Si falta una fecha absoluta, un responsable o una acción concreta, preguntar antes de inventar.
4. Aplicar [checklist.md](checklist.md) al borrador.
5. Presentar el texto al usuario, destacar supuestos y esperar confirmación.

### B. Revisar texto existente
1. Leer [checklist.md](checklist.md) y recorrerla punto por punto sobre el texto original.
2. Identificar burocratismos con [patrones.md](patrones.md) y proponer reemplazos.
3. Entregar una versión **antes / después** marcando qué pilar (Clara / Cercana / Confiable) motivó cada cambio.
4. Pedir aprobación explícita antes de sobrescribir en TM.

## Regla AI propone, usuario confirma

Nunca publicar ni modificar contenido en TM u otros canales sin aprobación explícita. Mostrar cambios, permitir al usuario ajustarlos y recién entonces ejecutar con `kb-publish`.

## Footer obligatorio

Todo documento publicado debe terminar con:

```
---
Generado con AI (tecnologia-morelos-workflow v0.1.0), revisado por [nombre]
```

## Archivos de referencia

- [principios.md](principios.md) — Clara / Cercana / Confiable con do / don't.
- [checklist.md](checklist.md) — Lista binaria de verificación pre-publicación.
- [patrones.md](patrones.md) — Burocratismos prohibidos con equivalentes ciudadanos.
- [ejemplos.md](ejemplos.md) — Ejemplos completos antes / después por canal.
- [templates/](templates/) — Plantillas por canal (comunicado, notificación, respuesta, CTA corto).
