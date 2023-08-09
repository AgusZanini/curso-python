def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print("hola")
        funcion(palabra)
        print("adios")

    return otra_funcion

def mayuscula(texto):
    print(texto.upper())


def minuscula(texto):
    print(texto.lower())


decorar_saludo(mayuscula("hola como va"))
print("------------")
mayuscula_decorada = decorar_saludo(mayuscula)
mayuscula_decorada("hola como va")
print("------------")
mayuscula("hola como va")
print("------------")


def mostrar_informacion(funcion):
    def interior():
        print(f'Ejecutando la función {funcion.__name__}')
        funcion()
        print('Ejecución finalizada')
    return interior


def impresion():
    print("Hola Mundo")


funcion_decorada = mostrar_informacion(impresion)
funcion_decorada("hola")
