
e=0
while e<1:
    print ("se le solocitara que elija una opcion a realizar")
    print ("a:  area triangulo", "b: area del cuadrado", "c:  Area del rectangulo", "d: area del circulo", "f: salir", sep = "\n")
    
    opcion = (input("ingrese una letra "))
    match opcion:
        case "a":
            a = int(input("ingrese la base"))
            b= int(input("ingrese la altura"))
            p= a*b/2
            print("el area del triangulo es: ", p, "unidades cuadradas")

        case "b":
            a = int(input("ingrese el la medida de uno de los lados del cuadrado"))
            p = a*a
            print("el area del cuadrado es =", p)
        
        case "c":
            a = int(input("ingrese el valor de la base del rectangulo"))
            b= int(input("ingrese el valor de la altura del rectangulo"))
            p= a*b
            print ("el area del rectangulo es: ", p, "unidades cuadradas")

        case "d":
            a = int(input("ingrese el valor del radio de su circulo"))
            p = 3.1416*a*a
            print("el area del circulo es: ", p ,"unidades cuadradas")
        
        case "f":
            e = e + 1
print ("ok, gracias")
 