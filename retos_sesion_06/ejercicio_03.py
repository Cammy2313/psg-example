print("Tabla de verdad - Sistema de Seguridad (Operador lógico utilizado: XOR)")

tarjeta = True
huella = True
print("Tarjeta:", tarjeta, "| Huella:", huella, "| Abrir puerta:", (tarjeta or huella) and not (tarjeta and huella))

tarjeta = True
huella = False
print("Tarjeta:", tarjeta, "| Huella:", huella, "| Abrir puerta:", (tarjeta or huella) and not (tarjeta and huella))

tarjeta = False
huella = True
print("Tarjeta:", tarjeta, "| Huella:", huella, "| Abrir puerta:", (tarjeta or huella) and not (tarjeta and huella))

tarjeta = False
huella = False
print("Tarjeta:", tarjeta, "| Huella:", huella, "| Abrir puerta:", (tarjeta or huella) and not (tarjeta and huella))