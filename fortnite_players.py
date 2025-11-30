import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("Fortnite_players_stats.csv")

st.write("""
# STATS FORTNITE PLAYERS.
## Gráficos usando la base de datos estadística de Fortnite.
---
""")

#--------------grafico de horas x partidas ganadas --------------#

st.subheader("Minutos Jugados Por victorias en Solo")

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
plt.title(f'Relacion de Minutos Jugados vs Victorias en Solo (Top {top_n} jugadores)', fontsize=14)
fig.tight_layout()

# 4. Mostrar en Streamlit
st.pyplot(fig)

# Mostrar tabla de datos opcional

#para que parta de 1 en teoría
df_chart.index = df_chart.index + 1

if st.checkbox("Mostrar datos en tabla"):
	st.dataframe(df_chart[['Player', 'Solo minutesPlayed', 'Solo top1']])
	
st.success(f" **Conclusión:** Este grafico nos muestra que no necesariamente la cantidad de tiempo te hace ganar mas")



st.markdown("---")
#________________grafico 2___________________

st.subheader("Minutos vs Puntaje")

# Datos y Tendencia
x = df['Solo minutesPlayed']
y = df['Solo score']
z = np.polyfit(x, y, 1)
p = np.poly1d(z)

# Gráfico
fig, ax = plt.subplots(figsize=(12, 6))
ax.scatter(x, y, alpha=0.5, c='#1f77b4', s=15) # Aumenté un poco el tamaño de los puntos (s=15)
ax.plot(x, p(x), "r--", linewidth=2, label='Tendencia') # Línea un poco más gruesa

# --- CORRECCIONES DE TAMAÑO ---
# Antes tenías fontsize=9 y 7, los he subido a 16 y 12 para que se lean bien.
ax.set_title("Relacion de Tiempo vs Puntaje", fontsize=16)
ax.set_xlabel("Minutos", fontsize=12)
ax.set_ylabel("Puntaje", fontsize=12)

# Antes labelsize era 6 (muy pequeño), ahora es 10
ax.tick_params(axis='both', labelsize=10) 
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

ax.ticklabel_format(style='plain', axis='y')

st.pyplot(fig, use_container_width=True)

corr = df['Solo minutesPlayed'].corr(df['Solo score'])
st.caption(f"Correlación: {corr:.2f}")


st.subheader("Datos del Modo Solitario")
st.write("Explora las estadísticas detalladas de los jugadores.")

# --- DATAFRAME FILTRADO ---
# Creamos el checkbox. Si el usuario lo marca, devuelve True
mostrar_datos = st.checkbox("Mostrar Datos en Tabla")

if mostrar_datos:
    st.write("Explora las estadísticas detalladas de los jugadores.")

	# Juntamos las tres columnas que necesitamos 
    cols_to_show = ['Player', 'Solo score', 'Solo minutesPlayed']

	
    # Si alguna columna no existe, usamos intersection para prevenir errores
    cols_validas = [c for c in cols_to_show if c in df.columns]

    df_filtrado = df[cols_validas]

    # Ordenamos por puntaje (de mayor a menor)
    df_filtrado = df_filtrado.sort_values(by='Solo score', ascending=False)

    # hide_index=True quita la columna de números 0,1,2... de la izquierda
    st.dataframe(df_filtrado, height=400, hide_index=True)


st.success(f" **Conclusión:** A mas minutos jugados se cumpliria que el usuario obtendria mas puntaje dado a la correlacion de un 0.98.")




#_____________grafico 3___________________




# --- TERCER GRÁFICO: Donut Chart de Kills por Modo ---

st.markdown("---")
st.title("¿Dónde se hacen más Kills?")
st.write("Distribución del total de eliminaciones por tipo de juego.")

# 1. Preparar los datos
kills_data = [
    df['Solo kills'].sum(),
    df['Duos kills'].sum(),
    df['Trios kills'].sum(),
    df['Squads kills'].sum()
]
labels_kills = ['Solo', 'Duos', 'Trios', 'Squads']
colors_kills = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'] # Azul, Naranja, Verde, Rojo

# 2. Crear el gráfico de Donut
fig_donut, ax_donut = plt.subplots(figsize=(10, 6))


wedges, texts, autotexts = ax_donut.pie(
    kills_data, 
    labels=None, # Quitamos las etiquetas del gráfico para ponerlas en la leyenda
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors_kills, 
    pctdistance=0.80, # Posición de los porcentajes
    wedgeprops=dict(width=0.4, edgecolor='w'), # Ancho del anillo y borde blanco
    textprops=dict(color="white", weight="bold")
)

# 3. Configurar la Leyenda a la derecha
ax_donut.legend(wedges, labels_kills,
          title="Modos de Juego",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1)) # Esto mueve la leyenda fuera del gráfico a la derecha

ax_donut.set_title("Porcentaje de Kills Totales", fontsize=16)

# 4. Mostrar en Streamlit
st.pyplot(fig_donut)


# Conclusión
max_kills_index = kills_data.index(max(kills_data))
mejor_modo = labels_kills[max_kills_index]
st.success(f" **Conclusión:** El modo **{mejor_modo}** concentra la mayor cantidad de kills.")






#________________grafico 4________________


st.markdown("---") 
st.title("Puntaje Total por Modo de Juego")

# 1. Preparar los datos 
modes_list = ['Solo', 'Duos', 'Trios', 'Squads']
total_scores = [
    df['Solo score'].sum(),
    df['Duos score'].sum(),
    df['Trios score'].sum(),
    df['Squads score'].sum()
]

# 2. Crear el gráfico
fig_bar, ax_bar = plt.subplots(figsize=(10, 6))

bar_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'] 
bars = ax_bar.bar(modes_list, total_scores, color=bar_colors)

ax_bar.set_xlabel('Modo de Juego', fontsize=12)
ax_bar.set_ylabel('Puntaje Total Acumulado', fontsize=12)
ax_bar.set_title('Tabla de Scores: Solo, Duos, Trios y Squads', fontsize=14)


ax_bar.ticklabel_format(style='plain', axis='y')



# Etiquetas encima de las barras
for bar in bars:
    height = bar.get_height()
    ax_bar.text(bar.get_x() + bar.get_width()/2., height,
            f'{int(height):,}', 
            ha='center', va='bottom', fontsize=10)

# 3. Mostrar en Streamlit
st.pyplot(fig_bar)


max_score_val = max(total_scores)

# Encontramos en qué posición (índice) está ese valor máximo
max_score_index = total_scores.index(max_score_val)

# Usamos ese índice para sacar el nombre del modo de la lista 'modes_list'
modo_ganador = modes_list[max_score_index]

st.success(f"**Conclusión:** El modo de juego que más Score te da es: **{modo_ganador}** con un total de {int(max_score_val):,} puntos.")


