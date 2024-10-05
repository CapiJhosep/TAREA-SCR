import os
os.system("cls")

radio = float( input("Ingrese el radio del cilindro: "))
altura = float( input("Ingrese la altura del cilindro: "))
π = 3.1416

área = 2 * π * ( radio + altura )
volumen = π * (radio**2) * altura

print( f"El Área del cilindro es {área: .2f} y el Volumen es {volumen: .2f}")