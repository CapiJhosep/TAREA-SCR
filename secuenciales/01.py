import os
os.system("cls")

varones = int( input("Ingrese la cantidad de varones: ") )
mujeres = int( input("Ingrese la cantidad de mujeres: ") )

total = varones + mujeres
porVar = (varones*100.0)/total
porMuj = (mujeres*100.0)/total

print( f"El porcentaje de varones es de {porVar: .2f}% y de mujeres es de {porMuj: .2f}%" )