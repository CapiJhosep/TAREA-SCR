import os
os.system("cls")

numero = int( input("Ingrese su número obtenido: "))
monto = float( input("Ingrese el monto de la compra: "))

if numero % 2 == 0 and numero >= 100:
    descuento = 15
else: descuento = 5

print( f"El número de la tarjeta es {numero}" )
print( f"El monto de la compra es {monto: .2f} soles" )
print( f"El descuento es del {descuento}%" )