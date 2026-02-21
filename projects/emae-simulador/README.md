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

-La incidencia de cada sector se calcula usando ponderadores implícitos obtenidos como (idx_sector,t‑12 / idx_EMAE,t‑12) × ponderación base 2004, multiplicados por la variación del sector en el período.

Tratamiento de casos especiales:

-Impuestos netos de subsidios: en simulación se recalculan a partir del cambio en el valor agregado de los sectores A–O, no de una variación propia. -Sector P (Hogares privados con servicio doméstico, pond. 0,63%): no cuenta con índice mensual; su ponderación se redistribuye proporcionalmente entre los sectores A–O e Impuestos (×1,006312) para que los ponderadores sumen 100%.

-La diferencia residual respecto al dato publicado por INDEC es normal dado el encadenamiento de índices.

## Fuente de datos
INDEC — EMAE base 2004=100. Elaboración propia.

## Deploy
Sitio estático desplegado en Vercel.

https://emae-simulador.vercel.app/


