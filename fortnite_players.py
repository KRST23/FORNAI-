import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Fortnite_players_stats.csv")

st.write("""
# STATS FORTNITE PLAYERS.
## Gráficos usando la base de datos estadística de Fortnite.
""")

df1 = df[['Solo score']]
df1 = df1.sort_values(by='Solo score', ascending=False).head(10)


fig, ax = plt.subplots(figsize=(12, 6)) 

ax.bar(df1.index.astype(str), df1['Solo score'], color='#06EAB9') 


ax.set_title('Top 10 Solo Scores')
ax.set_xlabel('Índice / Jugador')
ax.set_ylabel('Score')
plt.xticks(rotation=90, fontsize=8) 


st.pyplot(fig)
