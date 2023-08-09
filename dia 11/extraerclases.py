"""
 ": soup.select("div") todos los elementos con la etiqueta div
 #: soup.select("#estilo_4") elementos que contengan id="estilo4"
 .: soup.select(".columna_der") elementos que contengan class="columna_der"
 (espacio): soup.select("div span") cualquier elemento llamado "span" dentro de un elemento "div"
 >: soup.select("div>span") cualquier elemento llamado "span" directamente dentro de un elemento "div, sin nada en el medio
"""

import bs4
import requests

resultado = requests.get("https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html")
sopa = bs4.BeautifulSoup(resultado.text, "lxml")

# buscamos la clase page
columna_lateral = sopa.select(".page")


# buscamos todos los div dentro de la clase page
columna_lateral = sopa.select(".page div")

print(columna_lateral)
for div in columna_lateral:
    print(div.getText())
