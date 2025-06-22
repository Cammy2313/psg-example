cadena = input("Ingresa una palabra o frase: ")

cadena_limpia = ''.join(cadena.lower().split())
cadena_invertida = cadena_limpia[::-1]

es_palindromo = cadena_limpia == cadena_invertida

print(f"¿Es palíndromo? {es_palindromo}")