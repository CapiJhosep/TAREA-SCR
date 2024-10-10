import os
os.system("cls")

numero = input("Ingrese un número entero positivo de tres cifras: ")

if len(numero) == 3 and numero.isdigit():
    digito1 = int(numero[0])
    digito2 = int(numero[1])
    digito3 = int(numero[2])

    if digito1 + 1 == digito2 and digito2 + 1 == digito3:
        print("Las cifras están en orden ascendente.")
    elif digito1 - 1 == digito2 and digito2 - 1 == digito3:
        print("Las cifras están en orden descendente.")
    else:
        print("Las cifras no son consecutivas.")
else:
    print("Error: Debe ingresar un número entero positivo de tres cifras.")
    