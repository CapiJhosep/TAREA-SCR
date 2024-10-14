import os
os.system("cls")

mes = int(input("Ingrese el número del mes (1-12): "))
año = int(input("Ingrese el año: "))

bisiesto = (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", 
                "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if bisiesto:
    dias[1] = 29

if 1 <= mes <= 12:
    print( f"El mes es {meses[mes - 1]} y tiene {dias[mes - 1]} días." )
    if bisiesto:
        print( f"El año {año} es bisiesto." )
    else:
        print( f"El año {año} no es bisiesto." )
else:
    print("El número del mes es inválido")