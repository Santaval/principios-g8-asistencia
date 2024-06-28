def buscar_rutas(parada_origen, parada_destino, rutas):
    rutas_encontradas = []

    for archivo_rutas in rutas:
        with open(archivo_rutas, 'r', encoding='ISO-8859-1') as archivo:
            nombre_ruta = archivo.readline().strip()  # Lee el nombre de la ruta desde la primera línea
            ruta_actual = None

            for linea in archivo:
                datos = linea.strip().split(',')
                parada = datos[0].strip()  # Obtiene la parada
                hora = datos[1].strip()  # Obtiene la hora

                if parada == parada_origen:
                    # Si la parada es la de origen, inicia una nueva ruta
                    ruta_actual = {'Nombre Ruta': nombre_ruta, 'Hora': hora, 'Paradas': [parada]}

                elif ruta_actual:
                    ruta_actual['Paradas'].append(parada)  # Añade la parada a la lista de paradas

                    if parada == parada_destino:
                        # Si la parada es la de destino, completa la ruta y la añade a las rutas encontradas
                        ruta_actual['Hora Llegada'] = hora
                        rutas_encontradas.append(ruta_actual)
                        ruta_actual = None

    return rutas_encontradas

def main():
    parada_origen = input("Inserte la parada en la que se encuentra: ")
    parada_destino = input("Inserte la parada a la que desea llegar: ")

    rutas = [
        'routes/01.txt',
        'routes/02.txt',
        'routes/03.txt'
    ]

    rutas_encontradas = buscar_rutas(parada_origen, parada_destino, rutas)

    if rutas_encontradas:
        # Imprime las rutas encontradas
        print("Las rutas de bus que pasan por {} y llegan a {} son:".format(parada_origen, parada_destino))
        print("{:<20} {:<10}".format("Ruta", "Hora"))
        for ruta in rutas_encontradas:
            print("{:<20} {:<10}".format(ruta['Nombre Ruta'], ruta['Hora']))
    else:
        print("No hay rutas disponibles para llegar de {} a {}.".format(parada_origen, parada_destino))

if __name__ == "__main__":
    main()
