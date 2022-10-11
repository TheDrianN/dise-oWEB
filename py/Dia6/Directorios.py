import os


#ruta = os.getcwd()## ruta de donde esta tu archivo pyton
#ruta = os.chdir('C:\\Users\\User\\Desktop\\Estadistica')#Buscas la ruta
ruta = os.makedirs('C:\\Users\\User\\Desktop\\Estadistica\\otra')#crear una carpeta nueva
ruta = os.rmdir('C:\\Users\\User\\Desktop\\Estadistica\\otra')#Eliminar una carpeta
ruta = open('C:\\Users\\User\\Desktop\\Estadistica\\otra')
print(ruta.read())
ruta = 'I:\\Paginas  WEB\\py\\Dia6\\prueba.txt'

Elemento = os.path.basename(ruta)#nos retorna el nombre del arhcivo
Elemento = os.path.dirname(ruta)#nombre del directorio
Elemento = os.path.split(ruta)#rut ay despues el nombre del texto
print(Elemento)

archivo = open('otroArchivo.txt')
print(archivo.read())
print(ruta)

#Ahora conpath
from pathlib import Path

carpeta = Path('/Users/User/Desktop/Estadistica')#no importa el sistema operativo
archivo = carpeta / 'otraArchivo.txt'

carpeta = Path('/Users/User/Desktop/Estadistica')  / 'otraArchivo.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())