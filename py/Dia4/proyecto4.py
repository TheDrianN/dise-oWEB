from random import *

num_u = 0
intentos = 0
nombre = input("Hola, Cual es Tu Nombre: ")
print(f"Bienvenido {nombre}, Listo para jugar")
num = randint(1,101)
print("El sistema selecciono un numero aletorio del 1 al 100 tendras que adivinarlo \n tienes 8 itentos")

while intentos < 8:
    num_u = int(input("El numero es:"))
    intentos +=1
    if num_u  not in range(1,101):
        print("tu número no se encuuentra en el rango que va de 1 a 100")

    elif  num_u < num:
        print("El numero del sistema es mas alto")       
    elif num_u > num:
        print("El numero del sistema es mas bajo")
    else:
        print(f"Felicidades {nombre} Ganaste, intentos {intentos}")
        break
    
if num_u != num:
        print(f"Se acabaron tus intentos :c, el numero era {num}")   
#for