# Quality Requirements — [Nombre del Proyecto]

**Fecha**: [YYYY-MM-DD]
**Versión**: 1.0
**Autor**: AI (tecnologia-morelos-workflow), revisado por [nombre]
**Estado**: Draft / Aprobado

## Performance

| Métrica | Requisito | Condiciones | Método de verificación |
|---------|-----------|-------------|------------------------|
| Tiempo de respuesta (p50) | < [X] ms | [Carga normal] | [Load test / APM] |
| Tiempo de respuesta (p95) | < [X] ms | [Carga normal] | [Load test / APM] |
| Throughput | [X] requests/segundo | [Carga pico] | [Load test] |
| Concurrencia | [X] usuarios simultáneos | [Escenario típico] | [Load test] |
| Tiempo de carga inicial | < [X] segundos | [Conexión promedio] | [Lighthouse / WebPageTest] |

## Seguridad

### Autenticación

- [Mecanismo de autenticación requerido (e.g., SSO, OAuth 2.0, MFA)]
- [Política de contraseñas si aplica]
- [Timeout de sesión]

### Autorización

- [Modelo de control de acceso (RBAC, ABAC, etc.)]
- [Principio de mínimo privilegio]
- [Segregación de funciones si aplica]

### Cifrado

| Dato | En tránsito | En reposo | Estándar |
|------|-------------|-----------|----------|
| [Tipo de dato] | [TLS 1.2+] | [AES-256] | [Referencia normativa] |

### Auditoría

- [Qué eventos se registran]
- [Retención de logs]
- [Acceso a logs de auditoría]

## Disponibilidad

| Métrica | Requisito | Notas |
|---------|-----------|-------|
| Uptime SLA | [99.X%] | [Horario de servicio] |
| RTO (Recovery Time Objective) | [X horas] | [Tiempo máximo de recuperación] |
| RPO (Recovery Point Objective) | [X horas] | [Máxima pérdida de datos aceptable] |
| Ventana de mantenimiento | [Horario] | [Frecuencia y comunicación] |

### Disaster Recovery

- [Estrategia de respaldo (frecuencia, retención)]
- [Sitio de DR si aplica]
- [Procedimiento de failover]

## Escalabilidad

| Dimensión | Actual | Target (1 año) | Target (3 años) |
|-----------|--------|-----------------|------------------|
| Usuarios | [N] | [N] | [N] |
| Registros / datos | [N] | [N] | [N] |
| Transacciones / día | [N] | [N] | [N] |

- [Estrategia de escalado (horizontal/vertical)]
- [Límites conocidos]

## Accesibilidad

| Criterio | Requisito | Referencia |
|----------|-----------|------------|
| Estándar | WCAG 2.2 AA | [wcag.com] |
| Lectores de pantalla | Compatible | WCAG 4.1.2 |
| Navegación por teclado | Completa | WCAG 2.1.1 |
| Contraste de color | Ratio mínimo 4.5:1 | WCAG 1.4.3 |
| Textos alternativos | Todas las imágenes | WCAG 1.1.1 |
| Formularios | Labels asociados, errores descriptivos | WCAG 3.3 |

## Mantenibilidad

- [Cobertura de tests mínima requerida (e.g., 80% líneas)]
- [Estándares de código (linters, formatters)]
- [Documentación de código requerida]
- [Complejidad ciclomática máxima]
- [Estrategia de versionado (SemVer)]

## Compatibilidad

### Browsers

| Browser | Versión mínima | Nivel de soporte |
|---------|----------------|------------------|
| Chrome | [Últimas 2 versiones] | Completo |
| Firefox | [Últimas 2 versiones] | Completo |
| Safari | [Últimas 2 versiones] | Completo |
| Edge | [Últimas 2 versiones] | Completo |

### Dispositivos

| Tipo | Resolución mínima | Nivel de soporte |
|------|-------------------|------------------|
| Desktop | [1280x720] | Completo |
| Tablet | [768x1024] | Completo |
| Mobile | [360x640] | [Completo / Básico] |

## Internacionalización

[Incluir esta sección solo si el proyecto requiere soporte multilingüe.]

- Idioma principal: Español (es-MX)
- [Idiomas adicionales si aplica]
- [Formato de fechas, moneda, números]
- [Estrategia de localización]

---
Generado con AI (tecnologia-morelos-workflow v0.1.0), revisado por [nombre]
