import os
os.system("cls")

dividendo = int( input("Dividendo: ") )
divisor = int( input("Divisor: ") )

cociente = 0
while dividendo >= divisor:
    cociente += 1               # cociente = cociente + 1
    dividendo -= divisor        # dividendo = dividendo - divisor

print( f"El Cociente es {cociente}" )
print( f"El Residuo es {dividendo}" )