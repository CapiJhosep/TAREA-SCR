import os
os.system("cls")

monto = float( input("Ingrese el monto vendido: ") )
sueldo = 600
comision = monto * 0.15
sueldoBruto = sueldo + comision

if sueldoBruto > 1800:
    descuento = sueldoBruto * 0.1
else: descuento = sueldoBruto * 0.05

sueldoNeto = sueldoBruto - descuento

if monto > 1000:
    polos = 3
else: polos = 1

print( f"El Sueldo Bruto es {sueldoBruto: .2f} soles" )
print( f"El Descuento es {descuento: .2f} soles" )
print( f"El Sueldo Neto es {sueldoNeto: .2f} soles" )
print( f"Los Polos obsequiados son {polos}" )




