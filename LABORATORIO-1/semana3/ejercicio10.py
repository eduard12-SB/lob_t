"""
Conversor de Unidades de Longitud:
Pide al usuario una longitud en metros y la unidad a la que desea convertir ("pies", "pulgadas"
o "yardas"). Realiza la conversión e imprime el resultado.

"""

longitud = float(input("Introduce una longitud en metros: "))
unidad = input("Introduce la unidad a la que deseas convertir (pies / pulgadas / yardas): ").lower()

if unidad == "pies":
    conversión = longitud * 3.28084
elif unidad == "pulgadas":
    conversión  = longitud * 39.3701
elif unidad == "yardas":
    conversión = longitud * 1.09361
else:
    conversión = "Unidad no válida."

print(longitud,"metros son",conversión, unidad)