import os
os.system("cls")

tardanza = int( input("Ingrese sus minutos de tardanza: ") )
obs = int( input("Ingrese la cantidad de observaciones: ") )

if tardanza == 0:
    punT = 10
elif 1 <= tardanza <= 2:
    punT = 8
elif 3 <= tardanza <= 5:
    punT = 6
elif 6 <= tardanza <= 9:
    punT = 4
else: punT = 0

if obs == 0:
    punO = 10
elif obs == 1:
    punO = 8
elif obs == 2:
    punO = 5
elif obs == 3:
    punO = 1
else: punO = 0

puntaje = punT + punO

if puntaje < 11:
    bonificacion = puntaje * 2.5
elif 11 <= puntaje <= 13:
    bonificacion = puntaje * 5.0
elif 14 <= puntaje <= 16:
    bonificacion = puntaje * 7.5
elif 17 <= puntaje <= 19:
    bonificacion = puntaje * 10.0
elif 20 <= puntaje:
    bonificacion = puntaje * 12.5
    
print( f"El puntaje es: {puntaje} puntos" )
print( f"La bonificación es: {bonificacion: .2f} soles" )