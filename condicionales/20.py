import os
os.system("cls")

num1 = int( input("Ingrese el primer número: "))
num2 = int( input("Ingrese el segundo número: "))
num3 = int( input("Ingrese el tercer número: "))

if num1 < num2 < num3:
    print("Los números estan ordenados de forma ascendente")
elif num1 > num2 > num3:
    print("Los números estan ordenados de forma descendente")
else: print("Están en desorden")
