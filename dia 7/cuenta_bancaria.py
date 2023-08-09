class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, nro_cuenta):
        super().__init__(nombre, apellido)
        self.nro_cuenta = nro_cuenta
        self.balance = 0

    def __str__(self):
        return f"Nombre: {self.nombre}\n" \
               f"Apellido: {self.apellido}\n" \
               f"Nro_cuenta: {self.nro_cuenta}\n" \
               f"Balance: {self.balance}\n"

    def depositar(self, monto):
        self.balance += monto

    def retirar(self, monto):
        if monto > self.balance:
            print("Saldo insuficiente")
        else:
            self.balance -= monto


def crear_cliente():
    nombre = input("Ingrese nombre del cliente: ")
    apellido = input("ingrese apellido del cliente: ")
    nro_cuenta = input("Ingrese numero de cuenta del cliente: ")

    return Cliente(nombre, apellido, nro_cuenta)


def inicio():
    cliente = crear_cliente()
    operaciones = ["depositar", "retirar"]

    continuar = "y"

    while continuar == "y":
        print(cliente)

        print("ingrese operacion: ")
        cont = 1
        eleccion = 0

        while eleccion not in range(1,len(operaciones) + 1, 1):
            for operacion in operaciones:
                print(f"[{cont}] - {operacion}")
                cont += 1
            eleccion = int(input(": "))

        monto = float(input("Ingrese monto: "))
        match eleccion:
            case 1:
                cliente.depositar(monto)
            case 2:
                cliente.retirar(monto)
            case _:
                print("Operacion no valida")

        elec = ""

        while elec != "y" and elec != "n":
            elec = input("Desea realizar otra operacion? y/n ")

        continuar = elec
    print("Hasta luego")


inicio()

