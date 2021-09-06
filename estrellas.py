  #escribir una función mostrar_estrellas (cantidad) que muestre tantos * como indica la cantidad 

def estrellas (fin):
    for i in range (0,fin + 1):
        print("*" * i) #imprime tantas veces como la variable i.
           
    
fin = int(input("ingrese cantidad: "))
estrellas(fin) 


#otra forma
def estrellas (inicio,fin):
    a= "*"  
    inicio = 1      
    while  inicio<= fin:        
        print(a)       
        a += "*"        
        inicio += 1    
    return a    
    
fin = int(input("ingrese cantidad: "))
estrellas(1, fin) 
