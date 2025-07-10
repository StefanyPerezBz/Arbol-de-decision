# 🌳 Analizador de Árboles de Decisión

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/tu-usuario/tu-repositorio/app.py)

Una aplicación interactiva para evaluar árboles de decisión con nodos de azar y análisis de escenarios.

## 🚀 Características Principales

- **Interfaz intuitiva** con diseño responsive
- **Configuración de dos nodos de azar** con tres ramas cada uno
- **Cálculo automático** de valores esperados
- **Visualización gráfica** del árbol de decisión
- **Análisis comparativo** de alternativas
- **Recomendación inteligente** basada en valores esperados

## 📦 Requisitos

- Python 3.10+
- Dependencias:
1. streamlit>=1.13.0
2. pandas>=1.5.0
3. graphviz>=0.20

## 🖥️ Uso de la Aplicación
- Define la decisión principal en el campo de texto

- Configura los nodos de azar:

   - Describe cada evento incierto

   - Establece probabilidades (deben sumar 1.0)

   - Define valores económicos para cada resultado

- Analiza los resultados:

   - Valores esperados para cada alternativa

   - Mejor/peor escenario posible

   - Recomendación automatizada

- Explora el diagrama del árbol generado