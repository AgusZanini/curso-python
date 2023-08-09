diccionario = {"clave1":"valor1","clave2":"valor2"}
print(type(diccionario))
print(diccionario)

resultado = diccionario["clave1"]
print(resultado)

#ejemplo con cliente

cliente = {"nombre":"juansito","apellido":"perez","peso":80,"altura":1.80}
consulta = cliente["apellido"]
print(consulta)

#buscar en listas y diccionarios dentro de otros diccionarios

dic = {"c1":55, "c2":[10,20,30],"c3":{"s1":"100","s2":200}}
print(dic["c2"][2])
print(dic["c3"]["s2"])

# buscar indice de una lista que esta dentro de un diccionario y pasarla a mayuscula

dic2 = {"c1":["a","b","c"], "c2":["d","e","f"]}
print(dic2["c2"][1].upper())

# agregar elementos a un diccionario

dic3 = {1:"a",2:"b"}
print(dic3)
dic3[3] = "c"
print(dic3)

# sobreescribir un valor

dic3[2] = "la puta que te pario"
print(dic3)

# conocer todas las claves dentro de un diccionario

print(dic3.keys())

# conocer todos los valores pero sin las claves

print(dic3.values())

# conocer todo lo que hay dentro de un diccionario

print(dic3.items())