class Padre:
    def hablar(self):
        print("hola")


class Madre:

    def hablar(self):
        print("que tal")

    def reir(self):
        print("jejeje")

# si mi clase heredera, hereda de las dos clases un metodo que tiene el mismo nombre
# esta va a llamar al metodo de la clase que pongamos primero como parametro


class Hijo(Padre, Madre):
    pass


class Nieto(Hijo):
    pass


mi_nieto = Nieto()
mi_nieto.hablar()
mi_nieto.reir()
print(Nieto.__mro__)
