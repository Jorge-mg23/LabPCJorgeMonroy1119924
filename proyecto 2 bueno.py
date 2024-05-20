registro_cursos = []
alumnos = []
fechas = []
alumnos_y_notas = []

def crear_curso():
    id_curso = input("Ingrese el ID del curso: ")
    
    # Verificar si el curso existe
    if x (id_curso):
        print(f"El curso con ID {id_curso} ya existe en el registro.")
        return
    
    nombre = input("Ingrese el nombre del curso: ")
    horario = input("Ingrese el horario del curso: ")
    salon = input("Ingrese el salón del curso: ")
    catedratico = input("Ingrese el nombre del catedrático: ")
    
    curso = [id_curso, nombre, horario, salon, catedratico, []]
    registro_cursos.append(curso)
    print("Curso creado exitosamente.")

# verificar si la funcion se puede cumplir o no
def x (id_curso):
    for p in registro_cursos:
        if p[0] == id_curso:
            return True
    return False
# ediciones de cursos
def editar_curso():
    id_curso = input("Ingrese el ID del curso a editar: ")
    x = False
    
    for curso in registro_cursos:
        if curso[0] == id_curso:
            x = True
            print(f"Curso actual: ID: {curso[0]}, Nombre: {curso[1]}, Horario: {curso[2]}, Salón: {curso[3]}, Catedrático: {curso[4]}")
            curso[1] = input("Ingrese el nuevo nombre del curso (dejar en blanco para no cambiar): ") or curso[1]
            curso[2] = input("Ingrese el nuevo horario del curso (dejar en blanco para no cambiar): ") or curso[2]
            curso[3] = input("Ingrese el nuevo salón del curso (dejar en blanco para no cambiar): ") or curso[3]
            curso[4] = input("Ingrese el nuevo catedrático del curso (dejar en blanco para no cambiar): ") or curso[4]
            print("Curso editado exitosamente.")
            break
    
    if not x:
        print(f"No se encontró ningún curso con el ID {id_curso}.")
#mostrar los cursos junto con los detalles del curso
def mostrar_cursos():
    if not registro_cursos:
        print("No hay cursos registrados.")
    else:
        print("Cursos registrados:")
        for curso in registro_cursos:
            print(f"ID: {curso[0]}, Nombre: {curso[1]}, Horario: {curso[2]}, Salón: {curso[3]}, Catedrático: {curso[4]}, Alumnos: {len(curso[5])}")
#crear alumnos
def crear_alumnos():
    carne_alumno = input("ingrese el carne del alumno")
    nombre_alumno = input("ingrese el nombre del alumno")
    from datetime import datetime

    # Solicitar fechas al usuario
    fecha_alumno = input("Ingrese una fecha (AAAA-MM-DD)")
    try:
        fecha = datetime.strptime(fecha_alumno, "%Y-%m-%d").date()
        fechas.append(fecha)
    except ValueError:
        print("Formato de fecha inválido. Intente nuevamente.")
    
    datos_alumno = [carne_alumno, nombre_alumno, fecha_alumno]
    alumnos.append(datos_alumno)
    print ("alumno creado")
#editar alumnos
def editar_alumno():
    listar_alumnos()
    carne = input("Ingrese el carné del alumno a editar: ")
    for alumno in alumnos:
        if alumno[0] == carne:
            alumno[1] = input(f"Ingrese el nuevo nombre del alumno (actual: {alumno[1]}): ") or alumno[1]
            alumno[2] = input(f"Ingrese la nueva fecha de nacimiento del alumno (actual: {alumno[2]}) (AAAA-MM-DD): ") or alumno[2]
            print("Alumno editado exitosamente.")
            return
    print(f"No se encontró ningún alumno con el carné {carne}.")
#mostrar alumnos con detalles
def listar_alumnos():
    print("Alumnos registrados:")
    for alumno in alumnos:
        print(f"Carné: {alumno[0]}, Nombre: {alumno[1]}, Fecha de nacimiento: {alumno[2]}")
#agregar alumnos a cursos y calificar sus notas
def calificar_curso():
    mostrar_cursos()
    id_curso = input("Ingrese el ID del curso a calificar: ")
    curso_encontrado = False
    for curso in registro_cursos:
        if curso[0] == id_curso:
            curso_encontrado = True
            carne_alumno = input("Ingrese el carné del alumno a calificar: ")
            alumno_encontrado = False
            for alumno in alumnos:
                if alumno[0] == carne_alumno:
                    alumno_encontrado = True
                    nota = input(f"Ingrese la nota del alumno {alumno[1]} en el curso {curso[1]}: ")
                    curso[5].append((carne_alumno, nota))
                    print("Nota asignada exitosamente.")
                    break
            if not alumno_encontrado:
                    print(f"No se encontró ningún alumno con el carné {carne_alumno}.")
            break
    if not curso_encontrado:
            print(f"No se encontró ningún curso con el ID {id_curso}.")
