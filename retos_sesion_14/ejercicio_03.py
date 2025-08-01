def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)

n = int(input("Ingrese el valor de n para la serie de Lucas: "))
print("Lucas número", n, "es:", lucas(n))