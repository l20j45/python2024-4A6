#Programa para una fruteria basica
print ("Fruteria Don verduro")
descuento = 0

cantidadDeManzanas = float(input("Ingresa cuantas manzanas vendieron: "))
while cantidadDeManzanas != 0:
    costoDeManzanas = float(input("Ingresa cuanto valen las manzanas: "))
    total = cantidadDeManzanas * costoDeManzanas
    print(f"subTotal: {total}")
    if ( cantidadDeManzanas == 23 ):
        descuento = total *.20
        print (f"descuento secreto: {descuento}")
    elif ( cantidadDeManzanas > 10 ):
        descuento = total *.10
        print (f"descuento: {descuento}")
    else: 
        print("gracias por comprar con nosotros")
    print(f"el total a pagar es: {total-descuento} pesos")
    #YA TERMINO TODA LA LOGICA
    cantidadDeManzanas = float(input("Ingresa cuantas manzanas vendieron: "))
    
print("Adios, gracias por usar nuestro Sistema")