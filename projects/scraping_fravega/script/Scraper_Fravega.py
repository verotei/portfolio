from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
import pandas as pd
import time

# Función pata limpiar precios

def limpiar_precio(precio):
    return precio.replace('$', '').replace('.', '').replace(',', '.')

start_time = time.time()

# Configuración inicial
options = webdriver.EdgeOptions()
options.add_argument("--start-maximized")   # arranca maximizado
options.add_argument('--blink-settings=imagesEnabled=false')  # desactiva imágenes
options.add_argument("--incognito")         # modo incógnito

driver = webdriver.Edge(options=options)

fecha_actual = date.today().strftime('%d-%m-%Y')
fecha_actual_base = f"{date.today().day}/{date.today().month}/{date.today().year}"

max_paginas = 25  #acá se puede modificar la cantidad de páginas a scraper por sección

# Defino las secciones que quiero scrapear.
# Para agregarlas hay que ver la variable web_fravega e ir mirando las url de las productos.

secciones = [
    "heladeras-freezers-y-cavas",
    "climatizacion/aire-acondicionado",
    "lavado/lavarropas",
    "cocina",
    "termotanques-y-calefones"
]

dfs = []

for seccion in secciones:
    categoria = seccion.split("/")[-1]
    for i in range(1, max_paginas + 1):
        try:
            web_fravega = f"https://www.fravega.com/l/{seccion}/?page={i}"
            driver.get(web_fravega)
            time.sleep(5)

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

        except NoSuchElementException:
            print(f"La página {i} no existe.")
            break

        try:
            contenedor = driver.find_element(By.XPATH, "//ul[@data-test-id='results-list']")
        except NoSuchElementException:
            print(f"No se encontraron productos de {seccion} en la página {i}.")
            break

        articulos = contenedor.find_elements(By.XPATH, ".//article[@data-test-id = 'result-item']")

        lista_productos = []
        lista_precios = []
        lista_precios_lista = []
        lista_links = []

        for articulo in articulos:
            try:
                nombre_producto = articulo.find_element(By.XPATH, ".//span[@class = 'sc-1fa74e6c-0 kUaLHc']").text
                link = articulo.find_element(By.XPATH, ".//a").get_attribute("href")
                precio_producto = articulo.find_element(By.XPATH, ".//span[@class = 'sc-1d9b1d9e-0 OZgQ']").text

                try:
                    precio_lista = articulo.find_element(By.XPATH, ".//span[@class = 'sc-e081bce1-0 eudnWN']").text
                except NoSuchElementException:
                    precio_lista = precio_producto

                lista_productos.append(nombre_producto)
                lista_links.append(link)
                lista_precios.append(precio_producto)
                lista_precios_lista.append(precio_lista)

            except StaleElementReferenceException:
                print("El elemento se volvió 'stale'. Refrescando la página.")
                driver.refresh()
                time.sleep(5)

            except NoSuchElementException:
                print("Elemento no encontrado. Puede haber cambiado la estructura de la página.")


        # Estos print los incluí para poder ir viendo la descarga en consola.

        print(lista_productos)
        print(len(lista_productos))
        print(lista_precios)
        print(len(lista_precios))
        print(lista_precios_lista)
        print(len(lista_precios_lista))
        print(lista_links)
        print(len(lista_links))

        data = {
            'Fecha_relevamiento': fecha_actual_base,
            'Retailer': "Frávega",
            'Link': lista_links,
            'Categoría': categoria,
            'Producto': lista_productos,
            'Precio_venta': lista_precios,
            'Precio_lista': lista_precios_lista,

        }
        df = pd.DataFrame(data)
        df['Precio_venta'] = df['Precio_venta'].apply(limpiar_precio).astype(float)
        df['Precio_lista'] = df['Precio_lista'].apply(limpiar_precio).astype(float)
        df['Descuento'] = round(1 - (df['Precio_venta'] / df['Precio_lista']), 2)

        dfs.append(df)

if dfs:
    final_df = pd.concat(dfs, ignore_index=True)

    #Si se quiere cambiar el orden las columnas puede hacerse acá.
    columnas_ordenadas = [
        'Fecha_relevamiento', 'Retailer', 'Link', 'Categoría', 'Producto',
        'Precio_venta', 'Precio_lista', 'Descuento'
    ]
    final_df = final_df[columnas_ordenadas]

    excel_filename = f"fravega_scrap_{fecha_actual}.xlsx"

    final_df.to_excel(excel_filename, sheet_name='Fravega', index=False)

else:
    print("No se encontraron productos en ninguna sección.")

driver.quit()

end_time = time.time()
elapsed_time_seconds = end_time - start_time
elapsed_minutes = int(elapsed_time_seconds // 60)
elapsed_seconds = int(elapsed_time_seconds % 60)

print(f"El tiempo de ejecución del script de Fravega fue de: {elapsed_minutes} minutos y {elapsed_seconds} segundos")
