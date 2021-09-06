# ~ 1. Se tiene la siguiente lista de nombres:
# ~ nombres = ["Susana","Alejandro","Roberto"]
# ~ Insertar entre Alejandro y Roberto a Paula. Y luego
# ~ agregar al final a Silvina.
# ~ Para finalizar, hay que recorrer la lista y mostrar a todos
# ~ los nombres por pantalla
nombres = ["Susana","Alejandro","Roberto"]
#agregar a paula
nombres.insert(2,"Paula")
#agregar a silvina
nombres.append("Silvina")

#recorrer todos los elementos e imprimirlos
indice = 0
while indice < len(nombres):
	print(nombres[indice])
	indice = indice + 1



# ~ 2. Se tiene una lista de nombres y se desea recorrer con un bucle for.
nombres = ["Agustina","Marisa","Juan","Osvaldo"]

for x in nombres:
    print(x)


# 3. Escriba un programa que permita crear una lista de
# ~ nombres. Para ello, el programa tiene que pedir un
# ~ número y luego solicitar esa cantidad de nombres
# ~ para crear la lista. Por último, el programa tiene
# ~ que mostrar la lista creada.
# ~ (Verificar que la cantidad sea un número, en caso contrario
# ~ volver a pedir).


cantidad = input("¿Cuantos nombres desea ingresar?: ")
cantidad = int(cantidad)

#Arranca la lista vacia
nombres = []

contador = 0

while contador < cantidad:
    name = input("Ingrese un nombre: ")
    nombres.append(name)
    contador = contador + 1
print(nombres)

# Escriba un programa que permita crear una lista de
# nombres. Para ello, el programa tiene que pedir un número
# y luego solicitar esa cantidad de nombres para crear la lista.
# Por último, el programa tiene que mostrar la lista creada
# recorriendo la lista con un for.
# (Es similar a un ejercicio del módulo 2, pero ahora hay que verificar que
# la cantidad sea un número, en caso contrario volver a pedir). 


cantidad = input("¿Cuantos nombres desea ingresar?: ")

while cantidad.isdecimal() == False:
    print("¡Error. Solo numeros!")
    cantidad = input("Ingrese un numero: ")


cantidad = int(cantidad)

nombres = []
contador = 0

while contador < cantidad:
    name = input("Ingrese un nombre: ")
    nombres.append(name)
    contador = contador + 1

print(nombres)

# Escriba un programa que permita crear una lista de nombres
# (como en el ejercicio anterior). Luego pida un nombre y que
# diga cuántas veces aparece ese nombre en la lista.
# Python para no programadores 


cantidad = input("¿Cuantos nombres desea ingresar?: ")

while cantidad.isdecimal() == False:
    print("¡Error. Solo numeros!")
    cantidad = input("Ingrese un numero: ")

cantidad = int(cantidad)

nombres = []
contador = 0


while contador < cantidad:
    name = input("Ingrese un nombre: ")
    nombres.append(name)
    contador = contador + 1

print("*** ATENCION ***")

dato = input("Ingrese nombre para verificar: ")
veces = 0

for n in nombres:
    if n == dato:
        veces = veces + 1 
print( dato + " aparece " + str(veces) + " veces")

