# C4 Diagrams with Mermaid — Guide

## Overview

C4 model provides four levels of abstraction for software architecture.
This guide covers **Context** and **Container** levels using Mermaid's C4 syntax.

## C4 Context Diagram

Shows the system in scope and its relationships with external actors and systems.

### Syntax

```mermaid
C4Context
    title System Context — [Nombre del Sistema]

    Person(ciudadano, "Ciudadano", "Persona que realiza tramites gubernamentales")
    Person(funcionario, "Funcionario", "Personal del gobierno que procesa tramites")

    System(sistema, "Sistema de Tramites", "Permite a ciudadanos realizar tramites en linea")

    System_Ext(curp, "RENAPO/CURP", "Validacion de identidad via CURP")
    System_Ext(pagos, "Sistema de Pagos", "Procesamiento de pagos en linea")
    System_Ext(notif, "Servicio de Notificaciones", "Envio de SMS y correo electronico")

    Rel(ciudadano, sistema, "Realiza tramites", "HTTPS")
    Rel(funcionario, sistema, "Revisa y aprueba tramites", "HTTPS")
    Rel(sistema, curp, "Valida identidad", "API REST")
    Rel(sistema, pagos, "Procesa pagos", "API REST")
    Rel(sistema, notif, "Envia notificaciones", "API REST")
```

### Elements

| Element | Syntax | Use |
|---------|--------|-----|
| Person | `Person(id, "Name", "Desc")` | Human users |
| System | `System(id, "Name", "Desc")` | System in scope |
| External System | `System_Ext(id, "Name", "Desc")` | External systems |
| Relationship | `Rel(from, to, "Label", "Tech")` | Interactions |

### Government project patterns

Always include these actors where applicable:
- **Ciudadano** — end user requesting services
- **Funcionario** — government employee processing requests
- **Administrador** — system admin
- External: **RENAPO/CURP**, **SAT**, **Firma electronica**, **Payment gateway**

## C4 Container Diagram

Shows the internal containers (applications, databases, etc.) within the system.

### Syntax

```mermaid
C4Container
    title Container — [Nombre del Sistema]

    Person(ciudadano, "Ciudadano", "Realiza tramites en linea")

    Container_Boundary(sistema, "Sistema de Tramites") {
        Container(web, "Aplicacion Web", "Next.js", "Interfaz de usuario para ciudadanos")
        Container(api, "API Backend", "Node.js/Go", "Logica de negocio y API REST")
        Container(worker, "Worker", "Node.js/Go", "Procesamiento asincrono de tramites")
        ContainerDb(db, "Base de Datos", "PostgreSQL", "Almacena tramites, usuarios, documentos")
        ContainerDb(cache, "Cache", "Redis", "Cache de sesiones y datos frecuentes")
        ContainerDb(storage, "Almacenamiento", "S3/MinIO", "Documentos y archivos adjuntos")
        Container(queue, "Cola de Mensajes", "RabbitMQ", "Comunicacion asincrona entre servicios")
    }

    System_Ext(curp, "RENAPO/CURP", "Validacion de identidad")

    Rel(ciudadano, web, "Usa", "HTTPS")
    Rel(web, api, "Consume", "HTTPS/JSON")
    Rel(api, db, "Lee/Escribe", "SQL/TLS")
    Rel(api, cache, "Lee/Escribe", "Redis protocol")
    Rel(api, storage, "Almacena archivos", "S3 API")
    Rel(api, queue, "Publica eventos", "AMQP")
    Rel(worker, queue, "Consume eventos", "AMQP")
    Rel(worker, db, "Lee/Escribe", "SQL/TLS")
    Rel(api, curp, "Valida identidad", "API REST")
```

### Elements

| Element | Syntax | Use |
|---------|--------|-----|
| Container | `Container(id, "Name", "Tech", "Desc")` | Application/service |
| Container DB | `ContainerDb(id, "Name", "Tech", "Desc")` | Database/store |
| Container Queue | `ContainerQueue(id, "Name", "Tech", "Desc")` | Message queue |
| Boundary | `Container_Boundary(id, "Name") { ... }` | System boundary |

## Best practices

1. **One system per diagram** — don't mix multiple systems in scope
2. **Limit to 10-15 elements** — split if needed
3. **Use clear labels** — especially for relationships (verb + protocol)
4. **External systems outside boundary** — keep the visual distinction clear
5. **Consistent naming** — use the same names in Context and Container diagrams

## Mermaid C4 limitations

- No C4 Component or Code level support (use regular flowcharts instead)
- Limited styling options compared to dedicated C4 tools
- Boundary nesting is limited to one level
- Large diagrams may render poorly — keep element count low
- Always validate with `mermaid_validate` before publishing

## Fallback: Flowchart for C4 Component

When you need a Component-level diagram, use a standard flowchart:

```mermaid
graph TB
    subgraph "API Backend"
        router[Router / Middleware]
        auth[Auth Controller]
        tramites[Tramites Controller]
        docs[Documents Controller]
        authSvc[Auth Service]
        tramSvc[Tramites Service]
        docSvc[Documents Service]
        repo[Repository Layer]
    end

    router --> auth
    router --> tramites
    router --> docs
    auth --> authSvc
    tramites --> tramSvc
    docs --> docSvc
    authSvc --> repo
    tramSvc --> repo
    docSvc --> repo
```

---
Generado con AI (tecnologia-morelos-workflow v0.1.0), revisado por [nombre]
