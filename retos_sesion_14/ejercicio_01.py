def promedio(lista):
    suma = sum(lista)
    return suma / len(lista)

calificaciones = [50, 75, 80, 91, 70]
print("Lista de calificaciones:",calificaciones)
print("El promedio es:", promedio(calificaciones))