# HALLAR EL MCD DE DOS NÚMEROS

import os
os.system("cls")

def mcdRec(a, b):
    # Caso Base: si b es 0, el MCD es a
    if b == 0:
        return a
    else:
        # Caso Recursivo: llamar a mcd con (b, a % b)
        return mcdRec(b, a % b)

# Pidiendo Datos
num1 = int( input( "Ingrese el primer número: " ) )
num2 = int( input( "Ingrese el segundo número: " ) )
resultado = mcdRec(num1, num2)

# Mostrando Resultado
print(f"El MCD de {num1} y {num2} es {resultado}")