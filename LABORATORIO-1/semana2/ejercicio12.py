#--------------------------------EJERCICIO_12--------------------------------------

"""
Reemplazar espacios: Escribe un programa que reemplace todos los espacios en una cadena
dada por el usuario con guiones bajos.

"""
cadena = input("Introduce una cadena: ")
# usando el metodo replace
cadena_reemplazada = cadena.replace(" ", "_")
print(cadena_reemplazada)