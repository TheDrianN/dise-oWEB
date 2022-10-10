mi_set =  set([1,2,3,4,5])#forma 1
mi_set = {1,2,3,4,5}#Forma 2
print(type(mi_set))
print(mi_set)

#unir sets
s1 = {1,2,3}
s2 = {4,5,6}
s3 = s1.union(s2)

#Metodo add
s1.add(4)
print(s1)
#Eliminar 
s1.remove(3)
print(s1)
#Descartar
s1.discard(6)#metodo que no existe no lo  descarta
#pop
s1.pop()#elimina uno de los elementos aleatorio
#limpiar
s1.clear()#limpia todos
