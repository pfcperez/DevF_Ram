# -*- coding: utf-8 -*-
"""
Kata #1
Crea un programa que le pregunte al usuario su nombre y edad.
Imprime un mensaje dirigido a él,
que le diga el año en que cumplirá cien anioos
"""
import datetime

# def ask_questions():
#     nombre = raw_input("Hola!!!. Cual es tu nombre?: ")
#     edad = raw_input("Cual es tu edad?: ")
#     edad_entera = int(edad)
#     ahora = datetime.datetime.now()
#     hundred = 100 -edad_entera
#     print "Hola {} tu cumpliras tu centenario en el año {}".format(nombre, hundred+ahora.year)
# ask_questions()


"""
Kata #2
Pídele un número al usuario.
Dependiendo de si el número es par o impar,
imprime el mensaje apropiado al usuario
"""
# def par_impar():
#     numero = int(raw_input("Cual es el numero a revisar?: "))
#     div = numero % 2
#     if div == 0:
#         print "El {} numero es par".format(numero)
#     else:
#         print "El {} numoero es impar".format(numero)
#
# par_impar()

"""
Kata #3
Escribe un programa que tome una lista de números
(por ejemplo, a = [5, 10, 15, 20, 25]) y haz dos nuevas listas.
una que contenga sólo el primer y último número de la lista original
y otra que contenga todos los números intermedios
"""

def nuevas_listas():
    lista_original = []
    lista1 = []
    lista2 = []
    #num = int(raw_input( "Cuantos numeros quieres agregar?: "))
    for i in range(0,5):
        temp = raw_input("Ingresa el numero: ")
        lista_original.append(temp)

    lista1.append(lista_original[0])
    lista1.append(lista_original[-1])

    for t in range(1,4):
        lista2.append(lista_original[t])


    print lista1
    print lista2


    #print lista_original



nuevas_listas()

"""
Kata #4
Escribe una función que tome una lista de números y un número.
La función debe checar si el número pertenece a la lista y devolver
el booleano correspondiente
"""
# def chequear_numero():
#     lista = []
#
#     for i in range(0,5):
#         temp = int(raw_input("Ingresa el numero en lista: "))
#         lista.append(temp)
#
#     numero = int(raw_input("Cual es el numero que vas a revisar: "))
#
#     if numero in lista:
#         print "El numero {} esta en la lista".format(numero)
#     else:
#         print "El numero {} no se encuetra en la lista".format(numero)
#
# chequear_numero()
