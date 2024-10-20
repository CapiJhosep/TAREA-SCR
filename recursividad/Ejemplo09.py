# HALLAR Y MOSTAR LA CANTIDAD DE PERMUTACIONES

import os
os.system("cls")

def permutacionRec(cadena):
    # Caso base: si la cadena es de longitud 1, solo hay una permutación
    if len(cadena) == 1:
        return [cadena]
    
    # Lista para almacenar todas las permutaciones
    resultado = []
    
    # Caso Recursivo: Recorremos cada letra de la cadena
    for i in range( len(cadena) ):
        # Extraemos la letra actual
        letra = cadena[i]
        
        # Resto de la cadena sin la letra actual
        resto = cadena[: i] + cadena[i + 1:]
        
        # Generamos recursivamente todas las permutaciones del resto de la cadena
        for permutacion in permutacionRec(resto):
            resultado.append(letra + permutacion)
    
    return resultado

# Pidiendo Datos
cadena = input( "Ingrese la cadena: " )
resultado = permutacionRec(cadena)

# Mostrando Resultado
print( f"Las permutaciones de '{cadena}' son:" )
for permutacion in resultado:
    print(permutacion)
