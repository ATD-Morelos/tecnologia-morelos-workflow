# Security / Threat Model — [Nombre del Proyecto]

## Activos a proteger

| ID | Activo | Tipo | Clasificacion | Descripción |
|----|--------|------|---------------|-------------|
| A1 | [Datos personales de ciudadanos] | Datos | Confidencial | [CURP, nombre, domicilio, contacto] |
| A2 | [Credenciales de acceso] | Datos | Secreto | [Passwords, tokens, API keys] |
| A3 | [Documentos oficiales] | Datos | Interno | [Actas, constancias, resoluciones] |
| A4 | [Servicio de tramites] | Servicio | Crítico | [Disponibilidad del sistema] |
| A5 | [Infraestructura de computo] | Infra | Interno | [Servidores, redes, BD] |

## Superficies de ataque

### Interfaz web pública

- **Exposicion**: Internet
- **Usuarios**: Ciudadanos, publico general
- **Riesgos principales**: Inyeccion, XSS, CSRF, fuerza bruta

### API REST

- **Exposicion**: Internet (autenticada)
- **Usuarios**: Aplicaciones cliente, integraciones
- **Riesgos principales**: Inyeccion, broken auth, IDOR, rate abuse

### Panel de administracion

- **Exposicion**: Red interna / VPN
- **Usuarios**: Personal de gobierno
- **Riesgos principales**: Escalacion de privilegios, acceso no autorizado

### Base de datos

- **Exposicion**: Red interna
- **Usuarios**: Servicios backend
- **Riesgos principales**: SQL injection (via app), acceso directo no autorizado

### Integraciones externas

- **Exposicion**: Red interna / APIs externas
- **Sistemas**: [Listar sistemas con los que se integra]
- **Riesgos principales**: Man-in-the-middle, datos manipulados, disponibilidad

## Amenazas identificadas (STRIDE)

### Spoofing (Suplantacion de identidad)

| ID | Amenaza | Superficie | Activo | Probabilidad | Impacto | Riesgo |
|----|---------|------------|--------|--------------|---------|--------|
| S1 | [Suplantacion de ciudadano via credenciales robadas] | [Web] | [A1, A3] | [Media] | [Alto] | [Alto] |
| S2 | [Suplantacion de API client con token robado] | [API] | [A2] | [Media] | [Alto] | [Alto] |
| S3 | [Suplantacion de admin con credenciales comprometidas] | [Admin] | [A1-A5] | [Baja] | [Crítico] | [Alto] |

### Tampering (Alteracion)

| ID | Amenaza | Superficie | Activo | Probabilidad | Impacto | Riesgo |
|----|---------|------------|--------|--------------|---------|--------|
| T1 | [Modificacion de datos de tramite en tránsito] | [API] | [A3] | [Baja] | [Alto] | [Medio] |
| T2 | [Alteracion de documentos oficiales almacenados] | [BD] | [A3] | [Baja] | [Crítico] | [Alto] |
| T3 | [Manipulacion de parametros de request] | [Web/API] | [A1] | [Alta] | [Medio] | [Alto] |

### Repudiation (Repudio)

| ID | Amenaza | Superficie | Activo | Probabilidad | Impacto | Riesgo |
|----|---------|------------|--------|--------------|---------|--------|
| R1 | [Usuario niega haber realizado un tramite] | [Web] | [A3] | [Media] | [Medio] | [Medio] |
| R2 | [Admin niega haber modificado un registro] | [Admin] | [A1] | [Baja] | [Alto] | [Medio] |

### Information Disclosure (Divulgacion de información)

| ID | Amenaza | Superficie | Activo | Probabilidad | Impacto | Riesgo |
|----|---------|------------|--------|--------------|---------|--------|
| I1 | [Exposicion de datos personales via API] | [API] | [A1] | [Media] | [Crítico] | [Crítico] |
| I2 | [Fuga de información en mensajes de error] | [Web/API] | [A2, A5] | [Media] | [Medio] | [Medio] |
| I3 | [Acceso no autorizado a documentos de otros usuarios] | [Web] | [A3] | [Media] | [Alto] | [Alto] |

### Denial of Service (Denegacion de servicio)

| ID | Amenaza | Superficie | Activo | Probabilidad | Impacto | Riesgo |
|----|---------|------------|--------|--------------|---------|--------|
| D1 | [DDoS contra interfaz web pública] | [Web] | [A4] | [Media] | [Alto] | [Alto] |
| D2 | [Abuso de API sin rate limiting] | [API] | [A4] | [Alta] | [Medio] | [Alto] |
| D3 | [Consumo de recursos via uploads maliciosos] | [Web] | [A4, A5] | [Media] | [Medio] | [Medio] |

### Elevation of Privilege (Escalacion de privilegios)

| ID | Amenaza | Superficie | Activo | Probabilidad | Impacto | Riesgo |
|----|---------|------------|--------|--------------|---------|--------|
| E1 | [Ciudadano accede a funciones de admin] | [Web] | [A1-A5] | [Baja] | [Crítico] | [Alto] |
| E2 | [IDOR — acceso a recursos de otros usuarios] | [API] | [A1, A3] | [Media] | [Alto] | [Alto] |

## Controles existentes

| ID | Control | Amenazas mitigadas | Estado |
|----|---------|-------------------|--------|
| C1 | [HTTPS/TLS en todas las comunicaciónes] | [T1, I1] | [Implementado / Planeado] |
| C2 | [Autenticación con JWT + refresh tokens] | [S1, S2] | [Implementado / Planeado] |
| C3 | [RBAC para autorizacion] | [E1, E2] | [Implementado / Planeado] |
| C4 | [Validación de entrada en servidor] | [T3] | [Implementado / Planeado] |
| C5 | [Audit log de operaciones criticas] | [R1, R2] | [Implementado / Planeado] |

## Controles propuestos

| ID | Control | Amenazas mitigadas | Prioridad | Esfuerzo |
|----|---------|-------------------|-----------|----------|
| P1 | [WAF (Web Application Firewall)] | [D1, T3] | [Alta] | [Medio] |
| P2 | [Rate limiting por usuario/IP] | [D2] | [Alta] | [Bajo] |
| P3 | [MFA para panel de administracion] | [S3] | [Alta] | [Medio] |
| P4 | [Cifrado en reposo para datos personales] | [I1] | [Alta] | [Medio] |
| P5 | [Validación de integridad de documentos (hash)] | [T2] | [Media] | [Bajo] |
| P6 | [Limite de tamano y tipo de archivo en uploads] | [D3] | [Media] | [Bajo] |
| P7 | [Pruebas de penetracion periodicas] | [Todas] | [Media] | [Alto] |

## Plan de remediacion

| Fase | Controles | Timeline | Responsable |
|------|-----------|----------|-------------|
| Fase 1 — Críticos | [P2, P3, P4] | [Sprint 1-2] | [Equipo de seguridad] |
| Fase 2 — Altos | [P1, P5, P6] | [Sprint 3-4] | [Equipo de desarrollo] |
| Fase 3 — Continuos | [P7] | [Trimestral] | [Equipo de seguridad] |

## Referencias

- OWASP Top 10 (2021)
- STRIDE Threat Modeling
- LGPDPPSO — Ley General de Proteccion de Datos Personales en Posesion de Sujetos Obligados
- MAAGTICSI — Manual Administrativo de Aplicacion General en materia de TIC y de seguridad de la información

---
Generado con AI (tecnologia-morelos-workflow v0.1.0), revisado por [nombre]
