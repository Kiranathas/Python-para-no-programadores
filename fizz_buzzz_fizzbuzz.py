# ~ el usuario ingresa el taño de la colecciónd de datos (lista)
# ~ se le debe pedir al usuario que ingrese tantos numeros de acuerdo al tamaño de la colección
# ~ al finalizar la carga, mostrar por pantalla si el elemento es múltiplo de 3
# ~ imprimir "fizz", si es múltiplo de 5 "buzz" y si es de ambos "fizzbuzz" sino ,
# ~ mostrar el elemento.

lista = []
tamaño = int(input("ingrese el tamaño: "))

while len(lista) < tamaño:
    numeros = int(input("ingrese números: "))
    lista.append(numeros)
for numero in lista:
    if (numero %5) == 0 and (numero % 3) == 0:
        print("FizzBuzz")
    elif numero % 5 == 0:
        print("Buzz")
    elif numero % 3 == 0:
        print("Fizz")
    else:
        print(numero)
print(lista)

 
