import os
os.system("cls")

monto = float( input("Ingrese el monto total vendido: "))

sueldo = 500.00
comision = monto * 9/100
sueldoBruto = sueldo + comision
descuento = sueldoBruto * 11/100
sueldoNeto = sueldoBruto - descuento

print( f"La Comisión es {comision: .2f} soles" )
print( f"El Sueldo Bruto es {sueldoBruto: .2f} soles" )
print( f"El Descuento es {descuento: .2f} soles" )
print( f"El Sueldo Neto es {sueldoNeto: .2f} soles" )