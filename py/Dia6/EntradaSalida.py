mi_archivo = open('prueba.txt')#abrir

print(mi_archivo.read())
print(mi_archivo.readline())

una_linea = mi_archivo.readline()#solo una linea
print(una_linea.upper())#se puede ejecutar los metodos a los string

una_linea = mi_archivo.readline()
print(una_linea)

una_linea = mi_archivo.readline()
print(una_linea)
print(una_linea.rstrip())#quita el salto de linea

#puedes iterar dentro de las lineas de los archivos
for l in mi_archivo:
    print("Aqui dice: " + l)
todas = mi_archivo.readlines()# al imprimir me retorna una lista 
#se puede usar los metodos de ista
todas = todas.pop()#elimina la ultima linea y lo retorna
mi_archivo.close()