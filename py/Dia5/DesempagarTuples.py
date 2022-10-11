from random import *


precios_cafe = [('capuchino',1.5),('Expresso',1.2),('Moka',1.9)]

for elemento in precios_cafe:
    print(elemento[0])

#recorre un tuples
def cafe_mas_caro(lista_precio):
    precio_mayor = 0
    cafe_mas_caro = ''
    for cafe,precio in lista_precio:
        if precio > precio_mayor:
            precio_mayor= precio
            cafe_mas_caro = cafe
        else:
            pass
    return (cafe_mas_caro,precio_mayor)

cafe,precio = cafe_mas_caro(precios_cafe)
print(f'El cafe mas caro es{cafe} cuyo precio es {precio}')
print(cafe_mas_caro(precios_cafe))#mostrar

# Interacciones entre funciones
# lista inicial
palitos = ['-','--','---','----']

# Funcion de mezclar palitos
def mezclar_palitos(lista):
    shuffle(palitos)
    return lista

# funcion perdirle intento
def probar_suerte():
    intento = ''
    while intento not in ['1','2','3','4']:
        intento = input("Elige un numero del 1 al 4: ")
    return int(intento)

# Comprobar intento
def chequear_intento(lista,intento):
    if lista[intento -1] == '-':
        print("A lavar los platos")
    else:
        print("Esta vez te has salvado")
    print(f"Te ha tocado '{lista[intento-1]}'")

palitos_mezclados = mezclar_palitos(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados,seleccion)