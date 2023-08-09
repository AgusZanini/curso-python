import os
from pathlib import Path


base = Path.home()
guia = Path(base, "Europa", "Espania", Path("Barcelona", "Sagrada_Familia.txt"))
print(base)
print(guia)


print("-------- imprimir ultimo archivo")
guia2 = guia.with_name("La_Pedrera.txt")
print(guia2)

print("------- imprimir padres")
print(guia.parent)
print(guia.parent.parent)

print("------- imprimir todos los txt en carpeta Europa")
guia = Path(Path.home(), "Europa")
for txt in Path(guia).glob("*.txt"):
    print(txt)

print("------- imprimir todos los txt en Europa y en todas las carpetas dentro de Europa")
for txt in Path(guia).glob("**/*.txt"):
    print(txt)

print("------ relative to")
guia = Path("Europa", "Espania", "Barcelona", "sagrada_familia.txt")
en_europa = guia.relative_to(Path("Europa"))
en_espania = guia.relative_to((Path("Europa", "Espania")))

print(en_europa)
print(en_espania)