# Ficha Técnica — Schema de Entrada para manual-ciudadano

El usuario debe proporcionar estos datos antes de que Claude genere el manual.
Los campos marcados con `*` son **obligatorios**. Sin ellos, preguntar antes de continuar.

---

## Campos de la ficha técnica

```yaml
# ── IDENTIFICACIÓN ─────────────────────────────────────────────────────────────

nombre_tramite: *        # Nombre oficial del trámite o servicio
                         # Ej: "Refrendo Anual Vehicular Persona Física 2026"

dependencia: *           # Dependencia responsable del trámite
                         # Ej: "Coordinación de Movilidad y Transporte"

audiencia: *             # "persona_fisica" | "persona_moral" | "ambas"
                         # Si es "ambas", generar un manual por cada tipo

url_tramite: *           # URL directa al trámite en línea
                         # Ej: "https://digital.morelos.gob.mx/tramitesdigitales/refrendo-anual"

# ── ANTES DE INICIAR ────────────────────────────────────────────────────────────

requisitos_previos: *    # Lista de lo que el ciudadano debe tener ANTES de empezar
                         # Mínimo 3 items. Cada item = una línea
                         # Ej:
                         #   - Cuenta activa de Llave MX
                         #   - Ser el propietario registrado del vehículo
                         #   - No contar con adeudos de años anteriores

requisitos_documentos: * # Documentos/datos que el ciudadano debe tener a la mano
                         # Ej:
                         #   - Número de placas
                         #   - Últimos 5 dígitos del número de serie
                         #   - INE del propietario (anverso y reverso)

aviso_importante:        # Texto de advertencia especial (opcional)
                         # Ej: "Si ya inició un trámite anteriormente, retómelo
                         #      en Mis Trámites. No genere uno nuevo."

# ── PASO A PASO ─────────────────────────────────────────────────────────────────

pasos: *                 # Lista ordenada de pasos. Cada paso tiene:
                         #   - titulo: verbo imperativo corto (Ej: "Inicia sesión")
                         #   - descripcion: instrucción detallada
                         #   - nota: (opcional) aclaración o advertencia del paso
                         # Mínimo 3 pasos.
                         # Ej:
                         #   - titulo: "Ingresa al portal"
                         #     descripcion: "Ve a digital.morelos.gob.mx/refrendo"
                         #   - titulo: "Inicia sesión con Llave MX"
                         #     descripcion: "Usa tu correo y contraseña de Llave MX..."
                         #     nota: "Si no tienes cuenta, créala en llave.gob.mx"

consideraciones:         # Lista de notas importantes al final del paso a paso (opcional)
                         # Ej:
                         #   - Si ya existe un trámite iniciado, deberás concluirlo
                         #   - No generes una nueva línea de captura si ya pagaste

# ── VIDEO TUTORIAL ───────────────────────────────────────────────────────────────

video_url:               # URL del video tutorial (YouTube, Vimeo, etc.) — opcional
                         # Ej: "https://youtube.com/watch?v=..."

video_titulo:            # Título descriptivo del video — opcional si hay url
                         # Ej: "Tutorial: Refrendo Anual Vehicular Persona Física 2026"

# ── PREGUNTAS FRECUENTES ─────────────────────────────────────────────────────────

faq: *                   # Lista de preguntas y respuestas. Mínimo 3.
                         # Cada item:
                         #   - pregunta: texto de la pregunta
                         #   - respuesta: texto de la respuesta
                         # Las respuestas no deben incluir bloques de código.

# ── CTA Y ARTÍCULOS RELACIONADOS ─────────────────────────────────────────────────

cta_titulo: *            # Texto del botón/card de llamada a la acción
                         # Ej: "Iniciar Refrendo Digital"

cta_url: *               # URL a la que lleva el CTA (puede ser igual a url_tramite)

cta_descripcion:         # Frase corta bajo el CTA (opcional)
                         # Ej: "Sigue las recomendaciones y obtén tu trámite desde donde estés."

articulos_relacionados:  # Lista de artículos o manuales relacionados (opcional)
                         # Cada item:
                         #   - titulo: nombre del artículo
                         #   - url: link en TM o portal ciudadano

# ── FORMULARIO DE AYUDA ───────────────────────────────────────────────────────────

ayuda_url:               # URL del formulario de soporte/ayuda (opcional)
                         # Ej: "https://morelos-78762.zendesk.com/hc/es-419/requests/new?..."

ayuda_texto:             # Texto que acompaña el link de ayuda (opcional)
                         # Ej: "¿Tienes dudas? Llena el formulario de ayuda de Refrendo."
```

---

## Cómo compartir la ficha técnica

El usuario puede proporcionar los datos en cualquiera de estos formatos:

**Formato 1 — YAML estructurado** (el más completo, pegarlo directamente)

**Formato 2 — Texto libre** — Claude extrae los campos del texto y confirma antes de generar

**Formato 3 — Documento existente** — Si el usuario sube o pega un manual previo,
Claude lo reestructura al formato TM sin alterar los datos del trámite

---

## Validaciones antes de generar

Claude debe verificar:

- [ ] `nombre_tramite` presente
- [ ] `url_tramite` es una URL válida (comienza con http:// o https://)
- [ ] `audiencia` es uno de los valores válidos
- [ ] `requisitos_previos` tiene al menos 3 items
- [ ] `pasos` tiene al menos 3 items con `titulo` y `descripcion`
- [ ] `faq` tiene al menos 3 pares pregunta/respuesta
- [ ] `cta_titulo` y `cta_url` presentes

Si algún campo obligatorio falta, preguntar al usuario antes de continuar.
No asumir valores predeterminados para datos del trámite.
