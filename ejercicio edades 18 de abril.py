print ("Se le solicitaran 5 edades")
edades= []
i=1
while i <=5:
    edad= int(input("Ingrese una edad "))
    if edad <0 :
        print(" su edad no puede ser negativa")
        break
    else:
        edades.append(edad)
    i=i+1
p=1
for x in edades :
    print("la edad",p, "es",x)
    p=p+1
    