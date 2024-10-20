# SUMA DE LOS DÍGITOS DE UN NÚMERO

import os
os.system("cls")

def sumaDigitosRec(n):
    # Caso Base: si n es menor que 10, se devuelve el mismo número
    if n < 10:
        return n
    else:
        # Caso Recursivo: se suma el último dígito y se llama de nuevo con el resto de los dígitos
        return n % 10 + sumaDigitosRec(n // 10)

# Pidiendo Datos
numero = int( input( "Ingrese un número: " ) )
resultado = sumaDigitosRec(numero)

# Mostrando Resultado
print(f"La suma de los dígitos de {numero} es {resultado}")




