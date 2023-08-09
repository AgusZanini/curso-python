lista = ["a", "b", "c"]

for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f"letra nro {numero_letra}: {letra}")

lista = ["pablo", "laura", "fede", "luis", "julia"]

for nombre in lista:
    if nombre.startswith("l"):
        print(f"{nombre} empieza con L")
    else:
        print(f"{nombre} no empieza con L")

numeros = [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor += numero
    print(mi_valor)

palabra = "python esta re piche"

for letra in palabra:
    print(letra)

for objeto in [[1,2],[3,4],[5,6]]:
    print(objeto)

for a,b in [[1, 2], [3, 4], [5, 6]]:
    print(a)
    print(b)


dic = {"clave1":"a","clave2":"b","clave3":"c"}

for item in dic:
    print(item)

for item in dic.items():
    print(item)

for item in dic.values():
    print(item)

for item in dic.keys():
    print(item)