nombres = ['Juan','Ana','Carlos','Belén','Fran']

for elemento in nombres:
    print("Hola "+elemento)

lista = ['a','b','c','d']

for letra in lista:#letras es igual a objeto cada elemento de la lista
    numero_letra = lista.index(letra)+1 #conseguimos el indice
    print(f"Letra {numero_letra}: {letra}")


lista_1 = ['pablo','laura','fede','luis','julia']

for nombre in lista_1:
    if nombre.startswith('l'):#pregunta si comienza con L
        print(nombre)
    else:
        print('Nombre que no comienza con L')

numeros = [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero
print(mi_valor)

palabra = 'python'

for letra in palabra: #por cada elemento python imprime
    print(letra)

for letra in 'python':
    print(letra)

for numero in [1,2,3,4]:
    print(numero)
for objeto in [[1,2],3,4]:
    print(objeto)

for a,b in [[1,2],[3,4]]: #itero dentro de una lista dentro de otra lista
    print(a)
    print(b)

dic = {'clavea':'a','clave2':'b','clave3':'c'}

for item in dic: #solo claves
    print(item)

for item in dic.items():#se muestra todo el item
    print(item)

for item in dic.values():#se muestra todo los valores
    print(item)

for a,b in dic.items():#se muestra los dos valores
    print(a)
    print(b)