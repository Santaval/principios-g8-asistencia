# Autora Sharon Gutierrez, adaptado por Aaron Santana
# Universidad de Costa Rica
# Fecha: 2024-05-15


import math  # Importamos el módulo math para utilizar funciones matemáticas como sqrt (raíz cuadrada)

# Definimos una lista global para almacenar los valores ingresados
lista = []

# Esta función permite capturar valores numéricos ingresados por el usuario y almacenarlos en la lista
def capturar_valores():
    opcion = ''  # Inicializamos la variable opcion para controlar el ciclo while
    while opcion != 'salir':
        # Solicitamos al usuario que ingrese un valor numérico o que escriba 'salir' para detener la captura de valores
        valor = input("Ingrese un valor numérico o escriba 'salir' para regresar al menú: ")
        if valor == 'salir':
            break  # Si el usuario ingresa 'salir', rompemos el ciclo
        else:
            try:
                global lista  # Indicamos que usaremos la lista global
                lista.append(float(valor))  # Convertimos el valor ingresado a float y lo agregamos a la lista
            except ValueError:
                # Si el valor ingresado no es un número válido, mostramos un mensaje de error
                print("Ingrese un valor válido.")

# Esta función calcula la suma de todos los valores en la lista
def calcular_suma():
    if not lista:
        # Si la lista está vacía, informamos al usuario que no se han ingresado valores
        print("No se han ingresado valores.")
    else:
        suma = 0  # Inicializamos la suma en 0
        for valor in lista:
            suma += valor  # Sumamos cada valor de la lista a la suma total
        # Mostramos la suma total de los valores
        print("La suma de los valores es:", suma)

# Esta función calcula la media de todos los valores en la lista
def calcular_media():
    if not lista:
        # Si la lista está vacía, informamos al usuario que no se han ingresado valores
        print("No se han ingresado valores.")
    else:
        suma = 0  # Inicializamos la suma en 0
        for valor in lista:
            suma += valor  # Sumamos cada valor de la lista a la suma total
        media = suma / len(lista)  # Calculamos la media dividiendo la suma total entre el número de valores
        # Mostramos la media de los valores
        print("La media de los valores es:", media)

# Esta función calcula la desviación estándar de los valores en la lista
def calcular_desviacion_estandar():
    if not lista:
        # Si la lista está vacía, informamos al usuario que no se han ingresado valores
        print("No se han ingresado valores.")
    else:
        suma = 0  # Inicializamos la suma en 0
        varianza = 0  # Inicializamos la varianza en 0
        for valor in lista:
            suma += valor  # Sumamos cada valor de la lista a la suma total
        media = suma / len(lista)  # Calculamos la media dividiendo la suma total entre el número de valores
        for valor in lista:
            varianza += (media - valor) ** 2 / len(lista)  # Calculamos la varianza sumando los cuadrados de las diferencias entre cada valor y la media
        desviacion_estandar = math.sqrt(varianza)  # Calculamos la desviación estándar tomando la raíz cuadrada de la varianza
        # Mostramos la desviación estándar de los valores
        print("La desviación estándar de los valores es:", desviacion_estandar)

# Esta función obtiene y muestra el valor mínimo y el valor máximo de la lista
def obtener_minimo_maximo():
    if not lista:
        # Si la lista está vacía, informamos al usuario que no se han ingresado valores
        print("No se han ingresado valores.")
    else:
        minimo = min(lista)  # Obtenemos el valor mínimo de la lista
        maximo = max(lista)  # Obtenemos el valor máximo de la lista
        # Mostramos el valor mínimo y el valor máximo de la lista
        print("El mínimo de los valores es:", minimo)
        print("El máximo de los valores es:", maximo)

# Esta función muestra el menú principal y permite al usuario seleccionar diferentes opciones
def menu():
    while True:
        # Mostramos el menú con las diferentes opciones disponibles
        print("------ MENÚ ------")
        print("A- Agregar valores")
        print("B- Calcular y desplegar suma total de valores")
        print("C- Calcular y desplegar media")
        print("D- Calcular y desplegar desviación estándar")
        print("E- Desplegar el mínimo y máximo de los valores ingresados")
        print("S- Salir")

        # Solicitamos al usuario que seleccione una opción
        opcion = input("Seleccione una opción: ").upper()

        if opcion == 'A':
            capturar_valores()  # Llamamos a la función para capturar valores
        elif opcion == 'B':
            calcular_suma()  # Llamamos a la función para calcular la suma
        elif opcion == 'C':
            calcular_media()  # Llamamos a la función para calcular la media
        elif opcion == 'D':
            calcular_desviacion_estandar()  # Llamamos a la función para calcular la desviación estándar
        elif opcion == 'E':
            obtener_minimo_maximo()  # Llamamos a la función para obtener el mínimo y máximo de los valores
        elif opcion == 'S':
            print("Saliendo...")  # Informamos al usuario que se está saliendo del programa
            break  # Rompemos el ciclo y salimos del programa
        else:
            # Si el usuario ingresa una opción no válida, mostramos un mensaje de error
            print("Opción no válida.")

# Llamamos a la función del menú principal para iniciar el programa
menu()
