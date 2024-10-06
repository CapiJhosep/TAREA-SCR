import os
os.system("cls")

gb = float( input("Ingrese la cantidad de Gigabytes: "))

mb = gb * 1024
kb = gb * 1048576
b = gb * 1073741824

print( f"{gb}gb es igual a: {mb}mb; {kb}kb; {b}b" )