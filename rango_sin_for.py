# ~ crear una funcion rango (desde, hasta , intervalo) 
# que retorne una lista de números, tal como la función incorporada range()
# ~ aunque según el intervalo específicado. Por ejemplo, el siguiente código
def rango(inicio,fin,intervalo):
    resultado = []
    while inicio < fin:
        resultado.append(inicio)
        inicio = inicio + intervalo
    return(resultado)
    
print(rango (1,10,2))