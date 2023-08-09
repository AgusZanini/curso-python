texto = 'ABCDEFGHIJKLM'
# primer termino: desde donde
# segundo termino: hasta donde(no inclusive)
# tercer termino: cada cuantos caracteres
fragmento = texto[2:10:2]
print(fragmento)
fragmento = texto[::-1]
print(fragmento)
print(texto[9::2])