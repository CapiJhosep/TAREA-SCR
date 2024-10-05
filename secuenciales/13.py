import os
os.system("cls")

import math

cat1 = float ( input("Ingrese el primer cateto del triángulo: ") )
cat2 = float ( input("Ingrese el segundo cateto del triángulo: ") )

hipotenusa = math.sqrt( (cat1 ** 2) + (cat2 ** 2) )

print( f"La Hipotenusa del triángulo es {hipotenusa}" )