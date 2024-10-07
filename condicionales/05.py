import os
os.system("cls")

numero = input("Ingrese el número: ")
lista = []
if len(numero) == 4:
    lista.append(numero)
    print(lista)
else:
    print("Error")