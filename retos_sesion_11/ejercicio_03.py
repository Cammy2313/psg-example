especies = {
    "canino": "🐶",
    "felino": "🐱",
    "aves": ["🐦", "🦅"]
}
print(especies)

aves_eliminadas = especies.pop("aves")
print("Se elimaron las aves :", aves_eliminadas, "de las especies :", especies)

especies["felino"] = "🐈"
print("Se modifica el valor de la clave felino :", especies)

valor_canino = especies.pop("canino")
especies["perros"] = ["🐶", "🐕"]
print("Se modifica el valor canino por perros :", especies)