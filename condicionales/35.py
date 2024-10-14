import os
os.system("cls")

codigo = int( input("Ingrese el código: ") )

if codigo % 2 == 0 and codigo % 3 == 0 and codigo % 5 == 0:
    empleado = "Administrativo"
elif codigo % 3 == 0 and codigo % 5 == 0 and not codigo % 2 == 0:
    empleado = "Directivo"
elif codigo % 2 == 0 and not codigo % 3 == 0 and not codigo % 5 == 0:
    empleado = "Vendedor"
else:
    empleado = "Seguridad"
    
print( f"El còdigo es {codigo}" )
print( f"El tipo de empleado es: {empleado}" )