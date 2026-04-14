# Functional Spec — [Nombre del Proyecto]

**Fecha**: [YYYY-MM-DD]
**Versión**: 1.0
**Autor**: AI (tecnologia-morelos-workflow), revisado por [nombre]
**Estado**: Draft / Aprobado

## Alcance del sistema

[Descripción del alcance funcional del sistema. Qué hace y qué NO hace.
Referencia al PRD para contexto de producto.]

### Límites del sistema

[Dónde empieza y termina la responsabilidad de este sistema. Interfaces
con sistemas externos.]

## Actores y roles

| Actor | Descripción | Permisos / Capacidades |
|-------|-------------|------------------------|
| [Actor 1] | [Descripción del rol] | [Qué puede hacer en el sistema] |
| [Actor 2] | [Descripción del rol] | [Qué puede hacer en el sistema] |
| [Sistema externo] | [Descripción] | [Tipo de interacción] |

## Casos de uso detallados

### CU-001: [Nombre del caso de uso]

| Campo | Descripción |
|-------|-------------|
| **ID** | CU-001 |
| **Nombre** | [Nombre descriptivo] |
| **Actor principal** | [Actor] |
| **Precondiciones** | [Qué debe ser cierto antes de iniciar] |
| **Postcondiciones** | [Qué es cierto al terminar exitosamente] |
| **Requisitos relacionados** | RF-001, RF-002 |

**Flujo principal:**
1. [Paso 1]
2. [Paso 2]
3. [Paso 3]

**Flujos alternativos:**
- **2a.** [Condición alternativa]: [Qué sucede]
- **3a.** [Condición alternativa]: [Qué sucede]

**Flujos de excepción:**
- **E1.** [Error o condición excepcional]: [Cómo responde el sistema]

### CU-002: [Nombre del caso de uso]

| Campo | Descripción |
|-------|-------------|
| **ID** | CU-002 |
| **Nombre** | [Nombre descriptivo] |
| **Actor principal** | [Actor] |
| **Precondiciones** | [Qué debe ser cierto antes de iniciar] |
| **Postcondiciones** | [Qué es cierto al terminar exitosamente] |
| **Requisitos relacionados** | RF-003 |

**Flujo principal:**
1. [Paso 1]
2. [Paso 2]

**Flujos de excepción:**
- **E1.** [Error]: [Respuesta del sistema]

## Reglas de negocio

| ID | Regla | Descripción | Fuente |
|----|-------|-------------|--------|
| RN-001 | [Nombre corto] | [Descripción detallada de la regla] | [Normatividad / stakeholder] |
| RN-002 | [Nombre corto] | [Descripción detallada de la regla] | [Normatividad / stakeholder] |

## Validaciones y restricciones

| Campo / Dato | Validación | Mensaje de error |
|-------------|------------|------------------|
| [Campo 1] | [Regla de validación] | [Mensaje al usuario] |
| [Campo 2] | [Regla de validación] | [Mensaje al usuario] |

## Interfaces del sistema

### APIs

| Endpoint / Servicio | Método | Descripción | Autenticación |
|---------------------|--------|-------------|---------------|
| [Endpoint] | [GET/POST/etc.] | [Qué hace] | [Tipo de auth] |

### Interfaz de usuario

[Descripción de alto nivel de las pantallas o vistas principales.
Referencia a wireframes si existen en la fase de diseño.]

| Pantalla / Vista | Propósito | Actores |
|-----------------|-----------|---------|
| [Vista 1] | [Qué permite hacer] | [Quién la usa] |

### Integraciones externas

| Sistema externo | Tipo de integración | Protocolo | Datos intercambiados |
|----------------|---------------------|-----------|----------------------|
| [Sistema] | [Síncrona/Asíncrona] | [REST/SOAP/MQ/etc.] | [Descripción] |

## Manejo de errores

| Escenario | Tipo | Comportamiento esperado | Mensaje al usuario |
|-----------|------|-------------------------|-------------------|
| [Escenario 1] | [Validación/Sistema/Red] | [Qué hace el sistema] | [Qué ve el usuario] |
| [Escenario 2] | [Validación/Sistema/Red] | [Qué hace el sistema] | [Qué ve el usuario] |

---
Generado con AI (tecnologia-morelos-workflow v0.1.0), revisado por [nombre]
