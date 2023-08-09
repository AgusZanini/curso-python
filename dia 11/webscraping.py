import bs4
import requests

resultado = requests.get("https://escueladirecta-blog.blogspot.com")
print(resultado)
sopa = bs4.BeautifulSoup(resultado.text, "lxml")

# dentro del select va la etiqueta (label) que querramos buscar
print(sopa.select("title")[0].getText())
print(sopa.select("title")[0])
print(sopa.select("title"))

print(sopa.select("h1"))

parrafo_especial = sopa.select("p")
print(parrafo_especial)
