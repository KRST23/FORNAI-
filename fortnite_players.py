import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Fortnite_players_stats.csv")

st.write("""
# STATS FORTNITE PLAYERS.
## Gráficos usando la base de datos estadística de Fortnite.
""")

#--------------grafico de horas x partidas ganadas --------------#

#--- Preparación de Datos ---
# 1. Seleccionamos las columnas necesarias.
data_plot = df[['Solo minutesPlayed', 'Solo top1']].copy()

# 2. Para que el gráfico de Streamlit use "Solo minutesPlayed" como el eje X (la base de la tendencia),
#    establecemos esa columna como índice (etiquetas del eje X).
data_plot = data_plot.set_index('Solo minutesPlayed')

# 3. Renombramos la columna restante para que sea un buen título de leyenda.
data_plot = data_plot.rename(columns={'Solo top1': 'Victorias (Solo Top 1)'})

# 4. Ordenamos por el nuevo índice (Minutos Jugados) para asegurar una línea de tendencia clara.
data_plot = data_plot.sort_index()

# --- Creación del Gráfico de Líneas Nativo de Streamlit ---

st.subheader('Victorias (Solo Top 1) por Minutos Jugados')
# st.line_chart usa el índice (Minutos Jugados) como eje X y las columnas restantes (Victorias) como eje Y.
st.line_chart(data_plot)

# Opcional: Mostrar los datos subyacentes
st.subheader('Datos Utilizados')
st.dataframe(data_plot.head(10))
