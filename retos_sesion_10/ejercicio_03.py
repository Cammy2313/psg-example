tienda_fisica = ["Ana", "Luis", "Pedro", "María", "Juan"]
tienda_online = ["Pedro", "María", "Ana", "Carlos", "Laura"]

fisica = set(tienda_fisica)
online = set(tienda_online)

ambos = fisica & online
solo_fisica = fisica - online
solo_online = online - fisica

print("Ambos canales:", ambos)
print("Solo tienda física:", solo_fisica)
print("Solo tienda online:", solo_online)