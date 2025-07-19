entrada = input("Operación (formato: numero1, numero2, operación): ")
partes = entrada.split(",")

if len(partes) == 3:
    num1 = float(partes[0].strip())
    num2 = float(partes[1].strip())
    operacion = partes[2].strip()

    if operacion == "+":
        resultado = num1 + num2
        print("Resultado:", resultado)
    elif operacion == "-":
        resultado = num1 - num2
        print("Resultado:", resultado)
    elif operacion == "*":
        resultado = num1 * num2
        print("Resultado:", resultado)
    elif operacion == "/":
        if num2 != 0:
            resultado = num1 / num2
            print("Resultado:", resultado)
        else:
            print("Error: División por cero")
    else:
        print("Operación inválida")
else:
    print("Formato incorrecto")