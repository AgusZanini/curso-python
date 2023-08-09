mi_lista = ['a','b','c']
mi_lista1 = ['d','e','f']
print(len(mi_lista))
print(type(mi_lista))
print(mi_lista[0:2])
print(mi_lista + mi_lista1)

mi_lista[0] = "la puta que te pario"
print(mi_lista)
mi_lista.append("hola")
print(mi_lista)
eliminado = mi_lista.pop(0)
print(eliminado)
mi_lista.insert(0,"hola")
print(mi_lista)

lista = ['g','o','b','m','c']
lista.sort()
print(lista)



