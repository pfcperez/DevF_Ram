""""
Pseudocodigo
1 -recibir dinero, monto maximo es de 5
2 - Ver que productos alcanza

Costo de productos
2.5, 1.4, 4, 1.2
"""
def imprimir_Productos():
    print ("Papas Sabritas: $2.5")
    print ("Coca: $1.4")
    print ("Coca Familiar: $4")
    print ("Gansito: $1.2")

def calcular_Vuelto(monto, credito):
    vuelto = float (credito) - monto
    print ("Tu cambio es $", str(vuelto))



def iniciar():
    print ("Bienvenido al Vending machine, estos son los productos disponibles: ")
    imprimir_Productos()
    credit = raw_input("Credito a depositar: ")

    choice = raw_input("Cual es tu eleccion?: ")
    if choice == "Papas Sabritas":
        costo = 2.5
    elif choice == "Coca":
            costo = 1.4
    elif choice == "Coca Familiar":
        costo = 4
    elif choice == "Gansito":
        costo = 1.2

    calcular_Vuelto(costo, credit)

iniciar()

