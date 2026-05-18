# Markdoc Reference — Tecnología Morelos

Complete reference for Markdoc components supported by the TM renderer.

## The #1 Rule

**Code blocks (triple backtick) must be OUTSIDE `{% accordion %}`, `{% step %}`,
and `{% card %}`.** Only `{% codegroup %}` accepts code blocks inside.

**Mermaid diagrams must be OUTSIDE any Markdoc component.**

Violating these rules BREAKS the renderer silently — content may not display.

---

## Components

### Accordion

Collapsible section. Only text and inline code inside.

**Correct:**
```markdoc
{% accordion title="¿Cómo funciona?" %}
Este proceso toma los datos del formulario y los envía al servidor
usando el endpoint `/api/submit`. El resultado es un `JSON` con el
estado de la operación.
{% /accordion %}
```

**INCORRECT — code block inside accordion:**
```markdoc
{% accordion title="Ejemplo de código" %}
```json
{ "key": "value" }
```
{% /accordion %}
```
This BREAKS the renderer. Move the code block outside:

**Correct alternative:**
```markdoc
{% accordion title="Ejemplo de código" %}
Ver el ejemplo a continuación.
{% /accordion %}

```json
{ "key": "value" }
```
```

---

### Steps

Numbered steps. Only text and inline code inside each step.

**Correct:**
```markdoc
{% steps %}

{% step title="Crear el proyecto" %}
Navega a la sección de proyectos y haz clic en "Nuevo proyecto".
Ingresa el nombre usando el formato `[Producto] — Morelos`.
{% /step %}

{% step title="Configurar el team" %}
Selecciona el team asignado de la lista desplegable.
{% /step %}

{% /steps %}
```

**INCORRECT — code block inside step:**
```markdoc
{% steps %}
{% step title="Configurar" %}
```bash
npm install
```
{% /step %}
{% /steps %}
```
This BREAKS the renderer. Place code blocks after the steps block.

---

### Card

Link card with title and description. Only text inside.

**Correct:**
```markdoc
{% card title="PRD" href="/docs/prd" %}
Product Requirements Document con los requerimientos funcionales
y no funcionales del proyecto.
{% /card %}
```

**INCORRECT — code block inside card:**
```markdoc
{% card title="API" href="/docs/api" %}
```json
{ "endpoint": "/api/v1" }
```
{% /card %}
```

---

### Card Group

Grid of cards. Wraps multiple `{% card %}` components.

**Correct:**
```markdoc
{% cardgroup %}

{% card title="Discovery Report" href="/docs/discovery" %}
Resultado de la fase de investigación.
{% /card %}

{% card title="PRD" href="/docs/prd" %}
Requerimientos del producto.
{% /card %}

{% /cardgroup %}
```

---

### Code Group

**ONLY component that accepts code blocks inside.** Use for showing
multiple code examples with tab switching.

**Correct:**
```markdoc
{% codegroup %}

```javascript title="Frontend"
fetch('/api/submit', { method: 'POST', body: data })
```

```python title="Backend"
@app.post("/api/submit")
async def submit(data: SubmitRequest):
    return {"status": "ok"}
```

{% /codegroup %}
```

---

### Mermaid Diagrams

Mermaid diagrams render as SVGs. They must be at the **top level** —
OUTSIDE any Markdoc component.

**Correct:**
```markdoc
## Arquitectura

El siguiente diagrama muestra la arquitectura del sistema:

```mermaid
graph LR
    A[Frontend] --> B[API Gateway]
    B --> C[Backend]
    C --> D[(Database)]
```

{% accordion title="Detalles adicionales" %}
El API Gateway maneja autenticación y rate limiting.
{% /accordion %}
```

**INCORRECT — mermaid inside accordion:**
```markdoc
{% accordion title="Diagrama" %}
```mermaid
graph LR
    A --> B
```
{% /accordion %}
```
This BREAKS the renderer. Always keep Mermaid at the top level.

---

### YouTube

Embed de un video de YouTube. Tag **self-closing**. Debe ir al **top level** —
fuera de cualquier otro Markdoc component.

**Atributos:**

