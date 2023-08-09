texto = input("Ingrese un texto: ")
print("Ingrese 3 letras")
letra1 = input("Ingrese la primer letra: ")
letra2 = input("Ingrese la segunda letra: ")
letra3 = input("Ingrese la tercer letra: ")

texto = texto.lower()
letra1, letra2, letra3 = letra1.lower(), letra2.lower(), letra3.lower()
letras = " ".join([letra1, letra2, letra3])

cantletra1 = texto.count(letra1)
cantletra2 = texto.count(letra2)
cantletra3 = texto.count(letra3)

print(f"cantidad de letra1: {cantletra1} \ncantidad de letra2:{cantletra2}\ncantidad de letra3: {cantletra3}")

textolista = texto.split(" ")
print(f"La cantidad de palabras que hay en el texto es de: {len(textolista)}")
print(f"La primera letra del texto es: {texto[0]} \nLa ultima letra del texto es: {texto[-1]}")

textolista = texto.split(" ")
textoinvert = textolista[::-1]
textoinvert = " ".join(textoinvert)
print("el texto con sus palabras invertidas es: " + textoinvert)

dic = {True:"La palabra python se encuentra en el texto", False:"La palabra python no se encuentra en el texto"}
print(dic["python" in texto])