import os
os.system("cls")

horasTrabajadas = float( input("Ingrese la cantidad de horas trabajadas: "))
tarifaHoraria = float( input("Ingrese la tarifa horaria: "))

sueldoBasico = horasTrabajadas * tarifaHoraria
bonificacion = sueldoBasico * 20/100
sueldoBruto = sueldoBasico + bonificacion
descuento = sueldoBruto * 10/100
sueldoNeto = sueldoBruto - descuento

print( f"El sueldo Básico es {sueldoBasico: .2f} soles" )
print( f"El sueldo Bruto es {sueldoBruto: .2f} soles" )
print( f"El sueldo Neto es {sueldoNeto: .2f} soles" )