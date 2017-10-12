#print ("Hello World")

#print ("Ramiro Perez")
#print ("Chester and Brownie")
#say_hello = "Hello world"

#print (say_hello)

#se convierte con str el valor myInt a string
#myInt = 20
#bolean = True
#print(str(myInt) + say_hello )
#print(str(bolean))

#tipos de datos
#bool = True
#name = "Craig"
#age = 26
#pi = 3.14159
"""
Comentarios multilinea
"""
""" 
def happyBirthdayEmiliy():
    print ("Feliz cumple")
    print ("Feliz cumple")
    print ("Felicidades a ti!!!")

happyBirthdayEmiliy()
"""

"""

def cumple(nombre, mensaje):
    print ("Feliz cumple " + nombre )
    print ("Felicidades a ti!!")
    print ("Te mando un " + mensaje)
    #print (nombre + "\n" + mensaje)

nombre = "Ramiro"
mensaje = "abrazo"

#cumple(nombre, mensaje)
def primera():
    print("Hoy es Martes")
    print ("Septiembre 19")

def segunda():
    primera()
    print ("Comienza la segunda funcion")

segunda()
"""

"""
# Llamando una funcion a otra

def informacion(nombre, anio):
    edad = 2017 - anio
    return "Hola " + nombre + " tu edad es " + str(edad) + " anios"

def mensaje_a_enviar():
    print ("El mensaje de hoy es....")
    print ("Todo cambia y se transforma instante a instante")
    print  (informacion("Ramiro", 1981))

mensaje_a_enviar()

def tercera(nombre, apellido, edad):
    texto = "Tu nombre es {} {} y tu edad es {}".format(nombre,apellido,edad)
    print (texto)

tercera("Chester", "Zamo","10")

"""


#sentencias de control

def if_else_control():
    a = 10
    b = 9
    if a > b:
        print "{} es mayor a {} ".format(a,b)
    elif a == b:
        print "{} es igual a {} ".format(a,b)
    elif a < b:
        print "{} es menor a {} ".format(a,b)
    else:
        print("Verifica tus numeros")

if_else_control()

un_string = "Hola Ramiro Perez "

def tamano_string(string_size):

    if string_size > 10:
        print "string muy grande"
    else:
        print "nice"

tamano_string(len(un_string))

#ciclo while

count = 0
"""
while(count < 9):
    print "The count is ", count
    count = count + 1
"""

# Ciclos For
for x in range(0,3):
    print "We are in time %d" %(x)

