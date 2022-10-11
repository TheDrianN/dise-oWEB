
texto = "ABCDEFGHIJKLM"
fragmento = texto[2:5]#hasta 5 pero no incluyendo a 5
#fragmento = texto[2:]#del 2 hasta donde se pueda
#fragmento = texto[:5]#del comienzo hasta el 5
fragmento = texto[2:10:3]#cada 3 caracteres se va extrayendo
#framento = texto[::3]#cada 3 caracteres se va extrayendo de todo la cadena
#fragmento = texto[::-1]#Orden reberso
print(fragmento)

