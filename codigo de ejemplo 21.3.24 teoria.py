print("semana No. 11: Ejercicio 1")
n = int (input("ingrese un numero mayor 0"))

if (n<0):
    print ("Error, el número debe ser igual a 0")
    
 #definición de variables para la fibonacci
a=0
b=1
c=0
i=2

resultado = ""

if (n>0):
    resultado = str(a)

    if (n>1):
        resultado = resultado + "," + str(b)

    #Ciclo, se repite hasta que deje de cumplir la condición
    while(i<n):
        c=a+b
        resultado = resultado + "," + str(c)
        a=b
        b=c
        i = i + 1

    print(resultado)