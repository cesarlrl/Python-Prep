#1era pregunta
nro2 = 100
if nro2 > 0:
    print('El nro es mayor a 0')
elif nro2 < 0:
    print('El nro es menor a 0')

#2da pregunta
var1 = 3996
var2 = 2
if (type(var1) == type(var2)):
    print('Las variables ', var1, ' y ', var2, ' son del mismo tipo')
else:
    print('Las variables ', var1, ' y ', var2, ' NO son del mismo tipo')

#3ra pregunta
for n in range(1,21):
    if n % 2 == 0:
        print('El número ', n, ' es par.')
    else:
        print('El número ', n, 'es impar.') 

#4ta pregunta
for n in range(0,6):
    print('Valor: ', str(n), ' Elevado a la 3ra potencia es: ', str(n**3))

#5ta pregunta
var3 = 6
for n in range(0,var3):
    print(n)

#6ta pregunta -- I didn't use while :(
factorial = int(input('Porfavor introduzca un nro entero para calcular su factorial: '))
fac = factorial
if factorial < 0:
    print('El factorial de un entero negativo no existe.')
elif factorial == 0:
    print('El factorial de 0 es 1')
else:
    for i in range(1, factorial):
        factorial = factorial*i
        print(factorial)
    print('El factorial de ',fac,' es: ',factorial)

#7ma pregunta
n = 2
while n < 5:
    for n in range(0,10):
        print(n)
        print('Soy henry ', n)
        n += 1

#8va pregunta
for n in range(0,10):
    print(n)
    while n % 3 == 0:
        print('Soy henry es un bootcamp')
        n +=2

#9na pregunta
for nro in range(1, 31):
    es_primo = True
    for i in range(2, nro):
        if (nro % i == 0):
                es_primo = False
    if (es_primo == True):
        print(nro, 'es primo')
    else:
        print(nro, 'no es primo')

#10ma pregunta
for nro in range(1, 31):
    es_primo = True
    for i in range(2, nro):
        if (nro % i == 0):
                es_primo = False
                break
    if (es_primo == True):
        print(nro, 'es primo')
    else:
        print(nro, 'no es primo')

#11va pregunta
ciclos = 0
for nro in range(1, 100):
    es_primo = True
    for i in range(2, int(nro / 2 + 1)):
        ciclos += 1
        if (nro % i == 0):
            es_primo = False
            ciclos += 1
            break
    if (es_primo == True):
        print(nro, 'es primo')
    else:
        print(nro, 'no es primo')
print('Cantidad de ciclos: ',ciclos)

#13ra pregunta - Didn't use while
for n in range(100,301):
    if n % 12 != 0:
        continue
    print(n, ' es divisible por 12')

#14ta pregunta
es_primo = int(input('Introduce un numero entero para evaluar si es primo: '))
if (es_primo == 2) or (es_primo == 3) or (es_primo == 5):
    print(es_primo, ' es un número primo')
elif es_primo > 1:
    for i in range(2,es_primo//2):
        if(es_primo%i)==0:
            print(es_primo, ' no es un número primo')
            break
    else:
        print(es_primo, 'es un número primo')
else:
    print(es_primo, ' no es compuesto ni primo')

#15ta pregunta
n = 100
while n < 300:
    n += 1
    if n % 3 != 0:
        continue
    elif n % 6 == 0:
        print(n, ' es divisible por 3 y múltiplo de 6')
        break
    