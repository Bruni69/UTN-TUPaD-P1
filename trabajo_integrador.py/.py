import random
import timeit

#Sin semilla

def generar_lista_aleatoria(cantidad, maximo):
    return [random.randint(1, maximo) for _ in range(cantidad)]

# Configuración
cantidad = 10000
maximos = [10, 100, 1000, 10000]

# Medir tiempo para cada máximo
for max_val in maximos:
    tiempo = timeit.timeit(
        stmt=lambda: generar_lista_aleatoria(cantidad, max_val),
        number=10000  # Repetir 10000 veces para mayor precisión
    )
    print(f"Max: {max_val} | Tiempo promedio: {tiempo / 1000:.6f} segundos")
    

print()

#Con semilla
import random
import timeit

def generar_lista_con_semilla(cantidad, maximo, semilla=None):
    if semilla is not None:
        random.seed(semilla)
    return [random.randint(1, maximo) for _ in range(cantidad)]

# Configuración
cantidad = 1000
semilla = 42
maximos = [10, 100, 1000, 10000]

# Medir tiempo para cada máximo
for max_val in maximos:
    tiempo = timeit.timeit(
        stmt=lambda: generar_lista_con_semilla(cantidad, max_val, semilla),
        number=1000  # Repetir 1000 veces
    )
    print(f"Max: {max_val} | Tiempo promedio: {tiempo / 1000:.6f} segundos")