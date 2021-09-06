#VARIABLES:
# ~ crear 3 variables (a,b,c) con valores numéricos (x) y una cuarta variable llamada resultado que sea la suma de las primeras 3.
# ~ luego imprimir en pantalla cada una de ellas.
# ~ antes de mostrar el valor de cada variable, indicar su nombre en una línea anterior.

a= 1
b= 2
c= 3
resultado= a+b+c
print("a:")
print(a)
print("b:")
print(b)
print("c:")
print(c)
print("resultado:")
print(resultado)


#CONCATENAR DOS CADENAS:
saludo = "Hola"
nombre = "Florencia"
resultado = saludo+" "+nombre
print(resultado)


#ENTRADA DEL USUARIO:
# ~ crear un programa que permita ingresar dos cadenas vía la consola
# ~ y luego las compare, imprimiendo un mensaje en caso que sean iguales y otro en caso que sean diferentes
primero= input("ingrese su contraseña: ")
segundo=input("ingrese su contraseña: ")
if primero == segundo:
    print("son iguales")
else:
    print("no son iguales")



#CONCATENAR CADENAS: Armar una frase con 3 variables dadas
#primera opción
texto_uno="potente"
texto_dos="sol"
texto_tres="triunfo"
print("el",texto_uno, texto_dos,texto_tres,"sobre el mundo")
#segunda opción
frase="el"+texto_uno+ texto_dos+texto_tres+"sobre el mundo"
print(frase)

 

#CONTROL DE NOMBRE: crear un programa que solicite el nombre de un alumno a través de la consola, 
# y luego chequee que no esté vacío.
# en caso de estarlo, debe imprimir un mensaje de error; en caso contrario, imprimir un mensaje indicando que se ingresó correctamente.

nombre = input("ingrese su nombre: ")

if nombre == "":
    print("error, debe ingresar un nombre")
else:
    print("el nombre se ingresó correctamente")


# CONTROL DE NOMBRE 2:Crear un programa que permita ingresar dos cadenas vía la consola y
# ~ luego las compare, imprimiendo un mensaje en caso que sean iguales
# ~ y otro en caso que sean diferentes.

cadena1= input("ingrese su nombre: ")
cadena2=input("vuelva a ingresar su nombre: ")

if cadena1 == cadena2:
    print("identico")
else:
    print("datos incorrectos")


# ~ INCREMENTACIÓN:Con un bucle while incrementar una variable entera de uno en uno
# ~ (desde 0 a 10 sin incluir). Mostrar por pantalla el resultado por vuelta.
var = 0
while var <= 10:
    print (var)
    var = var+1
print(var)


# ~Control y saludo: Pedir por teclado el nombre de usuario, si está vacío,
# ~ volver a pedirlo hasta que se ingrese un nombre.
# ~ Luego, saludar al usuario.

nombre = input("ingrese su nombre: ")

while nombre == "":
    print("error")
    nombre = input("ingrese su nombre: ")
print("hola", nombre)

 

# ~ SUMAR NÚMEROS CON UNA FUNCIÓN
# ~ crear una función que tome como argumento una lista (considerando que siempre contendrá números enteros y de coma flotante)
#  y retorne la suma de todos sus elementos.
def sumar(l):
    r= 0
    for n in l:
        r= r+n
    return r
print(sumar([1,2,3,4,5]))




