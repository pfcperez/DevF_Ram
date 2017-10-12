import datetime
class Transaccion(object):

    def __init__(self, comprador,vendedor,rfc,direccion,ciudad,cantidad,descripcion,precio):
        self.fecha = datetime.datetime.now()
        self.comprador = comprador
        self.vendedor = vendedor
        self.rfc = rfc
        self.direccion = direccion
        self.ciudad = ciudad
        self.cantidad = cantidad
        self.precio = precio
        self.descripcion = descripcion
        self.total = float(self.precio * self.cantidad)
        self.impuesto = (self.total * self.cantidad) * .16
        self.status_transaccion = "En proceso"

    def imprmir_datos_cliente(self):
        return "Nombre: {}, Direccion: {}, RFC: {}, Ciudad: {}".format(self.comprador, self.direccion, self.rfc, self.ciudad)

    def modificar_datos_cliente(self):
        print "Los datos actuales del cliente son"
        print(self.imprmir_datos_cliente())
        print "-----------------------------"
        self.comprador = raw_input("Nombre: ")
        self.direccion = raw_input("Direccion: ")
        self.ciudad = raw_input("Ciudad ")
        self.rfc = raw_input("RFC: ")
        print(self.imprmir_datos_cliente())


    def cancelar_transaccion(self):
        self.status_transaccion = "Cancelada"
        print "El estatus de la transaccion es {}".format(self.status_transaccion)



    # def calcular_impuestos(self):
    #     impuesto = self.total * .16
    #     return "El IVA es de {}".format(impuesto)

    def descripcion_transaccion(self):
        print "El producto que se compro fue " + self.descripcion
        print "Cantidad: {}".format(self.cantidad)
        print "Precio: {}".format(self.precio)
        print "Impuesto: {}".format(self.impuesto)


class Vender(Transaccion):
    def __init__(self):
        super(Vender, self).__init__(comprador,vendedor,rfc,direccion,ciudad,cantidad,descripcion,precio)
        self.fecha_envio = datetime.datetime.now()

    def confirmar_embarque(self):
        print "La mercancia se embarco {}".format(self.fecha_envio)







tenis = Transaccion("Ramiro Perez","Juan Lopez","PEZT898934","Prolongacion Mariano Otero","Zapopan",1,"Nike shoes",800)


#tenis.descripcion_transaccion()



#tenis.cancelar_transaccion()
#tenis.modificar_datos_cliente()
#print(tenis.calcular_impuestos())
