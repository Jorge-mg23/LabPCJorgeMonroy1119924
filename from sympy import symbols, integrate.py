def case1():
    return (2+2+3+4+5+5+6+6+7+7+5+3+4+3+2+2+4+5+5)*2
def case2():
    return 2+2
def case3():
    return 5*5
def default_case():
    return "opción válida"

def switch_case (argument):
    switcher = {
        1: case1,
        2: case2,
        3: case3
 }
#obtener la función del diccionario
    func = switcher.get(argument, default_case)
    #llamar a la función
    return func()

# Ejemplo de uso
opcion = 1
print(switch_case(opcion))
