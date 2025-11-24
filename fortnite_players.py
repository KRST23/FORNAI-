import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Fortnite_players_stats.csv")

st.write("""
# STATS FORTNITE PLAYERS.
## Gráficos usando la base de datos estadística de Fortnite.
""")

df1 = df[['Solo score']]
df1 = df1.sort_values(by='Solo score', ascending=False).head(50)
fig1 = go.Figure(go.Bar(x=df1.index, y=df1['Solo score']))
fig1.show()

