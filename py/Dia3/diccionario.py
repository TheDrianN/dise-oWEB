diccionario = {'c1':'valor1','c2':'valor2'}

print(type(diccionario))#tipo dic
print(diccionario)

resultado  = diccionario['c1']#buscamos el contenido de la clave c1
print(resultado)

cliente = {'nombre':'Adriann','apellido':'Delgado','peso':72,'talla':1.75}
consulta = cliente['apellido']
print(consulta)

dic = {'c1':55,'c2':[10,20,30],'c3':{'s1':100,'s2':100}}#se puede agregar listas y dicionariso
print(dic['c2'][1])#impre lo que haya en ela clave 2 y dentro de ella el indice 1

print(dic['c3']['s2'])#obtengo el valor de la clave 3 que es un dic dentro de ella busca la clave s2

dic2 = {'c1':['a','b','c'],'c2':['d','e','f']}
print(dic2['c2'][1].upper())

#Agregar elementos  aun dicionario
dic3 =  {1:'a',2:'b'}
dic3[3] = 'c' #se agrega en el indice 3 el valor de C

#sobreescribir
dic[2] = 'B' #se sobreescribe el valor

#Conocer todo las claves
print(dic.keys())#las claves
print(dic.values())#obtengo los valores
print(dic.items())#todo lo que tenga 


mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
mi_dic[2] = 36
mi_dic[3] = 'Editora'
mi_dic['pais'] = 'Colombiana'
print(mi_dic)