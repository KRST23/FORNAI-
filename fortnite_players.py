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

# 2. Preparamos el DataFrame (no necesitamos indexarlo por nombre de jugador para este plot)
data_plot = df_sorted[['Solo minutesPlayed']].copy()

# --- Creación del Gráfico Personalizado con Matplotlib ---

# ⚠️ ADVERTENCIA: Este gráfico es estático y no tiene la funcionalidad de tooltip.
st.warning("⚠️ **Advertencia:** Este gráfico es **estático**. Para lograr este estilo, se desactivó la mini pestaña interactiva (tooltip).")

fig, ax = plt.subplots(figsize=(12, 6))

# Trazar la línea:
# Eje X: El índice (la secuencia de jugadores ordenados, de 0 a 1434)
# Eje Y: Los Minutos Jugados
ax.plot(
    data_plot.index,
    data_plot['Solo minutesPlayed'],
    color='blue',       # Color de la línea
    linewidth=2.5,      # Grosor de la línea
    linestyle='-',
    alpha=0.8
)

# Configuración y Etiquetas
ax.set_title('Minutos Jugados en Modo Solo (Ordenados de Menor a Mayor)', fontsize=16)
ax.set_xlabel('Jugador (Posición en el Ranking Ascendente)', fontsize=12)
ax.set_ylabel('Minutos Jugados', fontsize=12)

# Ocultamos las etiquetas del eje X ya que son más de 1400 puntos y son ilegibles
ax.set_xticks([]) 
ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()

# Mostrar el gráfico en Streamlit
st.pyplot(fig)

# Opcional: Mostrar los datos subyacentes
st.subheader('Vista Rápida de los Primeros Jugadores (Menos Minutos)')
st.dataframe(df_sorted[['Player', 'Solo minutesPlayed']].head(10))
