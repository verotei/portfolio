# Scraper de productos – Frávega 🛒

Proyecto de scraping sobre el e-commerce **Frávega**.  

El objetivo es recolectar información de productos de distintas categorías, obtener precios de venta y de lista, calcular descuentos y guardar los resultados en un archivo para análisis posterior.

---

## Funcionalidad

El script:
- Navega por distintas **categorías** de productos (ejemplo: heladeras, aires acondicionados, lavarropas).
- Recorre varias páginas por categoría.
- Extrae:
  - Nombre del producto
  - Precio de venta
  - Precio de lista
  - Link al producto
  - Descuento calculado
- Genera un **archivo Excel**.

---

## Justificación de la librería utilizada

Se utilizó **Selenium** porque el sitio de Frávega carga la mayoría de la información de los productos de manera dinámica con JavaScript.  
Con esta librería es posible automatizar la navegación, esperar a que los elementos se carguen y extraer la información de forma confiable, algo que no sería posible con un parser de HTML estático.

---

## Requisitos

Instalar las dependencias:

```bash
pip install -r requirements.txt
