import random
import string

def generar_contraseña(longitud):
    if longitud < 8:
        return "Error: La longitud debe ser de al menos 8 caracteres."
    
    caracteres = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    
    # Asegurar al menos un carácter de cada tipo
    contraseña = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    # Completar la contraseña con caracteres aleatorios
    contraseña += random.choices(caracteres, k=longitud - 4)
    
    # Mezclar la contraseña para mayor seguridad
    random.shuffle(contraseña)
    
    return ''.join(contraseña)

# Ejemplo de uso
longitud = 12
print("Contraseña generada:", generar_contraseña(longitud))
