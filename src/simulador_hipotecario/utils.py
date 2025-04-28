import csv
from datetime import datetime

def cargar_valores_uf(ruta_csv):
    """
    Carga los valores de la UF desde un archivo CSV.
    :param ruta_csv: Ruta al archivo CSV con los valores de la UF.
    :return: Diccionario con la fecha como clave (string) y el valor UF como float.
    """
    valores_uf = {}
    try:
        with open(ruta_csv, mode='r', encoding='utf-8') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            next(lector_csv)  # Saltar cabecera
            for fila in lector_csv:
                fecha = fila[0].strip()
                valor_uf = float(fila[1].replace(',', '').strip())
                valores_uf[fecha] = valor_uf
    except FileNotFoundError:
        raise FileNotFoundError(f"No se encontró el archivo: {ruta_csv}")
    except ValueError:
        raise ValueError("Error al procesar el archivo CSV. Verifique el formato de los datos.")
    return valores_uf

# Cargar valores de UF desde archivo
VALORES_UF = cargar_valores_uf('valores_uf.csv')

def obtener_valor_uf(fecha=None):
    """
    Obtiene el valor de la UF para una fecha específica.
    Si no se proporciona fecha, intenta usar la fecha de hoy.
    :return: Tuple (fecha_usada, valor_uf)
    """
    if fecha:
        valor = VALORES_UF.get(fecha)
        if valor is None:
            fecha_mas_reciente = max(VALORES_UF.keys())
            return fecha_mas_reciente, VALORES_UF[fecha_mas_reciente]
        else:
            return fecha, valor
    else:
        hoy = datetime.now().strftime("%Y-%m-%d")
        valor = VALORES_UF.get(hoy)
        if valor is not None:
            return hoy, valor
        else:
            fecha_mas_reciente = max(VALORES_UF.keys())
            return fecha_mas_reciente, VALORES_UF[fecha_mas_reciente]

def validar_float_positivo(valor):
    """Valida que el valor ingresado sea un número flotante positivo."""
    try:
        numero = float(valor)
        if numero > 0:
            return numero
        else:
            raise ValueError
    except ValueError:
        raise ValueError("Debe ingresar un número flotante positivo.")

def validar_entero_positivo(valor):
    """Valida que el valor ingresado sea un número entero positivo."""
    try:
        numero = int(valor)
        if numero > 0:
            return numero
        else:
            raise ValueError
    except ValueError:
        raise ValueError("Debe ingresar un número entero positivo.")
