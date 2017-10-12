def funcion_de_tres():
    maximo = 0
    num1 = int(input("Cual es el primer numero?: "))
    num2 = int(input("Cual es el segundo numero?: "))
    num3 = int((input("Cual es el tercer numero?: ")))

    if num1 >= num2 and num1 >= num3:
        maximo = num1

    elif num2 >= num1 and num2 >= num3:
        maximo = num2
    elif num3 >= num1 and num3 >= num2:
        maximo = num3

    print ("El valor maximo de los tres es {}".format(maximo))

funcion_de_tres()
