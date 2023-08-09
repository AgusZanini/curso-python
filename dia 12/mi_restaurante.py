from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

operador = ""
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]


def click_button(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)


def borrar():
    global operador
    operador = ""
    visor_calculadora.delete(0, END)


def obtener_resultado():
    global operador
    # eval hace el calculo solo parece
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ""


def revisar_check():
    x = 0
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == "0":
                cuadros_comida[x].delete(0, END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set("0")
        x += 1
    x = 0
    for c in cuadros_bebida:
        if variables_bebida[x].get() == 1:
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get() == "0":
                cuadros_bebida[x].delete(0, END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set("0")
        x += 1
    x = 0
    for c in cuadros_postre:
        if variables_postre[x].get() == 1:
            cuadros_postre[x].config(state=NORMAL)
            if cuadros_postre[x].get() == "0":
                cuadros_postre[x].delete(0, END)
            cuadros_postre[x].focus()
        else:
            cuadros_postre[x].config(state=DISABLED)
            texto_postre[x].set("0")
        x += 1


def total():
    sub_total_comida = 0
    p = 0
    for cantidad in texto_comida:
        sub_total_comida += float(cantidad.get()) * precios_comida[p]
        p += 1
    sub_total_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        sub_total_bebida += float(cantidad.get()) * precios_bebida[p]
        p += 1
    sub_total_postre = 0
    p = 0
    for cantidad in texto_postre:
        sub_total_postre += float(cantidad.get()) * precios_postres[p]
        p += 1

    sub_total = sub_total_comida + sub_total_bebida + sub_total_postre
    impuestos = sub_total * 0.07
    tot = sub_total + impuestos

    var_costo_comida.set(f"$ {round(sub_total_comida, 2)}")
    var_costo_bebida.set(f"$ {round(sub_total_bebida, 2)}")
    var_costo_postre.set(f"$ {round(sub_total_postre,2)}")
    var_subtotal.set(f"$ {round(sub_total, 2)}")
    var_impuestos.set(f"$ {round(impuestos, 2)}")
    var_total.set(f"$ {round(tot, 2)}")


def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f"N# - {random.randint(1000, 9999)}"
    fecha = datetime.datetime.now()
    fecha_recibo = f"{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}"
    texto_recibo.insert(END, f"Datos:\t{num_recibo}\t\t{fecha_recibo}\n")
    texto_recibo.insert(END, f"*" * 63 + "\n")
    texto_recibo.insert(END, "Items\t\tCant.\tCosto Items\n")
    texto_recibo.insert(END, f"-" * 75 + "\n")

    x = 0
    for comida in texto_comida:
        if comida.get() != "0":
            texto_recibo.insert(END, f"{lista_comidas[x]}\t\t{comida.get()}\t"
                                     f"$ {int(comida.get()) * precios_comida[x]}\n")
        x += 1

    x = 0
    for bebida in texto_bebida:
        if bebida.get() != "0":
            texto_recibo.insert(END, f"{lista_bebidas[x]}\t\t{bebida.get()}\t"
                                     f"$ {int(bebida.get()) * precios_bebida[x]}\n")
        x += 1

    x = 0
    for postre in texto_postre:
        if postre.get() != "0":
            texto_recibo.insert(END, f"{lista_postres[x]}\t\t{postre.get()}\t"
                                     f"$ {int(postre.get()) * precios_postres[x]}\n")
        x += 1

    texto_recibo.insert(END, f"-" * 75 + "\n")
    texto_recibo.insert(END, f"Costo de la comida: \t\t\t{var_costo_comida.get()}\n")
    texto_recibo.insert(END, f"Costo de la bebida: \t\t\t{var_costo_bebida.get()}\n")
    texto_recibo.insert(END, f"Costo del postre: \t\t\t{var_costo_postre.get()}\n")
    texto_recibo.insert(END, f"-" * 75 + "\n")
    texto_recibo.insert(END, f"Sub-total: \t\t\t{var_subtotal.get()}\n")
    texto_recibo.insert(END, f"Impuestos: \t\t\t{var_impuestos.get()}\n")
    texto_recibo.insert(END, f"Total: \t\t\t{var_total.get()}\n")
    texto_recibo.insert(END, "Lo esperamos pronto!")


def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo("Informacion", "Su recibo ha sido guardado")


def resetear():
    texto_recibo.delete(0.1, END)
    for texto in texto_comida:
        texto.set("0")
    for texto in texto_bebida:
        texto.set("0")
    for texto in texto_postre:
        texto.set("0")

    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postre:
        cuadro.config(state=DISABLED)

    for v in variables_comida:
        v.set(0)
    for v in variables_bebida:
        v.set(0)
    for v in variables_postre:
        v.set(0)

    var_costo_comida.set("")
    var_costo_bebida.set("")
    var_costo_postre.set("")
    var_subtotal.set("")
    var_impuestos.set("")
    var_total.set("")



# iniciar tkinter
aplicacion = Tk()

'''
configuracion de la ventana
'''
# tamanio de la ventana
aplicacion.geometry("1100x630+0+0")

# evitar maximizar
aplicacion.resizable(False, False)

# titulo de la ventana
aplicacion.title("Mi Restaurante - Sistema de Facturacion")

# color de fondo de la ventana
aplicacion.config(bg="burlywood")

'''
nose
'''
# panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

# etiqueta titulo
etiqueta_titulo = Label(panel_superior, text="Sistema de Facturacion", fg="azure4",
                        font=("Dosis", 48), bg="burlywood", width=27)
etiqueta_titulo.grid(row=0, column=0)

# panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# panel costos, dentro del panel izquierdo
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg="azure4", padx=40)
panel_costos.pack(side=BOTTOM)

# panel comidas, dentro del panel izquierdo
panel_comidas = LabelFrame(panel_izquierdo, text="Comidas", font=("Dosis", 19, "bold"),
                           bd=1, relief=FLAT, fg="azure4")
panel_comidas.pack(side=LEFT)

# panel bebidas, dentro del panel izquierdo
panel_bebidas = LabelFrame(panel_izquierdo, text="Bebidas", font=("Dosis", 19, "bold"),
                           bd=1, relief=FLAT, fg="azure4")
panel_bebidas.pack(side=LEFT)

# panel postres, dentro del panel izquierdo
panel_postres = LabelFrame(panel_izquierdo, text="Postres", font=("Dosis", 19, "bold"),
                           bd=1, relief=FLAT, fg="azure4")
panel_postres.pack(side=LEFT)

# panel derecha
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

# panel calculadora, dentro del panel derecho
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg="burlywood")
panel_calculadora.pack()  # no ponemos nada porque por defecto va en la parte de arriba

