# HALLAR LOS DIVISORES DE UN NÚMERO

import os
os.system("cls")

def generarDivisoresRec(num, divisor=1):
    # Caso Base: si el divisor es mayor que n, se termina la recursión
    if divisor > num:
        return []
    
    # Caso Recursivo: Si n es divisible por el divisor, incluirlo en la lista
    if num % divisor == 0:
        return [divisor] + generarDivisoresRec(num, divisor + 1)
    else:
        return generarDivisoresRec(num, divisor + 1)

# Pidiendo Datos
numero = int( input( "Ingrese el número: " ) )
resultado = generarDivisoresRec(numero)

# Mostrando Resultado
print(f"Los divisores de {numero} son: {resultado}")
