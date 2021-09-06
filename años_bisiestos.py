# CALCULAR AÑOS BISIESTOS:

año= int(input("ingrese el año: "))

if (año % 4)== 0:
    print("año bisiesto")
else:
    print("no es un año bisiesto")
    
#otra forma:
a = input("Ingrese año: ")
a = int(a)

if a % 400 == 0:
    print("Es bisiesto")
else:
    if a % 4 == 0 and a % 100 != 0 :
        print("Es bisiesto")
    else:
        print("No es bisiesto")

print("Fin")  
    