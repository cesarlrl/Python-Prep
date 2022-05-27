#Intento de programar un diagrama de flujo de la clase 3
nro = int(input('Ingresa un nro: '))
nro1 = nro
div = int(input('Ingresa el divisor a evaluar: '))

def funcion1(valor):
    return valor > 0

while (funcion1(nro) == True):
    nro = nro - div
if nro == 0:
    print('El nro ' + str(nro1) + ' SI es divisible por ' + str(div))
else:
    print('El nro ' + str(nro1) + ' NO es divisible por ' + str(div)) 