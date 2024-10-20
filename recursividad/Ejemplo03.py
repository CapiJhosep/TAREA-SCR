# POTENCIA DE UN NÚMERO

import os
os.system("cls")

def potenciaRec(base, exponente):
    # Caso base: cualquier número elevado a la 0 es 1
    if exponente == 0:
        return 1
    else:
        # Caso Recursivo: base * potencia(base, exponente - 1)
        return base * potenciaRec(base, exponente - 1)

# Pidiendo Datos
base = int( input( "Ingrese la base: " ) )
exponente = int( input( "Ingrese el exponte: " ) )
resultado = potenciaRec(base, exponente)

# Mostrando Resultado
print(f"{base} elevado a la {exponente} es {resultado}")
