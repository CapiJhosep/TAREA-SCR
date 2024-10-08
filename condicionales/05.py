import os
os.system("cls")

numero = input("Ingrese el número: ")
lista = []

if __name__ == "__main__" and len(numero) == 4:
    lista.append(numero)
    num = numero
    orden = "".join(sorted(num))
    print(orden)
else: print("Error")