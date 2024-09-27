"""
Calculadora Simple:
Escribe un programa que realice operaciones aritméticas básicas (suma, resta, multiplicación,
división) con dos números ingresados por el usuario
"""

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación (+, -, *, /): ")

if operacion == '+':
    resultado = num1 + num2
elif operacion == '-':
    resultado = num1 - num2
elif operacion == '*':
    resultado = num1 * num2
elif operacion == '/':
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "ERROR, no se puede dividir por 0."
else:
    resultado = "Operación no válida."

print("El resultado es:", resultado)