print("Ciclo infinito para palíndromo")
while True:
    frase = input("Ingresa una frase (o escribe 'salir' para terminar): ")
    if 'salir' in frase:
        break
    cadenalimpia = ''.join(ch.lower() for ch in frase if ch.isalnum())
    if cadenalimpia == cadenalimpia[::-1]:
        print("Es palíndromo")
    else:
        print("No es palíndromo")

print()