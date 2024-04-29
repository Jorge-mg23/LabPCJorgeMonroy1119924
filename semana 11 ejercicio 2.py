print("Semana 11. ")
n2= int(input("ingrese un número mayor a 0"))
if(n2 <= 0):
    print("error el número debe ser mayor a 0")

#Ejercicio A
CalculoA = 0
for xA in range (1 , n2 + 1):
    CalculoA += 1 / xA
print ("el resultado de A es:", CalculoA)

#Ejercico B
def sum_sequence(N):
    total = 0
    for n in range(1, N+1):
        term = 1 / (2**n)
        total += term
    return total

# Ejemplo de uso
N = 5  # Número de términos
result = sum_sequence(N)
print(f"La suma de la secuencia hasta el término {N} es: {result}")

#Ejercicio C
def sum_series():
    x = int(input("Ingrese el valor de x: "))
    a = int(input("Ingrese el valor de a: "))
    n = int(input("Ingrese el valor de n: "))
    
    total = 0
    for i in range(n+1):
        term = a * (x**(n-i))
        total += term
    
    return total

result = sum_series()
print(f"La suma de la serie es: {result}")