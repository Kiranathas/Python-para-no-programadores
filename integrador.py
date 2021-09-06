# Crear un programa que de 3 opciones, la primera es añadir un alumno a una lista
#la segunda es ver la lista de alumnos y la tercera es salir:

alumno= []
while True:
    print("Ingrese el número de la operación que desea ejecutar:")
    print("1 - Añadir un alumno a la lista.")
    print("2 - Ver la lista de alumnos.")
    print("3 - Salir.")
    elección = int(input(""))
    if elección == 1:
        nombre = input("ingrese su nombre: ")
        cursos = int(input("Ingrese la cantidad de cursos: "))
        if nombre == "":
            print("error en el nombre")
        else:
            alumno.append([nombre,cursos])
            print("el alumno fue agregado a la lista")
    elif elección == 2:
        for x in alumno:
            print(x)
    elif elección == 3:
        print("gracias por utilizar el programa")
        break
    else:
        ("La opción ingresada no es correcta, vuelva a intentarlo")
print("ha salido del sistema")


#  ahora debe ser un diccionario, en donde las claves
# serán nombres de alumnos y los valores sus respectivas
# cantidades de cursos.
# Para esto deberemos modificar el código de las opciones 1
# y 2 (agregar un nuevo alumno y ver la lista de alumnos).
# La tercera opción será “Ver la cantidad de cursos de un
# alumno”. Deberá solicitar el nombre de un alumno e
# imprimir en pantalla el número de cursos que tiene
# asociados como clave.
# La cuarta opción es la de salir, como en la versión anterior. 
# Python para no programadores
# Usar todo lo aprendido hasta el momento, el
# programa no debe de frenar de forma imprevista
# a causa de un error. Ya que en el material de
# lectura se vieron todas las posibles soluciones
# frente a los problemas que se puedan presentar. 

def verificar(dato):
    while dato == "":
        print("Error")
        dato = input("Ingrese el dato nuevamente: ")
    return dato


def convertir(valor):
    while valor.isdecimal() == False:
        print("Error")
        valor = input("Ingrese valor nuevamente: ")
    return valor

alumnos = {}
while True:
    print("Ingrese el número de la operación que desea ejecutar:")
    print("1 - Añadir un alumno a la lista.")
    print("2 - Ver la lista de alumnos.")
    print("3 - Ver la cantidad de cursos de un alumno.")
    print("4 - Salir.")

    opcion = input("Ingrese el número de opción: ")
    
    if opcion == "1":
        nombre_alumno = input("Ingrese el nombre del alumno: ")
        nombre_alumno = verificar(nombre_alumno)

        cursos = input("Ingrese la cantidad de cursos: ")
        cursos = convertir(cursos)

        alumnos[nombre_alumno] = cursos
        print("Has ingresado el alumno correctamente.")
    elif opcion == "2":
        print("Los alumnos:")   
        for nombre in alumnos:
            cursos = alumnos[nombre]
            print(nombre + " - " + str(cursos) + " cursos")
    elif opcion == "3":
        nombre = input("Ingrese el nombre del alumno: ")
        if nombre in alumnos:
            print(nombre +" tiene "+ str(alumnos[nombre])+" cursos.")
        else:
            print("Ese alumno no tiene cursos asignados")
    elif opcion == "4":
        print("¡Gracias por utilizar el programa!")
        break
    else:
        print("La opción ingresada no es correcta, vuelva a intentarlo.")
