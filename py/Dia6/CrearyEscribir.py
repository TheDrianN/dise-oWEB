#mi_archivo = open('prueba.txt','r')#viene por defecto solo permite leer
#mi_archivo = open('prueba.txt','w')#modo escritura si existe lo vacia y lo vuelve a escribir
#mi_archivo = open('prueba.txt','a')#si existe pone el cursor al final sino lo crea

#archivo = open('prueba.txt','r')
#archivo.write('Soy el nuevo texto')
#archivo.close()


archivo = open('prueba1.txt','w')#si existe lo reemplaza sino la crea
archivo.write('Soy el nuevo texto amigo')
archivo.close()

archivo = open('prueba.txt','w')#si existe lo reemplaza sino la crea
archivo.write('Soy el nuevo texto\n')
archivo.write('Otra fila\n')
archivo.close()

archivo = open('prueba.txt','w')#si existe lo reemplaza sino la crea
archivo.write('''hola mundo
como estas
hola''')
archivo.close()

archivo = open('prueba.txt','w')#este metodo escribe listas
archivo.writelines(['Hola','Mundo','Aqui','Estoy'])
archivo.close()

lista = ['Hola','Mundo','Aqui','Estoy']

for p in lista:
    archivo.write(p +'\n')

mi_archivo = open('prueba3.txt','a')#escribe al final

archivo.write('Bienvenidos')