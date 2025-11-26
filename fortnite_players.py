import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Fortnite_players_stats.csv")

st.write("""
# STATS FORTNITE PLAYERS.
## Gráficos usando la base de datos estadística de Fortnite.
""")

#--------------grafico de horas x partidas ganadas --------------#

# --- Preparación de Datos: Top 10 ---

# 1. Seleccionar columnas relevantes
data_plot = df[['Player', 'Solo minutesPlayed', 'Solo top1']].copy()

# 2. Ordenar por Minutos Jugados (descendente) y obtener el Top 10
data_plot = data_plot.sort_values(by='Solo minutesPlayed', ascending=False).head(10)

# 3. Preparar el DataFrame para st.bar_chart
#   a) Establecer 'Player' como índice para que se use como etiqueta del eje X (categoría).
data_plot = data_plot.set_index('Player')

#   b) Seleccionar y renombrar la columna de victorias para el eje Y.
data_plot = data_plot[['Solo top1']].rename(columns={'Solo top1': 'Victorias (Solo Top 1)'})

# --- Creación del Gráfico de Barras Nativo de Streamlit ---

st.subheader('Victorias (Solo Top 1) para el Top 10 de Jugadores por Minutos Jugados')
# st.bar_chart usa el índice (Player) como eje X y las columnas restantes (Victorias) como eje Y.
st.bar_chart(data_plot)

# Opcional: Mostrar los datos subyacentes
st.subheader('Tabla de Datos del Top 10')
# Volvemos a generar la tabla con las tres columnas para mayor claridad
df_top10_display = df.sort_values(by='Solo minutesPlayed', ascending=False).head(10)
st.dataframe(df_top10_display[['Player', 'Solo minutesPlayed', 'Solo top1']].rename(columns={
    'Solo minutesPlayed': 'Minutos Jugados',
    'Solo top1': 'Victorias (Top 1)'
}))
