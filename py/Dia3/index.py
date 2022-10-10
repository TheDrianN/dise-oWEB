mi_texto = "Esta es una prueba"
#Conocer el indice de un caracter
resultado = mi_texto.index("prueba")
print(resultado)
#buscar desde un indice
resultado = mi_texto.index("a",5,11)#5 inicio y 10 fin
resultado = mi_texto.rindex("a")#buscar de derecha a izquiera
print(resultado)
#Conocer que caracter existe en una posición
#resultado = mi_texto[9]
#resultado = mi_texto[-4]
#print(resultado)#muestra el caracter del numero 9

palabra = "ordenador"
print(palabra.index("n"))

palabra = "ordenador"
print(palabra.index(4))