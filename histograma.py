

class Histograma():

    def __init__(self, lista):
        self.lista = lista
        self.lista2 = []

    def imprimir(self):
        temp = []

        for i in self.lista:
            #print (i)

            for a in range(0,i):
                temp.append('*')
               
            self.lista2.append(temp)
            for t in self.lista2:
                print(t)






pilon = Histograma([8,4,9])
pilon.imprimir()

