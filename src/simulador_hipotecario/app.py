from simulador_hipotecario.utils import validar_float_positivo, obtener_valor_uf
from simulador_hipotecario.calculadora import calcular_dividendo

def formatear_pesos_chileno(valor):
    """
    Formatea un número como pesos chilenos: separador de miles con punto,
    sin decimales.
    """
    valor_entero = round(valor)
    return f"{valor_entero:,}".replace(",", "X").replace(".", ",").replace("X", ".")

# Obtener el valor de la UF vigente y la fecha correspondiente
fecha_valor_uf, valor_uf = obtener_valor_uf()

print("=== Simulador de Crédito Hipotecario ===")
print(f"Valor de la UF vigente al {fecha_valor_uf}: ${formatear_pesos_chileno(valor_uf)}")
print("Por favor, ingrese los siguientes datos:")

# Solicitar el valor de la propiedad en UF
print("1. Ingrese el valor de la propiedad en UF:")
valor_propiedad_uf = validar_float_positivo(input("Valor en UF: "))
monto_credito_pesos = valor_propiedad_uf * valor_uf
print(f"El valor de la propiedad en pesos es: ${formatear_pesos_chileno(monto_credito_pesos)}")

# Solicitar la tasa de interés anual
print("2. Ingrese la tasa de interés anual (en porcentaje):")
tasa_anual = validar_float_positivo(input("Tasa de interés anual (%): "))

# Solicitar el plazo del crédito en años
print("3. Ingrese el plazo del crédito en años:")
plazo_anios = validar_float_positivo(input("Plazo (años): "))

# Calcular el dividendo mensual y el costo total del crédito
dividendo_mensual, costo_total = calcular_dividendo(monto_credito_pesos, tasa_anual, plazo_anios)

# Mostrar los resultados
print("\n=== Resultados de la Simulación ===")
print(f"Valor propiedad en UF ingresado: {valor_propiedad_uf} UF")
print(f"Valor propiedad en pesos: ${formatear_pesos_chileno(monto_credito_pesos)}")
print(f"Tasa anual utilizada: {tasa_anual}%")
print(f"Plazo del crédito: {plazo_anios} años")
print(f"Dividendo mensual aproximado: ${formatear_pesos_chileno(dividendo_mensual)}")
print(f"Costo total del crédito: ${formatear_pesos_chileno(costo_total)}")
print("===================================")
