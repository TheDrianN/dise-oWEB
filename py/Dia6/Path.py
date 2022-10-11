from pathlib import Path
base = Path.home()
guia = Path("Barcelona","Sagrada_Familia")
guia = Path(base,"Europa","España",Path("Barcelona","Sagrada_Familia.txt"))#ruta relativa
guia.parent()#reduce el paren de guia
guia.parent().parent() #reduce
guia2 = guia.with_name("La_Pedrera.txt")
print(base)
print(guia)
print(guia2)


#Enumerar los archivos

guia = Path(Path.home(),"Europa")# ruta absoluta
for txt in Path(guia).glob("*.txt"):#archivo txt
    print(txt)

for txt in Path(guia).glob("**/*.txt"):#archivos y sub carpetas de txt
    print(txt)

guia  = Path("Europa","españa","Barcelona","Sagrada_Familia.txt")

en_europa = guia.relative_to(Path("Europa"))#Europa hacia abajo
en_espania = guia.relative_to(Path("Europa","España"))#españa  hacia abajo
print(en_europa)
print(en_espania)