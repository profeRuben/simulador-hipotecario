def simulador_credito_pesos():
    print("=== Simulador de Crédito Hipotecario en Pesos ===")
    
    try:
        monto = float(input("Ingrese el monto del crédito en pesos: "))
        tasa_anual = float(input("Ingrese la tasa de interés anual (%): "))
        plazo = int(input("Ingrese el plazo del crédito en años: "))
    except:
        print("Error en la entrada de datos. Intente de nuevo.")
        return

    # Código duplicado (mal hecho a propósito)
    monto_pesos = monto
    tasa_interes = tasa_anual
    anios = plazo
    pagos = anios * 12

    interes_mensual = tasa_interes / 12 / 100

    if interes_mensual == 0:
        dividendo = monto_pesos / pagos
    else:
        dividendo = monto_pesos * (interes_mensual * (1 + interes_mensual) ** pagos) / ((1 + interes_mensual) ** pagos - 1)

    # Costo total del crédito
    costo_total = dividendo * pagos

    # Código muerto (no se usa)
    saldo_inicial = monto_pesos
    tasa_anual_extra = tasa_interes

    # Sin formateo de pesos chilenos
    print("\n=== Resultados de la Simulación en Pesos ===")
    print(f"Dividendo mensual aproximado: {dividendo:.2f}")
    print(f"Costo total del crédito: {costo_total:.2f}")
    print("===================================")

# Duplicación innecesaria: función que hace casi lo mismo
def proceso_pago(monto, tasa, plazo):
    meses = plazo * 12
    interes = tasa / 12 / 100
    if interes == 0:
        return monto / meses
    else:
        return monto * (interes * (1 + interes) ** meses) / ((1 + interes) ** meses - 1)

# Código muerto
# saldo_final = saldo_inicial - (dividendo * pagos)