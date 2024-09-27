
#-----------------------------------------EJERCICIO_2-------------------------------------
"""
Compara la longitud de tu nombre y tu apellido
"""
nombre = "Eduard"
longitud_nombre = len(nombre)
apellido = "soto"
longitud_apellido= len(apellido)

print(f"Nombre: {nombre} \nLa longitud es de: {longitud_nombre} letras.")
print(f"Apellido: {apellido} \nLa longitud es de: { longitud_apellido} letras.")

#comparando
print("Comparamos las longitudes")
if longitud_nombre==longitud_apellido:
    print("la longitud del apellido y nombre son iguales")
else:
    print("Las longitudes del apellido y nombre son distintas")
    print()