import os
os.system("cls")

import math

print("ax^2 + bx + c")

a = int( input("Ingrese el valor de a: "))
b = int( input("Ingrese el valor de b: "))
c = int( input("Ingrese el valor de c: "))

discriminante =  (b ** 2) - (4 * a * c) 

if discriminante >= 0:
    raíz = math.sqrt(discriminante)
    x1 = (-b + raíz) / (2 * a)
    x2 = (-b - raíz) / (2 * a)
    print( f"La primera raíz es {x1} y la segunda raíz es {x2}")
else:
    print("La ecuación no tiene solución")