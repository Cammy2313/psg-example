print("Tupla de estudiantes")
estudiantes = [('Miguel', 51), ('Daniel', 80), ('Virginia', 90), ('Franco', 40), ('Flabio', 30)]
print(estudiantes)
for nombre, nota in estudiantes:
    if nota >= 51:
        print(f"¡Felicitaciones, {nombre}! aprobaste con {nota}")