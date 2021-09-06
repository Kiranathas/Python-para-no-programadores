# ~ El programa debe chequear que la fila y la columna
# ~ tengan valores válidos. En este caso, las únicas filas
# ~ válidas son 0 y 1; las columnas, 0, 1 y 2. Si alguno de
# ~ los dos valores es inválido, debe mostrar un mensaje
# ~ de error.
matriz = [[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]]
fila= int(input("ingrese una fila: "))
columna=int(input("ingrese una columna: "))
for x in matriz:
    if fila <=1 and columna <=2:
        print (matriz[fila][columna])
    elif fila <=1 and columna > 2:
        print("error en la columna")
        columna=int(input("ingrese una columna: "))
    elif fila >1 and columna <= 2:
        print("error en la fila")
        fila= int(input("ingrese una fila: "))
    else:
        print("error en los datos ingresados")


# otra forma
if fila < len(matriz):
	if columna < len(matriz[fila]):
		print(matriz[fila][columna])
	else:
		print("Error en las columnas")
else:
	print("Error en las filas")



# ~ Imprimir matriz con una función
# ~ Crear una función que tome como argumento una matriz, 
# de cualquier dimensión, e imprima cada
# ~ uno de sus números en una línea diferente: 
def imprimir_matriz(m):
    for n in m:
        for i in n:
            print(i)
        
m1 = [[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]]
imprimir_matriz(m1)