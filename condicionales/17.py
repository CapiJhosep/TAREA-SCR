import os
os.system("cls")

cantDocenas = int( input("Cantidad de docenas compradas: ") )
precio = float( input("Ingrese el precio por docena: ") )
pago = cantDocenas * precio

if cantDocenas >= 6:
    descuento = 15
else: descuento = 10

pagoTotal = pago - (pago * descuento/100)

if cantDocenas >= 30:
    lapiceros = (cantDocenas // 3) * 2
else: lapiceros = 0

print( f"El Monto de la compra es {pago: .2f} soles" )
print( f"El descuento es del {descuento}%" )
print( f"El Pago total es {pagoTotal: .2f} soles" )
print( f"Los laiceros obsequiados son {lapiceros}" )