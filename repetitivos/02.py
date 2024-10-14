import os
os.system("cls")

multiplicando = int( input("Multiplicando: ") )
multipicador = int( input("Multiplicador: ") )

producto = 0
while  multipicador > 0:
    multipicador -= 1               # multiplicador = multiplicador + 1
    producto += multiplicando        # producto = producto + multiplicando

print( f"El Producto es {producto}" )