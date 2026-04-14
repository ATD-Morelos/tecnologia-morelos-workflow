# Excalidraw Diagrams — Guide

## When to use Excalidraw vs Mermaid

| Use Excalidraw | Use Mermaid |
|----------------|-------------|
| User Flows (step-by-step journeys) | C4 Context / Container |
| Sequence diagrams (detailed interactions) | ERD (data model) |
| Wireframes (screen layouts) | Deployment Architecture |
| Conceptual sketches | Flowcharts with strict logic |
| Stakeholder presentations | Technical documentation |
| Anything that benefits from "draft" aesthetic | Anything that needs to be version-controlled as code |

**Rule of thumb**: Mermaid for structure, Excalidraw for communication.

## Creating diagrams via MCP

### Available tools

| Tool | Purpose |
|------|---------|
| `create-element` | Add a new element (rectangle, text, arrow, etc.) |
| `get-all-elements` | List all elements on the canvas |
| `update-element` | Modify an existing element |
| `delete-element` | Remove an element |
| `export-scene` | Export the diagram as image |
| `get-scene-info` | Get canvas dimensions and metadata |

### Element types

- **rectangle**: Boxes for steps, screens, components
- **ellipse**: Start/end nodes, actors
- **diamond**: Decision points
- **text**: Labels and descriptions
- **arrow**: Connections and flow direction
- **line**: Non-directional connections

## Pattern: User Flow

A user flow shows the step-by-step journey a user takes to accomplish a task.

### Structure

```
[Start] → [Step 1] → [Decision?] → [Step 2a] → [End]
                          ↓
                      [Step 2b] → [End]
```

### Building a user flow

1. **Start node** (ellipse, green background)
   - Label: "Inicio" or trigger event
   - Position: top-left or left

2. **Step nodes** (rectangle, light blue)
   - Label: action the user takes
   - Include screen/page name if relevant

3. **Decision nodes** (diamond, yellow)
   - Label: question (yes/no)
   - Two outgoing arrows labeled with conditions

4. **End node** (ellipse, red/green for failure/success)
   - Label: "Fin" or outcome

5. **Arrows** connecting in reading order (left-to-right or top-to-bottom)

### Example: Tramite flow

```
Elements to create:
1. Ellipse "Inicio: Ciudadano accede al portal" (x:100, y:300)
2. Rectangle "Buscar tipo de tramite" (x:350, y:300)
3. Rectangle "Llenar formulario" (x:600, y:300)
4. Rectangle "Adjuntar documentos" (x:850, y:300)
5. Diamond "Datos completos?" (x:1100, y:300)
6. Rectangle "Corregir datos" (x:1100, y:500)
7. Rectangle "Realizar pago" (x:1350, y:300)
8. Rectangle "Confirmar envio" (x:1600, y:300)
9. Ellipse "Fin: Tramite enviado" (x:1850, y:300)

Arrows: 1→2, 2→3, 3→4, 4→5, 5→6 (No), 6→4, 5→7 (Si), 7→8, 8→9
```

## Pattern: Sequence Diagram

Shows the interaction between actors and systems over time.

### Structure

```
Actor    Sistema    BD    Servicio Externo
  |         |       |          |
  |--req--->|       |          |
  |         |--qry->|          |
  |         |<-res--|          |
  |         |-------call------>|
  |         |<------resp-------|
  |<--resp--|       |          |
```

### Building a sequence diagram

1. **Actor columns** (rectangles at top, evenly spaced)
   - Ciudadano, Frontend, API, BD, External Service
   - Vertical dashed line below each (use line elements)

2. **Messages** (arrows between columns)
   - Solid arrow: synchronous request
   - Dashed arrow: response
   - Label with action name

3. **Activation boxes** (thin rectangles on lifelines)
   - Show when a component is processing

### Layout tips

- Space actors 250-300px apart horizontally
- Each message step 60-80px apart vertically
- Keep labels short (verb + noun)
- Number steps for complex sequences

## Pattern: Wireframe

Shows the basic layout of a screen without visual design details.

### Structure

```
┌──────────────────────────────────┐
│ [Logo]    Nav Item 1 | Nav Item 2│  ← Header
├──────────────────────────────────┤
│                                  │
│  ┌──────────┐  ┌──────────────┐  │
│  │ Sidebar  │  │   Content    │  │
│  │          │  │              │  │
│  │ - Link 1 │  │ [Form/Table] │  │
│  │ - Link 2 │  │              │  │
│  └──────────┘  └──────────────┘  │
│                                  │
├──────────────────────────────────┤
│ Footer                           │  ← Footer
└──────────────────────────────────┘
```

### Building a wireframe

1. **Page container** (rectangle, 1200x800 or similar)
2. **Header** (rectangle at top, full width, ~60px height)
   - Logo placeholder (small rectangle)
   - Navigation items (text elements)
3. **Content area** (rectangles for layout regions)
   - Sidebar (if applicable)
   - Main content area
4. **Form elements** (rectangles with labels)
   - Input fields: rectangle with label text above
   - Buttons: small rectangle with text
   - Tables: grid of rectangles
5. **Footer** (rectangle at bottom)

### Tips for wireframes

- Use gray/neutral colors — wireframes should look intentionally unfinished
- Include placeholder text: "[Nombre del usuario]", "[Fecha]"
- Label every interactive element
- Show one state per wireframe (empty, filled, error)
- Create separate wireframes for mobile if responsive

## General tips for Excalidraw MCP

1. **Plan layout before creating** — sketch the positions mentally first
2. **Use consistent spacing** — 50px gaps between elements, 250px between groups
3. **Color coding**:
   - Blue: user actions / primary flow
   - Green: success / start
   - Red: error / end
   - Yellow: decisions / warnings
   - Gray: system / background
4. **Font sizes**: 20px for titles, 16px for labels, 14px for descriptions
5. **Group related elements** — keep things visually clustered
6. **Export for TM** — use `export-scene` to get an image for embedding

## Coordinate system

- Origin (0,0) is top-left of canvas
- X increases to the right
- Y increases downward
- Standard element sizes:
  - Rectangle: 200x80 for steps, 300x60 for wireframe sections
  - Ellipse: 150x60 for start/end
  - Diamond: 120x120 for decisions
  - Text: auto-sized based on content

---
Generado con AI (tecnologia-morelos-workflow v0.1.0), revisado por [nombre]
