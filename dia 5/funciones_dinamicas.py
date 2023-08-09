def chequear_3_cifras(numero):
    return numero in range(100,1000)

resultado = chequear_3_cifras(658)
print(resultado)

def chequear(lista):

    lista_3_cifras = []

    for numero in lista:
        if numero in range(100,1000):
            lista_3_cifras.append(numero)
        else:
            pass
    return lista_3_cifras

resultado = chequear([12,45,6,122,6,2,728])
print(resultado)