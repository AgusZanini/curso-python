from send2trash import send2trash
import os
import shutil


print(os.getcwd())
archivo = open("curso.txt", "w")
archivo.write("texto de prueba")
archivo.close()

# shutil.move("curso.txt", "C:\\Users\\Usuario\\Desktop")

print(os.listdir())
send2trash("curso.txt")

'''
devuelve un generador que itera en
el arbol de carpeta que le pase como ruta
print(os.walk("ruta"))
for carpeta, subcarpeta, archivo in os.walk(ruta):
      print(f"en la carpeta {carpeta}")
      print("las subcarpetas son:")
      for sub in subcarpeta:
          print(f"\t{sub}")
      print("los archivos son:")
      for arch in archivo:
          if arch.startswith("2015"):
              print(f"\t{arch}")
      print("\n")
'''

"""Tanto unlink() como rmdir() pertenecen al módulo os.
 La diferencia radica en que el primero elimina un archivo del directorio
  indicado, y el segundo elimina una carpeta vacía."""