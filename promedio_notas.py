#COMPARAR notas
nota_uno=10
nota_dos=6
nota_tres=8
#promedio
promedio= (nota_uno+nota_dos+nota_tres)/3
print(promedio)
#mostrar si aprobó o no.
if promedio >=6:
    print("aprobado")
else:
    print("desaprobado")



# ~ El usuario debe ingresar una nota (Suponiendo que siempre es menor que 11)
# ~ Mostrar un msg "Excelente" si la nota es un 10
# ~ un "muy bien" si esta entre 7 y 9
# ~ un "bien" si esta entre un 4 y un 6
# ~ sino mostrar "mal"

nota= int(input("ingrese su nota: "))
if nota == 10:
    print("excelente")
elif nota >=7 and nota <=9:
    print("muy bien")
elif nota >=4 and nota <=6:
    print("bien")
else:
    print("mal")