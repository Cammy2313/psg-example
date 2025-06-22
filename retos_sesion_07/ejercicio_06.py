# casefold() - versión más agresiva de lower()
palabra = "PYTHON"
print(palabra.casefold())

# center() - centra texto en un ancho dado, rellenando con un caracter
palabra = "hola"
print(palabra.center(10, '*'))

# expandtabs() - convierte tabuladores en espacios
frase = "hola\tmundo"
print(frase.expandtabs(4))

# encode() - codifica la cadena a bytes
palabra = "abracadabra"
print(palabra.encode("utf-8"))

# index() - busca substring y devuelve la primera posición, falla si no existe
print(palabra.index("ca"))

# rindex() - busca substring desde el final y devuelve la posición, falla si no existe
print(palabra.rindex("bra"))

# splitlines() - divide en líneas
multiline = "linea1\nlinea2\nlinea3"
print(multiline.splitlines())

# rsplit() - divide desde la derecha
cadena = "uno,dos,tres,cuatro"
print(cadena.rsplit(",", 2))  # ['uno,dos,tres', 'cuatro']

# partition() - divide en tupla antes, separador y después (primera ocurrencia)
print(cadena.partition(","))

# rpartition() - lo mismo que partition pero desde el final
print(cadena.rpartition(","))

# startswith() - verifica si empieza con el prefijo dado
print(cadena.startswith("uno"))

# endswith() - verifica si termina con el sufijo dado
print(cadena.endswith("cuatro"))

# isspace() - verifica si todos los caracteres son espacios en blanco
print("   \t\n".isspace())
print(" a ".isspace()) 

# islower() - verifica si todos los caracteres son minúsculas
print("hola".islower())
print("Hola".islower())

# isupper() - verifica si todos los caracteres son mayúsculas
print("HOLA".isupper())
print("Hola".isupper())

# isnumeric() - verifica si todos los caracteres son numéricos
print("123".isnumeric())
print("½".isnumeric())
print("123a".isnumeric())

# isdecimal() - verifica si todos los caracteres son decimales (0-9)
print("123".isdecimal())
print("½".isdecimal())

# isidentifier() - verifica si la cadena es un identificador válido en Python
print("variable1".isidentifier())
print("1variable".isidentifier())

# isprintable() - verifica si todos los caracteres son imprimibles
print("Hola\n".isprintable())
print("Hola".isprintable())

# maketrans() y translate() - crean y usan tabla de traducción de caracteres
tabla = str.maketrans("aeiou", "12345")
print("hola mundo".translate(tabla))

# zfill() - rellena con ceros a la izquierda hasta longitud dada
s = "42"
print(s.zfill(5))

# lstrip() - elimina espacios (u otros caracteres) a la izquierda
s = "   hola   "
print(s.lstrip())

# rstrip() - elimina espacios (u otros caracteres) a la derecha
print(s.rstrip())