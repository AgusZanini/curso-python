import os
from Pathlib import Path
ruta = os.getcwd()
print(ruta)

ruta = os.chdir("C:\\Users\\Usuario\\Desktop\\alternativo")

archivo = open("otro_archivo.txt")
print(archivo.read())

ruta = os.makedirs("C:\\Users\\Usuario\\Desktop\\alternativo\\otra")
ruta = "C:\\Users\\Usuario\\Desktop\\Python\\dia 6\\prueba.txt"

elemento = os.path.basename(ruta)
print(elemento)

elemento = os.path.dirname(ruta)
print(elemento)

elemento = os.path.split(ruta)
print(elemento)

os.rmdir("C:\\Users\\Usuario\\Desktop\\alternativo\\otra")

otro_archivo = open("C:\\Users\\Usuario\\Desktop\\alternativo\\otro_archivo.txt")
print(otro_archivo.read())
otro_archivo.close()

carpeta = Path("C:/Users/Usuario/Desktop/alternativo")
archivo = carpeta / "otro_archivo.txt"

mi_arhivo = open(archivo)
print(mi_arhivo.read())