 #Actividad 3 semana 12
print ("se le solicitará un numero entero positivo")
n = int(input (" ingrese un número entero positivo "))
numero = 0
for i in range (1,n):
    if n % i == 0:
        numero += i

if numero == n:
    print ("el numero", n, "es un número perfecto")
else:
    print( "el número", n, "no es un número perfecto")
