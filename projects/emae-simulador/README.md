# Simulador EMAE — Incidencias Sectoriales

Herramienta interactiva para analizar y proyectar el impacto sectorial en el EMAE (Estimador Mensual de Actividad Económica) de Argentina.

## ¿Qué hace?

### Tab Análisis
Permite seleccionar un período publicado y simular escenarios alternativos de variación sectorial, calculando automáticamente el impacto en el EMAE total interanual.

### Tab Proyección
Permite proyectar el EMAE del mes siguiente al último dato disponible. Para cada sector se pueden ingresar tres valores alternativos sincronizados entre sí:
- **Índice proyectado**: el nivel esperado del índice
- **Variación interanual %**: respecto al mismo mes del año anterior
- **Variación mensual %**: respecto al mes anterior (t‑1)

Cualquiera de los tres campos se puede completar y los otros dos se calculan automáticamente.

## Metodología
- Ponderador implícito = (idx_sector_t12 / idx_EMAE_t12) × ponderación base 2004
- Impuestos netos de subsidios: variación propia en Análisis; proporcional al VA proyectado en Proyección
- Sector P (Hogares con servicio doméstico, 0,63%) sin índice mensual: ponderación redistribuida proporcionalmente entre sectores A–O e Impuestos (factor ×1,006312) para que los ponderadores sumen 100%

## Fuente de datos
INDEC — EMAE base 2004=100. Elaboración propia.

## Deploy
Sitio estático desplegado en Vercel.

https://emae-simulador.vercel.app/


