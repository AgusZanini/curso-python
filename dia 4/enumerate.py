lista = ["a", "b", "c"]
indice = 0

for item in lista:
    print(indice,item)
    indice += 1

# con enumerate

for item in enumerate(lista):
    print(item)

for indice, item in enumerate(lista):
    print(indice, item)

for indice, item in enumerate(range(50, 55)):
    print(indice, item)

# fuera de un loop

enumerate_lista = list(enumerate(lista))
print(enumerate_lista[1][0])

