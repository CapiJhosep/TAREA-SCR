import os
os.system("cls")

monto = float( input("Ingrese el monto de la donación: "))

if monto >= 10000:
    salud = 10000 * 30/100
    comedor = 10000 * 50/100
    bolsa = 10000 - (salud + comedor)
elif monto < 10000:
    salud = 10000 * 25/100
    comedor = 10000 * 60/100
    bolsa = 10000 - (salud + comedor)

print( f"Se destina al Centro de Salud {salud} soles\nSe destina al Comedor de Niños {comedor} soles\nSe invierte en la Bolsa {bolsa} soles")