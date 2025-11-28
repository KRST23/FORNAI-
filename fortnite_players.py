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





# --- SECCIÓN 1: Gráfico de Barras (Score por Tipo de Juego) ---
    st.header("Score Total por Tipo de Juego (Sin LTM)")
    
    # Calcular los totales
    modes = ['Solo', 'Duos', 'Trios', 'Squads']
    scores = [df[f'{mode} score'].sum() for mode in modes]
    
    # Crear DataFrame para el gráfico
    df_scores = pd.DataFrame({'Modo': modes, 'Score Total': scores})
    
    # Crear el gráfico
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(modes, scores, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
    
    # Etiquetas y formato
    ax.set_ylabel('Puntaje Total (Score)', fontsize=12)
    ax.set_title('Comparación de Puntaje Total por Modo', fontsize=14)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Formatear eje Y para que no use notación científica (opcional, visualmente mejor)
    ax.ticklabel_format(style='plain', axis='y')
    
    # Añadir los valores encima de las barras
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height):,}',
                ha='center', va='bottom', fontsize=10)

    st.pyplot(fig)

    # --- SECCIÓN 2: Tu gráfico anterior (Solo Minutes vs Top 1) ---
    st.header("Análisis de Jugadores: Minutos vs Top 1 (Solo)")
    
    # (El código del gráfico anterior iría aquí...)
    df_sorted = df.sort_values(by='Solo minutesPlayed', ascending=False)
    top_n = st.slider("Cantidad de jugadores a mostrar", 10, 200, 50)
    df_chart = df_sorted.head(top_n).reset_index(drop=True)
    
    fig2, ax1 = plt.subplots(figsize=(12, 6))
    ax1.plot(df_chart.index, df_chart['Solo minutesPlayed'], color='tab:blue', label='Minutos')
    ax1.set_ylabel('Minutos (Solo)', color='tab:blue')
    ax1.tick_params(axis='y', labelcolor='tab:blue')
    ax1.set_xticks(df_chart.index)
    ax1.set_xticklabels(df_chart['Player'], rotation=90, fontsize=8)
    
    ax2 = ax1.twinx()
    ax2.plot(df_chart.index, df_chart['Solo top1'], color='tab:red', linestyle='--', label='Top 1')
    ax2.set_ylabel('Top 1', color='tab:red')
    ax2.tick_params(axis='y', labelcolor='tab:red')
    
    st.pyplot(fig2)
