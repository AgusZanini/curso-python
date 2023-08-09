from collections import Counter
from collections import defaultdict
from collections import namedtuple

print("------------------- Counter ---------------------------")
numeros = [8, 6, 9, 5, 4, 5, 5, 5, 8, 7, 4, 5, 4, 4]

print(Counter(numeros))

print(Counter("mississippi"))

frase = "me tiene que contar cuantas veces se se se re re repite una palabra"
print(Counter(frase.split(" ")))

serie = Counter([8, 6, 9, 5, 4, 5, 5, 5, 8, 7, 4, 5, 4, 4])
print(serie.most_common())

print("de los mas comunes, me muestra el numero que esta en la posicion q le paso")
print(serie.most_common(1))

print("lista creada a partir de los elementos de serie, me devuelve una lista con los elementos unicos")
print(list(serie))

print("------------------ defaultdict ------------------------------")

print("asignar el valor deseado a una clave que no exista en un diccionario")
mi_dic = defaultdict(lambda: "nada")
mi_dic["uno"] = "verde"
print((mi_dic["cuatro"]))

print(mi_dic)

print("------------------ namedtuple --------------------")
mi_tupla = (500, 18, 65)

print(mi_tupla[1])

Persona = namedtuple("Persona", ["nombre", "altura", "peso"])
juan = Persona("juan", 1.76, 79)

print(juan.altura)
print(juan.peso)
