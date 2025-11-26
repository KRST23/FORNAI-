import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Fortnite_players_stats.csv")

st.write("""
# STATS FORTNITE PLAYERS.
## Gráficos usando la base de datos estadística de Fortnite.
""")

#--------------grafico de horas x partidas ganadas --------------#
# --- Creación del Gráfico de Líneas con Matplotlib ---

# 1. Crear la figura y los ejes
fig, ax = plt.subplots(figsize=(10, 6))

# 2. Trazar el gráfico de líneas
# Eje X: Solo minutesPlayed
# Eje Y: Solo top1

ax.plot(
    df_sorted['Solo minutesPlayed'],
    df_sorted['Solo top1'],
    linestyle='-',
    marker='o',
    markersize=2,
    linewidth=1.5,
    color='skyblue'
)

# 3. Personalizar el gráfico
ax.set_title('Victorias (Solo Top 1) vs. Minutos Jugados (Solo)', fontsize=16)
ax.set_xlabel('Minutos Jugados en Modo Solo', fontsize=12)
ax.set_ylabel('Victorias (Solo Top 1)', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout() # Ajusta el diseño para evitar truncar etiquetas

# 4. Mostrar el gráfico en Streamlit
st.pyplot(fig)

# Opcional: Mostrar los datos subyacentes
st.subheader('Datos Utilizados')
st.dataframe(df_sorted[['Player', 'Solo minutesPlayed', 'Solo top1']].head(10))
