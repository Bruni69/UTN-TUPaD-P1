# Ejercicio 1
def fact_recur(a):
    if a == 0:
        return 1
    else:
        return a*fact_recur(a-1)
                                
a=int(input("Elija un numero para calcula su factorial: "))
   #Se calcula el factorial de un numero.


# Ahora debe calcular el factorial de todos los numero enteros entre 1 el el número elejido.
for a in range(a,-1,-1):
    print(f"el factorial de {a} es: {fact_recur(a)}")
    
#Ejercicio 2
# Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada.
# Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

def sec_fibon(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return sec_fibon(n-1)+sec_fibon(n-2)
    
    
n=int(input("elija un numero para calcular la secuencia de fibonacci"))
print(sec_fibon(n))


#Falta consiga 2

##Ejercicio 3
#Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, 
# utilizando la fórmula 𝑛𝑚= 𝑛∗𝑛(𝑚−1). Prueba esta función en un algoritmo general.

def potencia(n,m):
    if m == 0:
        return 1
    else:
        return n*potencia(n,m-1)


base=int(input("ingrese el numero base para calcular alguna potencia: "))
exp=int(input("ingrese el exponente: "))
print(f"el resultado de calcular {base}^{exp} es = {potencia(base,exp)}")

#Ejercicio 4
#Crear una función recursiva en Python que reciba un número entero positivo en base decimal
# y devuelva su representación en binario como una cadena de texto.

def dec_bin(n):
    if n<0:
        return "el numero ingresado es negativo,debe ingresar uno positivo"
    elif n==0:
        return ""
    else:
       return dec_bin(n // 2) + str(n % 2)
            
num=int(input("ingrese un decimalpara realizar la conver"))
print(f"{num} en binario es: {dec_bin(num)}")

