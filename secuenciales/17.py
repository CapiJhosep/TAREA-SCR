import os
os.system("cls")

doncaion = float( input("Ingrese el monto de la donación total: "))

centroSalud = doncaion * 25/100
comedorInfantil = doncaion * 35/100
escuelaInfantil = doncaion * 25/100
asciloAncianos = doncaion - (centroSalud + comedorInfantil + escuelaInfantil)

print( f"Al Centro de Salud: {centroSalud} soles" ) 
print( f"Al Comedor  Infantil: {comedorInfantil} soles" )
print( f"A la Escuela Infantil: {escuelaInfantil} soles" ) 
print( f"Al Ascilo de Ancianos: {asciloAncianos} soles" ) 