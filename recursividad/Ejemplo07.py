# CONTAR LA CANTIDAD DE VOCALES EN UNA CADENA

import os
os.system("cls")

def contarVocalesRec(cadena):
    # Definir las vocales
    vocales = "aeiouAEIOU"
    
    # Caso base: si la cadena está vacía, no hay más vocales que contar
    if not cadena:
        return 0
    
    # Caso Recursivo: Verificar si el primer carácter es una vocal
    if cadena[0] in vocales:
        # Contar esta vocal y llamar recursivamente con el resto de la cadena
        return 1 + contarVocalesRec(cadena[1:])
    else:
        # Llamar recursivamente con el resto de la cadena sin contar esta letra
        return contarVocalesRec(cadena[1:])

# Pidiendo Datos
texto = input( "Ingrese el texto: " )
resultado = contarVocalesRec(texto)

# Mostrando Resultado
print(f"La cantidad de vocales en la cadena es: {resultado}")
