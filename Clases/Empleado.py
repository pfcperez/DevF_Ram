# -*- coding: utf-8 -*-

class Empleado(object):
    monto_para_aumento = 1.04
    numero_de_empleados = 0
    def __init__(self, nombre, apellido, salario):
        self.nombre = nombre
        self.apellido = apellido
        self.email = nombre+"."+apellido+"@company.com"
        self.salario = salario

    def muestra_nombre_completo(self):
        return "{} {}".format(self.nombre, self.apellido)

    def obtener_salario(self):
        return self.salario

    def aplicar_aumento(self):
        return self.salario *self.monto_para_aumento

class Utilerias(object):

    def __init__(self, seguro_social, tiempo_experiencia):
        self.seguro_social = seguro_social
        self.tiempo_experiencia = tiempo_experiencia

    def mostrar_informacion(self):
        print "La informacion extra es seguro social {} y años de experiencia {}".format(self.seguro_social, self.tiempo_experiencia)


class Developer(Empleado,Utilerias):
    monto_para_aumento = 1.10

    def __init__(self, nombre, apellido, salario,seguro_social, tiempo_experiencia, lenguaje_programacion):
        Empleado.__init__(nombre, apellido, salario)
        Utilerias.__init__(seguro_social,tiempo_experiencia)
        self.lenguaje_programacion = lenguaje_programacion


    def informacion_general(self):
        print "El empleado {} {} esta registrado como programador. Tiene un salario de {} y el lenaguje dominante es {}".format(self.nombre, self.apellido, self.salario, self.lenguaje_programacion)


developer1 = Developer("Ramiro","Perez",34000,"78787845","4","Python")

developer1.informacion_general()

