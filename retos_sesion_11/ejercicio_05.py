arca = {
    "🐶": 2,
    "🐱": 2,
    "🐯": 2,
    "🐵": 2,
    "🦄": 0,
    "🦒": 1
}
print(arca)

arca.update({
    "🦓": 2,
    "🦘": 2,
    "🦚": 2
})
print("Se añadió 3 especies más", arca)

for animal in arca:
    print("Se toma lista de los animales en el arca",animal)

existe = "🐲" in arca
print ("¿Existe 🐲 en el arca?",existe)

del arca["🦄"]
print("Se eliminó la especie unicornio del arca", arca)

arca["🦒"] = 2
print("Se modificó el valor de jirafa", arca)

print("////////////////DILUVIO//////////////////")
arca.clear()
print(arca)