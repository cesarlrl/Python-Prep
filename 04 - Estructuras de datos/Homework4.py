#Pregunta 1
lista = ['Buenos Aires', 'Caracas', 'Río de Janeiro', 'Nueva York', 'Los Angeles', 'Madrid']
print(lista)
lista_orig = lista

#Pregunta 2
print(lista[1])

#Pregunta 3
print(lista[1:4])

#Pregunta 4
print(type(lista))

#Pregunta 5
print(lista[2:])

#Pregunta 6
print(lista[:4])

#Pregunta 7
lista.append('Barcelona')
lista.append('Caracas') #No arroja ningún tipo de error añadir una ciudad que ya forme parte de la lista
print(lista)

#Pregunta 8
lista.insert(3, 'Dubai')
print(lista)

#Pregunta 9
lista2 = ['Tokyo']
lista.extend(lista2)
print(lista)

#Pregunta 10
print(lista.index('Caracas'))
#La particularidad encontrada es que el índice que toma es el del primer elemento

#Pregunta 12
lista.remove('Caracas')
print(lista)

#Pregunta 14
a = lista[-1]
print(a)
del(a)

#Pregunta 15
print(lista * 4)

#Pregunta 16
tupla = tuple(range(1,21))
print(tupla)

#Pregunta 17
print(tupla[10:15])

#Pregunta 18
a = [166, 8, 20, 30, 344]
for i in a:
    if i in tupla:
        print(i, 'está en la tupla')
    else:
        print(i, 'no pertence a la tupla')

#Pregunta 19
elemento = 'París'
valor = elemento in lista_orig
if valor == True:
    print(elemento, 'forma parte de la lista')
else:
    lista_orig.append(elemento)
    print('Añadiendo', elemento, 'a la lista, ya que no es parte de la lista')

#Pregunta 20
print(lista.count('Tokyo'))
print(tupla.count(3))

#Pregunta 21
lista2 = list(tupla)
print(lista2) 

#Pregunta 22
del lista2[3:]
tupla1 = tuple(lista2)
print('Mi nueva tupla es:',tupla1)
var1, var2, var3 = tupla1
print('Var1:',var1,'Var2',var2,'Var3',var3)

#Pregunta 23
mi_diccionario = { 'Ciudad': lista_orig, 'País': ['Argentina', 'Brasil', 'Emiratos Arabes Unidos', 'Estados Unidos', 'España', 'Venezuela', 'Japón', 'Francia'], 'Continente': ['America', 'Europa', 'Asia'] }

#Pregunta 24 y 25
print(mi_diccionario['Ciudad'])
print(mi_diccionario['País'])
print(mi_diccionario['Continente'])