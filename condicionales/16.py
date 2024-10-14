import os
os.system("cls")

ingreso = float( input("Ponga su ingreso mensual: ") )
casa = float( input("Ingrese el monto de la casa: ") )

if ingreso < 1250.00:
    inicial = casa * 15/100
    mensual = (casa - inicial) / 120
elif ingreso >= 1250.00:
    inicial = casa * 30/100
    mensual = (casa - inicial) / 75
    
print( f"La cuota inicial es {inicial} soles y el monto mensual es {mensual: .2f} soles")