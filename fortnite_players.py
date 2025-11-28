import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("Fortnite_players_stats.csv")

st.write("""
# STATS FORTNITE PLAYERS.
## Gráficos usando la base de datos estadística de Fortnite.
""")

#--------------grafico de horas x partidas ganadas --------------#


# 2. Procesar datos: Ordenar por 'Solo minutesPlayed' de mayor a menor
df_sorted = df.sort_values(by='Solo minutesPlayed', ascending=False)

# Widget para controlar cuántos jugadores mostrar (para que el gráfico sea legible)
st.sidebar.header("Configuración del Gráfico")
top_n = st.sidebar.slider("Cantidad de jugadores a mostrar (Top N)", min_value=10, max_value=200, value=50)

# Filtramos los top N jugadores según la selección
df_chart = df_sorted.head(top_n).reset_index(drop=True)




# 3. Crear el gráfico con Matplotlib
fig, ax1 = plt.subplots(figsize=(12, 6))

# Eje Y izquierdo: Solo Minutes Played (Línea Azul)
color1 = 'tab:blue'
ax1.set_xlabel('Jugador')
ax1.set_ylabel('Minutos Jugados (Solo)', color=color1, fontsize=12)
ax1.plot(df_chart.index, df_chart['Solo minutesPlayed'], color=color1, marker='o', markersize=4, label='Minutos Jugados')
ax1.tick_params(axis='y', labelcolor=color1)

# Configurar las etiquetas del eje X para mostrar los nombres de los jugadores
ax1.set_xticks(df_chart.index)
ax1.set_xticklabels(df_chart['Player'], rotation=90, fontsize=8)

# Eje Y derecho: Solo Top 1 (Línea Roja)
ax2 = ax1.twinx()  
color2 = 'tab:red'
ax2.set_ylabel('Top 1 (Victorias)', color=color2, fontsize=12)
ax2.plot(df_chart.index, df_chart['Solo top1'], color=color2, linestyle='--', marker='x', markersize=4, label='Top 1')
ax2.tick_params(axis='y', labelcolor=color2)

# Título y ajustes
plt.title(f'Relacion: Minutos Jugados vs Victorias (Top {top_n} jugadores)', fontsize=14)
fig.tight_layout()

# 4. Mostrar en Streamlit
st.pyplot(fig)

# Mostrar tabla de datos opcional

#para que parta de 1 en teoría
df_chart.index = df_chart.index + 1

if st.checkbox("Mostrar datos en tabla"):
	st.dataframe(df_chart[['Player', 'Solo minutesPlayed', 'Solo top1']])





#________________grafico 4________________



# --- SEGUNDO GRÁFICO: Barras de Score por Modo de Juego ---

st.markdown("---") # Separador visual
st.title("Puntaje Total por Modo de Juego")

# 1. Preparar los datos para el segundo gráfico
# Sumamos el score de toda la columna para cada modo
modes_list = ['Solo', 'Duos', 'Trios', 'Squads']
total_scores = [
    df['Solo score'].sum(),
    df['Duos score'].sum(),
    df['Trios score'].sum(),
    df['Squads score'].sum()
]

# 2. Crear el gráfico de barras con variables únicas
fig_bar, ax_bar = plt.subplots(figsize=(10, 6))

# Definir colores para diferenciar
bar_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'] # Azul, Naranja, Verde, Rojo

bars = ax_bar.bar(modes_list, total_scores, color=bar_colors)

ax_bar.set_xlabel('Modo de Juego', fontsize=12)
ax_bar.set_ylabel('Puntaje Total Acumulado (Score)', fontsize=12)
ax_bar.set_title('Comparación de Scores: Solo, Duos, Trios y Squads', fontsize=14)

ax.ticklabel_format(style='plain', axis='y')

# Opcional: Agregar el valor exacto encima de cada barra
for bar in bars:
    height = bar.get_height()
    ax_bar.text(bar.get_x() + bar.get_width()/2., height,
            f'{int(height):,}',  # Formato con separador de miles
            ha='center', va='bottom', fontsize=10)

# 3. Mostrar el segundo gráfico en Streamlit
st.pyplot(fig_bar)


