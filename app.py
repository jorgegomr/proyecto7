import pandas as pd
import plotly.express as px
import streamlit as st

# Configuración de la página (opcional)
st.set_page_config(page_title="Análisis de Vehículos", layout="wide")

# Título principal de la app
st.title("📊 Análisis de Datos de Vehículos Usados")

# Cargar datos
car_data = pd.read_csv('datasets/vehicles_us.csv')  

# --- HISTOGRAMA ---
st.header("1. Distribución del Kilometraje (Histograma)")
hist_button = st.button('Construir Histograma')  

if hist_button:
    st.write("Este histograma muestra la distribución de los kilometrajes de los vehículos listados.")
    fig_hist = px.histogram(
        car_data, 
        x="odometer",
        title="Distribución del Kilometraje",
        labels={"odometer": "Kilometraje (millas)"}
    )
    st.plotly_chart(fig_hist, use_container_width=True)

# --- GRÁFICO DE DISPERSIÓN ---
st.header("2. Relación Kilometraje vs Precio (Scatter Plot)")
scatter_button = st.button('Construir Gráfico de Dispersión')  

if scatter_button:
    st.write("Este gráfico explora la relación entre el precio y el kilometraje de los vehículos.")
    fig_scatter = px.scatter(
        car_data,
        x="odometer",
        y="price",
        title="Kilometraje vs Precio",
        labels={"odometer": "Kilometraje (millas)", "price": "Precio (USD)"},
        color="condition",  # Colorear por condición
        hover_name="model"   # Mostrar modelo al pasar el mouse
    )
    st.plotly_chart(fig_scatter, use_container_width=True)