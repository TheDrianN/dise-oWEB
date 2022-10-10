palabra = 'python'

lista = []

for letra in palabra:
    lista.append(letra)#inserta cada letra de palabra
print(lista)

#Con compresion
list = [letra for letra in palabra] #sea un lista de letra de cada letra en palabra

#Con compresion
list = [letra for letra in 'python'] #sea un lista de letra de cada letra en palabra
#numero
lista = [n for n in range(0,21,2)]
#modificiar
lista = [n/2 for n in range(0,21,2)] #numero dividio por 2 de numero en rango
lista = [n for n in range(0,21,2) if n * 2 >10]#ingresan aquellos numero que multiplicados por 2 sean mayor a 10

lista = [n if n * 2 >10 else 'no' for n in range(0,21,2)] #numero si es multpicado por 2 mayor que 10 se agrega sino se
#agrega no por cada numero en el rango

pies = [10,20,30,40,50]
metros = [ p * 3.281 for p in pies]#por cada pies multiplica y agrega por cada pie de la lista

temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(t-32)**(5/9) for t in temperatura_fahrenheit]
print(grados_celsius)