def reverso ():
    print ("se le pedira su nombre")
    H = []
    x = list(input("ingrese su nombre"))

    H.append ((x))
    c=  len (x) 
    print (" la cantidad de letras de su nombre es", c)
    i= x[::-1]
    print ("tu nombre al reves es", i)

