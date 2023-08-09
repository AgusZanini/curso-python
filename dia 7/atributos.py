class Pajaro:
    # atributos de clase
    alas = True

    def __init__(self, atributo, especie):
        # atributos de instancia
        self.parametro = atributo
        self.especie = especie

mi_pajaro = Pajaro("rojo", "paloma")

print(mi_pajaro.parametro)