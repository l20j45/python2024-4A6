import os

def saludo(nombre, edad):
    if(nombre == "raul"):
        print("Hola raul")
    else :
        print("no saludo")
    if(edad > 18) :
        print("Ya te duelen las rodillas")
    else :
        print("aun no")
        
def suma(numero1, numero2):
    total = numero1 + numero2
    return total

def inicio():
    os.system('cls' if os.name == 'nt' else 'clear')         
    print("Hola".center(50,"="))
    
inicio()

respuesta = suma(5,8)
print(respuesta)
print(suma(5,8))
