def empezar_tablero(n):
    # Crea un tablero de tamaño n x n inicializado con espacios en blanco
    return [[" " for _ in range(n)] for _ in range(n)]

def impr_tablero(tablero):
    n = len(tablero)  # Obtiene el tamaño del tablero
    for i in range(n):
        fila = ""
        for j in range(n):
            fila += f" {tablero[i][j]} "  # Añade el valor de la celda a la fila
            if j < n - 1:
                fila += "|"  # Añade separador de columnas si no es la última columna
        print(fila)  # Imprime la fila completa
        if i < n - 1:
            print("---" * n)  # Imprime separadores de filas si no es la última fila
    print("\nCoordenadas disponibles:")
    for i in range(n):
        for j in range(n):
            if tablero[i][j] == " ":
                print(f"({i},{j})", end=" ")  # Imprime las coordenadas de las celdas vacías
    print()

def coord_valida(coordenada, tablero):
    try:
        x, y = map(int, coordenada.split(","))  # Divide la coordenada en x e y
        if tablero[x][y] == " ":  # Verifica si la celda está vacía
            return x, y
        else:
            print("Coordenada ocupada, intenta nuevamente.")
            return None
    except (ValueError, IndexError):
        print("Coordenada inválida, intenta nuevamente.")
        return None

def ganador(tablero, jugador):
    n = len(tablero)
    for i in range(n):
        # Verifica si hay una fila completa del mismo jugador
        if all(tablero[i][j] == jugador for j in range(n)) or all(tablero[j][i] == jugador for j in range(n)):
            return True
    # Verifica las diagonales
    if all(tablero[i][i] == jugador for i in range(n)) or all(tablero[i][n - 1 - i] == jugador for i in range(n)):
        return True
    return False

def empate(tablero):
    # Verifica si todas las celdas están ocupadas
    return all(tablero[i][j] != " " for i in range(len(tablero)) for j in range(len(tablero)))

def juego():
    while True:
        try:
            n = int(input("Ingrese el tamaño del tablero (n): "))  # Solicita el tamaño del tablero
            if n < 1:
                print("El tamaño del tablero debe ser mayor a 0.")
                continue
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        tablero = empezar_tablero(n)  # Inicializa el tablero
        jugadores = ["O", "X"]  # Define los jugadores
        turno = 0

        while True:
            impr_tablero(tablero)  # Imprime el tablero
            jugador_actual = jugadores[turno % 2]  # Alterna entre los jugadores
            print(f"Turno del jugador {jugador_actual}")
            coordenada = input("Ingrese la coordenada en formato x,y: ")

            posicion = coord_valida(coordenada, tablero)  # Valida la coordenada ingresada
            if posicion:
                x, y = posicion
                tablero[x][y] = jugador_actual  # Actualiza el tablero con el movimiento del jugador

                if ganador(tablero, jugador_actual):  # Verifica si hay un ganador
                    impr_tablero(tablero)
                    print(f"¡Jugador {jugador_actual} ha ganado!")
                    break

                if empate(tablero):  # Verifica si hay un empate
                    impr_tablero(tablero)
                    print("¡Es un empate!")
                    break

                turno += 1  # Incrementa el turno

        continuar = input("¿Desea jugar otra vez? (s/n): ").lower()
        if continuar != "s":
            break  # Termina el juego si el usuario no quiere continuar

if __name__ == "__main__":
    juego()  # Inicia el juego si se ejecuta el script
