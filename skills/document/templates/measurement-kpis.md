# Measurement / KPIs — [Nombre del Proyecto]

## Objetivos del proyecto

[Extraidos del PRD. Cada objetivo debe ser SMART.]

| ID | Objetivo | Vinculo PRD |
|----|----------|-------------|
| O1 | [Objetivo 1] | [Seccion del PRD] |
| O2 | [Objetivo 2] | [Seccion del PRD] |
| O3 | [Objetivo 3] | [Seccion del PRD] |

## KPIs por objetivo

### O1 — [Nombre del objetivo]

| KPI | Baseline | Target | Frecuencia | Responsable |
|-----|----------|--------|------------|-------------|
| [KPI 1.1] | [Valor actual o N/A] | [Valor objetivo] | [Diaria/Semanal/Mensual] | [Nombre/Rol] |
| [KPI 1.2] | [Valor actual o N/A] | [Valor objetivo] | [Frecuencia] | [Nombre/Rol] |

### O2 — [Nombre del objetivo]

| KPI | Baseline | Target | Frecuencia | Responsable |
|-----|----------|--------|------------|-------------|
| [KPI 2.1] | [Valor actual o N/A] | [Valor objetivo] | [Frecuencia] | [Nombre/Rol] |
| [KPI 2.2] | [Valor actual o N/A] | [Valor objetivo] | [Frecuencia] | [Nombre/Rol] |

### O3 — [Nombre del objetivo]

| KPI | Baseline | Target | Frecuencia | Responsable |
|-----|----------|--------|------------|-------------|
| [KPI 3.1] | [Valor actual o N/A] | [Valor objetivo] | [Frecuencia] | [Nombre/Rol] |

## Métricas tecnicas

| Métrica | Descripción | Target | Alerta | Crítico |
|---------|-------------|--------|--------|---------|
| Latencia P50 | Mediana de tiempo de respuesta | [< X ms] | [> Y ms] | [> Z ms] |
| Latencia P95 | Percentil 95 de tiempo de respuesta | [< X ms] | [> Y ms] | [> Z ms] |
| Latencia P99 | Percentil 99 de tiempo de respuesta | [< X ms] | [> Y ms] | [> Z ms] |
| Uptime | Disponibilidad del servicio | [> 99.X%] | [< 99.X%] | [< 99.Y%] |
| Error rate | Porcentaje de requests con error 5xx | [< X%] | [> Y%] | [> Z%] |
| CPU usage | Uso promedio de CPU | [< X%] | [> Y%] | [> Z%] |
| Memory usage | Uso promedio de memoria | [< X%] | [> Y%] | [> Z%] |
| DB query time | Tiempo promedio de queries | [< X ms] | [> Y ms] | [> Z ms] |
| DB connections | Conexiones activas a BD | [< X] | [> Y] | [> Z] |

## Métricas de adopcion

| Métrica | Descripción | Baseline | Target (3 meses) | Target (6 meses) | Target (12 meses) |
|---------|-------------|----------|-------------------|-------------------|---------------------|
| Usuarios registrados | Total de cuentas creadas | [0 / N actual] | [Target] | [Target] | [Target] |
| Usuarios activos (MAU) | Usuarios unicos en 30 dias | [0 / N actual] | [Target] | [Target] | [Target] |
| Usuarios activos (DAU) | Usuarios unicos por dia | [0 / N actual] | [Target] | [Target] | [Target] |
| Transacciones completadas | Tramites finalizados exitosamente | [0 / N actual] | [Target] | [Target] | [Target] |
| Tasa de conversion | Tramites completados / iniciados | [N/A] | [> X%] | [> Y%] | [> Z%] |
| Tasa de abandono | Tramites abandonados / iniciados | [N/A] | [< X%] | [< Y%] | [< Z%] |
| Tiempo promedio de tramite | Minutos para completar un tramite | [N actual min] | [< X min] | [< Y min] | [< Z min] |
| NPS / Satisfaccion | Net Promoter Score o encuesta | [N/A] | [> X] | [> Y] | [> Z] |

## Dashboard propuesto

### Vista ejecutiva

Métricas para stakeholders y sponsor:
- Usuarios activos (grafica de linea, tendencia mensual)
- Transacciones completadas (grafica de barras, mensual)
- Tasa de conversion (indicador tipo gauge)
- NPS / Satisfaccion (indicador con tendencia)

### Vista operativa

Métricas para equipo tecnico:
- Latencia P95 (grafica de linea, tiempo real)
- Error rate (grafica de linea, tiempo real)
- Uptime (indicador de porcentaje, mensual)
- CPU/Memory usage (graficas de area, tiempo real)

### Vista de producto

Métricas para product owner:
- Funnel de conversion (grafica de embudo)
- Tiempo promedio por paso del tramite (barras horizontales)
- Top errores de usuario (tabla)
- Adopcion por municipio/region (mapa de calor)

### Herramientas sugeridas

| Herramienta | Uso | Audiencia |
|-------------|-----|-----------|
| [Grafana] | Métricas tecnicas en tiempo real | Equipo tecnico |
| [Metabase / Redash] | Dashboards de negocio | Stakeholders, PO |
| [Google Analytics / Plausible] | Métricas de adopcion web | PO, UX |
| [Sentry] | Monitoreo de errores | Equipo tecnico |

## Plan de revision

| Frecuencia | Que se revisa | Participantes | Formato |
|------------|---------------|---------------|---------|
| Diaria | Métricas tecnicas (alertas) | DevOps on-call | Automatico |
| Semanal | Métricas de adopcion | PO, Tech Lead | Reunion 15 min |
| Quincenal | KPIs de objetivo, tendencias | Equipo completo | Sprint review |
| Mensual | Dashboard ejecutivo, NPS | Sponsor, stakeholders | Reporte |
| Trimestral | Revision completa, ajuste de targets | Todos | Taller |

### Proceso de revision

1. Recopilar datos de las herramientas de monitoreo
2. Comparar con targets definidos
3. Identificar tendencias positivas y negativas
4. Documentar acciones correctivas si hay desviaciones
5. Ajustar targets si las condiciones han cambiado
6. Actualizar este documento con los resultados

---
Generado con AI (tecnologia-morelos-workflow v0.1.0), revisado por [nombre]
