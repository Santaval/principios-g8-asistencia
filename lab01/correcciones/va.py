
#Pregunta 1a
#𝑃 es la capacidad máxima del estanque (medida en cantidad de peces)
try:
    P=int(input("Ingrese la capacidad del estanque:"))
except ValueError:
    print("Error al leer la capacidad del estanque (P), ingrese un valor numérico que sea un número entero")
    exit(0)

try:
    t=int(input("Inserte el tiempo en días para estimar la cantidad de tilapias en el estanque:"))
except ValueError:
    print("Error, ingrese un valor numérico")
    exit(0)

#ƒ(𝑡) es la cantidad de tilapias en el estanque después de 𝑡 días
F= round(P/ (1 + 11 * 2.71828 ** (-0.2 *t)), 2)
print("La cantidad estimada de tilapias vivas en el estanque después de", t, "días es de:", F)

#Pregunta 1b
try:
    M=int(input("Ingrese el peso promedio de una tilapia (en gramos):"))
except ValueError:
    print("Error, ingrese un valor numérico")
    exit(0)
#PT es el peso total del 50% de las tilapias en el estanque después de t días
PT = round((F*0.5)*M, 2)
print("Si se pesca la mitad de los peces después de", t, "días se obtendrá", PT, "gramos de carne de tilapia en total.")

#Pregunta 1c
try:
    G=int(input("Ingrese las ganancias del mes pasado:"))
except ValueError:
    print("Error, ingrese un valor numérico")
    exit(0)
#GT es la ganancia total de la empresa con el PT dado anteriormente convertido a kilos
GT = (PT/1000)*6000
B = GT >= G
print("¿Las ganancias de este mes superarían o igualarían a las del anterior?", B)

