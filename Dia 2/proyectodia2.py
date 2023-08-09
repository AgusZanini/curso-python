nombre = input("Ingrese su nombre: ")
ventas = float(input("Ingrese cuanto ha vendido este mes: "))

comision = ventas * 0.13

print(f"OK {nombre}, este mes ganaste {round(comision, 2)}$ en comisiones")

