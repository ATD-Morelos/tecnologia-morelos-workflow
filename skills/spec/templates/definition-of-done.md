# Definition of Done (Draft) — [Nombre del Proyecto]

**Fecha**: [YYYY-MM-DD]
**Versión**: Draft (se finaliza en Fase 2)
**Autor**: AI (tecnologia-morelos-workflow), revisado por [nombre]
**Estado**: Draft

> **Nota:** Este es un borrador inicial basado en los requerimientos de calidad
> identificados en la fase de especificación. Se finalizará en la Fase 2
> (Design & Plan) después de tomar decisiones de arquitectura y tecnología.

## Criterios de código

- [ ] Code review aprobado por al menos [N] revisor(es)
- [ ] Sin errores de linting (configuración del proyecto)
- [ ] Sin warnings nuevos introducidos
- [ ] Código formateado según estándares del proyecto
- [ ] Sin secrets o credenciales hardcodeadas
- [ ] Sin TODOs sin ticket asociado

## Criterios de documentación

- [ ] Documentación técnica actualizada en TM
- [ ] Changelog actualizado con los cambios realizados
- [ ] README actualizado si hay cambios en setup o configuración
- [ ] Comentarios en código solo donde la lógica no es auto-explicativa
- [ ] API documentada (si se crearon/modificaron endpoints)

## Criterios de testing

### Unit tests

- [ ] Tests unitarios escritos para nueva funcionalidad
- [ ] Cobertura mínima: [X]% de líneas
- [ ] Todos los tests pasan en CI

### Integration tests

- [ ] Tests de integración para flujos principales
- [ ] Integraciones con sistemas externos verificadas
- [ ] Tests de base de datos (si aplica)

### End-to-end tests

- [ ] Flujos críticos cubiertos con tests E2E
- [ ] Tests ejecutados en ambiente similar a producción

### Otros tests

- [ ] Tests de regresión ejecutados
- [ ] Tests de performance (si aplica al cambio)

## Criterios de accesibilidad

- [ ] Navegación por teclado funcional
- [ ] Compatible con lectores de pantalla
- [ ] Contraste de color cumple WCAG 2.2 AA (ratio 4.5:1)
- [ ] Textos alternativos en imágenes
- [ ] Formularios con labels y mensajes de error descriptivos
- [ ] Verificado con herramienta automatizada (axe, Lighthouse)

## Criterios de seguridad

- [ ] Sin vulnerabilidades conocidas en dependencias
- [ ] Inputs validados y sanitizados
- [ ] Autenticación y autorización verificadas
- [ ] Sin exposición de datos sensibles en logs o responses
- [ ] Headers de seguridad configurados (CSP, HSTS, etc.)
- [ ] Revisión de OWASP Top 10 para cambios relevantes

## Criterios de deployment

- [ ] Desplegado y verificado en staging
- [ ] Smoke tests pasados en staging
- [ ] Plan de rollback documentado y probado
- [ ] Configuración de ambiente verificada (env vars, secrets)
- [ ] Monitoreo y alertas configuradas
- [ ] Migrations ejecutadas exitosamente (si aplica)

## Criterios de aceptación del usuario

- [ ] Criterios de aceptación de la user story cumplidos
- [ ] Demo o revisión con stakeholder(s) completada
- [ ] Feedback incorporado o documentado como ticket futuro
- [ ] Product Owner / usuario aprueba la funcionalidad

---
Generado con AI (tecnologia-morelos-workflow v0.1.0), revisado por [nombre]
