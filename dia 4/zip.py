nombres = ["Ana", "Hugo", "Valeria"]
edades = [65,29,42]
ciudades = ["Lima", "Madrid", "Mexico"]

combinados = zip(nombres, edades, ciudades)
print(combinados)
print(*combinados)

combinados = list(zip(nombres, edades, ciudades))
print(combinados)

for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} y vive en {ciudad}")
