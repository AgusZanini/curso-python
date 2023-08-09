import bs4
import requests

# crear url sin numero de pagina
url_base = "http://books.toscrape.com/catalogue/page-{}.html"

# lista de titulos con 4 o 5 estrellas
libros_buenos = []

# iterar paginas
for pagina in range(1, 51):

    # crear sopa en cada pagina
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, "lxml")

    # seleccionar datos de los libros
    libros = sopa.select(".product_pod")

    # iterar libros
    for libro in libros:

        # chequear que tengan 5 o 4 estrellas
        if len(libro.select(".star-rating.Four")) != 0 or len(libro.select(".star-rating.Five")) != 0:

            # guardar titulo en una variable
            titulo_libro = libro.select("a")[1]["title"]

            # agregar el libro a la lista
            libros_buenos.append(titulo_libro)

for libro in libros_buenos:
    print(libro)
