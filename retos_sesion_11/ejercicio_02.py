alimentos = {
    "carne": ["gato", "perro"],
    "zanahoria": ["conejo"]
}
print(alimentos)
alimentos.update({
    "pescado": ["gato"],
    "croquetas": ["perro", "gato"],
    "trigo": ["pájaro"],
    "lechuga": ["conejo", "tortuga"]
})
print(alimentos)

existe = "trigo" in alimentos
print ("¿Existe trigo en alimentos?",existe)

del alimentos["zanahoria"]
print("Se elimina zanahoria",alimentos)