# menú con las opciones de comida
desayunos = {
    1: ["Huevos", 20],
    2: ["cereal", 10],
    3: ["Avena", 7]
}

almuerzos = {
    1: ["carne", 20],
    2: ["Hamburguesa", 12],
    3: ["Sopa", 10]
}

cenas = {
    1: ["cereal", 7],
    2: ["Espagueti", 10],
    3: ["Fajitas", 15]
}

# Función para mostrar el menú y obtener la selección del usuario
def mostrar_menu():
    print("Bienvenido al restaurante. Seleccione una opción:")
    print("1. Desayuno")
    print("2. Almuerzo")
    print("3. Cena")
    print("4. Valor a pagar")
    opcion = int(input("Ingrese el número de la opción: "))
    return opcion

# Función para mostrar las opciones de comida y obtener la selección del usuario
def seleccionar_comida(tipo_comida):
    print(f"Opciones de {tipo_comida}:")
    for clave, valor in tipo_comida.items():
        print(f"{clave}. {valor[0]} - ${valor[1]:.2f}")
    opcion = int(input("Ingrese el número de la opción: "))
    return opcion

# Función principal
def main():
    total = 0
    while True:
        opcion = mostrar_menu()
        if opcion == 1:
            seleccion = seleccionar_comida(desayunos)
            total += desayunos[seleccion][1]
        elif opcion == 2:
            seleccion = seleccionar_comida(almuerzos)
            total += almuerzos[seleccion][1]
        elif opcion == 3:
            seleccion = seleccionar_comida(cenas)
            total += cenas[seleccion][1]
        elif opcion == 4:
            print(f"El valor total a pagar es: ${total:.2f}")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Llamada a la función principal
if __name__ == "__main__":
    main()