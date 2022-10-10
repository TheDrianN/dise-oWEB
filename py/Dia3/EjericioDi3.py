

texto = input("Ingresar un texto ").lower()

letras = []

letras.append(input("Ingresa primera letra ").lower()) #agrego a letras
letras.append(input("Ingresa Segunda letra ").lower()) #agrego a letras
letras.append(input("Ingresa Tercera letra ").lower()) #agrego a letras
#Mostrar la veces que aparece
print("\n")
print(f"Las veces que aparece la letra: ' {texto.count(letras[0])}', '{texto.count(letras[1])}',' {texto.count(letras[2])}'")
print("\n")
print(f"Las palabras en total es:  {len(texto.split())}")#separamos el texto y despues contamos pro cantidad de palabras spli recorta los espacios
print("\n")
print(f"la primera palabra es:  '{texto[0]}', la ultima es:  '{texto[-1]}'")#obtenemos la primera letra y la ultima letra
print("\n")
palabra = texto.split()
palabra.reverse()
textoIn = ' '.join(palabra)
print(f"Texto Invertido '{textoIn}'")#hacemos un inversion
print("\n")
print("Buscando la Palabra python")
buscar_python = 'python' in texto #buscamos y nos retorna un true o false
dic = {True:"si",False:"no"}#aqui usamos un dic dependiendo el dato de entrada me retorne 
print(f"la palabra 'python' {dic[buscar_python]} se encuentra en el texto")