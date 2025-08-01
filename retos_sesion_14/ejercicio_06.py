def pares_impares(lista):
    pares = []
    impares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares

entrada = input("Ingrese una lista de números separados por comas: ")
lista = [int(x.strip()) for x in entrada.split(",")]

pares, impares = pares_impares(lista)
print("Pares:", pares)
print("Impares:", impares)