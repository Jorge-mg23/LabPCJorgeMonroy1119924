print ("menu:", "1. ver cual es el mayor entre 5 números", "2. Mostrar las tablas de multiplicar del 1 al 10", sep="\n")
numero = input("elija una opción ")

match numero:
    case "1":
        n1 = int(input ("ingrese el primer número "))
        n2 = int(input ("ingrese el segundo número "))
        n3 = int(input ("ingrese el tercer número "))
        n4 = int(input ("ingrese el cuarto número "))
        n5 = int(input ("ingrese el quinto número "))