texto = "Este es el texto Federico"
#Upper para mayusculas
resultado = texto.upper()
resultado = texto[2].upper()#si solo queremos un indice pero en mayusculas
print(resultado)
#lower para minisculas
resultado = texto.lower()
print(resultado)
#split separa 
resultado = texto.split()#me lo separa y me lo guarda en una lista, toma como separador al espacio
resultado = texto.split("t")#esta compuestas tomando a t como separador
print(resultado)
#join une las string
a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d])#estoy creando una lista con cuatro elemento y lo unimos con join y seprados por el espacio
print(e)
#find encontrar un sub String
resultado = texto.find("s")#Buscar un determinado caraceter del texto
resultado = texto.find("g")#si buscamos un valor que no existe nos retorna -1
print(resultado)
#replace remplazar
resultado = texto.replace("Federico","Adriann")#rempalzar primer parametro dice cual quieres remplazar y el segundo por quein
#vas a remplazar

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
resultado = frase.replace("difícil","fácil").replace("mala","buena")#remplazar mas cantidad

print(resultado)