#!/usr/bin/env python3
"""
Generador de documentos institucionales — Gobierno del Estado de Morelos
Skill: doc-institucional | Plugin: tecnologia-morelos-workflow

Uso:
  1. Copiar este archivo a /tmp/gen_doc_institucional.py
  2. Ajustar las variables de CONFIGURACIÓN más abajo
  3. python3 /tmp/gen_doc_institucional.py

Dependencias: reportlab (pip install reportlab --break-system-packages)
"""

import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY, TA_RIGHT
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame,
    Paragraph, Spacer, HRFlowable, Image as RLImage, KeepTogether
)
from reportlab.pdfgen import canvas as pdfcanvas

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CONFIGURACIÓN — Claude ajusta estas variables según los datos del usuario
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Dependencia emisora: "jefatura" | "bienestar" | "atd" | "otra"
DEPENDENCIA = "atd"

# Nombre completo de la dependencia (usado en header programático y en "otra")
DEPENDENCIA_NOMBRE = "Agencia de Transformación Digital"

# Tipo de documento (mayúsculas para el encabezado del documento)
DOCUMENTO_TIPO = "COMUNICADO"

# Folio o número de oficio (dejar vacío si no aplica)
FOLIO = "ATD/COM/001/2026"

# Fecha y lugar
FECHA = "Cuernavaca, Morelos, a 15 de mayo de 2026."

# Destinatario (dejar vacío para comunicados públicos)
DESTINATARIO_NOMBRE = ""
DESTINATARIO_CARGO = ""
DESTINATARIO_DEPENDENCIA = ""

# Asunto
ASUNTO = "Asunto del documento institucional"

# Cuerpo del documento (usar \n para párrafos separados)
CUERPO = """Con fundamento en las atribuciones que me confiere el cargo, y con el propósito de mantener comunicación institucional clara y oportuna, me dirijo a usted para informar lo siguiente.

Primer párrafo del cuerpo. Aquí va el contenido principal del comunicado. La redacción debe ser directa, clara y en tono institucional ciudadano.

Segundo párrafo. Datos adicionales, instrucciones o información complementaria relevante para el destinatario o la ciudadanía.

Sin otro particular, le envío un cordial saludo."""

# Firmante
FIRMANTE_NOMBRE = "NOMBRE APELLIDO APELLIDO"
FIRMANTE_CARGO = "Cargo Institucional"
FIRMANTE_DEPENDENCIA = "Agencia de Transformación Digital"

# Archivo de salida
OUTPUT_PATH = "/tmp/documento-institucional.pdf"

# Directorio de assets (relativo a este script O ruta absoluta)
# Claude: ajustar esta ruta a la ubicación real del skill en el repo
ASSETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# DISEÑO — No modificar salvo para ajuste fino
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PAGE_WIDTH, PAGE_HEIGHT = letter  # 612 x 792 pt

GOLD        = HexColor('#D7B484')
DARK_GREEN  = HexColor('#4A5E3A')
TEXT_DARK   = HexColor('#1A1A1A')
TEXT_GRAY   = HexColor('#555555')

# Mapa dependencia → imagen de fondo (página completa)
BACKGROUNDS = {
    "jefatura": "letterhead-jefatura.jpg",
    # "atd" y "otra" usan header programático → no tienen fondo
}

# Márgenes según tipo de membretado
MARGINS = {
    "full_bg": dict(top=110, bottom=75, left=65, right=55),   # con imagen de fondo
    "programmatic": dict(top=100, bottom=75, left=65, right=55),  # header construido
}


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# FUNCIONES DE PÁGINA
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def _asset(filename):
    """Devuelve la ruta absoluta de un asset. Lanza error claro si no existe."""
    path = os.path.join(ASSETS_DIR, filename)
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Asset no encontrado: {path}\n"
            f"Verifica que ASSETS_DIR apunte a la carpeta assets/ del skill."
        )
    return path


def draw_page_full_bg(canvas_obj, doc, bg_filename):
    """Header/footer vía imagen de fondo de página completa."""
    canvas_obj.saveState()
    bg_path = _asset(bg_filename)
    canvas_obj.drawImage(
        bg_path, 0, 0,
        width=PAGE_WIDTH, height=PAGE_HEIGHT,
        preserveAspectRatio=False, mask='auto'
    )
    canvas_obj.restoreState()


