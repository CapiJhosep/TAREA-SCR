import os
os.system("cls")

peso = float( input("Ingrese su peso en kg: ") )
estatura = float( input("Ingrese su estatura en m: ") )
IMC = peso / (estatura ** 2)

if IMC <= 20:
    gradoObesidad = "Delgado"
elif 20 < IMC <= 25:
    gradoObesidad = "Normal"
elif 25 < IMC <= 27:
    gradoObesidad = "Sobrepeso"
elif 27 < IMC:
    gradoObesidad = "Obesidad"
    
print( f"El IMC de la perosona indica: {gradoObesidad}" )

