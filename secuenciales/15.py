import os
os.system("cls")

dol1 = float( input("Monto aportado de Juan: "))
dol2 = float( input("Monto aportado de Rosa: "))
sol = float( input("Monto aportado de Daniel: "))

dol3 = sol / 3
capital = dol1 + dol2 + dol3
porJ = (dol1 * 100) / capital
porR = (dol2 * 100) / capital
porD = (dol3 * 100) / capital

print( f"El Capital total es {capital: .2f} dólares" )
print( f"El porcentaje aportado de Juan es {porJ: .2f}%" )
print( f"El porcentaje aportado de Rosa es {porR: .2f}%" )
print( f"El porcentaje aportado de Daniel es {porD: .2f}%" )