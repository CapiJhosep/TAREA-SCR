import os
os.system("cls")

hijos = int( input("¿Cuántos hijos tiene? ") )
sueldo = float( input("¿Cuál es su sueldo? ") )

if hijos > 1:
    bonificacion = (sueldo * 0.125) + (40 * hijos)
else: bonificacion = sueldo * 0.1

sueldoNeto = sueldo + bonificacion

print( f"La Bonificación es: {bonificacion: .2f} soles" )
print( f"El Suledo Neto es: {sueldoNeto: .2f} soles " )