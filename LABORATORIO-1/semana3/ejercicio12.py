
"""
Día de la Semana:
Pide al usuario un número del 1 al 7 y utiliza una estructura if...elif...else para imprimir el día de
la semana correspondiente.
"""

dia = int(input("Ingresa un número del 1 al 7: "))

if dia == 1:
    print("DOMINGO")
elif dia == 2:
    print("LUNES")
elif dia == 3:
    print("MARTES")
elif dia == 4:
    print("MIERCOLES")
elif dia == 5:
    print("JUEVES")
elif dia == 6:
    print("VIERNES")
elif dia == 7:
    print("SABADO")
else:
    print("Ingresaste un numero no valido.")