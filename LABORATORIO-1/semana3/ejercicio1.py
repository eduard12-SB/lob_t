"""
Orden Alfabético:
Escribe un programa que solicite al usuario dos palabras y determine cuál va primero en orden
alfabético
"""

palabra1 = input("Ingrese la primera palabra: ")
palabra2 = input("Ingrese  la segunda palabra: ")

#Comparando
if palabra1 < palabra2:
    print(f"La palabra  {palabra1} va antes que {palabra2} en orden alfabético.")   
elif palabra1 > palabra2:
    print(f"La palabra {palabra2}, va antes que  {palabra1} en orden alfabético.")
else:
    print("Las palabras son iguales.")