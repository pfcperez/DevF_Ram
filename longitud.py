"""
Definir una funcion que calcule la longitud de una lista o una cadena
"""

class longitud_texto():

    def __init__(self):
        self.cadena = ""
        self.contador = 0

    def contar(self):
        self.cadena = input("Cual es la cadena a contar?: ")
        for i in self.cadena:
            self.contador += 1

        print ("La cadena es de {}".format(self.contador))

cont = longitud_texto()
cont.contar()

