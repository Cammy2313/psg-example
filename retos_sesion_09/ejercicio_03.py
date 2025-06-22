print("Lista de personas")
personas = ["Ana", "Luis", "Carlos", "Pedro", "Lucía", "María", "José", "Sofía", "Diego", "Andrés"]
print(personas)

print("1. Sublista de personas del índice 5 al 9 con salto de 2")
sub_lista = personas[5:10:2]
print(sub_lista)

print("2. ¿Está 'José' en la lista original?")
print("José" in personas)

print("3. Sublista ordenada alfabéticamente (A-Z)")
sub_lista.sort()
print(sub_lista)

print("4. Lista original ordenada de forma descendente (Z-A)")
personas.sort(reverse=True)
print(personas)