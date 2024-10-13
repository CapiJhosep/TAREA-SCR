import os
os.system("cls")

sueldoBasico = 250
monto = int( input("Ingrese la cantidad del monto vendido: ") )

if monto > 0:
    if monto <= 5000:
        comision = 0.05 * monto
    elif 5000 < monto <= 10000:
        comision = 0.08 * monto
    elif 10000 < monto <= 20000:
        comision = 0.1 * monto
    else: comision = 0.15 * monto
else: print("Ingrese una cantidad positiva")

sueldo = sueldoBasico + comision

if sueldo > 3500:
    descuento = 0.15 * sueldo
else: descuento = 0.08 * sueldo

sueldoBruto = sueldo + comision
sueldoNeto = sueldoBruto - descuento

print( f"El Sueldo Bruto es: {sueldoBruto: .2f} soles" )
print( f"El Sueldo Neto es: {sueldoNeto: .2f} soles" )
print( f"El Descuento es: {descuento: .2f} soles" )
print( f"La Comisión es: {comision: .2f} soles" )