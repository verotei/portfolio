# Scraper de productos – Frávega 🛒 [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Proyecto de scraping sobre el e-commerce **Frávega**.  

El objetivo es recolectar información de productos de distintas categorías, obtener precios de venta y de lista, calcular descuentos y guardar los resultados en un archivo Excel para análisis posterior.

---

## 🚀 Funcionalidad

El script:
- Navega por distintas **categorías** de productos (ejemplo: heladeras, aires acondicionados, lavarropas, cocinas).
- Recorre varias páginas por categoría (`?page=1, 2, 3...`).
- Extrae:
  - 🏷️ Nombre del producto  
  - 💲 Precio de venta  
  - 💲 Precio de lista  
  - 🔗 Link al producto  
  - 📉 Descuento calculado
- Genera un **archivo Excel** con todos los datos listos para análisis.

---

## 🤔 ¿Por qué Selenium?

Se utilizó **Selenium** porque el sitio de Frávega carga la mayoría de la información de los productos dinámicamente con **JavaScript**.  

Con esta librería es posible:
- Automatizar la navegación.  
- Esperar a que los elementos se carguen.  
- Extraer la información de forma confiable.  

Un parser de HTML estático (ej. BeautifulSoup solo) no alcanzaría en este caso.

---

## 📂 Salida

- `fravega_scrap_DD-MM-YYYY.xlsx` → archivo con los productos y precios recolectados.

### Columnas
- Fecha de relevamiento  
- Retailer  
- Link  
- Categoría  
- Producto  
- Precio de venta  
- Precio de lista  
- Descuento calculado  

---

## 📦 Requisitos

Instalar las dependencias:

```bash
pip install -r requirements.txt

---


