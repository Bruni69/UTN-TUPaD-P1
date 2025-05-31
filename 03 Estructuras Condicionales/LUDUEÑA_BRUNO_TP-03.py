# EJERCICIO 1.
# Un programa que debe decidir si una persona es mayor de edad
# Ingreso.
edad = int(input("Hola!!! Por favor, ingrese su edad "))
# Proceso y salida.
if edad >= 18:
    print("Usted es mayor de edad.")
else:
    print("Lo siento, usted no es mayor de edad.") 
    
# EJERCICIO 2.
# Un programa que diga aprobado si la nota  es mayor o igual a 6, si no dira desaprobado.
#Ingreso.
nota = float(input("Ingrese su nota "))
# Proceso y salida.
if nota >= 6:
    print("Usted aprobo!!!")       
else:
    print("Usted desasprobo, lo lamento")  
    
#EJERCICIO 3.
# El programa solo reconoce numeros pares, si se ingresa otro numero se imprime que ingrese un numero par
num = int(input("Por favor, ingrese un numero par "))
if num % 2 == 0:
    print("Ha ingresado un numero par!!!")
else:
    print("Por favor ingrese un numero par")      
    
#EJERCICIO 4.
# De acuerdo a la edad del usuario se le dira a que franja etarea pertenece
edad = int(input("Por favor ingrese su edad "))
if edad < 12:
    print("Usted es un niño/a")
elif edad < 18:
    print("Usted es un adolescente")
elif edad < 30:
    print("Usted es un adulto/a joven")
else:
    print("Usted es un adulto/a")   
    
# EJERCICIO 5.
 
# El usuario debe ingresar una contraseña, si tiene entre 8 y 14 caracteres es correcta.
# Ingreso.
contrasena = (input("ingrese una contraseña entre 8 y 14 caracteres "))
longitud = len(contrasena)

# Proceso y salida.
if 8 <= longitud <= 14:
    print(" Ha ingresado una contraseña es correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# EJERCICIO 6

#un programa que elije una lista de numeros aleatorios y calcula su mode, median, y mean.
from statistics import mode, median, mean
mi_lista = [1,2,5,5,3]
mean(mi_lista)

import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

mode = mode(numeros_aleatorios)
print(f"mode :{mode}")
median = median(numeros_aleatorios)
print(f"median :{median}")
mean = mean(numeros_aleatorios)
print(f"mean :{mean}")

# CONDICIONAL
if mode < median < mean:
    print("Esta lista tiene sesgo positivo o a la derecha")
elif mode > median > mean:
    print("Esta lista tiene sesgo negativo")
else:
    print("esta es una lista sin sesgo")   

# EJERCICIO 7
# Se solicita una frase o palabra y, si esta termina en vocal imprimir el string con un signo de exclamacion y si no imprimir sin el signo.

# INGRESO DE DATOS
palabra = input(str("Por favor ingrese una frase o palabra "))
vocales = "a, e, i, o, u"
ultima_letra = palabra[-1]

# CONDICIONAL, PROCESO Y SALIDA
if ultima_letra in vocales:
    print(f"{palabra}!")
else:
    print(f"{palabra}")
    
# EJERCICIO 8

#Se le pide al usuario que ingrese su nombre y un numero
# que correspondera a la manera que quiere ver en pantalla su nombre, 
# minuscula, mayuscula o primera letra mayuscula y resto minuscula.

#Ingreso.
nombre = input("Por favor ingrese su nombre ")
tipo_letra = int(input("Ahora ingrese el numero 1.En mayúsculas. 2.En minúsculas. 3. Nombre con la primera letra mayúscula."))

#Condicional y salida.
if tipo_letra == 1:
    nuevo_nombre = nombre.upper()
elif tipo_letra == 2:
    nuevo_nombre = nombre.lower()
elif tipo_letra == 3:
    nuevo_nombre = nombre.title()
else:
    print("El numero que ingreso no corresponde,ejecute de nuevo el programa. Gracias! ")            
print(f"{nuevo_nombre}")        

#EJERCICIO 9
# El usuario ingresara la magnitud del terremoto y segun la escala de Ritcher se lo clasifica

# Ingreso de datos.
magnitud =float(input("Por favor ingrese la magnitud del terremoto que presencio"))

# Condicional y salida.
if magnitud < 3:
    print("Muy leve(imperceptible)")
elif 4> magnitud >= 3:
    print("leve(ligeramente perceptible)")     
elif 5> magnitud >=4:
    print("Moderado (se siente , pero no causa daños)")
elif 6> magnitud >=5:
    print("Fuerte (causa daños)")
elif 7> magnitud >= 6:
    print("Muy fuerte (causa daños significativos)")
elif magnitud >=7:
    print("Extremo")                 

# EJERCICIO 10
# El usuario ingresa el hemisferio, que mes del año y que dia es, el 
#programa imprime la estacion del año en que se imprime

hemisferio = input("Por favor ingrese el hemisferio en que se encuentra ").lower()
dia = int(input("por favor ingrese el dia  "))
mes = int(input("el mes que transcurre (en numero, ejemplo 1=enero) "))

# Condicional y salida
if hemisferio == "norte":
    if dia >= 21 and mes == 12 or mes == 1 or mes == 2 or mes == 3 and dia < 20:
        print("Esta en temporada de invierno")
    elif dia >= 21 and mes == 3 or mes == 4 or mes == 5 or mes == 6 and dia < 20:
        print("Esta en temporada de primavera")
    elif dia >= 21 and mes == 6 or mes == 7 or mes == 8 or mes == 9 and dia < 20:
        print("Esta en temporada de verano")
    elif dia >= 21 and mes == 9 or mes == 10 or mes == 11 or mes == 12 and dia < 20:
        print("Esta en temporada de otoño")        
elif hemisferio == "sur":
    if dia >= 21 and mes == 12 or mes == 1 or mes == 2 or mes == 3 and dia < 20:
        print("Esta en temporada de verano")
    elif dia >= 21 and mes == 3 or mes == 4 or mes == 5 or mes == 6 and dia < 20:
        print("Esta en temporada de otoño")
    elif dia >= 21 and mes == 6 or mes == 7 or mes == 8 or mes == 9 and dia < 20:
        print("Esta en temporada de invierno")     
    elif dia >= 21 and mes == 9 or mes == 10 or mes == 11 or mes == 12 and dia < 20:
        print("Esta en temporada de primavera")      
    