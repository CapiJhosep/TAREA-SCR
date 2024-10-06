import os
os.system("cls")

radio = float( input("Ingrese el radio del cilindro: "))
altura = float( input("Ingrese la altura del cilindro: "))
π = 3.1416

aBase = π * (radio ** 2)
aLateral = 2 * π * radio * altura
aTotal = 2 * aBase * aLateral

print( f"El Área de la Base es {aBase: .2f}; el Área Lateral es {aLateral: .2f} y el Área Total es {aTotal: .2f}" )