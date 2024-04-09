try:
  P=int(input("Ingrese la capacidad del estanque:"))
except ValueError:
  print("Error, la capacidad máxima de peces debe ser un valor numérico entero")
  exit(0)

try:
  t=int(input("Inserte el tiempo en días para estimar la cantidad de tilapias en el estanque:"))
except ValueError:
  print("Error, el tiempo en días debe ser un valor numérico")
  exit(0)
F = P/(1+11*2.71828**(-0.2*t))
print("La cantidad estimada de tilapias vivas en el estanque después de", t, "dias es de", round (F,2),"tilapias")
try:
  m=float(input("Inserte el peso promedio de una tilapia (kg) :"))
except ValueError: 
  print("Error al leer el peso de la tilapia: debe ser un número")
  exit(0)

peso_mitad_tilapias = F * 0.5 * m
print("Si se pesca el 50% de los peces después de", t, "dias, se obtendrán", round(peso_mitad_tilapias,2),"kg de tilapia")
try:
  G=int(input("Inserte las ganancias del mes pasado:"))
except ValueError:
  print("Error, ingrese un valor numérico")
  exit(0)
Ganancias= peso_mitad_tilapias * 6000
if Ganancias > G:
  print("¿Las ganancias de este mes superarían o igualarían a las del anterior? true")
elif Ganancias < G:
  print("¿Las ganancias de este mes superarían o igualarían a las del anterior? false")