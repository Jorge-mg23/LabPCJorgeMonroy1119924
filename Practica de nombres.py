print (" se lo solicitara el nombre de 5 personas mas adelante")
nombres= []
i=1
while i <=5:
    nombre= str(input("ingrese un nombre"))
    nombres.append(nombre)
    i=i+1
p = 1
for x in nombres:
    print("nombre", p, "es", x)
    p = p+1
