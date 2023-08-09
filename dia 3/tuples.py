# los tuples ocupan menos espacio de memoria, y no pueden ser modificadas

mi_tuple = (1,2,(10,20),4)
print(type(mi_tuple))
print(mi_tuple)

# imprimir un indice de la lista que esta dentro del tuple

print(mi_tuple[2][0])

#convertir a lista

mi_tuple = list(mi_tuple)
print(type(mi_tuple))

# asignar el contenido de un tuple a diferentes variables
# la condicion es que tenga la misma cantidad
# de variables que de elemntos en el tuple
t = (1,2,3)
x,y,z = t
print(x,y,z)

# contar cantidad de apariciones de un valor dentro
# del tuple

t2 = (1,2,3,1)
print(t2.count(1))



