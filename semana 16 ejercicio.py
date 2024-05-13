#semana 16
import random
print ("semana 16: ejercicio 1")
lista = []
for x in range(10):
    lista.append (random.randint(1,10))
opcion = "0"
while (opcion != 'e'):
    print ("menú")
    print ("a. mostrar números", "b. promedio", "c. Longitud", "d. posicion")
    opcion = input("ingrese su opción")

    match opcion:
        case 'a':
            for x in range (len(lista)):
                print (f"No. {x}: {lista[x]}")
        case 'b':
            print ("promedio")
            sumatoria = 0
            for x in range (len(lista)):
                sumatoria += lista[x]
            promedio = sumatoria / len(lista)
            print (f"promedio", {promedio})

        case 'c':
            print ("la longitud es:", len (lista))

        case "d":
            suma_pares = sum(lista[i] for i in range(len(lista)) if i % 2 == 0)
            suma_impares = sum(lista[i] for i in range(len(lista)) if i % 2 != 0)
            print(f"La suma de posiciones pares es: {suma_pares}")
            print(f"La suma de posiciones impares es: {suma_impares}")

print("Semana No. 16 Ejercicio 2") 
mayor ="0"
cantFilas= int(input("Ingrese la cantidad de filas"))
cantCols= int(input("Ingrese la cantidad de Cols"))

matriz = [[0 for x in range(cantCols)]for y in range(cantFilas)]
mayor = 0
for xFilas in range (cantFilas):
    for xCols in range (cantCols):
        matriz[xFilas][xCols]= random.randint(0,1000)
        if (matriz[xFilas][xCols] > mayor):
            mayor = matriz [xFilas][xCols]
print(matriz)
print (f"el número mayor es: {mayor}")
