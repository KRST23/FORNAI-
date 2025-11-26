import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Fortnite_players_stats.csv")

st.write("""
# STATS FORTNITE PLAYERS.
## Gráficos usando la base de datos estadística de Fortnite.
""")

#--------------grafico de horas x partidas ganadas --------------#

# 1. Ordenar toda la base de datos por "Solo minutesPlayed" de menor a mayor (ascendente)
df_sorted = df.sort_values(by='Solo minutesPlayed', ascending=True).copy()

# 2. Preparar el DataFrame para el gráfico:
#    *** Solo incluimos 'Solo minutesPlayed' como línea a mostrar. ***
data_plot = df_sorted[['Player', 'Solo minutesPlayed']].copy()

# 3. Usar el nombre del jugador como índice (etiquetas del eje X)
data_plot = data_plot.set_index('Player')

# 4. Renombrar la columna para la leyenda
data_plot = data_plot.rename(columns={
    'Solo minutesPlayed': 'Minutos Jugados (Orden Ascendente)'
})

# --- Creación del Gráfico de Líneas Nativo de Streamlit ---

st.subheader('Visualización del Total de Minutos Jugados')
st.warning("⚠️ **Nota:** El eje X intenta mostrar el nombre de más de 1400 jugadores, por lo que estará muy denso. Use el cursor sobre la línea para ver el nombre del jugador y el valor exacto de minutos jugados. ")

# st.line_chart usa el índice (Jugador) como eje X y la columna restante como línea Y.
st.line_chart(data_plot)

# Opcional: Mostrar los datos subyacentes
st.subheader('Vista Rápida de los Jugadores con Menos Minutos Jugados')
st.dataframe(data_plot.head(10))
