# Simulador de Crédito Hipotecario 🏡

Este proyecto es un simulador simple de crédito hipotecario desarrollado en Python, pensado tanto para propósitos educativos como para ejercicios de análisis de calidad de código.

## 📚 Descripción

El proyecto permite a los usuarios simular un crédito hipotecario de dos formas:
- **Simulación en UF**: utilizando un flujo limpio, siguiendo buenas prácticas de programación.
- **Simulación en Pesos**: utilizando un flujo con errores intencionados, útil para prácticas de detección de problemas mediante herramientas como SonarQube.

Los errores intencionados incluyen código duplicado, código muerto y estructuras redundantes, permitiendo realizar análisis de calidad de software.

## 📂 Estructura del Proyecto

- `src/simulador_hipotecario/app.py`: Menú principal para seleccionar entre simulación limpia o con errores.
- `src/simulador_hipotecario/calculadora.py`: Funciones limpias para simulación en UF.
- `src/simulador_hipotecario/calculadora_pesos.py`: Funciones con errores para simulación en Pesos.
- `src/simulador_hipotecario/utils.py`: Funciones de utilidades, validaciones y carga de datos UF.
- `requirements.txt`: Dependencias para desarrollo y testing.
- `pyproject.toml`: Configuración del proyecto para instalación.

## 🚀 Instalación y Configuración

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/profeRuben/simulador-hipotecario.git
   cd simulador-hipotecario
