import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Fortnite_players_stats.csv")

st.write("""
# STATS FORTNITE PLAYERS.
## Gráficos usando la base de datos estadística de Fortnite.
""")

#--------------grafico de horas x partidas ganadas --------------#



# Eliminar filas con valores nulos después de la conversión (si los hay)
df.dropna(subset=['Solo minutesPlayed'], inplace=True)

# 2. Extraer la hora del día (0-23)
df['HOUR'] = df['Solo minutesPlayed'].dt.hour


# Esto nos da la cantidad total de alarmas (sumada) por cada una de las hora
alarms_per_hour = df.groupby('HOUR')['Solo minutesPlayed'].sum().reset_index()

# creamo la gráfica de líneas
plt.figure(figsize=(12, 6), facecolor='white')

plt.plot(alarms_per_hour['HOUR'], alarms_per_hour['Solo minutesPlayed'],
         marker='o', linestyle='-', color='b')


#permite que los datos del eje Y sean numeros enteros
plt.ticklabel_format(style='plain', axis='y')


# Configurar etiquetas y título
plt.title('Cantidad Total de Alarmas por Hora del Día')
plt.xlabel('Hora del Día (0-23)')
plt.ylabel('Suma de Solo minutesPlayed ')

# Asegurar que se muestren todas las horas en el eje x
plt.xticks(range(0, 24))

# Añadir una rejilla
plt.grid(True, linestyle='--', alpha=0.6)
