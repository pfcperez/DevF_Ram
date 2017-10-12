"""
Definir una funcion max que tome como argumento dos numeros y devuelva el mayor de ellos
"""

class My_Max():

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def max(self):
        maximo = 0
        if self.num1 > self.num2:
            maximo = self.num1
            print ("El numero mayor es {}".format(maximo))
        elif self.num2 > self.num1:
            maximo = self.num2
            print ("El numero mayor es {}".format(maximo))
        elif self.num1 == self.num2:
            maximo = self.num1
            print("Los numeros {} son iguales".format(maximo))




numero = My_Max(20, 89)
numero.max()