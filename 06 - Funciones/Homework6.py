#Pregunta 1
def es_primo(nro):
    ver = type(nro)
    if (ver != int) or (nro < 0):
        return 'El tipo de dato introducido no es un entero positivo!'
    else:
        primo = True
        for i in range(2, nro):
            if (nro % i == 0):
                primo = False
                return False
        if (primo == True):
            return True
        else:
            return False

print('__________END Pregunta #1__________')

#Pregunta 2
def lista_o_no(lista):
    if type(lista) != list:
        return False
    else:
        return True

def lista_vacia(lista):
    if lista_o_no(lista) == False:
        return 'Esta función solo acepta listas en su argumento'
    else:
        if len(lista) == 0:
            return True
        else:
            return False

def primos_en_lista(lista):
    if (lista_o_no(lista) == False) or (lista_vacia(lista) == True):
        return 'Esta función solo acepta listas no vacías en su argumento'
    else:
        nueva_lista = []
        contador = 0
        for i in lista:
            if es_primo(i) == True:
                nueva_lista.append(i)
                contador += 1
            else:
                continue
        if contador == 0:
            return 'No se encontraron primos en la lista dada'
        else:
             return nueva_lista       

lista1 = []
lista2 = ['a', 'b', 'c']
lista3 = [1, 89, 87, 'a', [1, 3, 7], (1, 2, 3), 'Caracas', 73.0, 11, 29]
lista4 = 'String'
lista5 = ('tupla', 'tupla', 'tupla', 5, 3, 7, 9)
lista6 = [1, 2, 3, 3, 33, 4, 5, 6]
lista7 = [99, 3.0, 'Caracas', (1, 3, 99.9), ['a', 'b', 'c'], 3+2j, 1, 2, 99, 3, 3]

a = primos_en_lista(lista1)
print(a)
b = primos_en_lista(lista2)
print(b)
c = primos_en_lista(lista3)
print(c)
d = primos_en_lista(lista4)
print(d)
e = primos_en_lista(lista5)
print(e)

del a, b, c, d, e

print('__________END Pregunta #2__________')

#Pregunta 3
'''Función para verificar si una lista dada posee algún número entero'''
def lista_numerica(lista):
    if (lista_o_no(lista) == False) or (lista_vacia(lista)):
        return 'El argumento de la función no es una lista o es una lista vacía'
    else:
        for i in lista:
            a = type(i)
            if a != int:
                return False
            else:
                return True

def tipo_dato(a):
    return type(a)

'''Exercise from solutions - Didn't solved it myself but after studying it I understood it.
Also it doesn't account for lists with stuff other than integers.'''
def nro_mas_repetido(lista):
    lista_unicos = []
    lista_repeticiones = []
    if len(lista) == 0:
        return None
    for elemento in lista:
        if elemento in lista_unicos:
            i = lista_unicos.index(elemento)
            lista_repeticiones[i] += 1
        else:
            lista_unicos.append(elemento)
            lista_repeticiones.append(1)
    moda = lista_unicos[0]
    maximo = lista_repeticiones[0]
    for i, elemento in enumerate(lista_unicos):
        if lista_repeticiones[i] > maximo:
            moda = lista_unicos[i]
            maximo = lista_repeticiones[i]
    return moda, maximo
            

a = nro_mas_repetido(lista1)
print(a)
b = nro_mas_repetido(lista2)
print(b)
c = nro_mas_repetido(lista3)
print(c)
d = nro_mas_repetido(lista4)
print(d)
e = nro_mas_repetido(lista5)
print(e)
f = nro_mas_repetido(lista6)
print(f)
g = nro_mas_repetido(lista7)
print(g)

print('__________END Pregunta #3__________')

