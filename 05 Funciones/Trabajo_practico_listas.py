# EJERCICIO 1
# Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

lista_range = list(range(1,101))
print(lista_range)

# EJERCICIO 2
#Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. 
# ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!

lista=["guitarra","naranja", 7, "flores","alfajor"]
print(lista[3])

# EJERCICIO 3
# Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla. 
# Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por ejemplo: lista_vacia = []

listita=[]
listita.append("solista")
listita.append("gajo")
listita.append("cascara")
print(listita)

# EJERCICIO 4
# Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. 
# Imprimir la lista resultante por pantalla. 
# ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos! 
# animales = ["perro", "gato", "conejo", "pez"]

animales = ["perro", "gato", "conejo", "pez"]
animales[1] ="loro"
animales[3] = "oso"
print(animales)

# EJERCICIO 5
# Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
numeros=[8,15,3,22,7]
numeros.remove(max(numeros))
print(numeros)
# Lo que realiza el codigo es remover de la lista el elemento de maximo valor en el caso de numeros

# EJERCICIO 6
#Crear una lista con números del 10 al 30 (incluído), 
# haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.

lista_num=list(range(10,31,5))
rango_mostrar = lista_num[0:2]
print(rango_mostrar)

#EJERCICIO 7 
# Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera. 
# autos = ["sedan", "polo", "suran", "gol"]

autos = ["sedan", "polo", "suran", "gol"]
autos[1:2] = "camaro", "silverado"
print(autos)

#EJERCICIO 8
#Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla.

dobles = []
a = 2*5
b = 10*2
c = 15*2
dobles.append(a)
dobles.append(b)
dobles.append(c)
print(dobles)

# EJERCICIO 9
# Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer clienTE

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
lista2=compras[2]
lista2.append("jugo")
print(compras)

compras[1]="arroz", "tallarines","salsa"
print(compras)

lista0=compras[0]
lista0.remove("pan")
print(compras)

#EJERCICIO 10
# Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
#● Posición lista_anidada[0]: 15
#● Posición lista_anidada[1]: True
#● Posición lista_anidada[2][0]: 25.5
#● Posición lista_anidada[2][1]: 57.9
#● Posición lista_anidada[3]: False
#Imprimir la lista resultante por pantalla

lista_anidada=[15,"true", [25.5, 57.9],"false"]
print(lista_anidada)
print(type(lista_anidada))
