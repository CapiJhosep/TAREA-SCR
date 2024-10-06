import os
os.system("cls")

pTramo = int( input("Ingrese el primer tramo en km: ") )
sTramo = int( input("Ingrese el segundo tramo en ft: ") )
tTramo = int( input("Ingrese el tercer tramo en millas: ") )

pM = pTramo * 1000
sM = sTramo / 3.2808
tM = tTramo * 1609.34
metros = pM + sM + tM

pY = pTramo / 1093.61
sY = sTramo * 3
tY = tTramo / 1760
Yardas = pY + sY + tY

print( f"La longitud total recorrida en metros es de {metros: .2f}m y en yardas es de {Yardas: .2f}yd" )