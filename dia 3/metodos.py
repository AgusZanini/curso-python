texto = "Este es un texto re piola"
resultado = texto.upper()
print(resultado)
resultado = texto.lower()
print(resultado)
print(texto[2:10].upper())
resultado = texto.split()
print(" ".join(resultado))
print(resultado)
a = "la"
b = "puta"
c = "madre"
d = "que"
e = "me remil pario"
# usamos el caracter con el que queremos
# separar los elementos, en este caso un espacio
f = " ".join([a,b,c,d,e])
print(f)
print(texto.find("a"))
print(texto.replace("re piola", "de mierda"))
