frutas_permitidas = ["🍅", "🍇", "🍈", "🍉", "🍊", "🍌", "🍍", "🍑"]

class FrutaInvalidaError(Exception):
    pass

canasta = []

while True:
    fruta = input("Ingresa una fruta (o 'salir' para terminar): ")
    if fruta.lower() == "salir":
        print("Canasta final:", canasta)
        break
    try:
        if fruta not in frutas_permitidas:
            raise FrutaInvalidaError(f"La fruta '{fruta}' no es válida.")
        canasta.append(fruta)
        print("Fruta agregada:", fruta)
    except FrutaInvalidaError as e:
        print("Error:", e)
