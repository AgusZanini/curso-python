precios_cafe = [("capuchino", 1.5),("expresso", 1.2), ("mocca", 1.9)]

for cafe,precio in precios_cafe:
    print(precio * 0.45)

def mas_caro(lista_precios):
    precio_max = 0
    cafe_max = ""

    for cafe, precio in lista_precios:
        if precio > precio_max:
            precio_max = precio
            cafe_max = cafe
        else:
            pass

    return (cafe, precio_max)

print(mas_caro(precios_cafe))