# panel recibo, dentro del panel derecho
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg="burlywood")
panel_recibo.pack()

# panel botones, dentro del panel derecho
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg="burlywood")
panel_botones.pack()

# lista de productos
lista_comidas = ["pollo", "cordero", "salmon", "merluza", "kebab", "pizza1", "pizza2", "pizza3"]
lista_bebidas = ["agua", "soda", "jugo", "gasosa", "vino1", "vino2", "cerveza1", "cerveza2"]
lista_postres = ["helado", "fruta", "brownies", "flan", "mousse", "pastel1", "pastel2", "pastel3"]


# generar items comida, dentro del panel izquierdo
def crear_item(lista, variables, panel):
    cnt = 0
    for element in lista:
        # crear checkbutton
        variables.append("")
        variables[cnt] = IntVar()
        element = Checkbutton(panel,
                              text=element.title(),
                              font=("Dosis", 19, "bold"),
                              onvalue=1,
                              offvalue=0,
                              variable=variables[cnt],
                              command=revisar_check)
        yield element, cnt
        cnt += 1


def grid_item(item, cnt):
    item.grid(row=cnt,
              column=0,
              sticky=W)


def crear_cuadros_entrada(cuadros, texto, cnt, panel):
    cuadros.append("")
    texto.append("")
    texto[cnt] = StringVar()
    texto[cnt].set("0")
    cuadros[cnt] = Entry(panel,
                         font=("Dosis", 18, "bold"),
                         bd=1,
                         width=6,
                         state=DISABLED,
                         textvariable=texto[cnt])


