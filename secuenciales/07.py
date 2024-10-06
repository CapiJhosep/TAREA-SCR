import os
os.system("cls")

base = float( input("Ingrese la medida de la base: ") )
altura = float( input("Ingrese la medida de la altura: ") )

área = base * altura
perímetro = 2 * (base + altura)

print( f"El Área del rectángulo es {área} y su perímetro es {perímetro}" )