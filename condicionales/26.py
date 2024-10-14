import os
os.system("cls")

monto = float( input("Ingrese el monto de la compra: ") )

if monto > 5000:
    porcentaje = 0.3
else: porcentaje = 0.2

prestamo = monto * porcentaje
interes = prestamo * 0.1
montoTotal = prestamo + interes
montoPropio = monto - prestamo

print( f"El préstamo es de {prestamo: .2f} soles y el interés es de {interes: .2f} soles" )
print( f"El monto a pagar con dinero propio es: {montoPropio: .2f} soles" )
print( f"El monto del préstamo es: {montoTotal: .2f} soles" )