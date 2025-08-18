print("Los primeros 20 números de la sucesión de Lucas son: ")
a, b = 2, 1
contador = 0
while contador < 20:
    print(a)
    a, b = b, a + b
    contador += 1