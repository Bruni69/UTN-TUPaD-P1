# LUDUEÑA BRUNO
# EJERCICIO 1
print("hola mundo!")

# EJERCICIO 2
nombre = input(str("ingrese su nombre"))
print(f"hola {nombre}!")

# EJERCICIO 3
# ingreso
nombre = str(input("ingrese su nombre"))
apellido = str(input("ingrese su apellido"))
edad = int(input("ingrese su edad"))
domicilio = str(input("ingrese su lugar de residencia"))
# salida
print(f"soy {nombre} {apellido}, tengo {edad} y vivo en: {domicilio}")

# EJERCICIO 4
# se debe ingresar el radio y se debe imprimir el area y perimetro.
# ingreso de datos.
r = float(input("ingrese el radio del ciculo"))
# proceso
pi = 3.14
radio = (pi*r)**2
perimetro = 2*pi*r
# salida
print(f"el area del circulo es: {radio} y el perimetro es: {perimetro}")

# EJERCICIO 5
# Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
# ingreso de datos.
seg = int(input("ingrese una cantidad de segundos y se le dira cuantas horas son "))
# proceso
hora = float(seg/3600)
# salida
print(f"la o las horas con respescto a los segundos que ingreso son:{hora}  horas")

# EJERCICIO 6
# Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
# ingreso de datos.
multiplo = int(input("ingrese el numero del que desea saber la tabla"))
# proceso y salida de datos.
print(f"{multiplo} x 1= {multiplo*1}")
print(f"{multiplo}x 2 = {multiplo*2}")
print(f"{multiplo}x 3 = {multiplo*3}")
print(f"{multiplo}x 4 = {multiplo*3}")
print(f"{multiplo}x 5 = {multiplo*5}")
print(f"{multiplo}x 6 = {multiplo*6}")
print(f"{multiplo}x 7 = {multiplo*7}")
print(f"{multiplo}x 8 = {multiplo*8}")
print(f"{multiplo}x 9 = {multiplo*9}")
print(f"{multiplo}x 10 = {multiplo*10}")

# EJERCICIO 7
# Crear un programa que pida al usuario dos números enteros distintos del 0 
# y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
# ingreso de datos
a = float(input("ingrese el primer numero distinto de 0:"))
b = float(input("ingrese el segundo numero distinto de 0:"))
# proceso
c = a+b
d = a-b
e = a*b
f = a/b
# salida de datos
print("el resultado de sumar ambos numeros es",c)
print("el resultado de restar ambos numeros es",d)
print("el resultado de multiplicar ambos numeros es",e)
print("el resultado de dividir ambos numeros es",f)

# EJERCICIO 8
# Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.
# ingreso de datos.
print("si usted quiere saber su indice de masa corporal, complete los siguientes datos:")
peso = float(input("ingrese su peso en kg:"))
altura = float(input("ingrese su altura en metros con centimetros:"))
# proceso.
IMC = peso/(altura)**2
# salida de datos.
print("su IMC es:",IMC)

# EJERCICIO 9
# Crear un programa que pida al usuario una temperatura en grados Celsius
# e imprima por pantalla su equivalente en grados Fahrenheit.
# ingreso de datos.
temp_c = int(input("ingrese la temperatura en grados celcius para saber en grados Fahrenheit:"))
# proceso.
temp_far = (9/5)*temp_c+32
# salida.
print("la temperatura en grados farenheit es:",temp_far)

# EJERCICIO 10
# Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números
# ingreso
a = float(input("ingrese el primer numero para realizar el promedio"))
b = float(input("ingrese el segundo numero para realizar el promedio"))
c = float(input("ingrese el tercer numero para realizar el promedio"))
# proceso.
promedio = (a+b+c)/3
# salida
print(f"el promedio de los tres numeros que ingreso es"{promedio})