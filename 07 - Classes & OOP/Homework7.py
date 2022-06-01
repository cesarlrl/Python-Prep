#Pregunta 1
class Vehiculo:
    def __init__(self, color, tipo, cilindrada):
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada

print('______________END Pregunta #1______________')

#Pregunta 2 y 3
class Vehiculo:
    def __init__(self, color, tipo, cilindrada):
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada
        self.velocidad = 0
        self.direccion = 0
    
    def Acelerar(self, vel):
        self.velocidad += vel

    def Frenar(self, vel):
        self.velocidad -= vel
    
    def Doblar(self, grados):
        self.direccion += grados 

a1 = Vehiculo('Azul', 'Carro', 3)
a2 = Vehiculo('Rojo', 'Camioneta', 2)
a3 = Vehiculo('Verde', 'Moto', 88)
a1.Acelerar(40)
a2.Acelerar(60)
a3.Acelerar(30)
a1.Doblar(30)
a3.Doblar(-30)
a2.Frenar(-100)

print('______________END Pregunta #2 y #3______________')


#Pregunta 4
class Vehiculo:
    def __init__(self, color, tipo, cilindrada):
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada
        self.velocidad = 0
        self.direccion = 0
    
    def Acelerar(self, vel):
        self.velocidad += vel

    def Frenar(self, vel):
        self.velocidad -= vel
    
    def Doblar(self, grados):
        self.direccion += grados 

    def Estado(self):
        print('Soy un vehiculo que tiene velocidad:', self.velocidad, 'y dirección', self.direccion)

    def Descripcion(self):
        print('Soy un vehiculo de color:', self.color, ', del tipo:', self.tipo, ' y cilindrada:', self.cilindrada)


a1 = Vehiculo('Azul', 'Carro', 3)
a2 = Vehiculo('Rojo', 'Camioneta', 2)
a3 = Vehiculo('Verde', 'Moto', 88)
a1.Acelerar(40)
a2.Acelerar(60)
a3.Acelerar(30)
a1.Doblar(30)
a3.Doblar(-30)
a2.Frenar(-100)
a1.Estado()
a2.Descripcion()
a3.Estado()

print('______________END Pregunta #4______________')

#Pregunta 5 y 6
class Herramientas:
    def __init__(self) -> None:
        pass

    def ver_primo(self, valor):
        es_primo = True
        for i in range(2, valor):
            if valor % i == 0:
                es_primo = False
                break
        return es_primo

    def valor_modal(self, lista, menor):
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

    def conversion_grados(self, valor, origen, destino):
        if (origen == 'celsius'):
            if (destino == 'celsius'):
                valor_destino = valor
            elif (destino == 'farenheit'):
                valor_destino = (valor * 9 / 5) + 32
            elif (destino == 'kelvin'):
                valor_destino = valor + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif (origen == 'farenheit'):
            if (destino == 'celsius'):
                valor_destino = (valor - 32) * 5 / 9
            elif (destino == 'farenheit'):
                valor_destino = valor
            elif (destino == 'kelvin'):
                valor_destino = ((valor - 32) * 5 / 9) + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif (origen == 'kelvin'):
            if (destino == 'celsius'):
                valor_destino = valor - 273.15
            elif (destino == 'farenheit'):
                valor_destino = ((valor - 273.15) * 9 / 5) + 32
            elif (destino == 'kelvin'):
                valor_destino = valor
            else:
                print('Parámetro de Destino incorrecto')
        else:
            print('Parámetro de Origen incorrecto')
        return valor_destino

    def factorial(self, numero):
        if(type(numero) != int):
            return 'El numero debe ser un entero'
        if(numero < 0):
            return 'El numero debe ser pisitivo'
        if (numero > 1):
            numero = numero * self.factorial(numero - 1)
        return numero

h = Herramientas()

print(h.ver_primo(7))
print(h.ver_primo(10))
print(h.factorial(4))


print('______________END Pregunta #5 y 6______________')