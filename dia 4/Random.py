from random import *

# elige un valor entero en el rango dado

aleatorio = randint(1, 50)
print(aleatorio)


# elige un valor aleatorio decimal contenido en el rango dado
aleatorio = round(uniform(1, 5),2)
print(aleatorio)


# elegir aleatoriamente un elemento de una lista
colores = ["azul", "rojo", "verde", "amarillo"]
aleatorio = choice(colores)
print(aleatorio)

numeros = list(range(5, 50, 5))

# mezclar los elementos de una lista
shuffle(numeros)

print(numeros)