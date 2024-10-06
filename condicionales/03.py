import os
os.system("cls")

ángulo = float( input("Ingresa la medida del ángulo: "))

if ángulo == 0:
    print("El ángulo es 'Nulo'")
elif 0 < ángulo < 90:
    print("El ángulo es 'Agudo'")
elif ángulo == 90:
    print("El ángulo es 'Recto'")
elif 90 < ángulo < 180:
    print("El ángulo es 'Obtuso'")
elif ángulo == 180:
    print("El ángulo es 'Llano'")
elif 180 < ángulo < 360:
    print("El ángulo es 'Cóncavo'")
elif ángulo == 360:
    print("El ángulo es 'Completo'")