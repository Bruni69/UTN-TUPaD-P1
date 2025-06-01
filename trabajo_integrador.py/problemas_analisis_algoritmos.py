# TRABAJO INTEGRADOR  PROGRAMACION.
# ANALISIS DE ALGORITMOS.

import time

def es_palindromo(palabra):
    palabra = palabra.lower()
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

def sera_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    return palabra == palabra[::-1]

# Palabras de prueba
palabra1 = "Reconocer"  # True
palabra2 = "Constantinopla"  # False

# Medición para la función recursiva
inicio_rec = time.time()
resultado1_rec = es_palindromo(palabra1)
resultado2_rec = es_palindromo(palabra2)
fin_rec = time.time()
print(f"Función recursiva: {resultado1_rec}, {resultado2_rec} | Tiempo: {fin_rec - inicio_rec:.8f} segundos")

# Medición para la función con slicing
inicio_slice = time.time()
resultado1_slice = sera_palindromo(palabra1)
resultado2_slice = sera_palindromo(palabra2)
fin_slice = time.time()
print(f"Función con slicing: {resultado1_slice}, {resultado2_slice} | Tiempo: {fin_slice - inicio_slice:.8f} segundos")

