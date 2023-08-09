class Pajaro:
    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print(f"piopio, mi color es {self.color}")

    def volar(self, metros):
        print(f"*vuela {metros} metros*")


mi_pajaro = Pajaro("rojo", "bandurria")
mi_pajaro.piar()
mi_pajaro.volar(40)
