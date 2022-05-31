#Pregunta 1
from tkinter import N


lista = []
i = -15
while i < 0:
    lista.append(i)
    i += 1
print(lista)
print('__________END Pregunta #1__________')

#Pregunta 2
a = len(lista)-1
while a > 0:
    new_list = []
    for item in lista:
        if item % 2 == 0:
            new_list.append(item)
        else:
            continue
    a -= 1
    
for i in new_list:
    print(i)
del(a)
del(new_list)
print('__________END Pregunta #2__________')

#Pregunta 3
for item in lista:
    if item % 2 == 0:
        print(item)
    else:
        continue
print('__________END Pregunta #3__________')

#Pregunta 4
marker = iter(lista)
for i in range(1,4):
    print(next(marker))
print('__________END Pregunta #4__________')

#Pregunta 5
for i, item in enumerate(lista):
    print(i, 'es el índice del elemento', item)

print('__________END Pregunta #5__________')

#Pregunta 6
del(lista)
lista = [1,2,5,7,8,10,13,14,15,17,20]
rango = range(1,21)
for i in rango:
    if i in lista:
        print(i, 'ya está en la lista')
        continue
    else:
        lista.insert(i-1, i)
        print('Se añadió', i, 'en la posición', i-1)
print('La lista completada con los números faltantes es', lista)
del(lista)
print('__________END Pregunta #6__________')

#Pregunta 7 -- Not time efficient but gets the job done.
lista = [0, 1]
for i in range(1,29):
    element = lista[i] + lista[i-1]
    lista.append(element)
print(lista)
print('__________END Pregunta #7__________')

#Pregunta 8
new_list = [0]
for i in range(0,len(lista)):
    a = lista[i]
    b = new_list[0]
    c = a + b
    new_list[0] = c
print(new_list[0])
print('__________END Pregunta #8__________')

#Pregunta 9
a = 8
for i in range(1,6):
    print(lista[a+i+1]/lista[a+i])
print('__________END Pregunta #9__________')

#Pregunta 10
cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'
for i in enumerate(cadena):
    for j in i:
        if j == 'n':
            print('n aparece en la posición', i[0])
    
print('__________END Pregunta #10__________')

#Pregunta 11
diccionario = {
    'Ciudad' : ['Caracas', 'Tokyo', 'Buenos Aires'],
    'Contiente' : ['America', 'Asia', 'America'],
    'Clave3' : [1, 2, 3]
}
for i in diccionario:
    print(i)

print('__________END Pregunta #11__________')

#Pregunta 12
n = list(cadena)
recorre = iter(n)
largo = len(n)
for i in range(0, largo):
    print(next(recorre))

print('__________END Pregunta #12__________')

#Pregunta 13
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
c = zip(lista1, lista2)
print(tuple(c))

#Pregunta 14
lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]
longitud = len(lis)
marcador = iter(lis)
nueva_lista = []
for i in range(0, longitud):
    a = next(marcador)
    if a % 7 == 0:
        nueva_lista.append(a)
    else:
        continue
print(nueva_lista)
del(lis)

print('__________END Pregunta #14__________')

#Pregunta 15
lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
cantidad = 0
for elemento in lis:
    if (type(elemento) == list):
        cantidad += len(elemento)
    else:
        cantidad += 1
print('La cantidad total de elementos es', cantidad)
del(lis)

print('__________END Pregunta #15__________')

#Pregunta 16
lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
for indice, elemento in enumerate(lis):
    if (type(elemento) != list):
        lis[indice]=[elemento]
print(lis)

print('__________END Pregunta #16__________')
