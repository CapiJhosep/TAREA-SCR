import os
os.system("cls")

# SOLUCIÓN CON FUNCIÓN
def factorial(num):
    factoria = 1
    while num > 1:
        factoria *= num 
        num -= 1

    return factoria

numero = int( input("Ingrese un número entero: ") )

print( f"El factorial de {numero} es { factorial(numero) }")


# SOLUCIÓN CON WHILE
numero = int( input("Ingrese un número entero: ") )

factoria = 1
while numero > 1:
    factoria *=  numero 
    numero -= 1

print( f"El factorial del número es {factoria}")


# SOLUCIÓN CON FUNCIÓN RECURSIVA
def factorialR( num ):
    if num == 1: return 1
    return num * factorialR(num - 1)

numero = int( input("Ingrese un número entero: ") )  

print( f"El factorial de {numero} es { factorialR(numero) }")