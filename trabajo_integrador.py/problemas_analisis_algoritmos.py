# TRABAJO INTEGRADOR  PROGRAMACION.
# ANALISIS DE ALGORITMOS.
# Se comparara el mismo ejercicio con un bucle for y luego con una funcion para asi luego evaluar

#Factorial

def fact_recur(a):
    if a == 0:
        return 1
    else:
        return a*fact_recur(a-1)
                                
a=int(input("elija un numero: "))
print(f"el factorial de {a} es: {fact_recur(a)}")


# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.
num = int(input("ingrese un entero: "))
suma = 0
for i in range(num+1):
    suma = suma + i
print("la suma de todos los numeros es: ",suma)



