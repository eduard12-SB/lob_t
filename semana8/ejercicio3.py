import random
import string


generar_contrasena = lambda longitud, mayus, minus, nums, especiales: ''.join(
    random.choice(
        (string.ascii_uppercase if mayus else '') +
        (string.ascii_lowercase if minus else '') +
        (string.digits if nums else '') +
        (string.punctuation if especiales else '')
    ) for _ in range(longitud)
) if any([mayus, minus, nums, especiales]) else ValueError("Debe incluir al menos un tipo de carácter.")


def solicitar_parametros():
    try:
        longitud = int(input("Introduce la longitud de la contraseña: "))
        if longitud <= 0: raise ValueError("La longitud debe ser un número positivo.")
        
        
        incluir_mayusculas = input("¿Incluir letras mayúsculas? (s/n): ").lower() == 's'
        incluir_minusculas = input("¿Incluir letras minúsculas? (s/n): ").lower() == 's'
        incluir_numeros = input("¿Incluir números? (s/n): ").lower() == 's'
        incluir_especiales = input("¿Incluir caracteres especiales? (s/n): ").lower() == 's'

       
        contrasena = generar_contrasena(longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_especiales)
        print(f"Contraseña generada: {contrasena}")

    except ValueError as a:
        print(f"Error: {a}")


solicitar_parametros()
