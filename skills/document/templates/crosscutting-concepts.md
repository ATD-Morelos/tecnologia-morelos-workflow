# Crosscutting Concepts — [Nombre del Proyecto]

## Modelo de dominio

### Entidades principales

[Describir las entidades clave del dominio y sus relaciones.
Incluir diagrama ERD — ver skill visualize.]

| Entidad | Descripción | Atributos clave |
|---------|-------------|-----------------|
| [Ciudadano] | [Persona que realiza un tramite] | [CURP, nombre, contacto] |
| [Tramite] | [Solicitud de servicio gubernamental] | [folio, tipo, estado, fecha] |
| [Documento] | [Archivo adjunto o generado] | [tipo, formato, hash] |

### Reglas de negocio

1. [Regla 1 — Ej. Un tramite debe tener al menos un documento de identificacion]
2. [Regla 2 — Ej. Los folios son unicos y secuenciales por tipo de tramite]
3. [Regla 3 — Ej. Un tramite no puede cambiar de estado retroactivamente]

## Patrones de arquitectura

### Patron principal

[Describir el patron arquitectonico elegido y por que.]

- **Patron**: [Ej. Layered / Hexagonal / Microservicios / Event-driven]
- **Razon**: [Por que este patron es adecuado para el proyecto]

### Patrones de diseño aplicados

| Patron | Donde se aplica | Beneficio |
|--------|-----------------|-----------|
| [Repository] | [Acceso a datos] | [Abstraccion de persistencia] |
| [CQRS] | [Lecturas vs escrituras] | [Optimizacion de consultas] |
| [Circuit Breaker] | [Integraciones externas] | [Resiliencia] |

## Estrategia de seguridad

### Autenticación

- **Método**: [Ej. JWT / OAuth 2.0 / SAML]
- **Proveedor**: [Ej. Propio / Keycloak / Auth0]
- **Sesiones**: [Duracion, refresh, revocacion]

### Autorización

- **Modelo**: [Ej. RBAC / ABAC]
- **Roles definidos**: [Listar roles y permisos principales]
- **Granularidad**: [Nivel de recurso / operacion]

### Proteccion de datos

- **En tránsito**: [TLS 1.2+ para todas las comunicaciónes]
- **En reposo**: [AES-256 para datos sensibles]
- **Datos personales**: [Referencia a Privacy Impact Assessment]
- **Sanitización**: [Validación de entrada, escapado de salida]

Ver **Security / Threat Model** para analisis de amenazas completo.

## Logging y monitoreo

### Estrategia de logging

| Nivel | Uso | Ejemplo |
|-------|-----|---------|
| ERROR | Fallos que requieren atencion inmediata | Fallo de conexion a BD |
| WARN | Situaciones inesperadas recuperables | Timeout en integracion, reintento exitoso |
| INFO | Eventos de negocio relevantes | Tramite creado, pago recibido |
| DEBUG | Detalle tecnico para depuracion | Query ejecutada, payload recibido |

### Formato de logs

```
[timestamp] [level] [service] [traceId] [message] [context]
```

### Métricas a monitorear

| Métrica | Tipo | Alerta |
|---------|------|--------|
| [Request latency P95] | [Histograma] | [> X ms] |
| [Error rate] | [Contador] | [> X%] |
| [CPU/Memory usage] | [Gauge] | [> X%] |
| [Active users] | [Gauge] | [Informativo] |

### Herramientas

- **Logs**: [Ej. ELK / CloudWatch / Loki]
- **Métricas**: [Ej. Prometheus + Grafana / Datadog]
- **Trazas**: [Ej. Jaeger / OpenTelemetry]
- **Alertas**: [Ej. PagerDuty / Grafana Alerting]

## Manejo de errores

### Estrategia general

- **Errores de validación**: Retornar 400 con detalle de campos invalidos
- **Errores de negocio**: Retornar 422 con codigo de error de dominio
- **Errores de servidor**: Retornar 500, loggear stack trace, no exponer detalles
- **Errores de integracion**: Aplicar circuit breaker, reintentar con backoff

### Formato de error estandar

```json
{
  "error": {
    "code": "[DOMAIN_ERROR_CODE]",
    "message": "[Mensaje legible para el usuario]",
    "details": [
      {
        "field": "[campo]",
        "issue": "[descripcion del problema]"
      }
    ],
    "traceId": "[ID para soporte tecnico]"
  }
}
```

### Codigos de error de dominio

| Codigo | Significado | HTTP Status |
|--------|-------------|-------------|
| [TRAMITE_NOT_FOUND] | [Tramite no existe] | [404] |
| [TRAMITE_INVALID_STATE] | [Transicion de estado no permitida] | [422] |
| [AUTH_EXPIRED] | [Sesion expirada] | [401] |

## Internacionalizacion

### Idiomas soportados

- **Idioma principal**: Espanol (es-MX)
- **Idiomas adicionales**: [Si aplica]

### Estrategia

- [Textos de UI externalizados en archivos de recursos]
- [Fechas y moneda en formato mexicano (dd/mm/yyyy, $X,XXX.XX MXN)]
- [Mensajes de error localizados]
- [Contenido legal solo en espanol]

## Testabilidad

### Principios

- [Inyeccion de dependencias para facilitar mocking]
- [Interfaces claras entre capas]
- [Datos de prueba separados de datos de produccion]
- [Ambientes de testing aislados]

### Estrategia por capa

| Capa | Tipo de test | Herramienta |
|------|-------------|-------------|
| [Dominio] | [Unit tests] | [Ej. Jest / Go test] |
| [API] | [Integration tests] | [Ej. Supertest / httptest] |
| [UI] | [E2E tests] | [Ej. Playwright / Cypress] |

Ver **Testing Strategy** para detalle completo.

## Configuración

### Estrategia

- [Variables de entorno para configuración por ambiente]
- [Secrets en vault seguro, nunca en codigo]
- [Configuración por defecto sensata para desarrollo local]
- [Feature flags para funcionalidad en progreso]

### Variables principales

| Variable | Descripción | Ambiente |
|----------|-------------|----------|
| [DATABASE_URL] | [Connection string de BD] | [Todos] |
| [API_SECRET_KEY] | [Llave de firma JWT] | [Todos] |
| [LOG_LEVEL] | [Nivel de logging] | [Por ambiente] |

---
Generado con AI (tecnologia-morelos-workflow v0.1.0), revisado por [nombre]
