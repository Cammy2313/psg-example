def calcular(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b != 0:
            return a / b
        else:
            return "No se puede dividir entre cero"
    else:
        return "Operación no válida"

entrada = input("Operación (formato: numero1, numero2, operación): ")
partes = entrada.split(",")

if len(partes) == 3:
    a = int(partes[0].strip())
    b = int(partes[1].strip())
    op = partes[2].strip()

    resultado = calcular(a, b, op)
    print("Resultado:", resultado)
else:
    print("Formato incorrecto")