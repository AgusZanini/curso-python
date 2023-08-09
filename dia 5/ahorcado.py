from random import *
import os

'''
corregir, que con la misma letra me descuente vidas y que me muestre las letras que ya use y no estaban
'''

palabras = ["espejismo", "calefactor", "individualismo", "polivalente", "messi", "valencia", "boliviano", "boliviani", "palabra"]

'''
Funcion que nos va a pedir que ingresemos una letra y la pasa a minuscula
'''


def pedir_letra():
    return input("Ingrese una letra: ").lower()


'''
Funcion que va a verificar que lo que hayamos ingresado sea una letra y solo una letra
'''


def validar_letra(letra):
    if letra in "abcdefghijkmnlopqrstuvwxyzABCDEFGHIJKMNLOPQRSTUVWXYZ" and len(letra) == 1:
        return True
    else:
        return False


'''
Funcion que va a elegir una palabra dentro de una lista de palabras dada
'''


def elegir_palabra(lista):
    return choice(palabras)


'''
Funcion que va a formar una lista de guiones bajos del largo de la palabra dada
por ejemplo: palabra = _______
'''


def ocultar_palabra(lista_palabra):
    palabra_oculta = []
    for n in lista_palabra:
        palabra_oculta.append("_")
    return palabra_oculta


'''
Funcion que va a buscar la letra que le pasemos como parametro dentro de una lista formada por 
cada letra de la palabra del juego
'''


def buscar_letra(letra, lista_palabra):
    cont = 0
    indices = []
    for let in lista_palabra:
        if let == letra:
            indices.append(cont)
            cont += 1
        else:
            cont += 1
    return indices


'''
Funcion que, si encontramos la letra dentro de la palabra, va a reemplazar el guion bajo 
que se encuentra en el indice de la letra correspondiente, por la letra que iria
'''


def reemplazar_letras(lista_indices, palabra_oculta, letra):
    if len(lista_indices) == 0:
        return False
    else:
        for indice in lista_indices:
            palabra_oculta[indice] = letra
        return True


'''
Funcion que, si no encontramos la letra dentro de la palabra, nos descuenta una vida, y sino
no hace nada
'''


def fallo(bool, vidas, letra, lista_fall):
    if not bool:
        vidas -= 1
        lista_fall.append(letra)
    else:
        pass
    return vidas


'''
Funion que compara la cantidad de vidas que nos quedan y si es igual a cero, nos avisa que perdimos
'''


def derrota(vidas, palabra):
    if vidas == 0:
        print(f"Has perdido, la palabra era {palabra}\n")
        return True
    else:
        return False


'''
Funcion que busca guiones bajos dentro de la palabra oculta, y si no encuentra ninguno es porque
ya completamos la palabra y nos avisara que ganamos
'''


def victoria(palabra_oculta):
    if "_" not in palabra_oculta:
        print("Has ganado\n")
        return True
    else:
        return False


'''
Funcion que recibe como parametros los resultado de las funciones de victoria y derrota, si alguno de estos
dos es verdadero, el juego termina
'''


def terminar_juego(victoria, derrota):
    if victoria or derrota:
        print("Fin del juego\n")
        return True
    else:
        return False


'''
Funcion que, una vez terminado el juego, nos pregunta si deseamos seguir jugando, si devuelve verdadero
volvemos a empezar otra partida y si es falso terminamos de jugar
'''


def nuevo_juego():
    seguir = ""
    while seguir != "y" or seguir != "n":
        seguir = input("Desea seguir jugando? y/n\n")
        match seguir:
            case "y":
                return True
            case _:
                return False


'''
ciclo principal, donde esta todo el juego, inicializa la palabra, las vidas y oculta la palabra
'''
jugar = True
while jugar:
    vidas = 6
    letras_fall = []
    palabra = elegir_palabra(palabras)
    lista_palabra = list(palabra)
    # print(palabra)
    palabra_oculta = ocultar_palabra(palabra)
    # print(palabra_oculta)
    finalizar = False
    '''
    Segundo ciclo, donde se nos ira descontando las vidas cada vez que fallemos y se ira 
    llenando la palabra cada vez que acertemos, una vez se nos acaben las vidas o completemos la palabra
    saldremos del ciclo
    '''
    while not finalizar:
        print(palabra_oculta)

        '''verificamos que se ingrse una letra valida'''
        letra = " "
        while not validar_letra(letra):
            letra = pedir_letra()

        '''
        formamos una lista de indices, donde cada elemento de la lista es un indice en el que se encuentra
        la letra en la palabra. Por ejemplo, para la letra a: [1,4], significara que en la posicion uno y cuatro estara
        la letra a: [_,a,_,_,a,_]
        '''
        indices = buscar_letra(letra, lista_palabra)
        # print(indices)

        '''
        reemplazamos la letra dentro de la palabra oculta
        '''
        reemplazo = reemplazar_letras(indices, palabra_oculta, letra)
        # print(reemplazo)

        '''
        descontamos vidas de ser necesario
        '''
        vidas = fallo(reemplazo, vidas, letra, letras_fall)
        print(f"Te quedan {vidas} vidas")
        if letras_fall:
            print(f"Letras erradas: {letras_fall}")

        '''
        verificamos si ganamos o si perdimos
        '''
        derr = derrota(vidas, palabra)
        vict = victoria(palabra_oculta)

        '''
        verificamos si ya termino el juego
        '''
        finalizar = terminar_juego(vict, derr)

        '''
        limpiamos pantalla (no funciona en pycharm)
        '''
        os.system("cls")

    '''
    verificamos si deseamos seguir jugando o no
    '''
    jugar = nuevo_juego()

print("Hasta la proxima broder")
