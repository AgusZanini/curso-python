from random import randint

intentos = 8
numero = randint(1,100)

nombre = input("Ingrese su nombre: ")

while intentos > 0:
    adivina = int(input(f"{nombre}, adivina el numero entre 1 y 100, te quedan {intentos} intentos"))
    if adivina not in range(1,101):
        print("ingrese un numero valido")
    elif adivina < numero:
        print("muy chico")
        intentos -= 1
    elif adivina > numero:
        print("muy grande")
        intentos -= 1
    else:
        print(f"has ganado, te tomo {9 - intentos} intentos")
        break

if adivina != numero:
    print(f"has perdido, el numero era {numero}")
