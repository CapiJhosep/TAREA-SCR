import os
os.system("cls")

cantidad = int( input("Ingrese la cantidad de unidad adquiridas: "))
precio = float( input("Ingrese el precio unitario: "))

importe = cantidad * precio
descuento1 = importe * 15/100
descuento2 = (importe - descuento1) * 15/100
importeFinal = importe - (descuento1 + descuento2)
descuentoTotal = descuento1 + descuento2

print( f"El importe de la compra es {importe: .2f}; el descuento es {descuentoTotal: .2f} y el importe a pagar es {importeFinal: .2f}")