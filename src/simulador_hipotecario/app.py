from calculadora import calcular_dividendo
from calculadora_pesos import simulador_credito_pesos
from utils import validar_float_positivo, validar_entero_positivo

def simulador_credito_uf():
    print("=== Simulador de Crédito Hipotecario en UF ===")
    try:
        monto_uf = validar_float_positivo(input("Ingrese el monto del crédito en UF: "))
        tasa_anual = validar_float_positivo(input("Ingrese la tasa de interés anual (%): "))
        plazo_anios = validar_entero_positivo(input("Ingrese el plazo en años: "))
    except ValueError as e:
        print(f"Error: {e}")
        return

    dividendo, costo_total = calcular_dividendo(monto_uf, tasa_anual, plazo_anios)
    print("\n=== Resultados de la Simulación en UF ===")
    print(f"Dividendo mensual aproximado: {dividendo:.2f} UF")
    print(f"Costo total del crédito: {costo_total:.2f} UF")
    print("===================================")

def main():
    print("Bienvenido al Simulador de Crédito Hipotecario")
    print("1. Simulación en UF")
    print("2. Simulación en Pesos Chilenos")
    opcion = input("Seleccione una opción (1 o 2): ")

    if opcion == "1":
        simulador_credito_uf()
    elif opcion == "2":
        simulador_credito_pesos()
    else:
        print("Opción inválida.")

if __name__ == "__main__":
    main()
