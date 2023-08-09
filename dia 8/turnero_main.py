import numeros

seguir = "y"

while seguir == "y":
    while True:
        try:
            area = 0
            while area not in range(1, 4, 1):
                print("Bienvenido, ingrese numero del area para la que desea un turno.\n"
                      "[1] - Cosmetica\n"
                      "[2] - Farmacia\n"
                      "[3] - Perfumeria\n")
                area = int(input(": "))
        except ValueError:
            print("Debe ingresar un numero")
        else:
            break

    numeros.decorador_turnos(area)

    opcion = ""
    while opcion != "y" and opcion != "n":
        opcion = input("Desea retirar otro turno? y/n: ")

    seguir = opcion

print("Hasta pronto")
