def contar_vocales(cadena):
    contador = 0
    for letra in cadena.lower():
        if letra in "aeiou":
            contador += 1
    return contador

texto = input("Ingrese una cadena: ")
print("Cantidad de vocales:", contar_vocales(texto))