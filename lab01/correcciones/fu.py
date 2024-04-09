import math
import sys

def calcular_tilapias(P, t, m, G):
    try:
        if not isinstance(P, int):
            raise ValueError("El valor de P debe ser un entero.")
        if not (isinstance(t, (int, float)) and isinstance(m, (int, float)) and isinstance(G, (int, float))):
            raise ValueError("Los valores de t, m y G deben ser números.")

        e = 2.71828
        f_t = P / (1 + 11 * math.exp(-0.2 * t))
        f_t = round(f_t, 2)
        print(f"La cantidad estimada de tilapias en el estanque después de {t} días es: {f_t}")

        peso_total = 0.5 * f_t * m / 1000  # Convertir gramos a kilogramos
        peso_total = round(peso_total, 2)
        print(f"El peso total de carne de tilapia que se obtendrá si se pesca el 50% de los peces después de {t} días es: {peso_total} kg")

        ganancias = peso_total * 6000
        ganancias = round(ganancias, 2)
        print(f"Las ganancias obtenidas con la pesca anterior serían mayores o iguales a G: {ganancias >= G}")

        if ganancias < G:
            print("Las ganancias obtenidas con la pesca anterior son menores que las ganancias del mes anterior. Terminando el programa.")
            sys.exit(0)

    except ValueError as ve:
        print(ve)
        sys.exit(0)


try: 
    P = int(input("Ingrese la capacidad del estanque:"))
except:
    print("Error al leer la capacidad del estanque, digite un numero entero")
    sys.exit(0)
    
    
try:
    t = float(input("Ingrese el número de días:"))
except:
    print("Error al leer el número de días, digite un número")
    sys.exit(0)
    
try:
    m = float(input("Ingrese el peso promedio de las tilapias en gramos:"))
except:
    print("Error al leer el peso promedio de las tilapias, digite un número")
    sys.exit(0)
    
try:
    G = float(input("Ingrese las ganancias del mes anterior:"))
except:
    print("Error al leer las ganancias del mes anterior, digite un número")
    sys.exit(0)
    
# Prueba de la función
calcular_tilapias(P, t, m, G)

