from pathlib import Path
import os
import shutil


def descomprimir(origen, destino):
    shutil.unpack_archive(origen, destino)
