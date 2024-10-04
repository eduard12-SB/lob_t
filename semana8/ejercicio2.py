def calculadora():
    try:
        
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))

        print("Selecciona la operación:")
        print("""
        [1]Suma
        [2] Resta
        [3] Multiplicación
        [4] División""")

        operacion = input("Introduce el número de la operación (1/2/3/4): ")
        if operacion == '1':
            resultado = num1 + num2
            print(f"{num1} + {num2} = {resultado}")
        elif operacion == '2':
            resultado = num1 - num2
            print(f"{num1} - {num2} = {resultado}")
        elif operacion == '3':
            resultado = num1 * num2
            print(f"{num1} * {num2} = {resultado}")
        elif operacion == '4':
            if num2 == 0:
                print("Error: No se puede dividir por cero.")
            else:
                resultado = num1 / num2
                print(f"{num1} / {num2} = {resultado}")
        else:
            print("Operación no válida. Por favor, selecciona una opción válida (1/2/3/4).")

    except ValueError:
        print("Error: Entrada no válida. Por favor, introduce números válidos.")

calculadora()