| Atributo | Tipo | Requerido | Descripción |
|----------|------|-----------|-------------|
| `id` | string | sí | ID del video (parte después de `v=` o de `youtu.be/`) |
| `title` | string | no | Título mostrado encima del player |

**Correcto:**
```markdoc
{% youtube id="YmQ7jRgf4f0" /%}

{% youtube id="YmQ7jRgf4f0" title="Claude FM" /%}
```

**INCORRECTO — dentro de accordion/step/card:**
```markdoc
{% accordion title="Demo del producto" %}
{% youtube id="YmQ7jRgf4f0" /%}
{% /accordion %}
```
Como con mermaid y code blocks, los embeds van fuera. Mover el `{% youtube %}`
al top level y dejar el accordion solo con texto.

---

## Supported Standard Markdown

TM renders these standard Markdown elements natively:

| Element | Syntax | Notes |
|---------|--------|-------|
| Headings | `# H1`, `## H2`, `### H3` | Standard levels |
| Bold | `**text**` | |
| Italic | `*text*` | |
| Inline code | `` `code` `` | Safe inside any Markdoc component |
| Code blocks | ` ```lang ``` ` | Must be OUTSIDE Markdoc components (except codegroup) |
| Unordered lists | `- item` | |
| Ordered lists | `1. item` | |
| Checklists | `- [ ] item` / `- [x] item` | Rendered with checkboxes |
| Blockquotes | `> text` | Useful for callouts and notes |
| Links | `[text](url)` | |
| Images | `![alt](/api/kb-images/uuid)` | Images use internal API URLs |
| Tables | `\| col \| col \|` | Standard pipe tables |
| Horizontal rule | `---` | |

### Images

Images in TM use internal API URLs:
```
![Description](/api/kb-images/9ce830d6-c803-461d-8cc2-c5eb49ec92e9?v=2d998889432adb6d)
```
Image UUIDs are generated when uploading through the TM web interface.

### Codegroup — Known fragility

`{% codegroup %}` is the ONLY component that accepts code blocks inside, but it
is **fragile**. If the syntax is not exactly right, backticks may appear as
escaped text instead of rendering as code tabs. Always verify rendering in the
browser after publishing codegroup content.

---

## Quick Reference

| Component | Code blocks inside? | Mermaid inside? | Text/inline code? |
|-----------|--------------------|-----------------|--------------------|
| `{% accordion %}` | NO | NO | YES |
| `{% step %}` | NO | NO | YES |
| `{% card %}` | NO | NO | YES |
| `{% cardgroup %}` | NO | NO | Only via cards |
| `{% codegroup %}` | **YES** | NO | NO |
| `{% youtube %}` | n/a (self-closing) | n/a | n/a |
| Top level | YES | **YES** | YES |

## Common Patterns

### Feature documentation with code example

```markdoc
## Autenticación

{% accordion title="¿Cómo funciona el flujo?" %}
El usuario envía sus credenciales al endpoint de login.
El servidor valida y retorna un token JWT.
{% /accordion %}

Ejemplo de request:

```json
{
  "email": "user@example.com",
  "password": "secret"
}
```
```

### Step-by-step guide with code

```markdoc
{% steps %}

{% step title="Instalar dependencias" %}
Ejecuta el siguiente comando en tu terminal (ver ejemplo abajo).
{% /step %}

{% step title="Configurar variables" %}
Crea un archivo `.env` con las variables necesarias (ver ejemplo abajo).
{% /step %}

{% /steps %}

Comando de instalación:

```bash
npm install @morelos/sdk
```

Archivo de configuración:

```env
API_KEY=your_key_here
API_URL=https://api.morelos.gob.mx
```
```

### Doc con texto + video explicativo

```markdoc
## ¿Cómo funciona el trámite?

Lee primero el flujo en texto, luego mira el recorrido en video.

{% youtube id="YmQ7jRgf4f0" title="Demo paso a paso" /%}

{% accordion title="¿Necesitas ayuda?" %}
Contacta a la Dirección de Atención Ciudadana al teléfono 777-XXX-XXXX.
{% /accordion %}
```
