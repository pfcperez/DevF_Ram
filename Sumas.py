
class Operaciones_Listas():

    def __init__(self):
        self.lista = []
        self.total = 0
        self.mult = 1

    def sumar_lista(self):

        for i in self.lista:

            self.total += i
        print("El total de la suma es {}".format(self.total))

    def multiplicar_lista(self):
        for a in self.lista:
            #print (a)
            self.mult = self.mult * a
        print("El total de la multiplicacion es {}".format(self.mult))

    def pedir_valores(self):

        print("Escribe 4 valores")
        for i in range(0,4):
            temp = int(input("Escibe el valor {} ".format(i + 1)))
            self.lista.append(temp)

oper = Operaciones_Listas()
oper.pedir_valores()
oper.sumar_lista()
oper.multiplicar_lista()







