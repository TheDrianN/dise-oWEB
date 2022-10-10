nombre = input("Cual es tu nombre: ")
ventas = int(input("Cuanto Vendiste este mes: "))
comision = round(ventas * 13 / 100,2)
print(f"Hola {nombre}, Tu ganacia este mes es: ${comision}")