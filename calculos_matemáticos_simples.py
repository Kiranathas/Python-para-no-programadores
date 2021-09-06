#Dada a y b, mostrar la suma, resta, multiplicación y división
#primera opción
a=20
b=10
print(a+b)
print(a-b)
print(a*b)
print(a/b)

#segunda opción
suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
print("La suma es:", suma)
print("La resta es:",resta)
print("La multiplicación es:", multiplicacion)
print("La división es:", division)

# Crea una función que calcule el factorial de un
# número pasado por parámetro(argumento). Y
# ‘muestre’ el resultado.
# Aclaración: En matemática el factorial se representa con un
# signo de exclamación “!” detrás de un número. Esta
# exclamación quiere decir que hay que multiplicar todos los
# números enteros positivos que hay entre ese número y el 1.
# Por ejemplo, el 6 factorial ( 6! ):

def factorial(numero):
    num = 1
    for n in range(1,numero+1,1):
        num = num * n
    print(num)

factorial(6)