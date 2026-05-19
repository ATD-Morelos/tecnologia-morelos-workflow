# Plantilla — Manual de Uso Ciudadano (Markdoc para TM)

Sustituir todos los placeholders `[...]` con el contenido real de la ficha técnica.
Esta plantilla genera Markdoc válido para el renderer de Tecnología Morelos.

---

```markdoc
# MANUAL DE USO — [NOMBRE DEL TRÁMITE EN MAYÚSCULAS]

## Introducción

[Párrafo de bienvenida que contextualiza el trámite y transmite certeza al ciudadano.
Menciona el compromiso de la dependencia. 2-3 oraciones máximo.]

Aquí encontrarás:

- Qué revisar antes de comenzar.
- Cómo avanzar en cada etapa.
- [Item adicional relevante al trámite — ej. "Recomendaciones para validar tu información correctamente."]
- Respuestas a las preguntas más frecuentes.

Nuestro objetivo es acompañarte en cada paso.

---

## Antes de iniciar

### [Requisito previo principal — ej. "Cuenta Llave MX (obligatorio)"]

[Párrafo explicando por qué es necesario este requisito y cómo obtenerlo si no se tiene.
Ser específico: qué necesita el ciudadano para cumplirlo.]

Verifica lo siguiente:

- [ ] [Condición 1 — ej. "Ser el propietario registrado del vehículo"]
- [ ] [Condición 2]
- [ ] [Condición 3]
- [ ] [Condición 4 — si aplica]

### Documentos y datos a la mano

- [Dato o documento 1 — ej. "Correo y contraseña de Llave MX"]
- [Dato o documento 2]
- [Dato o documento 3]
- [Dato o documento 4 — si aplica]

> **Importante:** [Aviso especial si existe — ej. "Si ya iniciaste un trámite anteriormente,
> ingresa a 'Mis Trámites' y retómalo. No generes uno nuevo."]

---

## Paso a Paso

{% steps %}

{% step title="[Verbo imperativo: acción del paso 1]" %}
[Descripción clara del paso. Si hay una URL específica, incluirla como link: [texto](url).
Sin bloques de código aquí. Máximo 3 oraciones.]
{% /step %}

{% step title="[Verbo imperativo: acción del paso 2]" %}
[Descripción del paso 2. Si hay una nota de advertencia, usar emoji 👉 al inicio:
👉 [Nota importante sobre este paso.]]
{% /step %}

{% step title="[Verbo imperativo: acción del paso 3]" %}
[Descripción del paso 3.]
{% /step %}

{% step title="[Verbo imperativo: acción del paso 4 — si aplica]" %}
[Descripción del paso 4.]
{% /step %}

{% step title="[Verbo imperativo: acción del paso N]" %}
[Descripción del último paso. Mencionar el resultado final que obtiene el ciudadano:
ej. "Descarga tu Tarjeta de Circulación Digital."]
{% /step %}

{% /steps %}

[Si hay consideraciones importantes después del paso a paso, incluirlas como párrafo
o lista con `>` blockquote para resaltarlas. NO dentro del bloque steps.]

> **Consideraciones:**
> - [Consideración 1 — ej. "Si ya existe un trámite iniciado, deberás concluirlo."]
> - [Consideración 2 — si aplica.]

---

## Video Tutorial

{% video src="[URL_DEL_VIDEO]" title="[Título descriptivo del video]" /%}

---

## Preguntas Frecuentes

{% accordion title="[¿Pregunta 1?]" %}
[Respuesta directa y clara. Sin tecnicismos. Sin bloques de código.
Si hay una URL en la respuesta, usar sintaxis Markdown: [texto](url).]
{% /accordion %}

{% accordion title="[¿Pregunta 2?]" %}
[Respuesta 2.]
{% /accordion %}

{% accordion title="[¿Pregunta 3?]" %}
[Respuesta 3.]
{% /accordion %}

{% accordion title="[¿Pregunta 4? — si aplica]" %}
[Respuesta 4.]
{% /accordion %}

---

## Realiza el trámite aquí

{% cardgroup %}

{% card title="[cta_titulo]" href="[cta_url]" %}
[cta_descripcion — frase corta que complementa el CTA.]
{% /card %}

{% card title="[Artículo relacionado 1]" href="[url_articulo_1]" %}
[Breve descripción de qué encontrará el ciudadano en ese artículo.]
{% /card %}

{% card title="[Artículo relacionado 2 — si aplica]" href="[url_articulo_2]" %}
[Descripción breve.]
{% /card %}

{% /cardgroup %}

---

[Si hay formulario de ayuda:]

## ¿Necesitas ayuda?

Si tienes dudas o estás atorado en algún paso, [llena el formulario de ayuda]([ayuda_url])
para que podamos orientarte más rápido.

Estamos para acompañarte durante todo el proceso.

---
Generado con AI (tecnologia-morelos-workflow v0.1.0), revisado por [nombre]
```

---

## Notas de uso para Claude

**Sobre los steps:**
- El `title` de cada `{% step %}` debe ser un verbo imperativo corto: "Ingresa", "Captura", "Selecciona", "Descarga"
- La descripción va dentro del step, sin código, sin listas anidadas
- Si un paso tiene sub-acciones, escribirlas en prosa separadas por punto y coma

**Sobre los accordions (FAQ):**
- Cada pregunta es un `{% accordion %}` independiente
- No agrupar múltiples preguntas en un solo accordion
- Las respuestas van en texto plano + links Markdown si necesario
- Nunca código dentro de accordion

**Sobre el video:**
- Si `{% video %}` no está disponible en TM aún, reemplazar con:
  ```markdoc
  {% card title="[video_titulo]" href="[video_url]" %}
  Tutorial en video: mira el paso a paso completo.
  {% /card %}
  ```

**Sobre las consideraciones:**
- Van DESPUÉS del bloque `{% /steps %}`, nunca dentro
- Usar `>` blockquote para destacarlas visualmente
- No poner listas dentro de `{% step %}` si son más de 2 items — escribir en prosa

**Longitud esperada:**
- Introducción: 3-5 líneas
- Antes de iniciar: tantos items como tenga la ficha
- Steps: uno por acción clara y diferenciada del proceso
- FAQ: todos los Q&A de la ficha + los más frecuentes inferibles del contexto
- Sin relleno: si una sección no tiene datos, omitir (excepto las obligatorias)
