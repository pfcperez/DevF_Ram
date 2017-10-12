# -*- coding: utf-8 -*-
"""
Encapsulacion
Se consigue a menudo mediante la ocultacion de informacion
En otras palabras es impedir el acceso a los metodos o variables del objecto,
para que solo se puedan usar dentro de la instancia del objecto.
- Variables públicas
- Variables privadas: __nombre
- Metodos públicos
- Metodos privados
"""
# class Persona(object):
#     def __init__(self, nombre, email, age):
#         self.nombre = nombre
#         self.__email = email
#         self.__age = age
#
#     def get_name(self):
#         pass
#
#     def update_email(self, new_email):
#         self.__email = new_email
#
#     def email(self):
#         return self.__email
#
#     def __show_age(self):
#         return self.__age
#
#     def show_age(self):
#         return self.__get_age()
#
#     def __get_age(self):
#         return self.__age
#
#     def update_email(self, new_email, algo_mas):
#         self.__email = new_email + algo_mas
#
#
#
# tk = Persona('Ram','ram@text.com',18)
# print tk.email()

"""
Clase Figura, que saca el area
Clase hija triangulo, cuadrado, circulo
"""
from math import pi

class Figura(object):
    def __init__(self, valor):
        # type: (object) -> object
        self.valor = valor

    # def check(self):
    #     raise NotImplementedError("Necesario implementar metodo check")

class Triangulo(Figura):

    def __init__(self, valor, valor2):
        super(Triangulo, self).__init__(valor)
        self.valor2 = valor2

    def area(self):
        return (self.valor * self.valor2) /2

class Circulo(Figura):
    def __init__(self,valor):
        super(Circulo, self).__init__(valor)

    def area(self):
        return (pi * self.valor**2)

class Cuadrado(Figura):
    def __init__(self, valor, valor2):
        super(Cuadrado, self).__init__(valor)
        self.valor2 = valor2

    def area(self):
        return self.valor * self.valor2

triangulo = Triangulo(12, 8)
print "Area triangulo"
print triangulo.area()

circulo = Circulo(34)
print "Area circulo"
print circulo.area()

cuadrado = Cuadrado(34, 23)
print "Area cuadrado"
print cuadrado.area()


"""
Metodo abstracto, sin cuerpo, una solo una accion

raise NotImplementedError("Subclss must implement abstract method")
"""