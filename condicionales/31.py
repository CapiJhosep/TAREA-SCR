import os
os.system("cls")

horas = int( input("Ingrese la cantidad de horas trabajadas: ") )
categoria = input("Ingrese su categoría ( A - B - C - D): ") 

if categoria == "A":
    pago = 21
elif categoria == "B":
    pago = 19.50
elif categoria == "C":
    pago = 17
elif categoria == "D":
    pago = 15.50
    
sueldo = horas * pago

if sueldo > 2500:
    descuento = sueldo * 0.2
else: descuento = sueldo * 0.15

sueldoNeto = sueldo - descuento

print( f"El sueldo bruto es: {sueldo: .2f} soles" )
print( f"El descuento es: {descuento: .2f} soles" )
print( f"El sueldo neto es: {sueldoNeto: .2f} soles" )