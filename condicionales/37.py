import os
os.system("cls")

Pamela = int( input("Los votos de Pamela: ") )
Carol = int( input("Los votos de Carol: ") )
Fanny = int( input("Los votos de Fanny: ") )

total = Pamela + Carol + Fanny
paraGanar = total // 2 + 1

if Pamela >= paraGanar:
    resultado = "Gana en la primera vuelta: Pamela"
elif Carol >= paraGanar:
    resultado = "Gana en la primera vuelta: Carol"
elif Fanny >= paraGanar:
    resultado = "Gana en la primera vuelta: Fanny"    
elif (Pamela == Carol == Fanny) or \
    (Pamela == Carol and Carol > Fanny) or \
    (Pamela == Fanny and Fanny > Carol) or \
    (Carol == Fanny and Fanny > Pamela):
        resultado = "Empate: Elección anulada"
elif Pamela > Carol and Pamela > Fanny:
    if Carol > Fanny:
        resultado = "Pasan a la segunda vuelta: Pamela y Carol"
    else:
        resultado = "Pasan a la segunda vuelta: Pamela y Fanny"
elif Carol > Pamela and Carol > Fanny:
    if Pamela > Fanny:
        resultado = "Pasan a la segunda vuelta: Carol y Pamela"
    else:
        resultado = "Pasan a la segunda vuelta: Carol y Fanny"
elif Fanny > Pamela and Fanny > Carol:
    if Pamela > Carol:
        resultado = "Pasan a la segunda vuelta: Fanny y Pamela"
    else:
        resultado = "Pasan a la segunda vuelta: Fanny y Carol"

print(resultado)