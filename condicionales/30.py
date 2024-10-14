import os
os.system("cls")

cuota = float( input("Ingrese la cuota mensual: ") )
dia = int( input("¿Dentro de cuántos dias hará el pago? ") )

if dia <= 10:
    descuento = max(5, cuota * 0.02)
    pago = cuota - descuento
elif 10 < dia <= 20:
    descuento = 0
    pago = cuota
else: 
    recargo = max(10, cuota * 0.03)
    pago = cuota + recargo

print( f"El pago en el mes es {pago: .2f} soles" )    