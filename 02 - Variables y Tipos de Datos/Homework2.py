from cmath import pi

# 1st question
variable = 3
print (variable)

# 2nd question
print(type(8.5))

# 3rd question
print(type(variable))

# 4th question
my_name = 'Cesar Rosendo'

#5th question
complex_number = 5 + 3j

#6th question
print("El tipo de dato de la variable creada en pregunta 5 es " + str(type(complex_number)))

#7h question
print("{0:.4f}".format(pi))

#8th question
var1 = 'True'
var2 = True

#9th question
print("Type of var1 is " + str(type(var1)))
print("Type of var2 is " + str(type(var2)))
#Most efficient answer (after I checked the answers I noticed this)
print('var1 es del tipo ', type(var1),' y var2 es del tipo ', type(var2))

#10th question
var3 = 10
var4 = 10.21
var5 = var3 + var4
print(var5)
print("Type of var5 is " + str(type(var5)))

#11th question
var6 = 7 + 7j
var7 = 1 + 2j
var8 = var6 + var7
print(var8)
print(type(var8))

#12th question
var9 = 11.1
var10 = 2 + 2j
var11 = complex(var9) + var10
print(var11)

#13th question
var12 = var3 * variable
print(var12)

#14th question
print(2**8)

#15th question
var13 = 27 
var14 = 4
print(var13 / var14)

#16th question
var15 = var13 // var14
print(var15)

#17th question
var16 = var13 % var14
print(var16)

#18th question
print(var15 * 4 + var16)

#19th question
var17 = "Cesar,"
var18 = " es mi nombre, y tengo 26 años"
print(var17 + var18)

#20th question
var19 = "2"
var20 = 2
print(var19 == var20)
print("'2' es distinto de 2 porque, '2' es del tipo string y 2 es del tipo integer (i.e. son tipos de datos distintos)" )

#21st question
print(int(var19) == var20)

#22nd question
print("El error de hacer a = float('3,8') está en el uso de la coma en vez del punto al separar los decimales")

#23rd question
var21 = 3
var21 -= 100
print(var21)

#24th question
print(1 << 2)

#25th question
print("No está permitido hacer la operación 2 + '2' porque uno es string y el otro integer")
print("Si los dos operandos fueran del mismo tipo arrojaría una string en un caso y un integer en el otro, así que no, no siempre arrojaría el mismo resultado")

#26th question
a = 2
b = '2'
print(b * a)