# En un sistema de agencia de viajes se tiene un sistema de
# ~ información para paquetes turísticos. Se quiere hacer un
# ~ programa que al ingresar el paquete (solo la letra) te de una
# ~ descripción de lo que contiene cada “combo”.
# ~ a. Paquete A: “Cancún 7 noches + Aéreos u$s 1200 por persona”
# ~ b. Paquete B: “Miami 8 noches + Aéreos + Alquiler de Auto u$s 1500
# ~ por persona”
# ~ c. Paquete C: “Bariloche 10 noches + Aéreos + excursiones u$s 1300
# ~ por persona”
# ~ d. Paquete D: “Rio de Janeiro 10 noches + Aéreos + excursiones u$s 1400
# ~ por persona

paquete = input("Ingrese el paquete: ")

if paquete =="A" or paquete == "a":
    print("Cancún 7 noches + Aéreos u$s 1200 por persona")
elif paquete == "B" or paquete == "b":
    print("Miami 8 noches + Aéreos + Alquiler de Auto u$s 1500 por persona")
elif paquete == "C" or paquete =="c":
    print("Bariloche 10 noches + Aéreos + excursiones u$s 1300 por persona")
elif paquete == "D" or paquete == "d":
    print("Rio de Janeiro 10 noches + Aéreos + excursiones u$s 1400 por persona")
else:
    print("Error de opción")