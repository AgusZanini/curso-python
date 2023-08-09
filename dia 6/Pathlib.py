from pathlib import Path, PureWindowsPath

carpeta = Path("C:/Users/Usuario/Desktop/Python/dia 6/prueba.txt")
print(carpeta.read_text())
print(f"el nombre de la carpeta es {carpeta.name}")
print(f"el sufijo de la carpeta es {carpeta.suffix}")
print(f"el nombre sin el sufijo es {carpeta.stem}")

if not carpeta.exists():
    print("este archivo no existe")
else:
    print("el archivo existe")

ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)