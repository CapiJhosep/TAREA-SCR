# INVERTIR UNA CADENA

import os
os.system("cls")

def invertirCadenaRec(cadena):
    # Caso Base: si la cadena está vacía o tiene un solo carácter, se devuelve la misma cadena
    if len(cadena) == 0:
        return cadena
    else:
        # Caso Recursivo: invierte el resto de la cadena y añade el primer carácter al final
        return invertirCadenaRec(cadena[1:]) + cadena[0]

# Pidiendo Datos
texto = input( "Ingrese el texto: " )
resultado = invertirCadenaRec(texto)

# Mostrando Resultado
print(f"La cadena invertida de '{texto}' es '{resultado}'")
