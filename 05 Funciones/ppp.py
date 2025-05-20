#Ejercicio 10
# Recibe 3 notas y saca el promedio.
def calcular_promedio():
    nota1=float(input("ingrese la primer nota"))
    nota2=float(input("ingrese la segunda nota"))
    nota3=float(input("ingrese la tercer nota"))
    
    suma=nota1+nota2+nota3
    promedio=suma/3
    print(f"el promedio de las tres notas es: {promedio}")
calcular_promedio()