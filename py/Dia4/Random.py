from random import * #es todo
#from random import randint #solo un metood

#Metodo randint
aletorio = randint(1,50)
print(aletorio)
#Metodo uniform valor decimal,round = redondear
aletorio = round(uniform(1,5),1)#e tercer 1 es la cantidad de deciamles
#Metodo random
aletorio = random()#un fraccion de un entero
#Metodo choice metodos colecionables
colores = ['azul','rojo','verder','amarillo']
aletorio =  choice(colores)
print(aletorio)
#Metodo shuffle mezclar aletorio, nose puede almancenar  cambia la lista
numeros = list(range(5,50),5)
shuffle(numeros)


