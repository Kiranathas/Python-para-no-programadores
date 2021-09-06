# Realizar un programa que, ingresando la edad de una persona,
# ~ determine si es menor, mayor con edad laboral o jubilado
edad= int(input("ingrese su edad: "))

if edad < 18:
    print("es menor de edad")
elif edad >= 60 and  edad <65:
    print("es jubilado mujer")
elif edad >= 65:
    print ("es jubilado hombre")
else:
    print(" es mayor con edad laboral")


#Comprobar ingreso
#Forzar el ingreso de solo números. Crear un programa que
#pida una edad, verificar que el ingreso por input sea un
#número entero. En caso contrario volver a pedir el ingreso.
#Después decidir si por la edad la persona es mayor o menor
#de edad.

edad = input("Ingrese edad: ")

while edad.isdecimal() == False:
	print("Error de ingreso")
	edad = input("Ingrese edad nuevamente: ")

edad = int(edad)

if edad < 18:
	print("Menor de edad")
else:
	print("Mayor de edad")

#  Crea una función que reciba un dato ingresado por
# teclado(str), que verifique que sea un número
# entero posible de convertir (a int), y si no lo es vuelva
# a pedir ese dato, hasta que sea posible de convertirlo.
# Luego que retorne el entero convertido.

def convertir(dato):
    while dato.isdecimal() == False:
        print("¡Error!")
        dato = input("Ingrese nuevamente: ")
    return int(dato)

###########################################

#ejemplo de como y donde se podría usar:

edad = input("Ingrese su edad: ")
edad = convertir(edad)

if edad < 18:
    print("Menor de edad")
else:
    print("Menor de edad")