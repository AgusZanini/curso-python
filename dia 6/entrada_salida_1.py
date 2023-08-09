mi_archivo = open("prueba.txt")
print(mi_archivo)

#read leetodo el archivo

una_linea = mi_archivo.readline()
print(una_linea.upper())

una_linea = mi_archivo.readline()

# rstrip quita los saltos de linea
print(una_linea.rstrip())

una_linea = mi_archivo.readline()
print(una_linea)

# readline guarda el punto en el que leyo por ultima vez y el proximo readline
# lo hace a partir de ese punto en el que quedo antes
mi_archivo.close()

mi_archivo = open("prueba.txt")

for l in mi_archivo:
    print("Aqui dice: " + l)

mi_archivo.close()

mi_archivo = open("prueba.txt")

# readlines devuelve una lista donde cada elemento es una linea del archivo
# restringir este metodo a archivos peque;os
todas = mi_archivo.readlines()
print(todas)
mi_archivo.close()

