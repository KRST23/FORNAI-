import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Fortnite_players_stats.csv")

st.write("""
# STATS FORTNITE PLAYERS.
## Gráficos usando la base de datos estadística de Fortnite.
""")

#--------------grafico de horas x partidas ganadas --------------#
# 1. Ordenar por "Solo minutesPlayed" y seleccionar el Top 10 (DESCENDENTE para encontrar a los más altos)
top_10_players = df.sort_values(by='Solo minutesPlayed', ascending=False).head(100).copy()

# 2. Preparar el DataFrame para el gráfico:
data_plot = top_10_players[['Player', 'Solo minutesPlayed', 'Solo top1']].copy()

# 3. Usar el nombre del jugador como índice (etiquetas del eje X)
data_plot = data_plot.set_index('Player')

# 4. Renombrar columnas para la leyenda
data_plot = data_plot.rename(columns={
    'Solo minutesPlayed': 'Minutos Jugados (Solo)',
    'Solo top1': 'Victorias (Solo Top 1)'
})

# 5. ¡NUEVO! Ordenar el DataFrame por "Minutos Jugados (Solo)" de menor a mayor (ASCENDENTE)
data_plot = data_plot.sort_values(by='Minutos Jugados (Solo)', ascending=True)

# --- Creación del Gráfico de Líneas Nativo de Streamlit ---

st.subheader('Comparativa de Minutos Jugados vs. Victorias (Top 1)')
st.warning("Advertencia: Debido a que los 'Minutos Jugados' son mucho mayores que las 'Victorias', la línea de 'Victorias' aparecerá cerca de la base. Use el cursor para ver el valor exacto.")

# st.line_chart usa el índice (Jugador) como eje X y las columnas restantes como líneas Y.
st.line_chart(data_plot)

# Opcional: Mostrar los datos subyacentes
st.subheader('Detalle de los 10 Jugadores (Ordenados por Minutos Jugados Ascendente)')
st.dataframe(data_plot)
