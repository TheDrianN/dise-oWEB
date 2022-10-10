mi_lista = ['a','b','c']
otra_lista = ['hola',55,6.1]
resultado = len(mi_lista) #retorna la cantida de elemtnos
resultado  = mi_lista[0]#asigno el elemento 0 a la variables resultado
print(resultado)
#print(type(mi_lista))
#unir listas
mi_lista2 = ['d','e','f']
mi_lista3 = mi_lista + mi_lista2#unir listas
print(mi_lista3)

#Alterar los elemento de una lista
mi_lista3[0] = 'alfa' #sobreescribe en el indice 0 la palabra alfa
mi_lista3.append('g') #el metodo nos permite agregar elementos a la lista
mi_lista3.pop(0) #metodo permiete remover uno de los elementos de la lista, sino hay parametros elimina el ultimo
eliminado = mi_lista3.pop(0)#se agrega el metodo eleminado a una variable que se elimina

#Ordenar las Listasr
lista = ['g','o','b','m','c']
lista.sort()#ordena alfabeticamente al igual que numeros, pero no retorna nada
print(lista)
#inversion
lista.reverse()#pone orden al reves , no retorna nada

print(len(lista))