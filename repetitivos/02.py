import os
os.system("cls")


# SOLUCIÓN CON FUNCIÓN
def multiplicar(multiplicando, multiplicador):
    producto = 0
    while  multiplicador > 0:
        multiplicador -= 1               # multiplicador = multiplicador + 1
        producto += multiplicando       # producto = producto + multiplicando
    return producto

multiplicando = int( input("Multiplicando: ") )
multiplicador = int( input("Multiplicador: ") )

print( f"El Producto es { multiplicar(multiplicando, multiplicador) }" )


# SOLUCIÓN CON WHILE
multiplicando = int( input("Multiplicando: ") )
multiplicador = int( input("Multiplicador: ") )

producto = 0
while  multiplicador > 0:
    multiplicador -= 1               
    producto += multiplicando        

print( f"El Producto es {producto}" )


# SOLUCIÓN CON FUNCIÓN RECURSIVA
def multiplica(multiplicando, multiplicador):
    if multiplicador == 1: return(multiplicando)
    return multiplicando + multiplica(multiplicando, multiplicador - 1)

multiplicando = int( input("Multiplicando: ") )
multiplicador = int( input("Multiplicador: ") )

print( f"El Producto es { multiplica(multiplicando, multiplicador) }" )