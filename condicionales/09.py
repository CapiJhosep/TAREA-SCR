import os
os.system("cls")

codigo = int( input("Ingrese el código del producto: ") )
cantidad = int( input("Ingrese la cantidad de productos: ") )

if 100 < codigo < 105:
    if codigo == 101:
        precio = 17
    elif codigo == 102:
        precio = 25
    elif codigo == 103:
        precio = 16
    elif codigo == 104:
        precio = 27
else: print("No existe el código del producto")

pago = cantidad * precio

if cantidad > 0:
    if 1 <= cantidad <= 10:
        descuento = pago * 0.05
    elif 11 <= cantidad <= 20:
        descuento = pago * 0.08
    elif 21 <= cantidad <= 30:
        descuento = pago * 0.1
    else: descuento = pago * 0.13
else: print("La cantidad no puede ser menor de 0")  

totalPago = pago - descuento 

print( f"El importe es {pago} soles" )
print( f"El descuento es {descuento} soles" )
print( f"Pago total es {totalPago} soles" )    
