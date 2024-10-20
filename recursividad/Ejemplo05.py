# SUMA DE NÚMEROS CONSECUTIVOS (no necesariamente desde el 1)

import os
os.system("cls")

def sumaConsecutivosRec(num1, num2):
    # Caso Base: si a es igual a b, la suma es solo ese número
    if num1 == num2:
        return num1
    else:
        # Caso Recursivo: sumar a al resultado de la suma de los números entre a+1 y b
        return num1 + sumaConsecutivosRec(num1 + 1, num2)
    
# Pidiendo Datos
num1 = int( input( "Ingrese el número inicial: " ) ) 
num2 = int( input( "Ingrese el número final: " ) ) 
resultado = sumaConsecutivosRec(num1, num2)

# Mostrando Resultado
print(f"La suma de los números consecutivos de {num1} a {num2} es {resultado}")
