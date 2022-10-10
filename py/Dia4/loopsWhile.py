monedas = 5

while monedas > 0:
    print(f"tengo {monedas} monedas")
    monedas -= 1
else:
    print("Te quedas sin modenas")

respuesta ='S'

while respuesta == 'S':
    respuesta  = input("Quieres Seguir? (S/N) ")
else:
    print("Gracias")

#PASS pasar no hacer nada, reserva 

while respuesta == 'S':
    pass
print("hola")

#BREAK interumpir y salir
nombre = input("Tu nombre: ")
for letra in nombre:
    if letra =='r': #Deje de ejecutra si se cumple
        break
    print(letra)

#continue continuar
nombre = input("Tu nombre: ")
for letra in nombre:
    if letra =='r': #Deje de ejecutra si se cumple
        continue
    print(letra)

