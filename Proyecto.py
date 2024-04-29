def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        raise ValueError("No se puede dividir entre cero")
    return x / y

def main():
    while True:
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            break
        except ValueError:
            print("Por favor, ingrese números válidos.")

    while True:
        print("\nMenú de opciones:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
            if 1 <= opcion <= 5:
                if opcion == 5:
                    print("¡Hasta luego!")
                    break
                else:
                    resultado = None
                    if opcion == 1:
                        resultado = sumar(num1, num2)
                    elif opcion == 2:
                        resultado = restar(num1, num2)
                    elif opcion == 3:
                        resultado = multiplicar(num1, num2)
                    elif opcion == 4:
                        resultado = dividir(num1, num2)

                    print(f"\nResultado: {resultado}")

        except ValueError:
            print("Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()