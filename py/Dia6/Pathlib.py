from pathlib import Path ,PureWindowsPath

carpeta = Path("I:/Paginas  WEB/py/Dia6/prueba.txt")
ruta_windows = PureWindowsPath(carpeta)#Transformara a ruta de windows
print(carpeta.read_text())
print(carpeta.name)#regresa el nombre y tipo
print(carpeta.suffix)#el tipo de archivo
print(carpeta.stem)#el nombre de archivo

if not carpeta.exists():
    print("Este archivo no existe")
else:
    print("Genial,existe")