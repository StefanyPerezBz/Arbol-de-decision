import streamlit as st
import pandas as pd
import graphviz
from io import StringIO

# Configuración de la página
st.set_page_config(
    page_title="Analizador de Árboles de Decisión",
    page_icon="🌳",
    layout="wide"
)

# Estilos CSS personalizados
st.markdown("""
<style>
    .header {
        color: #2E86C1;
        font-size: 24px;
        font-weight: bold;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .decision-node {
        background-color: #3498DB;
        color: white;
        padding: 8px;
        border-radius: 5px;
        font-weight: bold;
        text-align: center;
    }
    .chance-node {
        background-color: #F39C12;
        color: white;
        padding: 8px;
        border-radius: 50%;
        width: 40px;
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto;
    }
    .result-node {
        background-color: #2ECC71;
        color: white;
        padding: 8px;
        border-radius: 5px;
        text-align: center;
    }
    .metric-box {
        background-color: #F8F9F9;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Título principal
st.title("🌳 Analizador de Árboles de Decisión")
st.markdown("""
Esta herramienta te permite evaluar un árbol de decisión con:
- **Nodos de decisión**: Donde puedes elegir entre alternativas
- **Nodos de azar**: Donde ocurren eventos inciertos con probabilidades
- **Ramas de estado**: Posibles resultados de cada nodo
""")

# Sidebar con información teórica
with st.sidebar:
    st.header("📚 Conceptos Clave")
    st.markdown("""
    **Árbol de decisión**: Representación esquemática que facilita la toma de decisiones considerando:
    - Alternativas disponibles
    - Eventos inciertos
    - Probabilidades
    - Resultados esperados

    **Componentes**:
    - 🔵 Nodos de decisión (cuadrados)
    - 🟠 Nodos de azar (círculos)
    - 🟢 Resultados finales
    """)

# Creación del árbol de decisión
st.markdown('<div class="header">🔷 Paso 1: Definir la Decisión Principal</div>', unsafe_allow_html=True)
main_decision = st.text_input("Describe la decisión principal que necesitas tomar:", "Invertir en nuevo proyecto")

# Contenedor principal
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown('<div class="header">🔶 Paso 2: Configurar Nodos de Azar</div>', unsafe_allow_html=True)

    # Nodo de azar 1
    st.markdown('<div class="chance-node">1</div>', unsafe_allow_html=True)
    chance_node1 = st.text_input("Descripción nodo de azar 1:", "Demanda del mercado")

    # Ramas para nodo 1
    st.write("**Ramas de estado (3 posibles resultados):**")
    c1_prob1 = st.number_input("Probabilidad Rama 1 - Nodo 1", 0.0, 1.0, 0.3)
    c1_value1 = st.number_input("Valor económico Rama 1 - Nodo 1", value=100000)
    c1_prob2 = st.number_input("Probabilidad Rama 2 - Nodo 1", 0.0, 1.0, 0.5)
    c1_value2 = st.number_input("Valor económico Rama 2 - Nodo 1", value=50000)
    c1_prob3 = st.number_input("Probabilidad Rama 3 - Nodo 1", 0.0, 1.0, 0.2)
    c1_value3 = st.number_input("Valor económico Rama 3 - Nodo 1", value=-20000)

    # Validar probabilidades
    if abs((c1_prob1 + c1_prob2 + c1_prob3) - 1.0) > 0.001:
        st.warning(f"Las probabilidades suman {c1_prob1 + c1_prob2 + c1_prob3:.2f}. Deberían sumar 1.0")

    # Nodo de azar 2
    st.markdown('<div class="chance-node">2</div>', unsafe_allow_html=True)
    chance_node2 = st.text_input("Descripción nodo de azar 2:", "Costos de producción")

    # Ramas para nodo 2
    st.write("**Ramas de estado (3 posibles resultados):**")
    c2_prob1 = st.number_input("Probabilidad Rama 1 - Nodo 2", 0.0, 1.0, 0.4)
    c2_value1 = st.number_input("Valor económico Rama 1 - Nodo 2", value=80000)
    c2_prob2 = st.number_input("Probabilidad Rama 2 - Nodo 2", 0.0, 1.0, 0.4)
    c2_value2 = st.number_input("Valor económico Rama 2 - Nodo 2", value=60000)
    c2_prob3 = st.number_input("Probabilidad Rama 3 - Nodo 2", 0.0, 1.0, 0.2)
    c2_value3 = st.number_input("Valor económico Rama 3 - Nodo 2", value=30000)

    # Validar probabilidades
    if abs((c2_prob1 + c2_prob2 + c2_prob3) - 1.0) > 0.001:
        st.warning(f"Las probabilidades suman {c2_prob1 + c2_prob2 + c2_prob3:.2f}. Deberían sumar 1.0")

with col2:
    st.markdown('<div class="header">📊 Paso 3: Resultados y Análisis</div>', unsafe_allow_html=True)

    # Calcular valores esperados
    expected_value1 = c1_prob1 * c1_value1 + c1_prob2 * c1_value2 + c1_prob3 * c1_value3
    expected_value2 = c2_prob1 * c2_value1 + c2_prob2 * c2_value2 + c2_prob3 * c2_value3

    # Mostrar métricas
    col_metric1, col_metric2 = st.columns(2)
    with col_metric1:
        st.markdown(f"""
        <div class="metric-box">
        <b>Valor Esperado Nodo 1</b><br>
        {expected_value1:,.2f}
        </div>
        """, unsafe_allow_html=True)

    with col_metric2:
        st.markdown(f"""
        <div class="metric-box">
        <b>Valor Esperado Nodo 2</b><br>
        {expected_value2:,.2f}
        </div>
        """, unsafe_allow_html=True)

    # Recomendación
    best_option = "Nodo 1" if expected_value1 > expected_value2 else "Nodo 2"
    best_value = max(expected_value1, expected_value2)

    st.markdown(f"""
    <div class="metric-box" style="background-color: #E8F8F5;">
    <b>💡 Recomendación:</b> La mejor opción es <b>{best_option}</b> con un valor esperado de <b>{best_value:,.2f}</b>
    </div>
    """, unsafe_allow_html=True)

    # Visualización del árbol
    st.markdown('<div class="header">🌳 Diagrama del Árbol de Decisión</div>', unsafe_allow_html=True)

    dot = graphviz.Digraph()
    dot.attr(rankdir='LR')  # De izquierda a derecha

    # Nodo de decisión principal
    dot.node('D', main_decision, shape='box', style='filled', color='#3498DB', fontcolor='white')

    # Nodo de azar 1
    dot.node('C1', chance_node1, shape='ellipse', style='filled', color='#F39C12', fontcolor='white')
    dot.edge('D', 'C1', label=f"Invertir en {main_decision}")

    # Ramas nodo 1
    dot.node('C1_1', f"{c1_value1:,.0f}\n({c1_prob1:.0%})", shape='none')
    dot.edge('C1', 'C1_1', label="Alta demanda")

    dot.node('C1_2', f"{c1_value2:,.0f}\n({c1_prob2:.0%})", shape='none')
    dot.edge('C1', 'C1_2', label="Demanda media")

    dot.node('C1_3', f"{c1_value3:,.0f}\n({c1_prob3:.0%})", shape='none')
    dot.edge('C1', 'C1_3', label="Baja demanda")

    # Nodo de azar 2
    dot.node('C2', chance_node2, shape='ellipse', style='filled', color='#F39C12', fontcolor='white')
    dot.edge('D', 'C2', label="Alternativa")

    # Ramas nodo 2
    dot.node('C2_1', f"{c2_value1:,.0f}\n({c2_prob1:.0%})", shape='none')
    dot.edge('C2', 'C2_1', label="Costos bajos")

    dot.node('C2_2', f"{c2_value2:,.0f}\n({c2_prob2:.0%})", shape='none')
    dot.edge('C2', 'C2_2', label="Costos medios")

    dot.node('C2_3', f"{c2_value3:,.0f}\n({c2_prob3:.0%})", shape='none')
    dot.edge('C2', 'C2_3', label="Costos altos")

    st.graphviz_chart(dot)

    # Tabla resumen
    st.markdown('<div class="header">📋 Resumen de Alternativas</div>', unsafe_allow_html=True)

    summary_data = {
        'Nodo': [chance_node1, chance_node2],
        'Valor Esperado': [expected_value1, expected_value2],
        'Mejor Escenario': [max(c1_value1, c1_value2, c1_value3), max(c2_value1, c2_value2, c2_value3)],
        'Peor Escenario': [min(c1_value1, c1_value2, c1_value3), min(c2_value1, c2_value2, c2_value3)]
    }

    st.dataframe(pd.DataFrame(summary_data).style.format({
        'Valor Esperado': '{:,.2f}',
        'Mejor Escenario': '{:,.2f}',
        'Peor Escenario': '{:,.2f}'
    }), use_container_width=True)

# Información adicional
with st.expander("📌 ¿Cómo interpretar los resultados?"):
    st.markdown("""
    1. **Valor Esperado**: Representa el resultado promedio que puedes esperar considerando todas las probabilidades.
    2. **Mejor Escenario**: El resultado más favorable posible para cada alternativa.
    3. **Peor Escenario**: El resultado menos favorable posible para cada alternativa.

    **Recomendación**: La aplicación compara los valores esperados y te sugiere la opción con mayor beneficio esperado.
    """)

# Notas finales
st.markdown("---")
st.markdown("""
**Notas**:
- Los valores económicos deben ser consistentes (todos ingresos o todos costos)
- Las probabilidades deben sumar exactamente 1 (100%) para cada nodo
- Esta herramienta considera dos nodos de azar con tres ramas cada uno
""")