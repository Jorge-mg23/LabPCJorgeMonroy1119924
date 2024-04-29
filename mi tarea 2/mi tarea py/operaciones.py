def suma(a, b):
    return (a + b)

def resta (a, b):
    if a > b:
        return (a - b)
    else:
        print("el primer numero debe ser mayor al segundo")

def multiplicacion (a):
    print ("la tabla del", a, "es:")
    i = 1
    for x in range (1,11) :
     print (a, "por", i, "es", a*x)
     i = i+1
    
