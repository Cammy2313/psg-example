jane = {"Lemon Pie", "Brownie", "Tarta de Manzana", "Helado de Chocolate", "Flan"}
jhon = {"Carrot Cake", "Croissant de Chocolate", "Lemon Pie", "Tarta de Manzana", "Pudding"}

comunes = jane & jhon
porcentaje = len(comunes) / len(jane) * 100

print("Postres en común:", comunes)
print("Porcentaje de compatibilidad:", porcentaje)

print("¿Son compatibles?:", porcentaje > 50)