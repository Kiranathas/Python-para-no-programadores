#CALCULAR EL SUELDO:
#posible 1 solución:
enero=300
febrero=300
marzo=300
abril=300
mayo=300
junio=300
julio=500
agosto=500
septiembre=500
octubre=500
noviembre=700
diciembre=700

sueldo_promedio= (enero+febrero+marzo+abril+mayo+junio+julio+agosto+septiembre+octubre+noviembre+diciembre)/12
print(sueldo_promedio)

#solucion 2 dado los sueldos recibidos por mes:
sueldo_total = 300 * 6 + 500 * 4 + 700 * 2
sueldo_promedio = sueldo_total / 12

if sueldo_promedio <300:
    print("sueldo bajo")
elif sueldo_promedio >900:
    print("sueldo normal")
else:
 print("sueldo normal")
 