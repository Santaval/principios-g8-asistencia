def mostrar_menu():
    # Muestra el menú de opciones al usuario
    print("Seleccione una opción:")
    print("1. Codificar mensaje")
    print("2. Descodificar mensaje")
    print("3. Salir")

def codificar(mensaje, k):
    # Codifica el mensaje usando un cifrado con desplazamiento basado en la llave k
    hi = "qwertyuiopasdfghjklñzxcvbnm"
    hi_m = "QWERTYUIOPASDFGHJKLÑZXCVBNM"
    mensaje_codificado = ""
    for C in mensaje.lower():  # Convierte el mensaje a minúsculas
        if C in hi:
            # Encuentra el índice de la letra y aplica el desplazamiento
            indice = (hi.index(C) + k) % len(hi)
            mensaje_codificado += hi_m[indice]  # Añade la letra codificada en mayúsculas
        else:
            mensaje_codificado += C  # Añade los caracteres que no están en el alfabeto sin codificar
    return mensaje_codificado

def descodificar(mensaje, k):
    # Descodifica el mensaje usando un cifrado con desplazamiento basado en la llave k
    hi = "qwertyuiopasdfghjklñzxcvbnm"
    hi_m = "QWERTYUIOPASDFGHJKLÑZXCVBNM"
    mensaje_descodificado = ""
    for C in mensaje:
        if C in hi_m:
            # Encuentra el índice de la letra y aplica el desplazamiento inverso
            indice = (hi_m.index(C) - k) % len(hi_m)
            mensaje_descodificado += hi[indice]  # Añade la letra descodificada en minúsculas
        else:
            mensaje_descodificado += C  # Añade los caracteres que no están en el alfabeto sin descodificar
    return mensaje_descodificado

def llave():
    # Solicita al usuario que ingrese una llave válida entre 0 y 27
    while True:
        try:
            k = int(input("Ingrese la llave: "))
            if 0 <= k <= 27:
                return k
            else:
                print("Valor incorrecto.")
        except ValueError:
            print("Ingrese un número válido.")

def main():
    # Función principal que maneja el flujo del programa
    while True:
        mostrar_menu()  # Muestra el menú de opciones
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            mensaje = input("Ingrese mensaje para codificar: ")
            k = llave()
            mensaje_codificado = codificar(mensaje, k)
            print("Mensaje codificado:", mensaje_codificado)
        elif opcion == "2":
            mensaje = input("Ingrese mensaje para descodificar: ")
            k = llave()
            mensaje_descodificado = descodificar(mensaje, k)
            print("Mensaje descodificado:", mensaje_descodificado)
        elif opcion == "3":
            print("Programa finalizado")
            break  # Sale del bucle y termina el programa
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()
