#indice
lista = ['a','b','c']

mis_tuples = list(enumerate(lista))#creo una lista de tuples
print(mis_tuples[1][0])

for item in enumerate(lista): # imprime el indice 
    print(item)


for item in enumerate(lista): # imprime el valor segundo
    print(item[1])

for indice,item in enumerate(range(50,55)):#imprime indice y valor
    print(indice,item)


lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for nombre in enumerate(lista_nombres):
    print(f'{nombre[1]} se encuentra en el índice {nombre[0]}')#todos los valores
    #del tuples son 1 y los indices 0
#Caracater de cada strin
lista="Python"
lista_indices = list(enumerate(lista))


#Nombre que empiezen con M

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for nombre in enumerate(lista_nombres):
    if nombre[1].startswith('M'):
        print(nombre[0])
   