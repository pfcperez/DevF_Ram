class Encuenta_Vocal():

    def __init__(self):
        self.texto =""
        self.vocal = False

    def revisar(self):
        self.texto= input("Cual es el caracter:? ")

        if self.texto in ("aeiou"):
            self.vocal = True
        else:
            self.vocal = False

        print("{}".format(self.vocal))





vocal = Encuenta_Vocal()
vocal.revisar()