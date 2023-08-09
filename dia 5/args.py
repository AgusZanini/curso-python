def suma(a,b):
    return a + b

print(suma(6,5))

# pasar cantidad indefinida de parametros

def sumaargs(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(sumaargs(1,2,3,45,6,32))

def numeros_persona(nombre, *args):
    suma_numeros = sum(args)
    return print(f"{nombre}, la suma de tus números es {suma_numeros}")

numeros_persona("Federico", 75, 20, 65)