#Pregunta 4
def valor_modal(lista, menor):
    '''
    Not solved by me either -
    Esta función devuelve el valor modal y recibe de parámetros dos valores:
    1-Una lista de números
    2-Verdadero (por defecto) por si se requiere el mínimo de los más repetidos, o Falso si se requiere el máximo
    '''
    lista_unicos = []
    lista_repeticiones = []
    if len(lista) == 0:
        return None
    if (menor):
        lista.sort()
    else:
        lista.sort(reverse=True)
    for elemento in lista:
        if elemento in lista_unicos:
            i = lista_unicos.index(elemento)
            lista_repeticiones[i] += 1
        else:
            lista_unicos.append(elemento)
            lista_repeticiones.append(1)
    moda = lista_unicos[0]
    maximo = lista_repeticiones[0]
    for i, elemento in enumerate(lista_unicos):
        if lista_repeticiones[i] > maximo:
            moda = lista_unicos[i]
            maximo = lista_repeticiones[i]
    return moda, maximo

print('__________END Pregunta #4__________')

#Pregunta 5
def grados(valor, medida_origen, medida_destino):
    '''La función grados recibe 3 parámetros, el primero el valor a convertir, seguido de dos parámetros
    medida_origen y medida_destino que pueden ser 'k','c' o 'f' que representan los grados entre
    los cuales se va a convertir el valor dado, Kelvin, Celsius y Farenheit respectivamente'''
    if not(isinstance(valor, int)):
        return 'El valor indicado no es un entero'
    elif (medida_origen == medida_destino):
        return valor
    else:
        if (medida_origen == 'c'):
            if (medida_destino == 'k'):
                destino = valor + 273.15
                return destino
            elif (medida_destino == 'f'):
                destino = ( valor * 9/5 ) + 32
                return destino
        if (medida_origen == 'k'):
            if (medida_destino == 'c'):
                destino = valor - 273.15
                return destino
            elif (medida_destino == 'f'):
                destino = ( ( (valor - 32) * 5 ) / 9 ) + 273.15
                return destino
        if (medida_origen == 'f'):
            if (medida_destino == 'k'):
                destino = ( (valor - 32) * (5/9) ) + 273.15
                return destino
            elif (medida_destino == 'c'):
                destino = (valor - 32) * (5/9)
                return destino

a = grados(1001, 'f', 'c')
print(a)

print('1 grado Celsius a Celsius:', grados(1, 'c', 'c'))
print('1 grado Celsius a Kelvin:', grados(1, 'c', 'k'))
print('1 grado Celsius a Farenheit:', grados(1, 'c', 'f'))
print('1 grado Kelvin a Celsius:', grados(1, 'k', 'c'))
print('1 grado Kelvin a Kelvin:', grados(1, 'k', 'k'))
print('1 grado Kelvin a Farenheit:', grados(1, 'k', 'f'))
print('1 grado Farenheit a Celsius:', grados(1, 'f', 'c'))
print('1 grado Farenheit a Kelvin:', grados(1, 'f', 'k'))
print('1 grado Farenheit a Farenheit:', grados(1, 'f', 'f'))

print('__________END Pregunta #5__________')

#Pregunta 6
metricas = ['c','k','f']
for i in range(0,3):
    for j in range(0,3):
        print('1 grado', metricas[i], 'a', metricas[j],':', grados(1, metricas[i], metricas[j]))

print('__________END Pregunta #6__________')

#Pregunta 7
def factorial(numero):
    '''
    Devuelve el factorial de un numero dado
    '''
    x = isinstance(numero, int)
    if x:
        if (numero == 1) or (numero == 0):
            return 1
        elif (numero < 0):
            return 'El parámetro introducido no es un número entero positivo'
        elif (numero > 1):
            numero = numero * factorial(numero -1)
            return numero
    else:
        return 'El parámetro introducido no es un número entero positivo'

x = factorial(0)
y = factorial(1)
z = factorial('2')
f = factorial(4)
g = factorial(-3)
print(x)
print(y)
print(z)
print(f)
print(g)

print('__________END Pregunta #7__________')