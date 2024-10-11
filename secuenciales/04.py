import os
os.system("cls")

pies = int( input("Ingrese la cantidad de pies: ") )
pulgadas = int( input("Ingrese la cantidad de pulgadas: ") )

estatura = pies * 0.3048 + pulgadas * 0.0254

print( f"La estatura es {estatura} metros" )