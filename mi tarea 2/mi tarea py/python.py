import operaciones
c = int(input("ingrese el primer numero"))
d= int(input("ingrese el segundo numero"))

resultado_suma = operaciones.suma(c, d)
print ("el resultado de su suma es", resultado_suma)

resultado_resta = operaciones.resta (c,d)
print ("el resultado de su resta es", resultado_resta)

resultado_multiplicacion= operaciones.multiplicacion (c)

import arreglos
nombre_reverso = arreglos.reverso ()