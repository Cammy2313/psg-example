nombre = input("Nombre: ")
telefono = input("Teléfono: ")

if nombre and len(telefono) == 13 and telefono.startswith("+"):
    print("Contacto guardado")
else:
    print("Datos incorrectos")