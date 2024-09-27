#--------------------------------EJERCICIO_16--------------------------------------
"""
Extraer subcadena: Escribe un programa que extraiga una subcadena de una cadena dada por
el usuario, especificando los índices de inicio y fin.

"""

cadena = input("Ingrese una cadena: ")
inicio = int(input("Ingrese el índice de inicio: "))
fin = int(input("Ingrese el índice de fin: "))
ext_subcadena = cadena[inicio:fin]
print("Subcadena extraída:", ext_subcadena)