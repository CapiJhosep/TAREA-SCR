import os
os.system("cls")

categoria = input("Ingrese su categoría ( A - B - C - D): ")
promedio = float( input("Ingrese su promedio: ") )

if categoria == "A":
    pension = 550
elif categoria == "B":
    pension = 500
elif categoria == "C":
    pension = 450
elif categoria == "D":
    pension = 400

if promedio <= 13.99:
    descuento = 0
elif 14 <= promedio <= 15.99:
    descuento = pension * 0.1
elif 16 <= promedio <= 17.99:
    descuento = pension * 0.12
elif 18 <= promedio <= 20:
    descuento = pension * 0.15
    
pago = pension - descuento

print( f"Pensión actual es: {pension: .2f} soles" )
print( f"Descuento es: {descuento: .2f} soles" )
print( f"Pago total es: {pago: .2f} soles" )