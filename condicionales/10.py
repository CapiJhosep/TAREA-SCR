import os
os.system("cls")

nota1 = float( input("Ingrese la nota 1: ") )
nota2 = float( input("Ingrese la nota 2: ") )
nota3 = float( input("Ingrese la nota 3: ") )
nota4 = float( input("Ingrese la nota 4: ") )
nota5 = float( input("Ingrese la nota 5: ") )

notaMenor = nota1
if nota2 < notaMenor:
    notaMenor = nota2
if nota3 < notaMenor:
    notaMenor = nota3
if nota4 < notaMenor:
    notaMenor = nota4
if nota5 < notaMenor:
    notaMenor = nota5

# Determinar la nota mayor
notaMayor = nota1
if nota2 > notaMayor:
    notaMayor = nota2
if nota3 > notaMayor:
    notaMayor = nota3
if nota4 > notaMayor:
    notaMayor = nota4
if nota5 > notaMayor:
    notaMayor = nota5

suma = nota1 + nota2 + nota3 + nota4 + nota5 - notaMenor - notaMayor
promedio = suma / 3

print(f"Nota eliminada (menor): {notaMenor}")
print(f"Nota eliminada (mayor): {notaMayor}")
print(f"Promedio aprobatorio: {promedio:.2f}")