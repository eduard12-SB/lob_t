#--------------------------------EJERCICIO_17--------------------------------------

"""
Verificar prefijo y sufijo: Escribe un programa que verifique si una cadena dada por el usuario
comienza con un prefijo específico y termina con un sufijo específico.
"""
cadena = input("Ingrese una cadena: ")
prefijo = input("Ingrese el prefijo: ")
sufijo = input("Ingrese el sufijo: ")
p_s_especifico = cadena.startswith(prefijo) and cadena.endswith(sufijo) 
print(p_s_especifico)