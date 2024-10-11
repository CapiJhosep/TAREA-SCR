import os
os.system("cls")

base = float( input("Ingrese la medida de la base: ") )
altura = float( input("Ingrese la medida de la altura: ") )

area = base * altura
perimetro = 2 * (base + altura)

print( f"El Área del rectángulo es {area} y su Perímetro es {perimetro}" )