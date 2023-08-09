class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("*nace*")

    def hablar(self):
        print("*sonido*")


class Pajaro(Animal):

    '''
    una forma de crear atributos de una clase hija
    pasamos los atributos uno por uno de nuevo
        def __init__(self, edad, color, altura_vuelo):
        self.edad = edad
        self.color = color
        self.altura_vuelo = altura_vuelo
    '''

    # otra forma
    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print("*pio*")

    def volar(self, metros):
        print(f"*vuela {metros} metros*")


print(Pajaro.__bases__)
print(Animal.__subclasses__())


piolin = Pajaro(2, "marron", "30")
piolin.nacer()
print(piolin.color)

mi_animal = Animal(3, "caca")

piolin.hablar()
piolin.volar(100)

