#rango cumple la funcion de i java
for numero in range(5):
    print(numero)
for numero in range(1,5):#1 al 5
    print(numero)
for numero in range(1,5,2):#1 al 5 y cada dos pasos
    print(numero)

lista = list(range(1,101))#me retorna una lista con datos del 1 al 100

#suma de cuadrados
suma_cuadrados = 0

for i in range(1,16):
    suma_cuadrados += i**2