abs_valor = lambda x: x if x >= 0 else -x

numero = int(input("Ingrese un número para obtener su valor absoluto: "))
print("Valor absoluto:", abs_valor(numero))