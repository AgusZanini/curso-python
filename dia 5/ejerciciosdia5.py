## ejercicio 1
print("||||||||||| EJERCICIO 1 |||||||||||\n")
print("devolver distintos\n")
def devolver_distintos(num1, num2, num3):
    if num1 == num2 or num1 == num3 or num2 == num3:
        return "Todos los numeros deben ser distintos"

    suma = num1 + num2 + num3
    if suma > 15:
        return max(num1, num2, num3)
    elif suma < 10:
        return min(num1, num2, num3)
    elif suma in range(10, 16):
        if num1 > num2:
            medio = num1
            res = num2
        elif num1 < num2:
            medio = num2
            res = num1
        if medio > num3:
            medio = num3
        if medio < res:
            medio = res
        return medio


print(devolver_distintos(10,5,2))
print("")


print("devolver distintos mejorado\n")
def devolver_distintos_mejorado(num1, num2, num3):
    suma = num1 + num2 + num3
    lista = [num1, num2, num3]

    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    else:
        lista.sort()
        return lista[1]

print(devolver_distintos_mejorado(1,5,7))


## ejercicio 2
print("||||||||||| EJERCICIO 2 |||||||||||\n")

def funcion(palabra):
    lista = list(set(palabra))
    lista.sort()
    return lista

print(funcion("entretenido"))
print("")

print("||||||||||| EJERCICIO 3 |||||||||||\n")

def contar_ceros(*args):
    index = 0
    for arg in args:
        if index == len(args) - 1:
            return False
        elif args[index] == 0 and args[index + 1] == 0:
            return True
        else:
            index += 1
    return False

print(f"{contar_ceros(0,1,2,0,0,3,4)}\n")

print("||||||||||| EJERCICIO 4 |||||||||||\n")

def contar_primos(numero):
    primos = [2]
    iteracion = 3

    if numero < 2:
        return 0

    while iteracion <= numero:
        for n in range(3,iteracion,2):
            if iteracion % n == 0:
                iteracion += 2
                break
        primos.append(iteracion)
        iteracion += 2
    print(primos)
    return len(primos)

print(contar_primos(11))


