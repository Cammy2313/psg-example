class FondosInsuficientesError(Exception):
    pass

def cajero():
    saldo = 500
    while True:
        entrada = input("Monto a retirar (o 'salir' para terminar): ")
        if entrada.lower() == "salir":
            print("Operación finalizada.")
            break
        try:
            monto = float(entrada)
            if monto > saldo:
                raise FondosInsuficientesError("No hay fondos suficientes.")
            if monto > 1000:
                raise Exception("El monto excede el límite permitido por transacción.")
            saldo = saldo - monto
            print(f"Retiraste {monto}. Saldo restante: {saldo}")
        except ValueError:
            print("Error: ingresa un número válido.")
        except FondosInsuficientesError as e:
            print("Error:", e)
        except Exception as e:
            print("Error:", e)

cajero()
