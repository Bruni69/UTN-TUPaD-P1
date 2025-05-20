#Trabajo Practico funciones.
#Ejercicio 1 
#Crear una funcion que imprima hola mundo.

def imprimir_hola_mundo():
    print("Hola mundo!")
imprimir_hola_mundo()

#Ejercicio 2
#Crear una funcion que reciba un nombre y lo salude.
def saludar_usuario():
    nombre=input("Ingrese su nombre: ")
    print(f"hola {nombre}")
saludar_usuario()

#Ejercicio 3
#Crear una funcion que reciba 4 parametros de informacion personal
# y llamar a la funcion con los valores ingresados

def informacio_personal():
    nombre=input("Ingrese su nombre: ") 
    apellido=input("ingrese su apellido: ")
    edad=input("ingrese ahora su edad: ")
    residencia=input("por ultimo ingrese su lugar de residencia: ")
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
informacio_personal()

#Ejercicio 4
# Dos funciones q calculen el area y el perimetro cuando se le de un radio como parametro.
radio=float(input("ingrese el radio"))
def calcular_area_circulo():
    area=3.14*radio**2
    print(f"El area del circulo es: {area} y")

def calcular_perimetro_circulo():
    perimetro=2*3.14*radio
    print(f"El perimetro del circulo con ese radio es: {perimetro}, ")
   
calcular_area_circulo()
calcular_perimetro_circulo()   

# Ejercicio 5
#Crear una funcion que le ingrese los segundos y devuelva la hora.
def segundos_a_horas():
    segundos=float(input("ingrese la cantidad de segundos: "))
    horas=segundos/3600
    print(f"segun los segundos ingresados las horas son: {horas}")
segundos_a_horas()    

# Ejercicio 6
# Crar una funcion que dado un numero ingresado
# devuelva la tabla de multiplicar.

def tabla_multiplicar():
    numero=int(input("Ingrese el numero del que desea conocer su tabla: "))
    i=1
    for i in range(1,11):
        resultado=numero*i
        print(f"{numero}*{i}={resultado} ")
tabla_multiplicar()

#Ejercicio 7
#Ingresan dos parametros y devuelve una tupla con los
#resultados de suma, resta, mult y division.
def operaciones_basicas():
    a=float(input("ingrese un primer numero para sumar,restar, multiplicar y dividir"))
    b=float(input("ingrese el segundo numero"))
    while b == 0:
        b=float(input("ingrese un numerador diferente de cero")) 
    suma=a+b
    resta=a-b
    multiplicacion=a*b
    division=a/b
    mi_tupla=tuple([suma,resta,multiplicacion,division])
    
    print(f"los resultados de las operaciones son: {mi_tupla}")
operaciones_basicas()

#Ejercicio 8
#ingresar dos parametros y que devuelva el IMC con dos decimales.
def calcular_imc():
    peso=float(input("ingrese su peso en kilogramos "))
    altura=float(input("ingrese su altura "))
    while altura == 0:
        altura=float(input("ingrese su altura "))
    imc=peso/altura**2
    print(f"su IMC es: {imc:.2f}")
calcular_imc()

#Ejercicio 9
#crear una funcion que haga una converision entre centigrados a farenheit.
def celcius_a_farenheit():
    celcius=float(input("INgrese la temperatura en grados celcius para la conversion"))
    far=celcius*9/5+32
    print(f"la temperatura en grados farenheit es: {far}") 
celcius_a_farenheit()