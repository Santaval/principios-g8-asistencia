# Autor: Alejandro Salas, adaptado por Aaron Santana
# Universidad de Costa Rica
# Fecha: 2024-05-15

# Intentamos obtener la capacidad máxima del estanque del usuario.
# Usamos try y except para asegurar que el valor ingresado sea un número entero.
try:
    # Se solicita al usuario que ingrese la capacidad del estanque (P)
    tankCapacity = int(input("Ingrese la capacidad máxima del estanque:"))
except ValueError:
    print("Error, el valor ingresado como la capacidad del estanque debe ser un número entero.")
    exit(0)

# Intentamos obtener el tiempo en días para estimar la cantidad de tilapias en el estanque.
# Usamos try y except para asegurar que el valor ingresado sea un número.
try:
    # Se solicita al usuario que ingrese el tiempo en días (T)
    days = float(input("Inserte los días para estimar la cantidad de tilapias en el estanque:"))
except ValueError:
    print("Error, el valor ingresado como el tiempo en días debe ser un número.")
    exit(0)

# Calculamos la cantidad estimada de tilapias en el estanque después de T días usando la fórmula proporcionada.
# Almacenamos el resultado en la variable tilapiaAmount (F).
tilapiaAmount = tankCapacity / (1 + 11 * 2.71828**(-0.2 * days))
print("La cantidad estimada de tilapias en el estanque después de", days, "días es de", round(tilapiaAmount, 2))

# Intentamos obtener el peso promedio de una tilapia del usuario.
# Usamos try y except para asegurar que el valor ingresado sea un número.
try:
    # Se solicita al usuario que ingrese el peso promedio de una tilapia (M)
    tilapiaWeight = float(input("Inserte el peso promedio de una tilapia (kg):"))
except ValueError:
    print("Error, el peso promedio de una tilapia debe ser un valor numérico.")
    exit(0)

# Calculamos la cantidad de carne obtenida si se pesca la mitad de los peces después de T días.
# Almacenamos el resultado en la variable meatAmount (C).
meatAmount = tilapiaWeight * tilapiaAmount / 2
print("Si se pesca la mitad de los peces después de", days, "días, se obtendrá",
      round(meatAmount, 2), "kg de carne")

# Intentamos obtener las ganancias del mes pasado del usuario.
# Usamos try y except para asegurar que el valor ingresado sea un número.
try:
    # Se solicita al usuario que ingrese las ganancias del mes pasado (G)
    previousMonthGains = float(input("Inserte las ganancias del mes pasado:"))
except ValueError:
    print("Error, las ganancias del mes pasado deben ser un valor numérico.")
    exit(0)

# Calculamos las ganancias de este mes multiplicando la cantidad de carne obtenida por el precio por kg.
# Almacenamos el resultado en la variable actualMonthGains.
actualMonthGains = meatAmount * 6000

# Verificamos si las ganancias de este mes son mayores o iguales a las del mes pasado.
# Imprimimos el resultado de esta comparación.
print("¿Las ganancias de este mes superarían o igualarían a las del anterior?", bool(actualMonthGains >= previousMonthGains))
