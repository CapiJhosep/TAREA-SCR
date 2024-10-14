import os
os.system("cls")

hora = int( input("Introduce la Hora (0 - 24): ") )

if 0 <= hora <= 24:
    if hora == 0:
        hora1 = 12
        periodo = "AM"
    elif hora < 12:
        hora1 = hora
        periodo = "AM"
    elif hora == 12:
        hora1 = 12
        periodo = "PM"
    else:
        hora1 = hora - 12
        periodo = "PM"
else: print("Hora Inválida")

print( f"Son las {hora1}{periodo}" )