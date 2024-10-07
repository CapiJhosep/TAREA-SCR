import os
os.system("cls")

número = int( input("Número: "))

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"] 
if número >= 1 and número <= 7: print( dias[número - 1])
else: print("Error")

# if número == 1: print("Es Lunes")
# elif número == 2: print("Es Martes")
# elif número == 3: print("Es Miércoles")
# elif número == 4: print("Es Jueves")
# elif número == 5: print("Es Viernes")
# elif número == 6: print("Es Sábado")
# elif número == 7: print("Es Domingo")
# else: print("Error")