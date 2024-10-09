import os
os.system("cls")

num1 = int( input("Ingrese el primer número de 3 cifras: "))
num2 = int( input("Ingrese el segundo número de 3 cifras: "))


cif1Num1 = num1 // 100
cif2Num1 = (num1 // 10) % 10
cif3Num1 = num1 % 10

cif1Num2 = num2 // 100
cif2Num2 = (num2 // 10) % 10
cif3Num2 = num2 % 10

nuevoNum1 = cif3Num2 * 100 + cif2Num1 * 10 + cif1Num2
nuevoNum2 = cif3Num1 * 100 + cif2Num2 *10 + cif1Num1


print( f"Los nuevos numeros son {nuevoNum1} y {nuevoNum2}")