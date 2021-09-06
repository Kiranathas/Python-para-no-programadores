# ~ una jornada de trabajo es de 48 hs, dadas las horas trabajadas, hay que calcular el valor por hora.
# ~ Mostrar su salario e indicar las horas extras.
jornada= 48
vh = 15
he=20
n=48 * 15


horas= int(input("horas trabajadas: "))
if horas > jornada:
    print("el salario es: ",((horas-jornada)*he)+n)
    print("se trabajo: ",(horas-jornada),"hs extras")
elif horas == jornada:
    print("el salario es: ",n)
    print("no hubo hs extras")
else:
    print("el salario es: ",horas*vh)
