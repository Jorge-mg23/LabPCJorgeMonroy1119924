def mostrar_menu():
    print("Menú:")
    print("1. Desayuno")
    print("2. Almuerzo")
    print("3. Cena")
    print("4. Valor a pagar")
    print("5. Salir")

def obtener_desayuno():
    desayuno = {
        "descripcion": "Huevos revueltos con tocino y tostadas",
        "precio": 20
    }
    return desayuno

def obtener_almuerzo():
    almuerzo = {
        "descripcion": "Hamburguesa con papas fritas",
        "precio": 20
    }
    return almuerzo

def obtener_cena():
    cena = {
        "descripcion": "Filete de salmón a la plancha con ensalada",
        "precio": 20
    }
    return cena

def calcular_total(pedidos):
    total = 0
    for pedido in pedidos:
        total += pedido["precio"]
    return total

def main():
    pedidos = []
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")
        if opcion == "1":
            pedidos.append(obtener_desayuno())
            print("Has ordenado el desayuno.")
        elif opcion == "2":
            pedidos.append(obtener_almuerzo())
            print("Has ordenado el almuerzo.")
        elif opcion == "3":
            pedidos.append(obtener_cena())
            print("Has ordenado la cena.")
        elif opcion == "4":
            total = calcular_total(pedidos)
            print(f"El total a pagar es: Q{total:.2f}")
        elif opcion == "5":
            print("¡Gracias por tu visita!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()