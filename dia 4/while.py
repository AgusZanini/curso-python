monedas = 5

while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1
else:
    print("no tengo mas guitarra")

respuesta = "s"


while respuesta == 's':
    respuesta = input("quieres seguir? s/n ")
else:
    print("bai")

# solo pasa sin hacer nada

while respuesta == 's':
    pass

# break interrumpe el codigo y sale

nombre = input("Tu nombre: ")

for letra in nombre:
    if letra == "s":
        break
    print(letra)

# continue rompe la interaccion actual pero vuelve al loop
# principal

for letra in nombre:
    if letra == "s":
        continue
    print(letra)