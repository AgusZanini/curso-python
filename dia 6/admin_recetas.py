from pathlib import Path
import os


def contar_recetas(ruta):
    cont = 0
    for txt in Path(ruta).glob("**/*.txt"):
        cont += 1
    return cont


def contar_dir(ruta):
    cont = 0
    for n in Path(ruta).glob("*"):
        cont += 1
    return cont


def contar_txt(ruta):
    cont = 0
    for n in Path(ruta).glob("*.txt"):
        cont += 1
    return cont


def continuar():
    enter = 0
    while enter != "":
        enter = input("\nPresione enter para continuar: ")
    os.system("cls")


def elegir_opcion():
    opcion = ""
    while not opcion.isnumeric() or int(opcion) not in range(1, 7, 1):
        opcion = input("Elige una opcion:\n"
                       "\t[1] - Leer receta\n"
                       "\t[2] - Crear receta\n"
                       "\t[3] - Crear categoria\n"
                       "\t[4] - Eliminar receta\n"
                       "\t[5] - Eliminar categoria\n"
                       "\t[6] - Finalizar programa\n")
    return int(opcion)


def elegir_categoria(ruta):
    categoria = ""
    cont = 1
    categorias = {}
    print("Elija categoria")
    while not categoria.isnumeric() or int(categoria) not in range(1, contar_dir(ruta) + 1, 1):
        for folder in Path(ruta).glob("*"):
            print(f"[{cont}] - {folder.relative_to(ruta)}")
            categorias[cont] = folder.relative_to(ruta)
            cont += 1
        categoria = input(": ")
        cont = 1
    return Path(ruta, categorias[int(categoria)])


def crear_categoria(ruta):
    existe = True
    print("Categorias existentes: ")
    for categoria in Path(ruta).glob("*"):
        print(categoria.relative_to(ruta))

    cat = input("ingrese nombre de la nueva categoria: ")
    if not Path(ruta, cat).exists():
        Path.mkdir(Path(ruta, cat))
        print("Categoria creada")
    else:
        print("La categoria ya existe")
    continuar()


def eliminar_categoria(ruta):
    Path(ruta).rmdir()
    print(f"Categoria eliminada: {ruta.stem}")
    continuar()


def leer_receta(ruta):
    receta = ""
    cont = 1
    recetas = {}
    print("Elija receta: ")
    while not receta.isnumeric() or receta not in range(1, contar_txt(ruta) + 1, 1):
        for txt in Path(ruta).glob("*.txt"):
            nombre = str(txt.relative_to(ruta)).replace("_", " ").replace(".txt", "")
            print(f"[{cont}] - {nombre}")
            recetas[cont] = txt.relative_to(ruta)
            cont += 1
        if recetas == {}:
            print("No hay recetas cargadas en esta categoria")
            break
        else:
            receta = int(input(": "))
            cont = 1
    if receta != "":
        print(Path(ruta, recetas[receta]).read_text())
    continuar()


def eliminar_receta(ruta):
    receta = ""
    cont = 1
    recetas = {}
    print("Elija receta: ")
    while not receta.isnumeric() or receta not in range(1, contar_txt(ruta) + 1, 1):
        for txt in Path(ruta).glob("*.txt"):
            nombre = str(txt.relative_to(ruta)).replace("_", " ").replace(".txt", "")
            print(f"[{cont}] - {nombre}")
            recetas[cont] = txt.relative_to(ruta)
            cont += 1
        receta = int(input(": "))
        cont = 1
    Path(ruta, recetas[receta]).rmdir()
    print("Receta eliminada")
    continuar()


def crear_receta(ruta):
    receta = input("Ingrese el nombre de la nueva receta, si la receta ya existe, se reemplazara: ").replace(" ",
                                                                                                             "_") + ".txt"
    Path(ruta, receta).write_text(input("Ingrese el contenido de la nueva receta: "))
    print("Receta creada")
    continuar()


print("Bienvenido al administrador de recetas")
path = Path(Path.home(), "huevadaspython", "recetas")

seguir = True
while seguir:
    contar_recetas(path)
    opcion = elegir_opcion()
    match opcion:
        case 1:
            leer_receta(elegir_categoria(path))
        case 2:
            crear_receta((elegir_categoria(path)))
        case 3:
            crear_categoria(path)
        case 4:
            eliminar_receta(elegir_categoria(path))
        case 5:
            eliminar_categoria(elegir_categoria(path))
        case 6:
            seguir = False
        case _:
            print("caso no implementado")
print("Hasta la proxima!")

# a mejorar
# se podria haber usado metodo isnumeric para verificar que las opciones ingresadas sean numericas
# se podia usar metodo iterdir para iterar entre los archivos dentro de cada carpeta
# metodo name me da el nombre de la carpeta en una ruta
# metodo exists de path, para ver si existe la ruta ingresada
