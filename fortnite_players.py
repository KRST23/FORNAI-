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
#    Esto define el orden de la línea de tendencia, como usted solicitó.
df_sorted = df.sort_values(by='Solo minutesPlayed', ascending=False).head(50).copy()

# 2. Preparar el DataFrame para el gráfico:
data_plot = df_sorted[['Player', 'Solo minutesPlayed', 'Solo top1']].copy()

# 3. Usar el nombre del jugador como índice (etiquetas del eje X)
#    Esto asegura que las dos líneas estén perfectamente alineadas.
data_plot = data_plot.set_index('Player')

# 4. Renombrar columnas para la leyenda (Las dos líneas a mostrar)
data_plot = data_plot.rename(columns={
    'Solo minutesPlayed': 'Minutos Jugados (Línea 1 - Menor a Mayor)',
    'Solo top1': 'Victorias (Línea 2 - En el mismo orden)'
})

# --- Creación del Gráfico de Líneas Nativo de Streamlit ---

st.subheader('Gráfico de Doble Línea y Ordenamiento Ascendente')
st.warning("⚠️ **Nota:** El eje X intenta mostrar el nombre de los más de 1400 jugadores, por lo que aparecerá muy denso. El orden de los puntos sigue perfectamente la cantidad de minutos jugados de forma ascendente. **Use el cursor para ver el nombre del jugador y los valores exactos.**")

# st.line_chart usa el índice (Jugador) como eje X y las columnas restantes como líneas Y.
st.line_chart(data_plot)

# Opcional: Mostrar los datos subyacentes
st.subheader('Vista Rápida de los Primeros Jugadores')
st.dataframe(data_plot.head())