def draw_page_atd(canvas_obj, doc):
    """Header/footer programático para ATD."""
    canvas_obj.saveState()

    logo_path = _asset("logo-atd.jpg")
    logo_w = 185
    logo_h = 52
    logo_x = 55
    logo_y = PAGE_HEIGHT - logo_h - 20

    canvas_obj.drawImage(
        logo_path, logo_x, logo_y,
        width=logo_w, height=logo_h,
        preserveAspectRatio=True, mask='auto'
    )

    # Línea separadora dorada bajo el logo
    sep_y = logo_y - 8
    canvas_obj.setStrokeColor(GOLD)
    canvas_obj.setLineWidth(0.6)
    canvas_obj.line(55, sep_y, PAGE_WIDTH - 45, sep_y)

    # ── Footer ──
    footer_y = 55
    canvas_obj.setStrokeColor(GOLD)
    canvas_obj.setLineWidth(0.6)
    canvas_obj.line(55, footer_y + 12, PAGE_WIDTH - 45, footer_y + 12)

    canvas_obj.setFont("Helvetica", 7)
    canvas_obj.setFillColor(GOLD)
    canvas_obj.drawString(
        55, footer_y,
        "Plaza de Armas SN, Casa Morelos Mezzanine, Cuernavaca Centro, C.P. 62000, Morelos."
    )
    canvas_obj.drawRightString(PAGE_WIDTH - 45, footer_y, "morelos.gob.mx")

    canvas_obj.restoreState()


def draw_page_otra(canvas_obj, doc):
    """Header/footer programático genérico para dependencias sin imagen registrada."""
    canvas_obj.saveState()

    header_y = PAGE_HEIGHT - 30
    canvas_obj.setFont("Helvetica-Bold", 11)
    canvas_obj.setFillColor(DARK_GREEN)
    canvas_obj.drawString(55, header_y, DEPENDENCIA_NOMBRE.upper())

    canvas_obj.setStrokeColor(GOLD)
    canvas_obj.setLineWidth(0.6)
    canvas_obj.line(55, header_y - 10, PAGE_WIDTH - 45, header_y - 10)

    # Footer
    footer_y = 55
    canvas_obj.setStrokeColor(GOLD)
    canvas_obj.line(55, footer_y + 12, PAGE_WIDTH - 45, footer_y + 12)
    canvas_obj.setFont("Helvetica", 7)
    canvas_obj.setFillColor(GOLD)
    canvas_obj.drawString(55, footer_y,
        "Plaza de Armas SN, Casa Morelos Mezzanine, Cuernavaca Centro, C.P. 62000, Morelos.")
    canvas_obj.drawRightString(PAGE_WIDTH - 45, footer_y, "morelos.gob.mx")

    canvas_obj.restoreState()


