serie = "N-02"

if serie == "N-01":
    print("Samsung")
elif serie == "N-02":
    print("Nokia")
elif serie == "N-03":
    print("Motorola")
else:
    print("No existe ese producto")

match serie:
    case "N-01":
        print("samsung")
    case "N-02":
        print("nokia")
    case "N-03":
        print("motorola")
    case _:
        print("no existe ese producto")

cliente = {"nombre":"juansito",
           "edad":"80",
           "ocupacion":"gay"}

pelicula = {"titulo":"titanic",
            "ficha":{"protagonista":"no se",
                     "director":"no se"}}

elementos = [cliente, pelicula, "libro"]



# ejemplo de match

for e in elementos:
    match e:
        case {"nombre":nombre,
              "edad":edad,
              "ocupacion":ocupacion}:
            print("es un cliente")
            print(nombre, edad, ocupacion)
        case {"titulo":titulo,
              "ficha":{"protagonista":protagonista,
                       "director":director}}:
            print("es una pelicula")
            print(titulo, protagonista, director)
        case _:
            print("no se que es esto")

