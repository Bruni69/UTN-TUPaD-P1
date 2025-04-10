# EJERCICIO 1 imprime en pantalla todos los números enteros desde 0 hasta 100.
for i in range(101):
    print(i)


# EJERCICIO 2. Se ingresa un numero entero y dice cuantos digitos tiene.    
num = int(input("ingrese un numero entero sin decimales"))
num_int = str(num) 
num_dig = len(num_int)
print("la cantidad de digitos es: ",num_dig)


# EJERCICIO 3
# Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese un numero entero"))
num2 = int(input("Ingrese unsegundo numero entero"))
cont = 0
num1 = num1 +1
for i in range(num1,num2):
    cont = cont + i
print("la suma de todos los numero es:",cont)   

# EJERCICIO 4
# Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese cero se cierra

num = None
num_suma = 0
while num != 0:
    num = int(input("ingrese un numero entero y cero para ver la sumatoria"))                
    num_suma = num_suma + num 
print("la suma de todos los numeros es:",num_suma) 

# EJERCICIO 5
#Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
intentos = 0
num_aleat = random.randint(0,9)
num = None
while num_aleat != num:
    num = int(input("ingerse un numero entre 0 y 9 a ver si adivina "))
    intentos = intentos + 1
print("acerto!!! necesito", intentos, "intentos")

# EJERCICIO 6
#Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.
for i in range(100,0,-2):
    print(i)
    
# EJERCICIO 7
# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.
num = int(input("ingrese un entero: "))
suma = 0
for i in range(num+1):
    suma = suma + i
print("la suma de todos los numeros es: ",suma)

# EJERCICIO 8
# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).
num = input("ingrese una cantidad que quiera realizar el calculo de la media ")
i = 0
suma = 0
cant = 0
media = 0
for i in range(10):
    suma = suma + i
    cant = cant +1
media = suma/cant        
print("la media de todos los numeros es: ",media)       


# EJERCICIO 9
# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores.

# Inicializamos variables
i = 0
suma = 0
cant = 0
#inicio de bucle for e ingreso de datos. aqui se puede cambiar la cantidad de numeros a ingresar.
for i in range(2):
    num = int(input("ingrese los numeros que quiera realizar el calculo de la media "))
    suma = suma + num
    cant = cant + 1
# proceso y salida    
Smedia = suma/cant
print("la suma de todos los numeros ingresados es: ",suma)
print("la cantidad de numeros ingresada fue: ",cant)
        
print("Por lo tanto, la media de todos los numeros es : la suma de todos los numeros/cantidad= ",media) 


# EJERCICIO 10
# Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num = int(input("Ingrese un numero y yo (tu computadora) invertire los digitos para tu diversion"))
ult_dig = 0
num_inv = 0
while num > 0:
    ult_dig = num % 10
    num_inv =(num_inv * 10) + ult_dig
    num //=10
print(num_inv)