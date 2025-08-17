print("=== Arca de Noé ===")
arca = {"🐶": 2, "🐱": 2, "🐯": 2, "🐵": 2, "🦄": 0, "🦒": 1}
print("Arca inicial:")
print(arca)

# Añadir 3 especies más usando update()
arca.update({"🦊": 2, "🐘": 2, "🐧": 2})
print("Arca después de añadir 3 especies:")
print(arca)

print("Lista de animales en el arca:")
iterador = iter(arca.items())
par = next(iterador)
print(par)
par = next(iterador)
print(par)
par = next(iterador)
print(par)
par = next(iterador)
print(par)
par = next(iterador)
print(par)
par = next(iterador)
print(par)
par = next(iterador)
print(par)
par = next(iterador)
print(par)
par = next(iterador)
print(par)

# Verificar si está la especie 'dragon' 🐲
print("¿Existe el dragon 🐲 en el arca?")
existe = '🐲' in arca
print(existe)

# Eliminar la especie unicornio 🦄
print("Eliminar unicornio 🦄 del arca:")
del arca['🦄']
print(arca)

# Modificar el valor de la especie jirafa 🦒 por 2
print("Modificar cantidad de jirafas 🦒 a 2:")
arca['🦒'] = 2
print(arca)

# Vaciar el arca después del diluvio
print("\nVaciar el arca:")
arca.clear()
print(arca)