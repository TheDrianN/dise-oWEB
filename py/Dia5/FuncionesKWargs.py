#def suma(**kwargs):
 #   print(type(kwargs))##retorna un diccionario



def suma(**kwargs):
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")

suma(x=3,y=5,z=2)



def suma(**kwargs):
    total = 0
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    return total

print(suma(x=3,y=5,z=2))

def prueba(num1,num2,*args,**kwargs):
    print(f'el primer valor es {num1}')
    print(f'el primer valor es {num2}')
    for arg in args:
        print(f"arg = {arg}")
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")

prueba(15,50,100,200,300, x='uno',y ='dos' ,z='tres')

args = [100,200,300]
kwargs = {'x':'uno','y':'dos'}

prueba(15,50,*args, **kwargs)

##valores a lista
def lista_atributos(**kwargs):
    lista = []
    for valor in kwargs.values():
        lista.append(valor)
    return lista