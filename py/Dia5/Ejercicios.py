
# #Crea una 
# función llamada devolver_distintos() que reciba 3 integers como parámetros


def devolver_distintos(num1,num2,num3):
    suma = num1+num2+num3
    lista = [num1,num2,num3]

    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    else:
        lista.sort()#ordena la lista
        return lista[1]
print(devolver_distintos(20,5,7))
#2
def letras_unicas(palabra):
    lista = list(set(palabra))
    lista.sort()
    return lista


print(letras_unicas("entretenido"))

#3
def numero_cero(*args):

    contador = 0
    for num in args:
        if contador + 1 == len(args):
            return False
        elif args[contador] == 0 and args[contador +1] == 0:
            return True
        else:
            contador += 1
    return False

print(numero_cero(1,0,0,2))

def contar_primos(numero):
    primos = [2]
    iteracion = 3
    if numero < 2:
        return 0
    while iteracion <= numero:
        for num in range(3,iteracion,2):
            if iteracion % num == 0:
                iteracion +=2
                break
        else:
            primos.append(iteracion)
            iteracion +=2
    print(primos)
    return len(primos)

