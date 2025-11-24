import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Fortnite_players_stats.csv")

st.write("""
# STATS FORTNITE PLAYERS.
## Gráficos usando la base de datos estadística de Fortnite.
""")


--------------------- nuevo codigo ------------

df1 = df[['Solo score']]
df1 = df1.sort_values(by='Solo score', ascending=False).head(10)

# --- Configuración del Gráfico ---
fig, ax = plt.subplots(figsize=(12, 6))

# 1. Dibujar las barras (Color azul estilo Plotly)
ax.bar(df1.index.astype(str), df1['Solo score'], color='#636EFA', width=0.7)

# 2. Configurar el fondo y la rejilla (Estilo Plotly)
ax.set_facecolor('#E5ECF6')            # Fondo gris azulado interno
fig.patch.set_facecolor('white')       # Fondo blanco externo
ax.grid(axis='y', color='white', linewidth=1) # Rejilla blanca
ax.set_axisbelow(True)                 # Rejilla detrás de las barras

# 3. Quitar los bordes negros (Spines)
for spine in ax.spines.values():
    spine.set_visible(False)

# --- LÓGICA PARA EL EJE Y SIN USAR TICKER ---
# Calculamos hasta dónde llega el eje Y (el máximo valor de los datos)
max_val = df1['Solo score'].max()
# Definimos el paso: cada 1 millón (1,000,000)
step = 1_000_000

# Creamos la lista de números donde irán las marcas: [0, 1000000, 2000000, ...]
yticks_values = range(0, int(max_val) + step, step)

# Creamos las etiquetas de texto correspondientes: ["0", "1M", "2M", ...]
yticks_labels = [f'{int(y/1_000_000)}M' if y > 0 else '0' for y in yticks_values]

# Aplicamos las marcas y las etiquetas manualmente
ax.set_yticks(yticks_values)
ax.set_yticklabels(yticks_labels)

# 4. Ajustes del Eje X
plt.xticks(rotation=-90, fontsize=9)
plt.xlim(-0.6, len(df1) - 0.4)

# --- Mostrar en Streamlit ---
plt.tight_layout()
st.pyplot(fig)
