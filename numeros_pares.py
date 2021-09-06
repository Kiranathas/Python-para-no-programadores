#ESCRIBIR UNA FUNCIÓN QUE , DADA UNA LISTA, DEVUELVA OTRA CON LOS NUMEROS PARES DE LA LISTA ORIGINAL.


def num_pares(l):
    pares= []
    for i in l:
        if i%2 ==0:
            pares.append(i)
    return pares
    
print(num_pares([1,2,3,4,5]))