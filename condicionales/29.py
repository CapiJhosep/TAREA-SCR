import os
os.system("cls")

horas = int( input("Ingrese las horas trabajadas: ") )
pago = float( input("Ingrese el pago por hora: ") )

if horas <= 48:
    sueldo = horas * pago
else: 
    horasExtras = horas - 48
    sueldo = (horas * 48) + (horasExtras * pago * 1.2)
    
if sueldo > 1500:
    descuento = sueldo * 0.11
else: descuento = 0

total = sueldo - descuento

print( f"Las horas trabajadas son {horas} horas" )
print( f"El pago por hora es de {pago: .2f} soles" )
print( f"El sueldo bruto es {sueldo: .2f} soles" )
print( f"El descuento es {descuento: .2f} soles" )
print( f"El pago total es {total: .2f} soles" )