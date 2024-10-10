import os
os.system("cls")

doncaion = float( input("Ingrese el monto de la donación total: "))

centroSalud = doncaion * 25/100
comedorInfantil = doncaion * 35/100
escuelaInfantil = doncaion * 25/100
asciloAncianos = doncaion - (centroSalud + comedorInfantil + escuelaInfantil)

print( f"Al Centro de Salud: {centroSalud} \nAl Comedor  Infantil: {comedorInfantil} \nA la Escuela Infantil: {escuelaInfantil} \nAl Ascilo de Ancianos: {asciloAncianos}") 