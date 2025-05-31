#Trabajo Practico funciones.
#Ejercicio 1 
#Crear una funcion que imprima hola mundo.

def imprimir_hola_mundo():
    print("Hola mundo!")
imprimir_hola_mundo()

#Ejercicio 2
#Crear una funcion que reciba un nombre y lo salude.
def saludar_usuario(nombre):
    return f"hola {nombre}!"

nombre=input("Ingrese su nombre: ")
saludo=saludar_usuario(nombre)
print(saludo)

#Ejercicio 3
#Crear una funcion que reciba 4 parametros de informacion personal
# y llamar a la funcion con los valores ingresados

def informacio_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
    
nombre=input("Ingrese su nombre: ") 
apellido=input("ingrese su apellido: ")
edad=input("ingrese ahora su edad: ")
residencia=input("por ultimo ingrese su lugar de residencia: ")
informacio_personal(nombre, apellido, edad, residencia)


#Ejercicio 4
# Dos funciones q calculen el area y el perimetro cuando se le de un radio como parametro.
PI=3.14
def calcular_area_circulo(radio):
    return PI*radio**2
def calcular_perimetro_circulo(radio):
    return 2*PI*radio
   
radio=float(input("ingrese el radio: "))
area=calcular_area_circulo(radio) 
perimetro=calcular_perimetro_circulo(radio) 
print(f"El area del circulo es: {area:.2f} y")
print(f"El perimetro del circulo con ese radio es: {perimetro:.2f} ") 

# Ejercicio 5
#Crear una funcion que le ingrese los segundos y devuelva la hora.
def segundos_a_horas(segundos):
    return segundos/3600

segundos=float(input("ingrese la cantidad de segundos: "))
horas=segundos_a_horas(segundos)
print(f"segun los {segundos} segundos ingresados equivale a: {horas:.2f} horas")


# Ejercicio 6
# Crar una funcion que dado un numero ingresado
# devuelva la tabla de multiplicar.

def tabla_multiplicar(numero):
    for i in range(1,11):
        resultado=numero*i
        print(f"{numero}*{i}={resultado} ")

numero=int(input("Ingrese el numero del que desea conocer su tabla: "))
tabla_multiplicar(numero)

#Ejercicio 7
#Ingresan dos parametros y devuelve una tupla con los
#resultados de suma, resta, mult y division.
def operaciones_basicas(a,b):
    suma = a+b
    resta=a-b
    multiplicacion=a*b
    if b!= 0:
        division=a/b
    else:
        division=None
    return (suma, resta, multiplicacion, division)

a=float(input("ingrese un primer numero para sumar,restar, multiplicar y dividir"))
b=float(input("ingrese el segundo numero"))
suma, resta, multiplicacion, division =operaciones_basicas(a,b) 
           
print(f"los resultados de las operaciones son:")
print(f"suma: {suma}")
print(f"suma: {resta}")
print(f"suma: {multiplicacion}")
if division != None:
    print(f"division {division}")
else:
    print("No se puede dividir por cero")

#Ejercicio 8
#ingresar dos parametros y que devuelva el IMC con dos decimales.
def calcular_imc(peso,altura):
    if altura != 0:
        imc=peso/altura**2
    else:
        print("No se puede calcular si su altura es cero")    
    print(f"su IMC es: {imc:.2f}")
    return imc
peso=float(input("ingrese su peso en kilogramos "))
altura=float(input("ingrese su altura "))
calcular_imc(peso,altura)

#Ejercicio 9
#crear una funcion que haga una conversion entre centigrados a farenheit.
def celcius_a_farenheit(celcius):
    far=celcius*9/5+32
    print(f"la temperatura en grados farenheit es: {far}") 
    return far
celcius=float(input("INgrese la temperatura en grados celcius para la conversion"))
celcius_a_farenheit(celcius)

#ejercicio 10
def calcular_promedio(a,b,c):
    return (a+b+c)/3

a=float(input("ingrese la primer nota"))
b=float(input("ingrese la segunda nota"))
c=float(input("ingrese la tercer nota"))
promedio=calcular_promedio(a,b,c)
print(f"el promedio de las tres notas es: {promedio:.1f}")
