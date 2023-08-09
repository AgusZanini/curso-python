# sus elementos son unicos, ninguno se repite
# no se pueden indexar ni reorganizar
# sus elementos son inmutables
# no se pueden incluir listas ni diccionarios, etc

mi_set = set([1,2,3,4,5])
print(type(mi_set))
print(mi_set)

otro_set = {1,2,3}
print(type(otro_set))
print(otro_set)

# print(mi_set[0]) no se puede hacer, no se puede indexar
# mi_set[0] = 1 tampoco

otrotuple = {1,2,3,(1,2,3),4,5,6}
print(otrotuple)
print(len(otrotuple))
print(2 in mi_set)

# union de sets

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)

# agregar elementos al set

s1.add(4)
print(s1)
s1.remove(4)
# si queremos remover un elemento que no tiene, nos tira error
print(s1)

# con discard si queremos eliminar algo que no tiene no pasa nada
s1.discard(4)

# pop elimina un elemento random

s1.pop()

# vaciar el set

s1.clear()