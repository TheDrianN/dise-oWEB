#Conversion inplicita
num1 = 20
num2 = 30.5

#num1 = num1 + num2 #se convierte automaticamente en float

print(type(num1))
print(type(num2))

#Conversion Explicita
num1 = 5.8
num2 = int(num1)
print(num2)
print(type(num2))

##edad= int(input("Dime tu edad"))
##nueva_edad = 1 + edad
#print(nueva_edad)

num1 = "7.5"
num2 = "10"

print(float(num1)+float(num2))