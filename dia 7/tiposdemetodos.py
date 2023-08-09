class Pajaro:
    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print(f"piopio, mi color es {self.color}")

    def volar(self, metros):
        print(f"*vuela {metros} metros*")
        self.piar()

    def pintar_negro(self):
        self.color = "negro"
        print(f"ahora el pajaro es {self.color}")

    # metodos de clase
    @classmethod
    def poner_huevos(cls, cantidad):
        # no puedo llamar a self, no se puede acceder a los valores de la instancia
        print(f"*pone {cantidad} huevos*")
        # puedo acceder a los metodos de la clase
        cls.alas = False
        print(Pajaro.alas)

    # metodos estaticos
    @staticmethod
    def mirar():
        # no puedo llamar a self, por lo que no puedo modificar valores de instancia
        # no puedo llamar a cls, por lo que no puedo acceder a atributos de clase
        # sirve para tener metodos que no quiero que modifiquen ni atributos de clase ni de isntancia
        print("*mira*")

# los metodos de clase los puedo invocar sin necesidad de crear una instancia
# si llamara de la misma manera a un metodo de instancia me tiraria error

Pajaro.poner_huevos(3)
Pajaro.mirar()

piolin = Pajaro("amarillo", "canario")
piolin.pintar_negro()
piolin.volar(50)

piolin.alas = False
print(piolin.alas)