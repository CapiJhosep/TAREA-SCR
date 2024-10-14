import os
os.system("cls")

monto = float( input("Introduce el monto vendido: ") )
sueldo = monto * 0.1

if monto > 5000:
    restante = monto - 5000
    bonificacion = (restante // 500) * 25
else: bonificacion = 0

sueldoTotal = sueldo + bonificacion

print( f"El sueldo del vendedor es: {sueldoTotal: .2f} soles" )