def get_on_page(dependencia_key):
    """Devuelve la función onPage correcta según la dependencia."""
    if dependencia_key in BACKGROUNDS:
        bg = BACKGROUNDS[dependencia_key]
        return lambda c, d: draw_page_full_bg(c, d, bg)
    elif dependencia_key == "atd":
        return draw_page_atd
    else:
        return draw_page_otra


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ESTILOS DE PÁRRAFO
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def build_styles():
    return {
        "tipo_doc": ParagraphStyle(
            "tipo_doc",
            fontName="Helvetica-Bold", fontSize=11,
            textColor=TEXT_DARK, leading=14,
            spaceAfter=2, alignment=TA_LEFT,
        ),
        "folio": ParagraphStyle(
            "folio",
            fontName="Helvetica", fontSize=9,
            textColor=TEXT_GRAY, leading=12,
            spaceAfter=10, alignment=TA_LEFT,
        ),
        "fecha": ParagraphStyle(
            "fecha",
            fontName="Helvetica", fontSize=10,
            textColor=TEXT_DARK, leading=13,
            spaceAfter=12, alignment=TA_RIGHT,
        ),
        "destinatario": ParagraphStyle(
            "destinatario",
            fontName="Helvetica", fontSize=10,
            textColor=TEXT_DARK, leading=14,
            spaceAfter=12, alignment=TA_LEFT,
        ),
        "asunto_label": ParagraphStyle(
            "asunto_label",
            fontName="Helvetica-Bold", fontSize=10,
            textColor=TEXT_DARK, leading=13,
            spaceAfter=0, alignment=TA_LEFT,
        ),
        "asunto_texto": ParagraphStyle(
            "asunto_texto",
            fontName="Helvetica", fontSize=10,
            textColor=TEXT_DARK, leading=13,
            spaceAfter=14, alignment=TA_LEFT,
        ),
        "cuerpo": ParagraphStyle(
            "cuerpo",
            fontName="Helvetica", fontSize=10,
            textColor=TEXT_DARK, leading=14,
            spaceAfter=8, alignment=TA_JUSTIFY,
        ),
        "firma_nombre": ParagraphStyle(
            "firma_nombre",
            fontName="Helvetica-Bold", fontSize=10,
            textColor=TEXT_DARK, leading=13,
            spaceAfter=2, alignment=TA_LEFT,
        ),
        "firma_cargo": ParagraphStyle(
            "firma_cargo",
            fontName="Helvetica", fontSize=9,
            textColor=TEXT_GRAY, leading=12,
            spaceAfter=0, alignment=TA_LEFT,
        ),
    }


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CONSTRUCCIÓN DEL DOCUMENTO
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def build_document():
    dep_key = DEPENDENCIA.lower().strip()
    margin_set = "full_bg" if dep_key in BACKGROUNDS else "programmatic"
    m = MARGINS[margin_set]

    frame = Frame(
        m["left"], m["bottom"],
        PAGE_WIDTH - m["left"] - m["right"],
        PAGE_HEIGHT - m["top"] - m["bottom"],
        id="main", showBoundary=0
    )

    on_page = get_on_page(dep_key)

    doc = BaseDocTemplate(
        OUTPUT_PATH,
        pagesize=letter,
        title=f"{DOCUMENTO_TIPO} — {DEPENDENCIA_NOMBRE}",
        author=DEPENDENCIA_NOMBRE,
    )
    doc.addPageTemplates([
        PageTemplate(id="membretado", frames=[frame], onPage=on_page)
    ])

    styles = build_styles()
    story = []

    # ── Tipo de documento y folio ──
    story.append(Paragraph(DOCUMENTO_TIPO, styles["tipo_doc"]))
    if FOLIO:
        story.append(Paragraph(FOLIO, styles["folio"]))
    story.append(Spacer(1, 6))

    # ── Fecha ──
    story.append(Paragraph(FECHA, styles["fecha"]))

    # ── Destinatario ──
    if DESTINATARIO_NOMBRE or DESTINATARIO_CARGO:
        dest_lines = []
        if DESTINATARIO_NOMBRE:
            dest_lines.append(f"<b>{DESTINATARIO_NOMBRE}</b>")
        if DESTINATARIO_CARGO:
            dest_lines.append(DESTINATARIO_CARGO)
        if DESTINATARIO_DEPENDENCIA:
            dest_lines.append(DESTINATARIO_DEPENDENCIA)
        story.append(Paragraph("<br/>".join(dest_lines), styles["destinatario"]))
        story.append(Spacer(1, 4))

    # ── Asunto ──
    story.append(Paragraph("Asunto:", styles["asunto_label"]))
    story.append(Paragraph(ASUNTO, styles["asunto_texto"]))

    # ── Línea separadora ──
    story.append(HRFlowable(
        width="100%", thickness=0.5,
        color=GOLD, spaceAfter=10, spaceBefore=2
    ))

    # ── Cuerpo ──
    for parrafo in CUERPO.strip().split("\n\n"):
        texto = parrafo.strip()
        if texto:
            story.append(Paragraph(texto, styles["cuerpo"]))

    # ── Firma ──
    story.append(Spacer(1, 36))
    story.append(HRFlowable(
        width="45%", thickness=0.4,
        color=HexColor('#AAAAAA'), spaceAfter=6
    ))
    firma_block = [
        Paragraph(FIRMANTE_NOMBRE, styles["firma_nombre"]),
        Paragraph(FIRMANTE_CARGO, styles["firma_cargo"]),
        Paragraph(FIRMANTE_DEPENDENCIA, styles["firma_cargo"]),
    ]
    story.append(KeepTogether(firma_block))

    doc.build(story)
    print(f"✓ PDF generado: {OUTPUT_PATH}")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ENTRY POINT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

if __name__ == "__main__":
    try:
        build_document()
    except FileNotFoundError as e:
        print(f"ERROR — Asset no encontrado:\n{e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"ERROR — Generación fallida:\n{e}", file=sys.stderr)
        sys.exit(1)
