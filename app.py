# ==========================================
# LABORATORIO 13 - BUSINESS INTELLIGENCE
# FASE 4 - DASHBOARD CON STREAMLIT
# ==========================================

# Importar librerías
import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar el dataset
df = pd.read_csv('citas_medicas.csv')

# ==========================================
# TÍTULO DEL DASHBOARD
# ==========================================

st.title("Dashboard de Gestión de Citas Médicas")

# ==========================================
# GRÁFICO 1
# Citas por Especialidad
# ==========================================

st.subheader("Citas por Especialidad")

fig1 = px.bar(
    df['especialidad'].value_counts(),
    labels={'value':'Cantidad'}
)

st.plotly_chart(fig1)

# ==========================================
# GRÁFICO 2
# Estado de las Citas
# ==========================================

st.subheader("Estado de las Citas")

fig2 = px.pie(
    df,
    names='estado'
)

st.plotly_chart(fig2)

# ==========================================
# GRÁFICO 3
# Citas por Mes
# ==========================================

df['fecha'] = pd.to_datetime(df['fecha'])
df['mes'] = df['fecha'].dt.month

citas_mes = df.groupby('mes').size().reset_index(name='cantidad')

st.subheader("Citas por Mes")

fig3 = px.line(
    citas_mes,
    x='mes',
    y='cantidad',
    markers=True
)

st.plotly_chart(fig3)