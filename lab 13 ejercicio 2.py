#"Semana No. 12: Ejercicio 2"
print("Semana No. 12: Ejercicio 2")

x, y = 0, 0

def mover_hacia_arriba():
    global y
    y += 1

def mover_hacia_abajo():
    global y
    y -= 1

def mover_hacia_derecha():
    global x
    x += 1

def mover_hacia_izquierda():
    global x
    x -= 1

while True:
    print("\nMenú:")
    print("a. Sube")
    print("b. Baja")
    print("c. Izquierda")
    print("d. Derecha")
    print("e. Salir")
    opcion = input("Ingrese una opción: ").lower()

    if opcion == "a":
        mover_hacia_arriba()
    elif opcion == "b":
        mover_hacia_abajo()
    elif opcion == "c":
        mover_hacia_izquierda()
    elif opcion == "d":
        mover_hacia_derecha()
    elif opcion == "e":
        # 5. Mostrar coordenadas finales del personaje
        print(f"Coordenadas finales del personaje: {x}, {y}")
        break
    else:
        print("Opción inválida. Intente nuevamente.")