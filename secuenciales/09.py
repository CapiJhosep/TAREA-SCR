import os
os.system("cls")

numero = int( input("Ingrese el número de 4 cifras: ") )

cifra1 = numero // 1000
cifra2 = (numero // 100) % 10
cifra3 = (numero // 10) % 10
cifra4 = numero % 10
suma = cifra1 + cifra2 + cifra3 + cifra4

print( f"El número es {numero} y la suma de cifras es {suma}" )