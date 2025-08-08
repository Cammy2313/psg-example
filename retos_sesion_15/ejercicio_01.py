while True:
    entrada = input("Ingresa dos números separados por espacio, o 'salir' para terminar: ")
    if entrada.lower() == "salir":
        print("Saliendo de la calculadora.")
        break
    try:
        num1_str, num2_str = entrada.split()
        num1 = float(num1_str)
        num2 = float(num2_str)
        print("Suma:", num1 + num2)
        print("Resta:", num1 - num2)
        print("Multiplicación:", num1 * num2)
        print("División:", num1 / num2)
    except ValueError:
        print("Error: debes ingresar dos valores numéricos válidos.")
    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero.")
    except Exception as e:
        print("Error inesperado:", e)