# Architecture Overview — [Nombre del Proyecto]

## 1. Introduccion y objetivos

### Requerimientos funcionales clave

[Listar los 3-5 requerimientos funcionales mas importantes del PRD que impactan la arquitectura.]

### Objetivos de calidad

| Prioridad | Atributo de calidad | Descripción |
|-----------|---------------------|-------------|
| 1 | [Ej. Disponibilidad] | [Descripción del objetivo] |
| 2 | [Ej. Seguridad] | [Descripción del objetivo] |
| 3 | [Ej. Rendimiento] | [Descripción del objetivo] |

### Stakeholders

| Rol | Expectativas |
|-----|-------------|
| [Sponsor] | [Expectativas respecto a la arquitectura] |
| [Usuarios finales] | [Expectativas de experiencia] |
| [Equipo de desarrollo] | [Expectativas tecnicas] |
| [Operaciónes] | [Expectativas de mantenimiento] |

## 2. Restricciones

### Restricciones tecnicas

- [Ej. Debe ejecutarse en infraestructura del estado de Morelos]
- [Ej. Debe integrarse con sistemas legacy existentes]
- [Ej. Lenguaje/framework mandatorio]

### Restricciones organizacionales

- [Ej. Equipo de N personas]
- [Ej. Presupuesto limitado]
- [Ej. Timeline de N meses]

### Restricciones regulatorias

- [Ej. LGPDPPSO — datos personales]
- [Ej. MAAGTICSI — gestion de TI en gobierno]
- [Ver Normatividad Aplicable para detalle]

## 3. Contexto del sistema

### Contexto de negocio

[Describir el sistema y sus actores externos desde la perspectiva de negocio.
Incluir un diagrama C4 Context — ver skill visualize.]

| Actor/Sistema externo | Interaccion | Formato |
|-----------------------|-------------|---------|
| [Ciudadano] | [Descripción] | [Web/API/etc.] |
| [Sistema X] | [Descripción] | [API REST/SOAP/etc.] |

### Contexto tecnico

[Describir la infraestructura tecnica y las interfaces del sistema.]

| Interfaz | Protocolo | Descripción |
|----------|-----------|-------------|
| [API pública] | [HTTPS/REST] | [Descripción] |
| [Base de datos] | [PostgreSQL] | [Descripción] |
| [Cola de mensajes] | [RabbitMQ] | [Descripción] |

## 4. Estrategia de solucion

### Decisiones tecnologicas

| Aspecto | Decision | Razon |
|---------|----------|-------|
| Lenguaje backend | [Ej. Go / Node.js] | [Razon] |
| Framework frontend | [Ej. Next.js / React] | [Razon] |
| Base de datos | [Ej. PostgreSQL] | [Razon] |
| Infraestructura | [Ej. Kubernetes / VM] | [Razon] |

### Enfoque de integracion

[Describir la estrategia para integrar con sistemas existentes.]

### Decisiones organizacionales

[Describir decisiones sobre equipo, proceso, herramientas.]

## 5. Vista de building blocks

### Nivel 1 — Sistema general

[Diagrama C4 Container — ver skill visualize.]

[Describir cada contenedor/componente principal:]

| Building block | Responsabilidad |
|----------------|-----------------|
| [API Gateway] | [Punto de entrada, autenticación, rate limiting] |
| [Servicio Core] | [Logica de negocio principal] |
| [Base de datos] | [Persistencia de datos] |
| [Frontend] | [Interfaz de usuario] |

### Nivel 2 — Componentes internos

[Para cada building block importante, detallar sus componentes internos.]

## 6. Vista de runtime

### Escenario 1: [Nombre del flujo principal]

[Describir el flujo paso a paso. Incluir diagrama de secuencia si aplica.]

1. [Paso 1]
2. [Paso 2]
3. [Paso 3]

### Escenario 2: [Nombre del flujo secundario]

[Describir otro escenario importante.]

## 7. Vista de deployment

[Describir la infraestructura donde se desplegara el sistema.
Incluir diagrama de deployment — ver skill visualize.]

| Componente | Ambiente | Infraestructura |
|------------|----------|-----------------|
| [API] | [Producción] | [Ej. Kubernetes cluster, VM] |
| [BD] | [Producción] | [Ej. RDS, servidor dedicado] |
| [Frontend] | [Producción] | [Ej. CDN, servidor web] |

### Ambientes

| Ambiente | Proposito | URL |
|----------|-----------|-----|
| Desarrollo | [Desarrollo local y pruebas] | [URL] |
| Staging | [Pre-produccion, pruebas de integracion] | [URL] |
| Producción | [Ambiente productivo] | [URL] |

## 8. Conceptos transversales

Ver documento **Crosscutting Concepts** para detalle completo.

Resumen de conceptos clave:
- Modelo de dominio
- Patrones de arquitectura
- Estrategia de seguridad
- Logging y monitoreo
- Manejo de errores

## 9. Decisiones de arquitectura

Las decisiones significativas se documentan como ADRs (Architecture Decision Records).

| ADR | Titulo | Estado | Fecha |
|-----|--------|--------|-------|
| [ADR-001] | [Titulo de la decision] | [Aceptada/Propuesta] | [Fecha] |

Ver carpeta **ADRs/** para detalle completo.

## 10. Requisitos de calidad

### Arbol de calidad

| Atributo | Escenario | Métrica |
|----------|-----------|---------|
| Disponibilidad | [El sistema debe estar disponible 99.X%] | [Uptime mensual] |
| Rendimiento | [Respuesta < Xms para el Y% de requests] | [P95 latency] |
| Seguridad | [Datos sensibles cifrados en tránsito y reposo] | [Audit compliance] |
| Usabilidad | [Un ciudadano completa el tramite en < X min] | [Task completion time] |

### Escenarios de calidad

[Detallar 3-5 escenarios concretos de calidad con estimulo, respuesta esperada y metrica.]

## 11. Riesgos

Ver documento **Risks & Technical Debt** para el registro completo.

Riesgos principales que impactan la arquitectura:
1. [Riesgo 1 — breve descripcion]
2. [Riesgo 2 — breve descripcion]
3. [Riesgo 3 — breve descripcion]

## 12. Glosario

Ver **Glosario** del proyecto para la terminologia completa.

Terminos clave para este documento:

| Termino | Definicion |
|---------|-----------|
| [Termino 1] | [Definicion] |
| [Termino 2] | [Definicion] |

---
Generado con AI (tecnologia-morelos-workflow v0.1.0), revisado por [nombre]
