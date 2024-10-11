import os
os.system("cls")

cantidad = int( input("Ingrese la cantidad de artículos que desee comprar: "))

if cantidad > 51:
    precio = cantidad * 23 
    descuento =  15/100 * precio
    total = precio - descuento
elif 25 < cantidad <= 50:
    precio = cantidad * 25
    descuento = 5/100 * precio
    total = precio - descuento
else:
    precio = cantidad * 27
    descuento = 5/100 * precio
    total = precio - descuento
    
print( f"El importe de la compra es {precio: .2f} soles" )
print( f"El descuento es de {descuento: .2f} soles" ) 
print( f"Total a pagar es de {total: .2f} soles" )