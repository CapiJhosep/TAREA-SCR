import os
os.system("cls")

mate = float( input("Ingrese la nota de Matemática: ") )
fisica = float( input("Ingrese la nota de Física: ") )
promedio = (mate + fisica) / 2

if mate > 17:
    propinaM = mate * 3
else: propinaM = mate * 1

if fisica > 15:
    propinaF = fisica * 2
else: propinaF = fisica * 0.5

proinaTotal = propinaM + propinaF
print( f"La propina que recibió es {proinaTotal: .2f} soles" )

if promedio > 16:
    print("Recibió un reloj de obsequio")
else: print("No recibió ningún obsequio")

