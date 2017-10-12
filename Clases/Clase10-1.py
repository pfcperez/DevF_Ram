# class Figura(object):
#     def __init__(self, valor):
#         self.valor = valor
#
#     def test(self):
#         raise NotImplementedError("test class")
#
# class Triangulo(Figura):
#
#     def __init__(self, valor, valor2):
#         super(Triangulo, self).__init__(valor)
#         self.valor2 = valor2
#
#     def area(self):
#         return (self.valor * self.valor2) /2
#
# class Circulo(Figura):
#     def __init__(self,valor):
#         super(Circulo, self).__init__(valor)
#
#     def area(self):
#         return (3.1416 * self.valor**2)
#
# class Cuadrado(Figura):
#     def __init__(self, valor, valor2):
#         super(Cuadrado, self).__init__(valor)
#         self.valor2 = valor2
#
#     def area(self):
#         return self.valor * self.valor2
#
# triangulo = Triangulo(12, 8)
# print "Area triangulo"
# print triangulo.area()
#
# circulo = Circulo(34)
# print "Area circulo"
# print circulo.area()
#
# cuadrado = Cuadrado(34, 23)
# print "Area cuadrado"
# print cuadrado.area()


class parent(object):
    def __init__(self, valor1):
        self.valor1 = valor1

    def talk(self):
        raise NotImplementedError("Error ")

class child(parent):
    def __init__(self,valor1):
        super(child, self).__init__(valor1)

    def hola(self):
        print "hola"

test = child("yt")
test.hola()

"""
Parsear un archivo JSON. Para abstraer en clases, la informacion contenida
en el archivo
"""
import json
json_file = open("marvel.json").read()
json_data = json.loads(json_file)
print json_data['data']['results'][0]['name']




