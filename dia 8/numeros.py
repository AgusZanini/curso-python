def generador_p():
    for x in range(1, 101, 1):
        if x == 100:
            x = 1
        yield f"P - {x:02d}"


def generador_f():
    for x in range(1, 101, 1):
        if x == 100:
            x = 1
        yield f"F - {x:02d}"


def generador_c():
    for x in range(1, 101, 1):
        if x == 100:
            x = 1
        yield f"C - {x:02d}"


p = generador_p()
f = generador_f()
c = generador_c()


def decorador_turnos(area):

    print("Su numero es")
    match area:
        case 1:
            print(next(p))
        case 2:
            print(next(f))
        case 3:
            print(next(c))
        case _:
            print("anda a la mierda")
    print("Aguarde, pronto sera atendido")
