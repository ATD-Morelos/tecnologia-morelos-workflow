---
name: doc-institucional
description: >
  Genera documentos institucionales del Gobierno del Estado de Morelos en PDF
  con membretado oficial. Soporta: comunicados, oficios, convocatorias y reportes.
  Aplica el diseño del membretado base: header con logotipo institucional,
  paleta dorada, borde prehispánico y pie de página. La dependencia emisora
  es configurable (Jefatura, Bienestar, ATD u otra).
argument-hint: "[tipo-documento] [dependencia]"
allowed-tools: Read Glob mcp__workspace__bash
---

# doc-institucional — Generador de Documentos con Membretado Oficial

## Cuándo usar este skill

- Usuario pide crear un comunicado, oficio, convocatoria, reporte o circular oficial
- El documento requiere el membretado institucional del Gobierno del Estado de Morelos
- Se necesita salida en PDF listo para firma o distribución

## Documentos soportados

| Tipo | Descripción |
|------|-------------|
| `comunicado` | Aviso o comunicación oficial hacia ciudadanía u otras dependencias |
| `oficio` | Documento formal de correspondencia entre dependencias o autoridades |
| `convocatoria` | Llamado público a participación, licitación o evento |
| `reporte` | Informe de resultados, avances o diagnóstico |
| `circular` | Instrucción o lineamiento de aplicación interna |

## Dependencias disponibles

| Clave | Fondo de página | Descripción |
|-------|----------------|-------------|
| `jefatura` | `assets/letterhead-jefatura.jpg` | Jefatura de la Oficina de la Gubernatura del Estado |
| `atd` | Header programático con `assets/logo-atd.jpg` | Agencia de Transformación Digital |
| `otra` | Header programático con texto | Dependencia sin imagen de fondo registrada |

Para agregar una nueva dependencia: colocar el JPG/PNG del membretado completo en `assets/` y registrarlo en `membretado-spec.md`.

## Flujo

### 1. Recopilar información

Si el usuario no la proporcionó completa, preguntar:

```
- Tipo de documento (comunicado / oficio / convocatoria / reporte / circular)
- Dependencia emisora (jefatura / bienestar / atd / otra)
- Número o folio del documento (ej. ATD/COM/001/2026) — opcional
- Fecha (ej. Cuernavaca, Morelos, 15 de mayo de 2026)
- Destinatario: nombre, cargo, dependencia — para oficios; omitir en comunicados públicos
- Asunto (una línea)
- Cuerpo del documento (el usuario puede dar borrador o puntos clave)
- Firmante: nombre completo, cargo, dependencia
- Cargo del firmante
```

### 2. Revisar y generar contenido

Lee la plantilla correspondiente en `templates/`:
- `templates/comunicado.md` para comunicados y circulares
- `templates/oficio.md` para oficios

Genera el contenido siguiendo la plantilla. Si el usuario da solo puntos clave,
redactar el cuerpo completo en tono institucional claro y directo (pilares Clara /
Cercana / Confiable del skill `voice`). No inventar datos: fecha, folio, firmante
y destinatario deben venir del usuario.

Presentar el borrador de contenido al usuario y esperar confirmación antes de
generar el PDF.

### 3. Generar el PDF

Después de aprobación del contenido, leer `membretado-spec.md` para los valores
exactos de márgenes y colores. Luego escribir y ejecutar el script Python:

```
# Ruta del script (escribir en el directorio de trabajo temporal):
/tmp/gen_doc_institucional.py

# Ejecutar:
python3 /tmp/gen_doc_institucional.py

# El PDF se guarda en el directorio de salida configurado en el script.
```

Usar `generate_pdf.py` como base — copiar su contenido, ajustar las variables
de configuración (DEPENDENCIA, TIPO, FECHA, DESTINATARIO, CUERPO, FIRMANTE, etc.)
y ejecutar.

### 4. Entregar

Proporcionar el enlace `computer://` al PDF generado. Informar al usuario que
puede abrirlo, imprimirlo o firmarlo digitalmente.

## Reglas

- **Nunca inventar datos**: folio, fecha, destinatario y firmante siempre los da el usuario
- **Aprobar antes de generar**: presentar el contenido en texto antes de correr el script PDF
- **Un documento por llamada**: no generar múltiples PDFs en una sola ejecución sin confirmar cada uno
- **Reportar errores de ReportLab**: si el script falla, mostrar el error completo al usuario
- **Footer obligatorio en el borrador de texto** (no en el PDF):
  ```
  ---
  Generado con AI (tecnologia-morelos-workflow), revisado por [nombre]
  ```

## Archivos de referencia

- [membretado-spec.md](membretado-spec.md) — colores, márgenes, área de contenido por dependencia
- [generate_pdf.py](generate_pdf.py) — script base ReportLab para copiar y adaptar
- [templates/comunicado.md](templates/comunicado.md) — estructura de comunicado oficial
- [templates/oficio.md](templates/oficio.md) — estructura de oficio
- [assets/](assets/) — imágenes de membretado por dependencia
