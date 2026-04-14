# API Reference — [Nombre del Proyecto]

> **Nota**: Este documento define la API inicial basada en los requerimientos. La referencia viva
> debe auto-generarse del codigo (OpenAPI/Swagger) una vez que la implementacion comience.

## Base URL

| Ambiente | URL |
|----------|-----|
| Producción | `https://[dominio]/api/v1` |
| Staging | `https://staging.[dominio]/api/v1` |
| Desarrollo | `http://localhost:[puerto]/api/v1` |

## Autenticación

### Método

[Ej. Bearer Token (JWT)]

### Obtener token

```
POST /auth/login
Content-Type: application/json

{
  "email": "usuario@ejemplo.com",
  "password": "********"
}
```

**Respuesta exitosa (200)**:
```json
{
  "accessToken": "eyJhbG...",
  "refreshToken": "eyJhbG...",
  "expiresIn": 3600,
  "tokenType": "Bearer"
}
```

### Usar token

```
Authorization: Bearer eyJhbG...
```

### Renovar token

```
POST /auth/refresh
Content-Type: application/json

{
  "refreshToken": "eyJhbG..."
}
```

## Endpoints

### [Recurso 1 — Ej. Tramites]

| Método | Path | Descripción | Auth |
|--------|------|-------------|------|
| GET | `/tramites` | Listar tramites del usuario | Si |
| POST | `/tramites` | Crear nuevo tramite | Si |
| GET | `/tramites/:id` | Obtener detalle de tramite | Si |
| PUT | `/tramites/:id` | Actualizar tramite | Si |
| DELETE | `/tramites/:id` | Cancelar tramite | Si |
| POST | `/tramites/:id/documentos` | Adjuntar documento | Si |
| PUT | `/tramites/:id/estado` | Cambiar estado (admin) | Si (admin) |

#### GET /tramites

**Query parameters**:

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `page` | integer | No | Numero de pagina (default: 1) |
| `limit` | integer | No | Resultados por pagina (default: 20, max: 100) |
| `estado` | string | No | Filtrar por estado |
| `tipo` | string | No | Filtrar por tipo de tramite |
| `desde` | date | No | Fecha inicio (ISO 8601) |
| `hasta` | date | No | Fecha fin (ISO 8601) |

**Respuesta (200)**:
```json
{
  "data": [
    {
      "id": "uuid",
      "folio": "TRM-2026-00001",
      "tipo": "licencia_funcionamiento",
      "estado": "en_revision",
      "solicitante": {
        "nombre": "Juan Perez",
        "curp": "PEPJ900101HMSRRL09"
      },
      "createdAt": "2026-01-15T10:30:00Z",
      "updatedAt": "2026-01-16T14:22:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 145,
    "totalPages": 8
  }
}
```

#### POST /tramites

**Request body**:
```json
{
  "tipo": "licencia_funcionamiento",
  "datos": {
    "nombreNegocio": "Tienda Ejemplo",
    "direccion": "Calle Principal 123, Cuernavaca, Morelos",
    "giro": "comercial"
  }
}
```

**Respuesta (201)**:
```json
{
  "id": "uuid",
  "folio": "TRM-2026-00146",
  "estado": "borrador",
  "createdAt": "2026-04-14T13:00:00Z"
}
```

### [Recurso 2 — Agregar segun Functional Spec]

[Repetir estructura de endpoints para cada recurso.]

## Codigos de error

### Errores HTTP estandar

| Codigo | Significado | Cuando ocurre |
|--------|-------------|---------------|
| 400 | Bad Request | Datos de entrada invalidos |
| 401 | Unauthorized | Token ausente, expirado o invalido |
| 403 | Forbidden | Sin permisos para la operacion |
| 404 | Not Found | Recurso no existe |
| 409 | Conflict | Conflicto de estado (ej. tramite ya completado) |
| 422 | Unprocessable Entity | Error de logica de negocio |
| 429 | Too Many Requests | Rate limit excedido |
| 500 | Internal Server Error | Error inesperado del servidor |

### Errores de dominio

| Codigo | Significado | HTTP |
|--------|-------------|------|
| TRAMITE_NOT_FOUND | Tramite no existe | 404 |
| TRAMITE_INVALID_STATE | Transicion de estado no permitida | 422 |
| TRAMITE_DUPLICATE | Tramite duplicado para este solicitante | 409 |
| DOCUMENT_TOO_LARGE | Archivo excede tamano maximo | 400 |
| DOCUMENT_INVALID_TYPE | Tipo de archivo no permitido | 400 |
| AUTH_INVALID_CREDENTIALS | Credenciales incorrectas | 401 |
| AUTH_TOKEN_EXPIRED | Token de acceso expirado | 401 |
| AUTH_INSUFFICIENT_ROLE | Rol insuficiente para la operacion | 403 |
| RATE_LIMIT_EXCEEDED | Limite de solicitudes excedido | 429 |

### Formato de error

```json
{
  "error": {
    "code": "TRAMITE_INVALID_STATE",
    "message": "No se puede cambiar el estado de 'completado' a 'borrador'",
    "details": [
      {
        "field": "estado",
        "issue": "Transicion no permitida: completado → borrador"
      }
    ],
    "traceId": "abc123-def456"
  }
}
```

## Rate limiting

| Tipo de usuario | Limite | Ventana |
|-----------------|--------|---------|
| Ciudadano | [100 requests] | [por minuto] |
| Servicio interno | [1000 requests] | [por minuto] |
| Admin | [500 requests] | [por minuto] |

**Headers de rate limit**:
```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1714600000
```

## Versionamiento

- **Estrategia**: URL path versioning (`/api/v1/`, `/api/v2/`)
- **Politica de deprecacion**: Versiones anteriores soportadas por [6 meses] despues de públicar nueva version
- **Comunicación**: Header `Deprecation` y `Sunset` en versiones antiguas

## Paginacion

Todos los endpoints de listado usan paginacion basada en offset:

```
GET /tramites?page=2&limit=20
```

Respuesta incluye metadata de paginacion:
```json
{
  "pagination": {
    "page": 2,
    "limit": 20,
    "total": 145,
    "totalPages": 8
  }
}
```

## Ejemplos

### Flujo completo: Crear y enviar un tramite

```bash
# 1. Autenticarse
TOKEN=$(curl -s -X POST https://api.ejemplo.com/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"user@ejemplo.com","password":"***"}' | jq -r '.accessToken')

# 2. Crear tramite
TRAMITE=$(curl -s -X POST https://api.ejemplo.com/api/v1/tramites \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"tipo":"licencia_funcionamiento","datos":{"nombreNegocio":"Mi Tienda"}}')

ID=$(echo $TRAMITE | jq -r '.id')

# 3. Adjuntar documento
curl -X POST "https://api.ejemplo.com/api/v1/tramites/$ID/documentos" \
  -H "Authorization: Bearer $TOKEN" \
  -F "archivo=@identificacion.pdf" \
  -F "tipo=identificacion_oficial"

# 4. Enviar tramite
curl -X PUT "https://api.ejemplo.com/api/v1/tramites/$ID/estado" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"estado":"enviado"}'
```

---
Generado con AI (tecnologia-morelos-workflow v0.1.0), revisado por [nombre]
