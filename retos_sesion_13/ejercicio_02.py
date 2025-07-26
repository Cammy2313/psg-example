print("Los 20 primeros números que sean múltiplos de 2 y 5 son:")
n = 1
contador = 0
while contador < 20:
    if n % 10 == 0:
        print(n)
        contador += 1
    n += 1

print()