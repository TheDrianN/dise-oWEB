def chequear_3_cifras(numero):
    return numero in range(100,1000)

suma = 586 + 302
resultado = chequear_3_cifras(suma)
print(resultado)


#todos los elementso de una lista

def chequear_3_cifras_lista(lista):
    for n in lista:
        if n in range(100,1000):
            return True
        else:
            pass
    return False

resultado = chequear_3_cifras([55,99,6000])

def chequear_3_cifras_lista(lista):
    lista_3_cifras = []
    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
            return lista_3_cifras
        else:
            pass
    return lista_3_cifras 

resultado = chequear_3_cifras([55,99,6000])



##Valor promedio
lista_numeros = [1,2,15,7,2,8]

def reducir_lista(lista):
    lista = list(set(lista))
    lista.sort()
    lista.pop(-1)
    return lista
 
def promedio(lista):
    valor_medio = sum(lista)/len(lista)
    return valor_medio

def reducir_lista(lista_numeros):
    lista_numeros = list(set(lista_numeros))
    lista_numeros.sort()
    lista_numeros.pop(-1)
    return lista_numeros

def promedio(lista):
    valor_medio = sum(lista)/len(lista)
    return valor_medio

#Moneda
import random

lista_numeros = []

def lanzar_moneda():
    resultado = random.choice(["Cara", "Cruz"])
    return resultado
 
def probar_suerte(moneda, lista):
    if moneda == "Cara":
        print("La lista se autodestruirá")
        return []
    elif moneda == "Cruz":
        print("La lista fue salvada")
        return lista