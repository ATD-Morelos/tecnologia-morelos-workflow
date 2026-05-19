# Plantilla — Oficio Oficial

Usar cuando el documento es correspondencia formal entre dependencias,
dirigida a un destinatario nominal (nombre + cargo + dependencia).

---

## Estructura

```
OFICIO
[Número de oficio — ej. ATD/OF/042/2026]

                        [Ciudad], [Estado], a [día] de [mes] de [año].

[NOMBRE DEL DESTINATARIO EN MAYÚSCULAS]
[Cargo del destinatario]
[Dependencia del destinatario]
[Ciudad — opcional]
P R E S E N T E

ASUNTO: [Una línea]
────────────────────────────────────────────────────────────────

[Párrafo 1 — Fundamento y motivo]
Por medio del presente, y con fundamento en [atribución/ley aplicable],
me permito dirigirme a usted para [exponer / solicitar / informar / comunicar]:

[Párrafo 2 — Desarrollo]
[Información principal. Hechos, datos, fechas, referencias a otros documentos
si aplica (ej. "según Oficio ATD/OF/038/2026 de fecha..."). Claro y directo.]

[Párrafo 3 — Solicitud o acción requerida — si aplica]
[Qué se solicita, en qué plazo, a quién se dirige la respuesta o acción.]

[Cierre]
Agradezco de antemano la atención prestada al presente y quedo a sus órdenes.

A T E N T A M E N T E

─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
[NOMBRE COMPLETO EN MAYÚSCULAS]
[Cargo]
[Dependencia]
```

---

## Diferencias clave vs. Comunicado

| Aspecto | Comunicado | Oficio |
|---------|-----------|--------|
| Destinatario | Colectivo / público | Persona nominal |
| Saludo inicial | Sin saludo personal | "PRESENTE" |
| Cierre | "cordial saludo" | "ATENTAMENTE" |
| Número de folio | Opcional | Obligatorio |
| Tono | Más público / informativo | Más formal / institucional |
| Referencias cruzadas | Raro | Frecuente (otros oficios) |

---

## Formato del número de oficio

```
[SIGLAS DEPENDENCIA] / [TIPO] / [NÚMERO CONSECUTIVO] / [AÑO]

Ejemplos:
  ATD/OF/042/2026       → Agencia de Transformación Digital, Oficio 42
  JEFGUB/COM/007/2026   → Jefatura de Gubernatura, Comunicado 7
  SS/CIRC/001/2026      → Secretaría de Salud, Circular 1
```

---

## Guía de redacción (pilares Clara / Cercana / Confiable)

Igual que en comunicado. Regla adicional para oficios:

- **Citar bien los antecedentes**: si hay oficios previos, mencionarlos con número y fecha exacta.
- **La solicitud debe ser específica**: qué se pide, a quién, para cuándo.
- **"PRESENTE"** y **"ATENTAMENTE"** van siempre en mayúsculas y centrados (el script los maneja).

---

## Notas para Claude

- El número de oficio es obligatorio en oficios; preguntar al usuario si no lo proporciona.
- Incluir "P R E S E N T E" con espacios entre letras (formato protocolario estándar).
- Si el usuario da referencias a otros oficios, incluirlas en el cuerpo con número y fecha completa.
- Presentar el texto completo al usuario antes de correr el script PDF.
- El script colocará "ATENTAMENTE" y la firma al final automáticamente — no duplicar en el cuerpo.
