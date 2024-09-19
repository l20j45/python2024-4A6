""" 
Nuestro Programa va a convertir de 
Dolares a pesos, 
de pesos a Dolares, 
de Dolares a Euros,  
Euros a Dolares,  
Pesos a Euros,  
Euros a pesos


El programa de las verduras, hacerlo para que se puedan vender 5 verduras o frutas diferentes
manzanas
mandarinas
peras
cebollas
tomates


17/09/2024
si no lo entregan el taller no se va a acreditar


"""
def pedirDivisa (moneda1, moneda2):
    return float(input(f"cuantos {moneda1} deseas Cambiar a {moneda2}: "))

def mostrarResultado(valorAConvertir, monedaDeOrigen, monedaDeSalida, conversionDeDivisa):
    print(f"tus {valorAConvertir} {monedaDeOrigen} valen : {(conversionDeDivisa)*valorAConvertir} {monedaDeSalida}")

PESO  = 1
DOLAR = 19.53
EURO = 21.62
DOLARAEURO = 0.90
EUROADOLAR = 1.11
opcionElegida = 1

while (opcionElegida != 0):
    print("""Casa de divisas
    1.- Dolares a pesos 
    2.- Pesos a Dolares 
    3.- Pesos a Euros  
    4.- Euros a pesos
    5.- Dolares a Euros  
    6.- Euros a Dolares
    0.- Salir""")
    opcionElegida = int(input("Ingresa tu opcion: "))
    if opcionElegida == 1 :
        monedaDeOrigen = "Dolares"
        monedaDeSalida = "Pesos"
        valorAConvertir = pedirDivisa(monedaDeOrigen, monedaDeSalida)
        mostrarResultado(valorAConvertir,monedaDeOrigen,monedaDeSalida, DOLAR/PESO)
    elif opcionElegida == 2 :
        monedaDeOrigen = "Pesos"
        monedaDeSalida = "Dolares"
        valorAConvertir = pedirDivisa(monedaDeOrigen, monedaDeSalida)
        mostrarResultado(valorAConvertir,monedaDeOrigen,monedaDeSalida, PESO/DOLAR)
    elif opcionElegida == 3 :
        monedaDeOrigen = "Pesos"
        monedaDeSalida = "Euros"
        valorAConvertir = pedirDivisa(monedaDeOrigen, monedaDeSalida)
        mostrarResultado(valorAConvertir,monedaDeOrigen,monedaDeSalida, PESO/EURO)
    elif opcionElegida == 4 :
        monedaDeOrigen = "Euros"
        monedaDeSalida = "Pesos"
        valorAConvertir = pedirDivisa(monedaDeOrigen, monedaDeSalida)
        mostrarResultado(valorAConvertir,monedaDeOrigen,monedaDeSalida, EURO/PESO)
    elif opcionElegida == 5 :
        monedaDeOrigen = "Dolares"
        monedaDeSalida = "Euros"
        valorAConvertir = pedirDivisa(monedaDeOrigen, monedaDeSalida)
        mostrarResultado(valorAConvertir,monedaDeOrigen,monedaDeSalida, DOLARAEURO)
    elif opcionElegida == 6 :
        monedaDeOrigen = "Euros"
        monedaDeSalida = "Dolares"
        valorAConvertir = pedirDivisa(monedaDeOrigen, monedaDeSalida)
        mostrarResultado(valorAConvertir,monedaDeOrigen,monedaDeSalida, EUROADOLAR)
    else: 
        print("opcion no valida")
print("Gracias por usar nuestro programa")
    