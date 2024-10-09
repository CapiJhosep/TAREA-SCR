import os
os.system("cls")

sexo = input("Ingrese su sexo (F/M): ")
edad = int( input("Ingrese su edad: "))

if sexo == "F" and edad < 23:
    print("Es de categoría FA")
elif sexo == "F" and edad >= 23:
    print("Es de categoría FB")
elif sexo == "M" and edad < 25:
    print("Es de categoría MA")
elif sexo == "M" and edad >= 25:
    print("Es de categoría MB")

