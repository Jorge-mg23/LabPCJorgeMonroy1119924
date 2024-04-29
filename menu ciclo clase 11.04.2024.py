print ("menu:", "1. ver cual es el mayor entre 5 números", "2. Mostrar las tablas de multiplicar del 1 al 10", sep="\n")
numero = input("elija una opción ")
n1 = 0
match numero:
    case "1":

        i = 0
        numeros = []

        while (i<5):
            n1 = int(input ("ingrese un número "))

            numeros.append (n1)
            numeros.sort()
            i=i+1
        print (numeros)
        print ("el numero mayor es el que esta al final de la lista")

    case "2":
        print("   tablas1", " tablas2", " tablas3", " tablas4","tablas5", "tablas6", "tablas7", "tablas8", " tablas9", "tablas10")
        titulocol = ""            
        for col in range (1,11):
            titulocol += str(col) + "\t"


        textofila = ""        
        for fila in range (1,11):
            textofila += str(fila) + "\t"

            for col in range (1,11):
                textofila += str(fila * col) + "\t"
            print(textofila)
            textofila = ""
