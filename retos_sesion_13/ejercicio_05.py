print("Tablero de ajedrez 8x8 con # y *")
for fila in range(8):
    linea = ""
    for col in range(8):
        if (fila + col) % 2 == 0:
            linea += "#"
        else:
            linea += "*"
    print(linea)