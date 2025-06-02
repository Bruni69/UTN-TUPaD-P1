import time

# Funciones de verificación de palíndromos
def es_palindromo_rec(palabra):
    palabra = palabra.lower().replace(" ", "")
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo_rec(palabra[1:-1])

def es_palindromo_slice(palabra):
    palabra = palabra.lower().replace(" ", "")
    return palabra == palabra[::-1]

# Lista base de palabras (10 palíndromos + 10 no palíndromos)
palabras_base = [
    # Palíndromos
    "Reconocer", "Anita lava la tina", "A man a plan a canal Panama", 
    "oso", "arenera", "Salas", "Somos", "Rayar", "Rotator", "Neuquén",
    # No palíndromos
    "Python", "Computadora", "Algoritmo", "Programación", "OpenAI",
    "JavaScript", "Bucle", "Función", "Variable", "String"
]

# Función para medir tiempos
def medir_tiempos(funcion, palabras):
    inicio = time.perf_counter()  # Mayor precisión
    for palabra in palabras:
        funcion(palabra)
    fin = time.perf_counter()
    return fin - inicio

# Experimentación con tamaño creciente
print("=== Crecimiento del tiempo vs tamaño de lista (n) ===")
print("n\tTiempo Recursivo\tTiempo Slicing\t\tDiferencia")

n_inicial = 20  # Empezamos con las 20 palabras base
for i in range(1, 11):  # 10 iteraciones
    n = n_inicial * (2 ** (i-1))  # Duplicamos n en cada iteración
    palabras = palabras_base * (n // 20 + 1)  # Extendemos la lista
    palabras = palabras[:n]  # Aseguramos tamaño exacto
    
    # Medición
    tiempo_rec = medir_tiempos(es_palindromo_rec, palabras)
    tiempo_slice = medir_tiempos(es_palindromo_slice, palabras)
    
    # Resultados
    print(f"{n}\t{tiempo_rec:.6f} s\t\t{tiempo_slice:.6f} s\t\t{tiempo_rec - tiempo_slice:.6f} s")