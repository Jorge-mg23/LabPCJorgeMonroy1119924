print("semana No.12: Ejercicio 1")
print ("Menú", "a. sumatoria", "b. factorial", "c. Tablas de multiplicar", "d. número perfecto", sep="\n")

opcion = input("ingrese su opción")

match opcion:
    case "a":
        n = int(input("ingrese un número entero positivo"))
        if(n <=0):
            print("Error, número debe ser mayor a cero")
        
        contador = 1
        sumatoria = 0
        while(contador <= n):
            sumatoria += contador
            contador += 1

        print(f"Sumatoria: {sumatoria}")
        
    case "b":
        def factorial(n):
            if n == 0:
                return 1
            else:
             return n * factorial(n-1)

        # Solicitar al usuario el número N
        n = int(input("Ingrese un número entero positivo: "))

        if n < 0:
            print("Error: El número debe ser positivo.")
        else:
            result = factorial(n)
            print(f"El factorial de {n} es: {result}")

    case "c":
        titulocol = ""            
        for col in range (1,11):
            titulocol += str(col)
        print(titulocol)

        textofila = ""        
        for fila in range (1,11):
            textofila += str(fila) + "\t"

            for col in range (1,11):
                textofila += str(fila * col) + "\t"
            print(textofila)
            textofila = ""