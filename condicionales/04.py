import os
os.system("cls")

nota1 = float( input("Ingrese la primera nota: "))
nota2 = float( input("Ingrese la segunda nota: "))
nota3 = float( input("Ingrese la tercera nota: "))

if nota3 > 10:
    promedio = (nota1 + nota2 + (nota3 + 3)) / 3
else:
    promedio = (nota1 + nota2 + nota3) / 3

print( f"El promedio de sus notas es {promedio}")