import os
os.system("cls")

metros = int( input("Ingrese la cantidad de metros: ") )

centímetros = metros * 100
pulgadas = metros * 39.3701 
pies = metros * 3.2808
yardas = metros * 1.0936

print( f"{metros}m es igual a {centímetros: .2f}cm; {pulgadas: .2f}in; {pies: .2f}ft y {yardas: .2f}yd" )