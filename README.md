# Simulador de Crédito Hipotecario 🏡

Este proyecto es un simulador simple de crédito hipotecario desarrollado en Python. Permite calcular el dividendo mensual y el costo total de un crédito hipotecario basado en el monto solicitado, la tasa de interés anual y el plazo en años.

## 📚 Descripción

El simulador ofrece dos modalidades:
- **Simulación en UF**: utilizando una estructura limpia de programación.
- **Simulación en Pesos**: estructura alternativa para cálculos en moneda nacional.

El usuario puede seleccionar el tipo de simulación que desea realizar desde un menú interactivo.

## 📂 Estructura del Proyecto

- `src/simulador_hipotecario/app.py`: Menú principal para seleccionar la modalidad de simulación.
- `src/simulador_hipotecario/calculadora.py`: Funciones para el cálculo de dividendos en UF.
- `src/simulador_hipotecario/calculadora_pesos.py`: Funciones para el cálculo de dividendos en Pesos.
- `src/simulador_hipotecario/utils.py`: Utilidades generales, validaciones de entrada y carga de datos de UF.
- `requirements.txt`: Dependencias mínimas utilizadas en el proyecto.
- `pyproject.toml`: Configuración básica del proyecto para instalación opcional.

## 🚀 Instalación y Configuración

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/profeRuben/simulador-hipotecario.git
   cd simulador-hipotecario
   ```

2. (Opcional) Crear y activar un entorno virtual:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instalar dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Ejecución del Programa

Desde la raíz del proyecto, abrir una terminal y ejecutar:

```bash
python3 src/simulador_hipotecario/app.py
```

El sistema solicitará al usuario seleccionar:
- **1** para simular un crédito en UF.
- **2** para simular un crédito en Pesos.

Luego pedirá los datos necesarios para realizar los cálculos y entregará los resultados en pantalla.

## 📋 Autor

- profe Rubén
