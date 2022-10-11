#def es la palabra para hacer una funcion
def saludar_persona():
    print("hola")

saludar_persona()#llamamos ala funcion

def saludar_persona2(nombre):
    print("hola" + nombre)
    
saludar_persona2("Fernando")#llamamos ala funcion

##Def con return
def multiplicar(num1,num2):
    return num1 * num2

resultado = multiplicar(2,2)

def invertir_palabra(palabra):
    palabra = palabra[::-1].upper()
    return palabra

palabra = invertir_palabra("Python")
print(palabra)