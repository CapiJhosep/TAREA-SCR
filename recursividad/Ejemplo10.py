# HALLAR EL LOGARITMO DE UN NÚMERO

import os
os.system("cls")
import math

def logaritmoRec(a, b):
    # Caso Base: Verificamos que la base sea mayor que 0 y diferente de 1
    if b <= 0 or b == 1:
        print( "La base debe ser mayor que 0 y diferente de 1." )
    else:
        # Caso Recursivo: Calculamos el logaritmo en base b utilizando el cambio de base
        return math.log(a) / math.log(b)


# Pidiendo Datos
numero = int( input( "Introduce el número del logaritmo: " ) )
base = int( input( "Introduce la base del logaritmo: " ) )
resultado = logaritmoRec(numero, base)

# Mostrando Resultado
print( f"El logaritmo de {numero} en base {base} es: {resultado: .2f}" )
