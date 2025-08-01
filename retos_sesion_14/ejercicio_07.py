def crear_tablero():
    return [[" " for _ in range(3)] for _ in range(3)]

def imprimir_tablero(tab):
    for fila in tab:
        print(fila)
    print()

def gana(tab, jugador):
    for fila in tab:
        if all(c == jugador for c in fila):
            return True
    for col in range(3):
        if all(tab[f][col] == jugador for f in range(3)):
            return True
    if tab[0][0] == tab[1][1] == tab[2][2] == jugador:
        return True
    if tab[0][2] == tab[1][1] == tab[2][0] == jugador:
        return True
    return False

def tablero_lleno(tab):
    for fila in tab:
        if " " in fila:
            return False
    return True

def tres_en_raya():
    tablero = crear_tablero()
    jugador = "X"
    while True:
        print(f"Juega '{jugador}'")
        imprimir_tablero(tablero)
        fila = int(input("Fila (0, 1, 2): "))
        col = int(input("Columna (0, 1, 2): "))

        if fila < 0 or fila > 2 or col < 0 or col > 2:
            print("Posición fuera de rango. Intenta de nuevo.")
            continue

        if tablero[fila][col] != " ":
            print("Esa casilla ya está ocupada. Intenta otra.")
            continue

        tablero[fila][col] = jugador

        if gana(tablero, jugador):
            imprimir_tablero(tablero)
            print(f"¡Jugador '{jugador}' gana!")
            break

        if tablero_lleno(tablero):
            imprimir_tablero(tablero)
            print("Empate.")
            break

        jugador = "O" if jugador == "X" else "X"

tres_en_raya()