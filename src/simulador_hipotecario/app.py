from simulador_hipotecario.utils import validar_float_positivo, obtener_valor_uf
from simulador_hipotecario.calculadora import calcular_dividendo
from simulador_hipotecario.calculadora_pesos import simulador_credito_pesos

def formatear_pesos_chileno(valor):
    valor_entero = round(valor)
    return f"{valor_entero:,}".replace(",", "X").replace(".", ",").replace("X", ".")

# Preguntar al usuario qué tipo de crédito desea simular
print("Seleccione el tipo de crédito que desea simular:")
print("1. Crédito en UF")
print("2. Crédito en Pesos")

opcion = input("Ingrese opción [1/2]: ")

if opcion == "2":
    simulador_credito_pesos()
    exit()

# Aquí continúa tu flujo actual intacto (crédito en UF)
fecha_valor_uf, valor_uf = obtener_valor_uf()

print("=== Simulador de Crédito Hipotecario ===")
print(f"Valor de la UF vigente al {fecha_valor_uf}: ${formatear_pesos_chileno(valor_uf)}")
print("Por favor, ingrese los siguientes datos:")

# Solicitar el valor de la propiedad en UF
valor_propiedad_uf = validar_float_positivo(input("1. Ingrese el valor de la propiedad en UF: "))
monto_credito_pesos = valor_propiedad_uf * valor_uf
print(f"El valor de la propiedad en pesos es: ${formatear_pesos_chileno(monto_credito_pesos)}")

# Solicitar la tasa de interés anual
tasa_anual = validar_float_positivo(input("2. Ingrese la tasa de interés anual (en porcentaje): "))

# Solicitar el plazo del crédito en años
plazo_anios = validar_float_positivo(input("3. Ingrese el plazo del crédito en años: "))

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
