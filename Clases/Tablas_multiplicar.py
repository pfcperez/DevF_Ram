"""
def tablas():
    m = 1
    while m <11:
        print("Imprimiendo tabla del {}".format(m) )
        for a in range(0,11):
            valor = m * a
            print valor
        m += 1
tablas()
"""

def tablas():
    for mult in range(1,11):
        print("Imprimiendo tabla del {}".format(mult))
        for a in range(0,11):
            total = a * mult
            print total
tablas()