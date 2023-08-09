def mi_funcion():
    return 4


def mi_generador():
    yield 45


print(mi_funcion())
print(mi_generador())

g = mi_generador()
print(next(g))


def otra_funcion():
    lista = []
    for x in range(1, 5):
        lista.append(x * 10)
    return lista


def otro_generador():
    for x in range(1, 5):
        yield x * 10


print("----------------")
print(otra_funcion())

g = otro_generador()
print(next(g))
print(next(g))
print(next(g))


def otro_generador_mas():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x


g = otro_generador_mas()
print(next(g))
print(next(g))
print(next(g))

