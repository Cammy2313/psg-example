edad = int(input("Edad del cliente: "))
compra = float(input("Monto de la compra: "))

if edad > 60 and compra > 1000:
    descuento = 0.20
elif 18 <= edad <= 60 and compra > 500:
    descuento = 0.10
else:
    descuento = 0.02

monto_final = compra - (compra * descuento)
print("Monto con descuento:", monto_final)