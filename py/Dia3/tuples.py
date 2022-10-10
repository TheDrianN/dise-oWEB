mi_tuple = (1,2,3,4)
mi_tuple = list(mi_tuple)#cateamos a tipo lista
t = (1,2,3)

x,y,z = t
print(x,y,z)#al tener el mismo valor de elementos se asigna uno cada uno
print(mi_tuple[0])#imprime en el indice 0

#Metodo count
print(t.count(1))#cuantas veces se repite el 1
#Metodo index
print(t.index(2))#en que indice se encuentra