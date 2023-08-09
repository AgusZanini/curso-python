# abrir como solo lectura
archivo = open('prueba.txt', 'r')
archivo.close()

# abrir con "w" reemplaza el contenido para escribir contenido nuevo
# si no existe el archivo, este se crea
archivo = open("prueba1.txt", "w")
archivo.write("soy el nuevo texto\n")
# si escribimos entre 3 comillas se toman los saltos de linea
archivo.write('''soy
el
nuevo
texto
broder''')
archivo.writelines(["hola", "loco", "que", "te", "pasa"])

lista = ["hola", "loco", "que", "te", "pasa"]
for palabra in lista:
    archivo.writelines(palabra + "\n")

# con "a" escribimos lo que deseemos al final del archivo
archivo = open('prueba.txt')
archivo.close()