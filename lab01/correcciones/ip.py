try: 
  P=int(input("Ingrese la capacidad del estanque:"))  # cantidad max de tilapias en el estanque
except ValueError:
  print("Error al leer la capacidad del estanque: Ingrese un valor  numérico" )
  exit(0)

try:
   T=int(input("Ingrese el tiempo en días para estimar la cantidad de tilapias en el estanque :")) # tiempo a calcular la cantidad de tilapias
except ValueError:
  print("Error: Ingrese un valor numérico" )
  exit(0)

F = P / (1 + 11 * 2.71828**(-0.2 * T)) # la cantidad de tilapias luego de (t) días
print("La cantidad estimada de tilapias vivas en el estanque después de" , T, "días es de", round (F,2))


try:
   M=float(input("Ingrese el peso promedio de una tilapia (kg):" )) # peso promedio en kg de cada tilapia
except ValueError:
  print("Error: Ingrese un valor numérico" ) 
  exit(0)

peso_mitad_tilapias = (F / 2) * M
# G=F/2
# K=G/M
print("Si se pesca el 50% de los peces después de" , T, "días, se obtendrá" , round(peso_mitad_tilapias,2), "kg de carne de tilapia en total.")


# Calcular las ganancias del mes ACTUAL multiplicando el peso de la mitad de las tilapias por 6000 (el precio por kg de tilapia)
ganancias = peso_mitad_tilapias * 6000

# Recibir del usuario las ganancias del mes pasado
try:
  G=int(input("Inserte las ganancias del mes pasado (colones):")) # ganancias del mes/pesca pasada
except ValueError:
  print("Error: Ingrese un valor numérico" )
  exit(0)
  

print(" Las ganancias obtenidas con la pesca anterior son mayores o iguales al mes anterior")
print(ganancias >= G)
