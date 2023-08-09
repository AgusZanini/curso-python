import time
import timeit


"""inicio = time.time()
prueba_for(100000)
final = time.time()
print(final - inicio)

inicio = time.time()
prueba_while(100000)
final = time.time()
print(final - inicio)"""

declaracion = '''
prueba_for(10)
'''

setup = '''
def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista
'''

duracion = timeit.timeit(declaracion, setup, number=10000000)
print(duracion)

declaracion1 = '''
prueba_while(10)
'''

setup1 = '''
def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
'''

duracion1 = timeit.timeit(declaracion1, setup1, number=10000000)
print(duracion1)
