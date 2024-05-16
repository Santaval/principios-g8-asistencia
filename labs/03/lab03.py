# autor: Bryan Mendez, adaptado por Aaron Santana
# Universidad de Costa Rica
# Fecha: 2024-05-15

import math
import random

# Esta función calcula la cantidad de casas y locales que se construyen en una ciudad.
# Recibe como parámetro la latitud y retorna "Casa" o "Local" dependiendo de una probabilidad calculada.
def calcular_casa_o_local(latitud):
    # Calcula la probabilidad de construir una casa en la latitud dada
    probability = 1 / (1 + math.e**(-1000 * (latitud - 9.746)))
    # Genera un número aleatorio entre 0 y 1
    # Si el número aleatorio es menor que la probabilidad, se construye una casa
    if random.random() < probability:
        return "Casa"
    else:
        return "Local"

# Esta función simula la construcción de edificios en una ciudad.
# Recibe la cantidad de edificios a construir (n) y retorna la cantidad de casas y locales construidos.
def edificios_ciudad(n):
    casas = 0  # Contador de casas construidas
    locales = 0  # Contador de locales construidos

    # Realiza la construcción de n edificios
    for i in range(n):
        # Genera una latitud aleatoria entre 9.74 y 9.75
        latitud = random.uniform(9.74, 9.75)
        # Determina si se construye una casa o un local en la latitud generada
        if calcular_casa_o_local(latitud) == "Casa":
            casas += 1  # Incrementa el contador de casas
        else:
            locales += 1  # Incrementa el contador de locales

    # Retorna la cantidad de casas y locales construidos
    return casas, locales

# Esta función calcula el promedio de casas y locales construidos en m simulaciones.
# Recibe la cantidad de simulaciones a realizar (m) y la cantidad de edificios a construir en cada simulación (n).
# Retorna el promedio de casas y locales construidos.
def promedio_edificios(m, n):
    total_casas = 0  # Contador total de casas construidas en todas las simulaciones
    total_locales = 0  # Contador total de locales construidos en todas las simulaciones

    # Realiza m simulaciones
    for i in range(m):
        # Simula la construcción de edificios en la ciudad
        casas, locales = edificios_ciudad(n)
        total_casas += casas  # Acumula la cantidad de casas construidas
        total_locales += locales  # Acumula la cantidad de locales construidos

    # Calcula el promedio de casas y locales construidos
    prom_casas = round(total_casas / m, 1)
    prom_locales = round(total_locales / m, 1)

    # Retorna los promedios de casas y locales construidos
    return prom_casas, prom_locales

# Esta función muestra el menú principal de la simulación.
# Solicita al usuario la cantidad de simulaciones (m) y la cantidad de edificios a construir en cada simulación (n).
# Luego, muestra el promedio de casas y locales construidos.
def menu_principal():
    try:
        # Solicita al usuario la cantidad de simulaciones
        m = int(input("Ingrese la cantidad de simulaciones: "))
    except ValueError:
        print("Error: Debe ingresar un número entero.")
        return

    try:
        # Solicita al usuario la cantidad de edificios en cada simulación
        n = int(input("Ingrese la cantidad de edificios en cada simulación: "))
    except ValueError:
        print("Error: Debe ingresar un número entero.")
        return

    # Calcula y muestra el promedio de casas y locales construidos
    prom_casas, prom_locales = promedio_edificios(m, n)
    print(f"En promedio se construyen {prom_casas} casas y {prom_locales} locales.")

# Llama a la función del menú principal para iniciar la simulación
menu_principal()
