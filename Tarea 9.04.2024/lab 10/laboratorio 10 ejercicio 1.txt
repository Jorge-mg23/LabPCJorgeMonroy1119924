print("Semana No.10: Ejercicio 1")
mesEntrada = int(input("Ingrese un número del 1 al 12"))
mesSalida = ""

match mesEntrada:
   case 1:
       mesSalida = "Enero"
   case 2:
       mesSalida = "Febrero"
   case 3:
       mesSalida = "Marzo"
   case 4:
       mesSalida = "Abril"
   case 5:
       mesSalida = "Mayo"
   case 6:
       mesSalida = "Junio"
   case 7:
       mesSalida = "Julio"
   case 8:
       mesSalida = "Agosto"
   case 9:
       mesSalida = "Septiembre"
   case 10:
       mesSalida = "Octubre"
   case 11:
       mesSalida = "Noviembre"
   case 12:
       mesSalida = "Diciembre"

print("Mes:", mesSalida)
