import os
os.system("cls")


edad1 = int( input("Ingrese la primera edad: "))
edad2 = int( input("Ingrese la segunda edad: "))
edad3 = int( input("Ingrese la tercera edad: "))

if edad1 >= edad2 and edad1 >= edad3:
    print( f"La edad mayor es {edad1}")
elif edad2 >= edad1 and edad2 >= edad3:
    print( f"La edad mayor es {edad2}")
else:
    print( f"La edad mayor es {edad3}")