#mini menú de reportes
def reportes():
    def fechas_orden():
        # Ordenar las fechas de mayor a menor
        fechas.sort(reverse=True)
        print("Fechas ordenadas de mayor a menor:")
        for fecha in fechas:
            print(fecha)
    #funcion para listar estudiantes por curso
    def Listar_estudiantes(id_curso):
        y = False
        for curso in registro_cursos:
            if curso[0] == id_curso:
                y = True
                print(f"Estudiantes y notas del curso {curso[1]}:")
                for alumno_nota in curso[5]:
                    carne_alumno = alumno_nota[0]
                    nota = alumno_nota[1]
                    for alumno in alumnos:
                        if alumno[0] == carne_alumno:
                            print(f"Alumno: {alumno[1]}, Nota: {nota}")
                break
        if not y:
            print(f"No se encontró ningún curso con el ID {id_curso}.")
    #reporte de notas de alumno por curso
    def reporte_notas(carne_alumno):
        x = False
        for alumno in alumnos:
            if alumno[0] == carne_alumno:
                x = True
                print(f"Notas del alumno {alumno[1]}:")
                for curso in registro_cursos:
                    for alumno_nota in curso[5]:
                        if alumno_nota[0] == carne_alumno:
                            print(f"Curso: {curso[1]}, Nota: {alumno_nota[1]}")
                break
        if not x:
            print(f"No se encontró ningún curso con el ID {id_curso}.")
    #funcion para el promedio de notas
    def reporte_nota_media():
        for curso in registro_cursos:
            suma_notas = 0
            cantidad_notas = 0
            for alumno_nota in curso[5]:
                suma_notas += float(alumno_nota[1])
                cantidad_notas += 1
            if cantidad_notas > 0:
                nota_media = suma_notas / cantidad_notas
                print(f"Nota media del curso {curso[1]}: {nota_media:.2f}")
    #funcion para el estudiante destacado
    def reporte_mejor_estudiante():
        promedios_alumnos = {alumno[0]: sum(float(nota[1]) for curso in registro_cursos for nota in curso[5] if nota[0] == alumno[0]) / sum(1 for curso in registro_cursos for nota in curso[5] if nota[0] == alumno[0]) for alumno in alumnos}

        if not promedios_alumnos:
            print("No hay alumnos con notas registradas.")
            return

        mejor_promedio = max(promedios_alumnos.values())
        mejores_alumnos = [carne for carne, promedio in promedios_alumnos.items() if promedio == mejor_promedio]

        print("Estudiante(s) con mejor desempeño en general:")
        for carne in mejores_alumnos:
            for alumno in alumnos:
                if alumno[0] == carne:
                    print(f"Nombre: {alumno[1]}, Carné: {carne}, Promedio: {promedios_alumnos[carne]}")
    #menu secundario
    print("\nMenú secundario")
    print("1. Ver las fechas de nacimiento ordenadas de mayor a menor")
    print ("2. Listar estudiantes de un curso seleccionado junto con las notas de ese curso")
    print ("3. Listar para un estudiante seleccionado sus notas")
    print ("4. reporte de nota media del curso")
    print ("5. reporte mejor estudiante")
    opcion = input("ingrese una opción")
    #menu funciones
    if opcion == "1":
        fechas_orden()
    elif opcion == "2":
        id_curso= input("ingrese el id del curso para ver el listado de estudiantes")
        Listar_estudiantes(id_curso)
    elif opcion =="3":
        carne_alumno = ("ingrese el carne del alumno del que quiere ver las notas")
        reporte_notas(carne_alumno)
    elif opcion=="4":
        reporte_nota_media()
    elif opcion == "5":
        reporte_mejor_estudiante()
#menú
while True:
    print("\nMenú principal:")
    print("1. Crear curso")
    print("2. Editar curso")
    print("3. Mostrar cursos")
    print("4. Agregar alumno")
    print ("5. calificar curso")
    print ("6. Reportes")
    print ("7. editar alumno")
    print ("8. listar alumnos")
    print("9. Salir")

#menú funciones
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        crear_curso()
    elif opcion == "2":
        editar_curso()
    elif opcion == "3":
        mostrar_cursos()
    elif opcion == "4":
        crear_alumnos()
    elif opcion == "5":
        calificar_curso()
    elif opcion == "6":
        reportes()
    elif opcion == "7":
        editar_alumno()
    elif opcion == "8":
        listar_alumnos()
    elif opcion == "9":
        print("saliendo")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")