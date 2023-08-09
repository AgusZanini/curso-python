def suma():
    n1 = int(input("numero 1: "))
    n2 = int(input("numero 2: "))
    print(n1 + n2)
    print("gracias por sumar" + n1)

try:
    # codigo a probar
    suma()
except TypeError:
    # codigo a ejecutar en caso de error
    print("no se puede concatenar un int con string de esta forma")
except ValueError:
    print("ese no es un numero")
else:
    # codigo a ejecutar si no hay un error
    print("salio todo bien")
finally:
    # codigo que se va a ejecutar pase lo que pase
    print("hasta luego")


def pedir_numero():

    while True:
        try:
            numero = int(input("dame un numero"))
        except:
            print("ese no es un numero")
        else:
            print(f"ingresaste el numero {numero}")
            break

    print("gracias")


pedir_numero()