import zipfile
import shutil

"""
comento para que no se genere el archivo cada vez que pruebo esto

se crea el archivo zip vacio
mi_zip = zipfile.ZipFile("archivo_comprimido.zip", "w")

mi_zip.write("mi_texto_A.txt")
mi_zip.write("mi_texto_B.txt")

mi_zip.close()
"""

"""
# abrir el archivo zip creado
zip_abierto = zipfile.ZipFile("archivo_comprimido.zip", "r")
# extraer el archivo
zip_abierto.extractall()
"""

"""
print("otra forma con shutil")
carpeta_origen = "C:\\Users\\Usuario\\Desktop\\Python\\dia 9\\carpeta1"
archivo_destino = "todo_comprimido"

shutil.make_archive(archivo_destino, "zip", carpeta_origen)
"""

"""
print("descomprimir con shutil")

# en la carpeta se puede poner la ruta completa donde deseemos, si ponemos
# solo el nombre de la carpeta va a asumir que es en la carpeta donde
# estamos parados

shutil.unpack_archive("todo_comprimido.zip", "carpeta_tu_mama")
"""
