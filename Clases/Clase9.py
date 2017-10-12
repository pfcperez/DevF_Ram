"""
Paradigma de programacion para resolver un problema
Pensar que todo es un objeto

Abstraer cosas del mundo real en objetos y propiedades

Instancia o Objecto

Nombres de clases se esriben con convencion Camel Case
"""
class Empleado(object):
    #variable de clase
    #Constante para todoas las instancias
    monto_para_aumento = 1.04
    numero_de_empleados = 0

    #metodo init va a correr automaticamente cda que creamos una nueva instancia

    def __init__(self, nombre, apellido, salario):
        #self -> current instance
        self.nombre = nombre
        self.apellido = apellido
        self.email = nombre +"."+"apellido" + "@company.com"
        self.salario = salario

        Empleado.numero_de_empleados += 1

    def nombre_completo(self):
        return "{} {}".format(self.nombre, self.apellido)

    def obtener_salario(self):
        return self.salario

    def aplicar_aumento(self):
        self.salario = int(self.salario * self.monto_para_aumento)

# qa = Empleado("chester","cheetos",8900)
# developer = Empleado("mark","sanchez",654456)

#imprime la informacion en un diccionario
# print qa.__dict__
# print developer.__dict__
class Utilerias(object):

    def __init__(self, informacion, seguro_social, experiencia):
        self. informacion = informacion
        self.seguro_social = seguro_social
        self.experiencia = experiencia

    def imprime_todo(self):
        print "El empleado {}, su seguro social es {}, y tiene {} anios de experiencia ".format(self.informacion, self.seguro_social,self.experiencia)


class Developer(Empleado, Utilerias):
    monto_para_aumento = 1.10

    def __init__(self, nombre, apellido, salario, informacion, seguro_social, experiencia, prog_lang):
        super(Developer, self).__init__(nombre, apellido, salario)
        super(Developer, self).__init__(informacion,seguro_social, experiencia)
        self.prog_lang = prog_lang

    def toda_info(self):
        print "Hola!!"


empleado1 = Empleado("hugo","mecalco",90000)
developer1 = Developer("gerardo","lopez",9086,"No tiene problemas con perfil", "67679328943", "19", "python")


"""
Clase de tipo television
5 atributos
Imprimir tamano, marca y precio
Y por cada que se cree una instacia aumentar el contador
"""

# class Television:
#     numero_tvs = 0
#
#     def __init__(self, marca, tamano, precio, numero_serie):
#         self.marca = marca
#         self.tamano = tamano
#         self.precio = precio
#         self.numero_serie = numero_serie
#
#         Television.numero_tvs += 1
#
#     def imprime_marca(self):
#         return self.marca
#
#     def imprime_tamano(self):
#         return  self.tamano
#
#     def imprime_precio(self):
#         return self.precio
#
#     def imprime_todo(self):
#
#         return "La tv de la marca {} es de {} pulgadas, tiene un precio de {}".format(self.marca, self.tamano, self.precio)
#
#     def precio_con_iva(self):
#         return "El precio con iva para la tv {} es de $ {}".format(self.marca, self.precio*1.16)
#
#
# sony = Television("Sony","32",5000, "hjjhfsd3",)
# toshiba = Television("Toshiba","50",8900,"jkhjhjhfsd")
#
# lista = []
# print sony.__dict__
# print toshiba.__dict__
#
# print sony.imprime_todo()
# print toshiba.imprime_todo()
#
# print sony.precio_con_iva()
# print toshiba.precio_con_iva()
#
# print toshiba.numero_tvs






