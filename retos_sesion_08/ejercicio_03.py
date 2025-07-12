ingresar_pregunta = input("Ingresa una pregunta: ")
pregunta = tuple(ingresar_pregunta)

pregunta_completa = ('¿', ) + pregunta + ('?', )

print("Pregunta en tupla:", pregunta_completa)

pregunta_repetida = pregunta_completa * 2
print("Pregunta repetida:", pregunta_repetida)