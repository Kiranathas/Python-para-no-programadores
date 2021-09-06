 # ~ pide un numero por teclado y guarda en una lista su tabla de multiplicar hasta el 10
lista= []
numero = int(input("ingrese un número: "))
contador = 1

while contador <= 10:
    lista.append(numero * contador)
    contador += 1
print(lista)

#otra forma
for n in range (1,11): #paso el 11 porq es último argumento - 1
    lista.append(numero * n)
print(lista)