print("Ciclo infinito que recibe número y verifica si es múltiplo de 7")
while True:
    entrada = int(input("Ingresa un número (0 para salir): "))
    if entrada == 0:
        break
    if entrada % 7 == 0:
        print(f"{entrada} es múltiplo de 7")
    else:
        print(f"{entrada} no es múltiplo de 7")

print()