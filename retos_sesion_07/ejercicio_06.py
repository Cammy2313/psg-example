#Ejemplo A: .capitalize()
texto = "hola mundo"
print("Capitalizado:", texto.capitalize())
#Ejemplo B: .count()
frase = "El velo del cielo es bello"
print("Cantidad de 'el':", frase.count("el"))
#Ejemplo C: .startswith() y .endswith()
print("¿Empieza con 'El'? ", frase.startswith("El"))
print("¿Termina con 'bello'? ", frase.endswith("bello"))
#Ejemplo D: .replace()
nueva = frase.replace("bello", "hermoso")
print("Frase modificada:", nueva)
#Ejemplo E: .title()
print("Estilo título:", frase.title())