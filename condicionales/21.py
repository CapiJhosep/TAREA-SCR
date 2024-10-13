import os
os.system("cls")

numero = int( input("Introduce su número asignado: ") )
numeroStr = str(numero)
estado = int( numeroStr[0] )
edad = int( numeroStr[1:3] )
sexo = int( numeroStr[3] )

if estado == 1:
    estadoCivil = "Soltero"
elif estado == 2:
    estadoCivil = "Casado"
elif estado == 3:
    estadoCivil = "Divorciado"
elif estado == 4:
    estadoCivil = "Viudo"
else:
    estadoCivil = "Desconocido"

if sexo == 1:
    sexoStr = "Masculino"
elif sexo == 2:
    sexoStr = "Femenino"
else:
    sexoStr = "Desconocido"
    
print( f"El Estado Civil es: {estadoCivil}" )
print( f"La Edad es: {edad}" )
print( f"El Sexo es: {sexoStr}" )