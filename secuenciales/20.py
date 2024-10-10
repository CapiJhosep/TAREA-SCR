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

print(f"Billetes de 200: {billetes200}\nBilletes de 100: {billetes100}\nBilletes de 50: {billetes50}\nBilletes de 20: {billetes20}\nBilletes de 10: {billetes10}\nMonedas de 5: {monedas5}\nMonedas de 2: {monedas2}\nMonedas de 1: {monedas1}")