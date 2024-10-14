import os
os.system("cls")

horas = float( input("Ingrese las horas de ausencia: ") )
tornillosDefectuosos = int( input("Ingrese la cantidad de tornillos defectuosos: ") )
tornillosNoDefectuosos = int( input("Ingrese la cantidad de tornillos no defectuosos: ") )

eficiencia = 5

if horas <= 1.5 and tornillosDefectuosos < 300 and tornillosNoDefectuosos > 10000:
    eficiencia = 20
elif horas <= 1.5 and tornillosDefectuosos < 300:
    eficiencia = 12
elif horas <= 1.5 and tornillosNoDefectuosos > 10000:
    eficiencia = 13
elif tornillosDefectuosos < 300 and tornillosNoDefectuosos > 10000:
    eficiencia = 15
elif horas <= 1.5:
    eficiencia = 7
elif tornillosDefectuosos < 300:
    eficiencia = 8
elif tornillosNoDefectuosos > 10000:
    eficiencia = 9

print( f"El grado de eficiencia del operario es: {eficiencia}" )