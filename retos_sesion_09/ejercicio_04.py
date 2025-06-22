print("Lista de productos y precios")
productos = ["Oreo", "Chizitos", "Bon Bon Bum", "Trululú"]
precios = [1.5, 2.0, 0.5, 1.2]
print(productos)
print(precios)

print("1. Agregar dos productos nuevos")
productos.append("Snickers")
precios.append(2.5)
productos.append("M&M")
precios.append(2.3)
print(productos)
print(precios)

print("2. Eliminar 'Bon Bon Bum'")
index_bonbon = productos.index("Bon Bon Bum")
productos.pop(index_bonbon)
precios.pop(index_bonbon)
print(productos)
print(precios)

print("3. Precio de 'Oreo' y 'Chizitos'")
print("Oreo:", precios[productos.index("Oreo")])
print("Chizitos:", precios[productos.index("Chizitos")])

print("4. Producto más caro y más barato")
mas_caro = max(precios)
mas_barato = min(precios)
print("Más caro:", productos[precios.index(mas_caro)], mas_caro)
print("Más barato:", productos[precios.index(mas_barato)], mas_barato)

print("5. Cantidad total de productos")
print(len(productos))

print("6. Costo total de todos los productos")
print(sum(precios))

# print("Ordenar productos por precio (de menor a mayor)")
# productos_ordenados = []
# precios_ordenados = []

# menor = min(precios) 
# indice = precios.index(menor)
# productos_ordenados.append(productos.pop(indice))
# precios_ordenados.append(precios.pop(indice))

print("7. Ordenar productos y precios del más barato al más caro")
productos_ordenados = []
precios_ordenados = []

for _ in range(len(precios)):
     precio_menor = min(precios)
     indice = precios.index(precio_menor)
     productos_ordenados.append(productos.pop(indice))
     precios_ordenados.append(precios.pop(indice))

print(productos_ordenados)
print(precios_ordenados)

print("8. Eliminar todos los productos")
productos.clear()
precios.clear()
print(productos)
print(precios)
