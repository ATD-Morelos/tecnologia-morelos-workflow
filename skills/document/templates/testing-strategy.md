# Testing Strategy — [Nombre del Proyecto]

## Niveles de testing

### Unit tests

- **Alcance**: Funciones, metodos, clases individuales
- **Objetivo**: Verificar logica de negocio aislada
- **Cobertura objetivo**: [>80% en logica de dominio]
- **Ejecucion**: En cada commit (CI pipeline)
- **Herramienta**: [Ej. Jest / Go test / pytest]
- **Responsable**: Desarrollador que escribe el codigo

### Integration tests

- **Alcance**: Interaccion entre componentes, API endpoints, acceso a BD
- **Objetivo**: Verificar que los componentes trabajan juntos correctamente
- **Cobertura objetivo**: [>70% de endpoints, todos los flujos criticos]
- **Ejecucion**: En cada PR (CI pipeline)
- **Herramienta**: [Ej. Supertest / httptest / pytest + testcontainers]
- **Responsable**: Desarrollador + equipo de QA

### End-to-End (E2E) tests

- **Alcance**: Flujos completos de usuario desde la interfaz
- **Objetivo**: Verificar escenarios de negocio de principio a fin
- **Cobertura objetivo**: [100% de flujos criticos, >60% de flujos secundarios]
- **Ejecucion**: Pre-deploy a staging, nightly en staging
- **Herramienta**: [Ej. Playwright / Cypress]
- **Responsable**: Equipo de QA

### Performance tests

- **Alcance**: Endpoints criticos, flujos de alta carga
- **Objetivo**: Verificar que el sistema cumple los requisitos de rendimiento
- **Métricas clave**:
  - Latencia P95 < [X ms]
  - Throughput > [X requests/segundo]
  - Tiempo de respuesta bajo carga de [X] usuarios concurrentes
- **Ejecucion**: Pre-release, mensual en staging
- **Herramienta**: [Ej. k6 / JMeter / Artillery]
- **Responsable**: Equipo de desarrollo + DevOps

### Security tests

- **Alcance**: OWASP Top 10, autenticación, autorizacion, datos sensibles
- **Objetivo**: Identificar vulnerabilidades antes de produccion
- **Tipos**:
  - SAST (analisis estatico de codigo) — en cada PR
  - DAST (analisis dinamico) — pre-release
  - Dependency scanning — diario
  - Penetration testing — trimestral
- **Herramienta**: [Ej. SonarQube / OWASP ZAP / Snyk / Trivy]
- **Responsable**: Equipo de seguridad + desarrollo

## Herramientas

| Herramienta | Proposito | Capa |
|-------------|-----------|------|
| [Jest / Go test] | Unit testing | Backend |
| [React Testing Library] | Component testing | Frontend |
| [Playwright] | E2E testing | Full stack |
| [k6] | Performance testing | Backend/API |
| [SonarQube] | SAST, code quality | Codigo |
| [OWASP ZAP] | DAST | Aplicacion |
| [Snyk / Trivy] | Dependency scanning | Dependencias |

## Cobertura objetivo

| Capa | Nivel | Objetivo | Medicion |
|------|-------|----------|----------|
| Logica de dominio | Unit | [>80%] | [Statements coverage] |
| API endpoints | Integration | [>70%] | [Endpoints cubiertos / total] |
| Flujos de usuario | E2E | [100% criticos] | [Flujos cubiertos / flujos criticos] |
| Codigo total | SAST | [0 vulnerabilidades criticas/altas] | [SonarQube] |

## Ambientes de testing

| Ambiente | Proposito | Datos | Actualizacion |
|----------|-----------|-------|---------------|
| Local | Desarrollo y unit tests | Fixtures/seeds locales | Continua |
| CI | Unit + integration en pipeline | BD efimera (testcontainers) | Por commit/PR |
| Staging | E2E, performance, DAST | Datos anonimizados de produccion | Pre-release |
| Pre-prod | Smoke tests, validación final | Copia de produccion anonimizada | Pre-release |

## Datos de prueba

### Estrategia

- **Unit tests**: Fixtures y factories en codigo
- **Integration tests**: Seeds de BD + testcontainers
- **E2E tests**: Datos de prueba predefinidos en staging
- **Performance tests**: Dataset sintetico representativo del volumen de produccion

### Datos sensibles

- **Nunca** usar datos reales de ciudadanos en ambientes no productivos
- Datos de prueba deben ser sinteticos o anonimizados
- CURPs, nombres, direcciones de prueba claramente ficticios
- Cumplir con LGPDPPSO en manejo de datos de prueba

## Criterios de pase/fallo

### Para un PR (merge a main)

- [ ] Unit tests pasan al 100%
- [ ] Integration tests pasan al 100%
- [ ] Cobertura de codigo >= umbral definido
- [ ] 0 vulnerabilidades criticas/altas en SAST
- [ ] Code review aprobado
- [ ] No regresiones en tests existentes

### Para un release (deploy a produccion)

- [ ] Todos los criterios de PR
- [ ] E2E tests pasan al 100% en staging
- [ ] Performance tests dentro de umbrales
- [ ] DAST sin vulnerabilidades criticas
- [ ] Smoke tests exitosos en pre-prod
- [ ] Aprobacion de QA lead

### Para un hotfix

- [ ] Unit tests del fix pasan
- [ ] Integration tests afectados pasan
- [ ] Smoke tests en staging
- [ ] Aprobacion de tech lead

## Responsabilidades

| Rol | Responsabilidad |
|-----|-----------------|
| Desarrollador | Escribir unit tests, integration tests para su codigo |
| QA Engineer | Disenar y mantener E2E tests, validar criterios de release |
| Tech Lead | Definir estandares de testing, revisar cobertura |
| DevOps | Mantener pipeline de CI/CD, ambientes de testing |
| Security | Configurar SAST/DAST, coordinar pentesting |
| Product Owner | Definir flujos criticos que requieren E2E |

---
Generado con AI (tecnologia-morelos-workflow v0.1.0), revisado por [nombre]
