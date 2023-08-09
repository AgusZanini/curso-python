import time
from pathlib import Path
import os
from datetime import date
import re
import math
import modulo_aux_proy as aux


class Reporte:
    fecha = date.today()

    def __init__(self, pattern, route):
        self.pattern = pattern
        self.route = route

    @staticmethod
    def _calcular_fecha_actual():
        return "/".join(str(date.today()).split("-"))

    @staticmethod
    def mostrar_reporte(dic, cont, duracion, fecha):
        print(f"----------------------------------------------------\n"
              f"Fecha de busqueda: {fecha}\n"
              f"\n"
              f"ARCHIVO\t\t\tNRO. SERIE\n"
              f"-------\t\t\t----------")
        for archivo, contenido in dic.items():
            print(f"{archivo}\t{contenido}")
        print(f"Numeros encontrados: {cont}\n"
              f"Duracion de la busqueda: {duracion}\n"
              f"----------------------------------------------------")

    def generar(self):
        cont = 0
        dic = {}
        inicio = time.time()
        fecha = self._calcular_fecha_actual()
        for carpeta, subcarpeta, archivo in os.walk(self.route):
            for arch in archivo:
                ruta_arch = Path(self.route, carpeta, arch)
                contenido = re.search(self.pattern, ruta_arch.read_text())
                if contenido is not None:
                    cont += 1
                    dic[ruta_arch.name] = contenido.group()
        final = time.time()
        duracion = math.ceil(final - inicio)
        self.mostrar_reporte(dic, cont, duracion, fecha)



"""
def generar_reporte(pattern, route):
    cont = 0
    fecha_hoy = "/".join(str(date.today()).split("-"))
    print(f"----------------------------------------------------\n"
          f"Fecha de busqueda: {fecha_hoy}\n"
          f"\n"
          f"ARCHIVO\t\t\tNRO. SERIE\n"
          f"-------\t\t\t----------")
    inicio = time.time()
    for carpeta, subcarpeta, archivo in os.walk(route):
        for arch in archivo:
            ruta_arch = Path(route, carpeta, arch)
            contenido = re.search(pattern, ruta_arch.read_text())
            if contenido is not None:
                cont += 1
                print(f"{ruta_arch.name}\t{contenido.group()}")
    final = time.time()
    print(f"\nNumeros encontrados: {cont}\n"
          f"Duracion de la busqueda: {math.ceil(final - inicio)}\n"
          f"----------------------------------------------------")
"""

rutaconsignas = Path(Path.home(), "Downloads", "Proyecto+Dia+9.zip")
rutadestino = Path(Path.home(), "Desktop", "Python", "Dia 9", "Consignas")
instrucciones = Path(rutadestino, "Instrucciones.txt")

'''
funcion comentada una vez descomprimido el archivo

aux.descomprimir(rutaconsignas, rutadestino)
'''

directorio_proyecto = Path(Path.home(), "Desktop", "Python", "Dia 9", "Consignas", "Mi_gran_Directorio")
patron = r'N\w{3}-\d{5}'

reporte = Reporte(patron, directorio_proyecto)
reporte.generar()
