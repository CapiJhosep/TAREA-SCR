import os
os.system("cls")

curso = input("Ingrese el curso (Matemática, Física, Química): ")

pc1 = float(input("Ingrese la nota de la PC1: "))
pc2 = float(input("Ingrese la nota de la PC2: "))
pc3 = float(input("Ingrese la nota de la PC3: "))
ep = float(input("Ingrese la nota del Examen Parcial: "))
ef = float(input("Ingrese la nota del Examen Final: "))

if curso == "Matemática":
    notaFinal = pc1 * 0.10 + pc2 * 0.20 + pc3 * 0.10 + ep * 0.30 + ef * 0.30
elif curso == "Física":
    notaFinal = pc1 * 0.20 + pc2 * 0.20 + pc3 * 0.20 + ep * 0.20 + ef * 0.20
elif curso == "Química":
    notaFinal = pc1 * 0.10 + pc2 * 0.30 + pc3 * 0.10 + ep * 0.25 + ef * 0.25
else:
    print("Curso no válido. Ingrese Matemática, Física o Química.")
    exit()

condicion = "Aprobado" if notaFinal >= 13 else "Desaprobado"

print(f"\nEl promedio final del curso de {curso} es: {notaFinal:.2f}")
print(f"Condición: {condicion}")