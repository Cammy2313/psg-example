print("Serie del 1 al 100 con Fizz/Buzz/FizzBuzz para múltiplos de 5 y 7")
for i in range(1, 101):
    if i % 5 == 0 and i % 7 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Fizz")
    elif i % 7 == 0:
        print("Buzz")
    else:
        print(i)