def grid_cuadro(cuadro, cnt, column):
    cuadro.grid(row=cnt, column=column)


variables_comida = []
cuadros_comida = []
texto_comida: list = []

variables_bebida = []
cuadros_bebida = []
texto_bebida: list = []

variables_postre = []
cuadros_postre = []
texto_postre: list = []


def armar_panel(generador, lista, cuadros, texto, panel):
    for n in lista:
        element, cnt = next(generador)
        grid_item(element, cnt)
        crear_cuadros_entrada(cuadros, texto, cnt, panel)
        grid_cuadro(cuadros[cnt], cnt, 1)


elemento_gen = crear_item(lista_comidas, variables_comida, panel_comidas)
armar_panel(elemento_gen, lista_comidas, cuadros_comida, texto_comida, panel_comidas)

elemento_gen = crear_item(lista_bebidas, variables_bebida, panel_bebidas)
armar_panel(elemento_gen, lista_bebidas, cuadros_bebida, texto_bebida, panel_bebidas)

elemento_gen = crear_item(lista_postres, variables_postre, panel_postres)
armar_panel(elemento_gen, lista_postres, cuadros_postre, texto_postre, panel_postres)
"""
variables_comida = []
cuadros_comida = []
texto_comida: list = []
cont = 0
for comida in lista_comidas:
    # crear checkbutton
    variables_comida.append("")
    variables_comida[cont] = IntVar()
    comida = Checkbutton(panel_comidas,
                         text=comida.title(),
                         font=("Dosis", 19, "bold"),
                         onvalue=1,  # # onvalue: valor que tendra cuando esta activado
                         offvalue=0,  # offvalue: lo contrario
                         variable=variables_comida[cont])
    comida.grid(row=cont,
                column=0,
                sticky=W)

    # crear los cuadros de entrada
    cuadros_comida.append("")
    texto_comida.append("")
    texto_comida[cont] = StringVar()
    texto_comida[cont].set("0")
    cuadros_comida[cont] = Entry(panel_comidas,
                                 font=("Dosis", 18, "bold"),
                                 bd=1,
                                 width=6,
                                 state=DISABLED,
                                 textvariable=texto_comida[cont])

    cuadros_comida[cont].grid(row=cont, column=1)

    cont += 1

# generar items bebida, dentro del panel izquierdo
variables_bebida = []
cuadros_bebida = []
texto_bebida: list = []
cont = 0
for bebida in lista_bebidas:
    variables_bebida.append("")
    variables_bebida[cont] = IntVar()
    bebida = Checkbutton(panel_bebidas, text=bebida.title(), font=("Dosis", 19, "bold"),
                         onvalue=1,  # # onvalue: valor que tendra cuando esta activado
                         offvalue=0,  # offvalue: lo contrario
                         variable=variables_bebida[cont])
    bebida.grid(row=cont, column=0, sticky=W)

    # crear los cuadros de entrada
    cuadros_bebida.append("")
    texto_bebida.append("")
    texto_bebida[cont] = StringVar()
    texto_bebida[cont].set("0")
    cuadros_bebida[cont] = Entry(panel_bebidas,
                                 font=("Dosis", 18, "bold"),
                                 bd=1,
                                 width=6,
                                 state=DISABLED,
                                 textvariable=texto_bebida[cont])

    cuadros_bebida[cont].grid(row=cont, column=1)

    cont += 1

# generar items bebida, dentro del panel izquierdo
variables_postre = []
cuadros_postre = []
texto_postre: list = []
cont = 0
for postre in lista_postres:
    variables_postre.append("")
    variables_postre[cont] = IntVar()
    postre = Checkbutton(panel_postres, text=postre.title(), font=("Dosis", 19, "bold"),
                         onvalue=1,  # # onvalue: valor que tendra cuando esta activado
                         offvalue=0,  # offvalue: lo contrario
                         variable=variables_postre[cont])
    postre.grid(row=cont, column=0, sticky=W)

    # crear los cuadros de entrada
    cuadros_postre.append("")
    texto_postre.append("")
    texto_postre[cont] = StringVar()
    texto_postre[cont].set("0")
    cuadros_postre[cont] = Entry(panel_postres,
                                 font=("Dosis", 18, "bold"),
                                 bd=1,
                                 width=6,
                                 state=DISABLED,
                                 textvariable=texto_postre[cont])

    cuadros_postre[cont].grid(row=cont, column=1)

    cont += 1
"""

# variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuestos = StringVar()
var_total = StringVar()


# funcion para crear etiquetas de costo
def crear_etiq_costo():
    lista_costos = ["Comida", "Bebida", "Postre", "Subtotal", "Impuestos", "Total"]
    for costo in lista_costos:
        etiqueta_costo = Label(panel_costos,
                               text="Costo {}".format(costo),
                               font=("Dosis", 12, "bold"),
                               bg="azure4",
                               fg="white")
        yield etiqueta_costo


# funcion para ubicar etiquetas a lo largo de una columna
def grid_etiqs_column(etiquetas, column):
    cnt = 0
    for etiqueta in etiquetas:
        etiqueta.grid(row=cnt, column=column, padx=20)
        cnt += 1


# funcion para crear entrys de costos
def crear_entry_costos(var):
    texto = Entry(panel_costos,
                  font=("Dosis", 12, "bold"),
                  bd=1,
                  width=10,
                  state="readonly",
                  textvariable=var)
    return texto


botones_creados = []


# funcion que crea botones dada una lista de nombres de botones
def crear_botones(lista_botones):
    cont = 0
    for boton in lista_botones:
        boton = Button(panel_botones,
                       text=boton.title(),
                       font=("Dosis", 14, "bold"),
                       fg="white",
                       bg="azure4",
                       bd=1,
                       width=7)

        global botones_creados
        botones_creados.append(boton)

        boton.grid(row=0, column=cont)
        cont += 1


# generador de etiquetas de costo
etiqueta_costo_gen = crear_etiq_costo()

# etiquetas de costos
etiqueta_costo_comida = next(etiqueta_costo_gen)
etiqueta_costo_bebida = next(etiqueta_costo_gen)
etiqueta_costo_postre = next(etiqueta_costo_gen)
etiqueta_subtotal = next(etiqueta_costo_gen)
etiqueta_impuestos = next(etiqueta_costo_gen)
etiqueta_total = next(etiqueta_costo_gen)

# textos junto a las etiquetas
texto_costo_comida = crear_entry_costos(var_costo_comida)
texto_costo_bebida = crear_entry_costos(var_costo_bebida)
texto_costo_postre = crear_entry_costos(var_costo_postre)
texto_subtotal = crear_entry_costos(var_subtotal)
texto_impuestos = crear_entry_costos(var_impuestos)
texto_total = crear_entry_costos(var_total)

# ubicar etiquetas
lista_etiquetas = [etiqueta_costo_comida, etiqueta_costo_bebida,
                   etiqueta_costo_postre]
lista_etiquetas1 = [etiqueta_subtotal,
                    etiqueta_impuestos, etiqueta_total]

grid_etiqs_column(lista_etiquetas, 0)

# ubicar textos de las etiquetas
lista_textos = [texto_costo_comida, texto_costo_bebida,
                texto_costo_postre]
lista_textos1 = [texto_subtotal,
                 texto_impuestos, texto_total]
# ubicar tres primeros elementos
grid_etiqs_column(lista_textos, 1)
# ubicar los 3 elementos restantes
grid_etiqs_column(lista_etiquetas1, 2)
grid_etiqs_column(lista_textos1, 3)

