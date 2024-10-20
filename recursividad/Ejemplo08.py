# VERIFICAR SI UNA PALABRA ES O NO PALÍNDROMO

import os
os.system("cls")

def palindromoRec(palabra):
    # Caso Base: Si la palabra tiene 0 o 1 letra, es un palíndromo
    if len(palabra) <= 1:
        return True
    # Caso Recursivo: Verifica si la primera y última letra son iguales
    elif palabra[0] != palabra[-1]:
        return False
    else:
        # Llama a la función de forma recursiva, eliminando la primera y última letra
        return palindromoRec(palabra[1:-1])

# Pidiendo Datos
palabra = input( "Ingrese la palabra: " )

# Mostrar Resultado
if palindromoRec(palabra):
    print( f"'{palabra}' es un palíndromo." )
else:
    print( f"'{palabra}' no es un palíndromo." )