import os
os.system("cls")

num1 = int( input("Ingrese el primer número: "))
num2 = int( input("Ingrese el segundo número: "))
num3 = int( input("Ingrese el tercer número: "))

if num1 < num2 < num3:
    print( f"El número intermedio es {num2}")
elif num3 < num2 < num1:
    print( f"El número intermedio es {num2}")
elif num2 < num1 < num3:
    print( f"El número intermedio es {num1}")
elif num3 < num1 < num2:
    print( f"El número intermedio es {num1}")
elif num1 < num3 < num2:
    print( f"El número intermedio es {num3}")
elif num2 < num3 < num1:
    print( f"El número intermedio es {num3}")
