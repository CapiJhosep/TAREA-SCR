import os
os.system("cls")

cantidad = int(input("Ingrese la cantidad de dinero en soles: "))

billetes200 = cantidad // 200; cantidad %= 200
billetes100 = cantidad // 100; cantidad %= 100
billetes50 = cantidad // 50; cantidad %= 50
billetes20 = cantidad // 20; cantidad %= 20
billetes10 = cantidad // 10; cantidad %= 10
monedas5 = cantidad // 5; cantidad %= 5
monedas2 = cantidad // 2; cantidad %= 2
monedas1 = cantidad

print(f"Billetes de 200: {billetes200}" )
print( f"Billetes de 100: {billetes100}" )
print( f"Billetes de 50: {billetes50}" )
print( f"Billetes de 20: {billetes20}" )
print( f"Billetes de 10: {billetes10}" )
print( f"Monedas de 5: {monedas5}" )
print( f"Monedas de 2: {monedas2}" )
print( f"Monedas de 1: {monedas1}" )