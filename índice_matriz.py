#crear un programa que solicite una fila y una columna 
# e imprima en pantalla el numero en esa posición según
#  la siguiente matriz=[[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]]
# se deben chequear los resultados o indicar error.

matriz=[[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]]
fila= int(input("ingrese la fila del 0 al 1: "))
columna= int(input("ingrese la columna del 0 al 2: "))

if fila != 0 and fila != 1:
    print("error en los datos ingresados en fila")
elif columna != 0 and columna != 1 and columna != 2:
    print("error en los datos ingresados columna")
else:
    print(matriz[fila][columna])

#otra forma
if (fila == 0 or fila ==1) and (columna >=0 and columna <=2):
    print(matriz[fila][columna])
else:
    print("fila o columna inválida")


# Se tiene la “matriz” (una lista de listas):
# ~ m = [ [10,50,5], [20,30,70], [15,45,80] ] .
# ~ Recorrerla con 2 sentencias ‘for’ para mostrar cada
# ~ uno de los elementos que la componen. 

m = [ [10,50,5], [20,30,70], [15,45,80] ] 
for i in m:
    for j in i:
        print(j)