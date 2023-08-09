import re

"""
caracteres especiales para contruir expresiones regulares:
    \d digito numerico
    \w caracter alfanumerico (letra, digito numerico o simbolo)
    \s espacio en blanco
    \D NO es un digito numerico
    \W NO es alfanumerico (solo signos, como ?!=)
    \s NO esapcio en blanco

cuantificadores
    + 1 o mas veces
    {n} se repite n veces
    {n,m} se repite entre n a m veces
    {n,} se repite desde n hacia arriba
    * 0 o mas veces
    ? 1 o 0 veces
"""


texto = "si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online"

palabra = "ayuda" in texto
print(palabra)

patron = "ayuda"

busqueda = re.search(patron, texto)
print(busqueda)
print("solo ubicacion del patron")
print(busqueda.span())
print("solo ubicacion del comienzo del patron")
print(busqueda.start())

print("encontrar todas las repeticiones de la palabra que queremos buscar")
busqueda = re.findall(patron, texto)
print(busqueda)

print("encotrar el lugar de todas las repeticiones del patron que buscamos")
for hallazgo in re.finditer(patron, texto):
    print(hallazgo.span())

texto = "llama al 544-525-6588 ya mismo"

patron = r'\d{3}-\d{3}-\d{4}'

resultado = re.search(patron, texto)
print(resultado)

print("hacer que nos devuelva solo el patron que buscamos")
print(resultado.group())

print("iterar")
for hallazgo in re.finditer(patron, texto):
    print(hallazgo.span())

print("agrupar patron dado con ()")
patron = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
resultado = re.search(patron, texto)

# el indexado empieza con 1 y no con 0
print(resultado.group(2))


clave = input("Clave: ")
patron = r'\D{1}\w{7}'

chequear = re.search(patron, clave)

print(chequear)

texto = "no atendemos los lunes por la tarde"
buscar = re.search(r'lunes|martes', texto)
print(buscar)

print("comodines")
buscar = re.search(r'....demos....', texto)
print(buscar)

print("buscamos si hay tal patron al principio del texto con ^")
buscar = re.search(f'^\D', texto)
print(buscar)

print("buscamos si hay tal patron al final del texto con $")
buscar = re.search(f'\D$', texto)
print(buscar)

print("encontrar todos los que excluyan algo dentro de []")
buscar = re.findall(f'[^\s]+', texto)
print(''.join(buscar))


print("--------------\n"
      "--------------\n"
      "--------------\n")


def verificar_email(email):
    patron = r'\w+@\w+.com'

    if re.search(patron, email) is not None:
        print("Ok")
    else:
        print("La dirección de email es incorrecta")


email1 = "zaniniagustin06@gmail.com"
email2 = "tumamalocotumama"

patron = r'\w+@\w+\.com'
# verificar_email(email1)
# ejemplo: patron = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
# patron = re.compile(r'(\w+@\w+)(\.com)')
# patron = r'\w+@\w+.com[.ar]?'

print(re.search(patron, email1))
