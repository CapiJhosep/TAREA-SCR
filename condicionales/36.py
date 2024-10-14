import os
os.system("cls")

cuadernos = int( input("Ingrese la cantidad de cuadernos adquiridos: ") )
lapiceroFaber = 0
lapiceroLucas = 0    
lapiceroPilot = 0
    
if cuadernos < 12:
    lapiceroFaber = 0
    lapiceroLucas = 0    
    lapiceroPilot = 0
elif 12 <= cuadernos < 24:
    lapiceroLucas = cuadernos // 4
elif 24 <= cuadernos < 36:
    lapiceroFaber = (cuadernos // 4) * 2
else:
    lapiceroPilot = (cuadernos // 4) * 2
    lapiceroFaber = cuadernos // 6
    lapiceroLucas = cuadernos // 12
    
print( "Se obsequian: ")
print( f"{lapiceroLucas} Lapiceros Lucas" )
print( f"{lapiceroFaber} Lapiceros Faber" )
print( f"{lapiceroPilot} Lapiceros Pilot" )