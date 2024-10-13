import os
os.system("cls")

unidadesA = int( input("Ingrese la cantidad de unidades del Producto A: ") )
unidadesB = int( input("Ingrese la cantidad de unidades del Producto B: ") )
precioA = 25
precioB = 30

importeBrutoA = unidadesA * precioA
importeBrutoB = unidadesB * precioB
importeBruto = importeBrutoA + importeBrutoB

if unidadesA > 50:
    descuentoA = importeBrutoA * 0.15
else: descuentoA = 0

if unidadesB > 60:
    descuentoB = importeBrutoB * 0.1
else: descuentoB = 0

descuento = descuentoA + descuentoB
pago = importeBruto - descuento

print( f"El Importe Bruto es: {importeBruto: .2f} soles" )
print( f"El Descuento es: {descuento: .2f} soles" )
print( f"El Pago es: {pago: .2f} soles" )