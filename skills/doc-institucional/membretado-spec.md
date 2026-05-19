# Membretado Spec — Gobierno del Estado de Morelos

Especificación técnica para la generación de PDFs institucionales con ReportLab.

## Página

| Parámetro | Valor | Equivalencia |
|-----------|-------|-------------|
| Tamaño | `letter` | 612 × 792 pt |
| Orientación | Vertical (portrait) | — |

## Márgenes y área de contenido

El membretado (header + footer) está **integrado en la imagen de fondo de página completa**.
El área de contenido es la zona libre entre ambos elementos visuales.

| Zona | Valor pt | Valor cm | Descripción |
|------|----------|----------|-------------|
| Margen superior | 110 pt | ~3.9 cm | Deja libre el header (logotipo + nombre dependencia) |
| Margen inferior | 75 pt | ~2.6 cm | Deja libre el footer (dirección + morelos.gob.mx + borde decorativo) |
| Margen izquierdo | 65 pt | ~2.3 cm | Alineado con el logotipo del header |
| Margen derecho | 55 pt | ~1.9 cm | Margen estándar |

> **Nota**: Estos valores aplican para `letterhead-jefatura.jpg` y `letterhead-bienestar.png`.
> Para ATD (header programático), el margen superior es 100 pt.

## Paleta de colores

| Nombre | Hex | Uso |
|--------|-----|-----|
| Dorado institucional | `#D7B484` | Líneas decorativas, header ATD, folio |
| Verde oscuro ATD | `#4A5E3A` | Tipografía principal en header ATD programático |
| Guinda ATD | `#7A3B5E` | Elemento decorativo en header ATD (opcional) |
| Texto principal | `#1A1A1A` | Cuerpo del documento |
| Texto secundario | `#555555` | Metadatos: fecha, folio, destinatario |

## Tipografía (ReportLab built-in)

| Elemento | Fuente | Tamaño | Color |
|----------|--------|--------|-------|
| Tipo de documento (ej. COMUNICADO) | Helvetica-Bold | 11 pt | `#1A1A1A` |
| Folio / número de oficio | Helvetica | 9 pt | `#555555` |
| Fecha y lugar | Helvetica | 10 pt | `#1A1A1A` |
| Destinatario | Helvetica | 10 pt | `#1A1A1A` |
| Asunto | Helvetica-Bold | 10 pt | `#1A1A1A` |
| Cuerpo | Helvetica | 10 pt | `#1A1A1A` |
| Firma (nombre) | Helvetica-Bold | 10 pt | `#1A1A1A` |
| Firma (cargo) | Helvetica | 9 pt | `#555555` |
| Header ATD programático | Helvetica-Bold | 13 pt | `#4A5E3A` |

Interlineado del cuerpo: `14 pt` (leading). Espacio entre párrafos: `8 pt`.

## Dependencias registradas

### `jefatura` — Fondo completo
```
Asset: assets/letterhead-jefatura.jpg
Dimensiones: 1592 × 2048 px → escalar a 612 × 792 pt (página completa)
Área de contenido: margen_top=110, margen_bottom=75, margen_left=65, margen_right=55
```

### `atd` — Header programático
```
Asset logo: assets/logo-atd.jpg
Área de contenido: margen_top=100, margen_bottom=75, margen_left=65, margen_right=55

Header layout (construido en ReportLab):
  - Logo ATD: x=55, y=PAGE_HEIGHT-90, width=180, height=50 (preserveAspectRatio=True)
  - Línea separadora dorada: x=55..557, y=PAGE_HEIGHT-95, grosor=0.5pt, color=#D7B484
  - Footer: línea dorada + texto dirección en 8pt Helvetica color #D7B484
    "Plaza de Armas SN, Casa Morelos Mezzanine, Cuernavaca Centro, C.P. 62000, Morelos."
    "morelos.gob.mx" (alineado a la derecha)
```

## Agregar nueva dependencia

1. Conseguir el JPG/PNG del membretado completo (página A4 o Letter en blanco con header/footer)
2. Colocar en `assets/` con nombre `letterhead-[clave].jpg`
3. Registrar en esta tabla con su área de contenido medida
4. Agregar la clave al mapa `BACKGROUNDS` en `generate_pdf.py`
