import os
os.system("cls")

precio = 20
unidades = int( input("Ingrese la cantidad de Unidades compradas: "))

compra = precio * unidades

if compra <= 500: 
    descuento = compra * 0.12
elif compra <= 700:
    descuento = compra * 0.14
else: descuento = compra * 0.16

if unidades <= 50:
    caramelos = 5
elif unidades <= 100:
    caramelos = 10
else: caramelos = 15

print( f"El importe es {compra: .2f} soles" ) 
print( f"El descuento es {descuento} soles" )
print( f"El total a pagar {(compra - descuento): .2f} soles" ) 
print( f"Los caramelos obsequiados son {caramelos}" )