# 🌳 Analizador de Árboles de Decisión

<p align="center">
  <img src="https://img.shields.io/badge/python-3776AB.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/streamlit-FF4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"/>
</p>

Una aplicación interactiva en **Streamlit** para evaluar **árboles de decisión** con nodos de azar, probabilidades y análisis de escenarios económicos.  

## 🚀 Características Principales

- **Interfaz intuitiva** con diseño responsive  
- **Definición de la decisión principal**  
- **Configuración de dos nodos de azar** con tres ramas cada uno  
- **Cálculo automático de valores esperados**  
- **Visualización gráfica** del árbol de decisión en tiempo real  
- **Análisis comparativo** de alternativas (mejor/peor escenario)  
- **Recomendación automática** basada en el mayor valor esperado  
- **Resumen tabular interactivo** con métricas de cada alternativa

## 📚 Conceptos Clave  

Un **árbol de decisión** es una herramienta que permite representar gráficamente decisiones, eventos inciertos y resultados esperados.  

**Componentes principales:**  
- 🔵 **Nodos de decisión**: donde se elige entre alternativas  
- 🟠 **Nodos de azar**: donde ocurren eventos inciertos con probabilidades  
- 🟢 **Resultados finales**: beneficios o costos asociados a cada escenario  

## 📦 Requisitos  

- Python **3.10+**  
- Dependencias:  
  - `streamlit>=1.13.0`  
  - `pandas>=1.5.0`  
  - `graphviz>=0.20`  

Instálalas manualmente o con `requirements.txt`.  

## 🛠️ Instalación

1. Clona el repositorio:
 ```bash
 git clone https://github.com/tu-usuario/tu-repositorio.git
 cd tu-repositorio
 ```
2. Instala las dependencias
 ```bash
 pip install -r requirements.txt
 ```
3. Ejecuta la aplicación localmente
 ```bash
streamlit run app.py
 ```

## 🖥️ Uso de la Aplicación
### 1. Definir decisión principal
Ejemplo: **Invertir en nuevo proyecto**

### 2. Configurar nodos de azar
- Describe cada evento incierto  
  *(Ejemplo: Demanda del mercado, Costos de producción)*
  
### 3. Ingresar probabilidades
- Asigna probabilidades para cada rama  
- ⚠️ **Deben sumar 1.0**
  
### 4. Definir valores económicos
- Ingresa ganancias o costos asociados a cada resultado

### 5. Analizar resultados
- Se calculan automáticamente los **valores esperados**  
- Se muestran el **mejor y peor escenario**  
- La app recomienda la **opción con mayor beneficio esperado**

### 6. Explorar el diagrama del árbol
- El árbol se genera dinámicamente con **Graphviz**  
- Incluye ramas, probabilidades y resultados
  
## 📊 Ejemplo de Resultados

| Nodo                 | Valor Esperado | Mejor Escenario | Peor Escenario |
| -------------------- | -------------: | --------------: | -------------: |
| Demanda del mercado  |      52,000.00 |         100,000 |        -20,000 |
| Costos de producción |      64,000.00 |          80,000 |         30,000 |

💡 Recomendación: elegir la opción con el mayor valor esperado.

## 📌 Notas Importantes

- Las probabilidades deben sumar 1.0 (100%) para cada nodo de azar
- Los valores económicos deben ser consistentes (todos ingresos o todos costos)
- La versión actual soporta 2 nodos de azar con 3 ramas cada uno

## 📜 Licencia
Este proyecto es de uso libre para fines académicos y educativos.