# botones
botones = ["total", "recibo", "guardar", "resetear"]
crear_botones(botones)
botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)

# area de recibo
texto_recibo = Text(panel_recibo,
                    font=("Dosis", 12, "bold"),
                    bd=1,
                    width=42,
                    height=10)
texto_recibo.grid(row=0,
                  column=0)

# calculadora
visor_calculadora = Entry(panel_calculadora,
                          font=("dosis", 16, "bold"),
                          width=32,
                          bd=1)
visor_calculadora.grid(row=0,
                       column=0,
                       columnspan=4)

lista_botones_calc = ["7", "8", "9", "+", "4", "5", "6", "-",
                      "1", "2", "3", "x", "CE", "Borrar", "0", "/"]

botones_guardados = []


def botones_calculadora(lista_botones):
    fila = 1
    columna = 0
    for boton in lista_botones:
        boton = Button(panel_calculadora,
                       text=boton.title(),
                       font=("Dosis", 16, "bold"),
                       fg="white",
                       bg="azure4",
                       bd=1,
                       width=7)

        botones_guardados.append(boton)

        boton.grid(row=fila,
                   column=columna)
        if columna == 3:
            fila += 1

        columna += 1

        if columna == 4:
            columna = 0


botones_calculadora(lista_botones_calc)

botones_guardados[0].config(command=lambda: click_button("7"))
botones_guardados[1].config(command=lambda: click_button("8"))
botones_guardados[2].config(command=lambda: click_button("9"))
botones_guardados[3].config(command=lambda: click_button("+"))
botones_guardados[4].config(command=lambda: click_button("4"))
botones_guardados[5].config(command=lambda: click_button("5"))
botones_guardados[6].config(command=lambda: click_button("6"))
botones_guardados[7].config(command=lambda: click_button("-"))
botones_guardados[8].config(command=lambda: click_button("1"))
botones_guardados[9].config(command=lambda: click_button("2"))
botones_guardados[10].config(command=lambda: click_button("3"))
botones_guardados[11].config(command=lambda: click_button("x"))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda: click_button("0"))
botones_guardados[15].config(command=lambda: click_button("/"))

# evitar que la pantalla se cierre
aplicacion.mainloop()

"""
# etiquetas de costo y campos de entrada
etiqueta_costo_comida = Label(panel_costos,
                              text="Costo Comida",
                              font=("Dosis", 12, "bold"),
                              bg="azure4",
                              fg="white")
etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costos,
                           font=("Dosis", 12, "bold"),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1)

# etiquetas de costo y campos de entrada
etiqueta_costo_bebida = Label(panel_costos,
                              text="Costo Bebida",
                              font=("Dosis", 12, "bold"),
                              bg="azure4",
                              fg="white")
etiqueta_costo_bebida.grid(row=1, column=0)

texto_costo_bebida = Entry(panel_costos,
                           font=("Dosis", 12, "bold"),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1)

# etiquetas de costo y campos de entrada
costos = ["comida"]

etiqueta_costo_postre = Label(panel_costos,
                              text="Costo Postre",
                              font=("Dosis", 12, "bold"),
                              bg="azure4",
                              fg="white")
etiqueta_costo_postre.grid(row=2, column=0)

texto_costo_postre = Entry(panel_costos,
                           font=("Dosis", 12, "bold"),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_postre)
texto_costo_postre.grid(row=2, column=1)

# etiquetas de costo y campos de entrada
etiqueta_costo_postre = Label(panel_costos,
                              text="Costo Postre",
                              font=("Dosis", 12, "bold"),
                              bg="azure4",
                              fg="white")
etiqueta_costo_postre.grid(row=2, column=0)

texto_costo_postre = Entry(panel_costos,
                           font=("Dosis", 12, "bold"),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_postre)
texto_costo_postre.grid(row=2, column=1)
"""
