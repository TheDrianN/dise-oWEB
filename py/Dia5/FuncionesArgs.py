def suma(*args):
    total = 0
    for arg in args:
        total += arg
    return total

def suma(*args):
    return sum(args)


#abs valor absoluto
def suma_absolutos(*args):
    suma = 0
    for arg in args:
        suma += abs(arg)
    
    return suma