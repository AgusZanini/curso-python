texto = "hola como andas"

#en mayuscula

print(texto.upper())

#en minuscula

print(texto.lower())

#separar y hacer una lista, tomando el espacio como separador

listatexto = texto.split(" ")
print(listatexto)

#unir variables en un string

a = "que"
b = "te"
c = "te"

abc = " ".join([a,b,c])
print(abc)

lista_palabras = ["La","legibilidad","cuenta."]
lista_palabras_string = " ".join(lista_palabras)
print(lista_palabras_string)

#buscar caracter o string dentro de otro string

print(abc.find("te"))

#reemplazar un texto por otro dentro de un string

print(abc.replace("calienta", "importa"))





