import os
os.system("cls")

nota1 = float( input("Ingrese la nota del primer exámen: "))
nota2 = float( input("Ingrese la nota del segundo exámen: "))
nota3 = float( input("Ingrese la nota del tercer exámen: "))

propina1 = 20 + 5*3
propina2 = 20 + 5*2
propina3 = 20 + 5

if nota1 > 10.5 and nota2 > 10.5 and nota3 > 10.5:
    print( f"La propina mensual es {propina1}so")
elif (nota1 > 10.5 and nota2 > 10.5) or (nota1 > 10.5 and nota3 > 10.5) or (nota2 > 10.5 and nota3 > 10.5): 
    print( f"La propina mensual es {propina2}")
elif nota1 > 10.5: print( f"La propina mensual es {propina3}so")
elif nota2 > 10.5: print( f"La propina mensual es {propina3}so")
elif nota3 > 10.5: print( f"La propina mensual es {propina3}so")
else: print( "La propina mensual es 20so")