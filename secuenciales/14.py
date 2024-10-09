import os
os.system("cls")

import math

num1 = float( input("Ingrese la primera nota: "))
num2 = float( input("Ingrese la segunda nota: "))
num3 = float( input("Ingrese la tercera nota: "))
num4 = float( input("Ingrese la cuarta nota: "))
num5 = float( input("Ingrese la quinta nota: "))
notas = [num1, num2, num3, num4, num5]

orden = sorted(notas, reverse=True)
tresMayores = orden[:3]
promedio = sum(tresMayores) / 3

print( f"El promedio de las notas es {promedio}")