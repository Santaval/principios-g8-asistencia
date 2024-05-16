# Autora: Valeria Castro, adaptado por Aaron Santana
# Universidad de Costa Rica
# Fecha: 2024-05-15

# Esta función se encarga de leer un número entero de la entrada estándar, lo valida y lo retorna.
def numero_entero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

# Esta función se encarga de leer una respuesta 'sí' o 'no' de la entrada estándar, la valida y la retorna.
def si_no(mensaje):
    while True:
        respuesta = input(mensaje)
        if respuesta == "s" or respuesta == "n":
            return respuesta == "s"
        else:
            print("Por favor, responda únicamente con 's' o 'n'")

# Pregunta 1: Cantidad de bits de la interfaz con el chip puente.
# Utiliza la función numero_entero para obtener un número entero de la entrada estándar.
# Este número representa la cantidad de bits de la interfaz con el chip puente (B) y se almacena en la variable bits.
bits = numero_entero("Ingrese la cantidad de bits de la interfaz con el chip puente:")

# Pregunta 2: Grosor del empaquetamiento.
# Utiliza la función numero_entero para obtener un número entero de la entrada estándar.
# Este número representa el grosor del empaquetamiento (G) y se almacena en la variable thickness.
thickness = numero_entero("Ingrese el grosor del empaquetamiento (nm):")

# Pregunta 3: Cantidad de errores obtenidos en la prueba de software en un minuto.
# Utiliza la función numero_entero para obtener un número entero de la entrada estándar.
# Este número representa la cantidad de errores obtenidos en la prueba de software en un minuto (E) y se almacena en la variable errors.
errors = numero_entero("Ingrese la cantidad de errores obtenidos en la prueba de software en un minuto:")

# Pregunta 4: ¿El procesador se va a utilizar para administrar energía eléctrica?
# Utiliza la función si_no para obtener una respuesta 'sí' o 'no' de la entrada estándar.
# Esta respuesta indica si el procesador se va a utilizar para administrar energía eléctrica (A) y se almacena en la variable usedForPowerAdministration.
usedForPowerAdministration = si_no("¿El procesador se va a utilizar para administrar energía eléctrica? (s/n):")

# Pregunta 5: Si el procesador se usa para administrar energía eléctrica, ¿pasa la prueba con Power 603E?
# Utiliza la función si_no para obtener una respuesta 'sí' o 'no' de la entrada estándar.
# Solo se pregunta si el procesador se utiliza para administrar energía eléctrica.
# El resultado se almacena en la variable passPowerProve.
if usedForPowerAdministration:
    passPowerProve = si_no("¿El procesador pasa la prueba con Power 603E? (s/n):")
else:
    passPowerProve = False

# Esta función verifica si un procesador es apto para la NASA basado en ciertos criterios.
def apto_para_NASA(B, G, E, A, P):
    # Verificar que la interfaz tenga 32 o 64 bits.
    if B != 32 and B != 64:
        return False
    
    # Verificar que el grosor del empaquetamiento sea mayor o igual a 750 nm.
    if G < 750:
        return False
    
    # Verificar que la cantidad de errores en la prueba de software sea menor o igual a 700.
    if E > 700:
        return False
    
    # Si el procesador se utiliza para administrar energía eléctrica, debe pasar la prueba con Power 603E.
    if A and not P:
        return False
    
    return True

# Determinar si el procesador es apto para la NASA.
if apto_para_NASA(bits, thickness, errors, usedForPowerAdministration, passPowerProve):
    print("Apto para la NASA")
else:
    print("No apto para la NASA")
