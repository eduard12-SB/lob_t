def celsius_a_fahrenheit(celsius):
    """Convierte de grados Celsius a Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    """Convierte de grados Fahrenheit a Celsius."""
    return (fahrenheit - 32) * 5/9

def convertir_temperatura(valor, unidad):
    """Convierte la temperatura según la unidad ingresada."""
    if unidad.upper() == 'C':
        return f"{valor}°C son {celsius_a_fahrenheit(valor):.2f}°F"
    elif unidad.upper() == 'F':
        return f"{valor}°F son {fahrenheit_a_celsius(valor):.2f}°C"
    else:
        return "Error: Unidad no reconocida."
def manejar_entrada():
    """Gestiona la entrada del usuario y maneja errores."""
    try:
        valor = float(input("Ingresa la temperatura: "))
        unidad = input("Ingresa la unidad (C o F): ").strip()
        if unidad.upper() not in ['C', 'F']:
            print("Error: Debes ingresar 'C' para Celsius o 'F' para Fahrenheit.")
        else:
            print(convertir_temperatura(valor, unidad))
    except ValueError:
        print("Error: Entrada no válida. Asegúrate de ingresar un número para la temperatura.")

# Ejemplo de uso
manejar_entrada()
