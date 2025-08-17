productos = ["Chizitos", "Bon Bon Bum", "Oreo", "Galleta Animalitos"]
precios = [2.5, 1.0, 3.5, 2.0]
print("Lista de productos y precios")
print(productos, precios)

# 1. Agregar 2 productos nuevos al final de las listas
productos.append("Rocklets")
precios.append(4.0)

productos.append("Snickers")
precios.append(3.0)
print("Se agregaron dos productos nuevos:", productos, precios)

# 2. Eliminar el producto "Bon Bon Bum" de las listas
indice_bonbonbum = productos.index("Bon Bon Bum")
productos.pop(indice_bonbonbum)
precios.pop(indice_bonbonbum)
print("Se elimino el producto 'Bon Bon Bum':", productos, precios)

# 3. ¿Cuánto cuesta el producto "Oreo" y "Chizitos"?
indice_oreo = productos.index("Oreo")
indice_chizitos = productos.index("Chizitos")
print("Precio de 'Oreo':")
print(precios[indice_oreo])
print("Precio de 'Chizitos':")
print(precios[indice_chizitos])

# 4. ¿Cuál es el producto más caro y el más barato?
precio_max = max(precios)
precio_min = min(precios)
indice_max = precios.index(precio_max)
indice_min = precios.index(precio_min)
print("El producto más caro es:")
print(productos[indice_max])
print("El producto más barato es:")
print(productos[indice_min])

# 5. ¿Cuántos productos tienes en total?
print("Cantidad de productos en total:")
print(len(productos))

# 6. ¿Cuánto cuestan todos los productos?
print("Precio total de los productos:")
print(sum(precios))

# 7. Ordena los productos y precios del más barato al más caro
precios_ordenados = precios[:]
precios_ordenados.sort()

productos_ordenados = []
indice0 = precios.index(precios_ordenados[0])
productos_ordenados.append(productos[indice0])

precios_temp = precios[:]
productos_temp = productos[:]
precios_temp.pop(indice0)
productos_temp.pop(indice0)

indice1 = precios_temp.index(precios_ordenados[1])
productos_ordenados.append(productos_temp[indice1])

precios_temp.pop(indice1)
productos_temp.pop(indice1)

indice2 = precios_temp.index(precios_ordenados[2])
productos_ordenados.append(productos_temp[indice2])

precios_temp.pop(indice2)
productos_temp.pop(indice2)

indice3 = precios_temp.index(precios_ordenados[3])
productos_ordenados.append(productos_temp[indice3])

precios_temp.pop(indice3)
productos_temp.pop(indice3)

productos_ordenados.append(productos_temp[0])

print("Productos y precios del más barato al más caro:")
print(productos_ordenados)
print(precios_ordenados)

# 8. Eliminar todos los productos de las listas
productos.clear()
precios.clear()
print("Eliminar todos los productos")
print(productos)
print(precios)