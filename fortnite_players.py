import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Fortnite_players_stats.csv")

st.write("""
# STATS FORTNITE PLAYERS.
## Gráficos usando la base de datos estadística de Fortnite.
""")

#--------------grafico de horas x partidas ganadas --------------#

# Sort the dataframe by 'Solo minutesPlayed' descending
df_sorted = df.sort_values(by='Solo minutesPlayed', ascending=False)

# Take the top 20 players for readability
top_players = df_sorted.head(20)

# Create the plot
fig, ax1 = plt.subplots(figsize=(14, 7))

# Plot 'Solo minutesPlayed' on the primary y-axis
color = 'tab:blue'
ax1.set_xlabel('Player')
ax1.set_ylabel('Solo minutesPlayed', color=color)
ax1.plot(top_players['Player'], top_players['Solo minutesPlayed'], color=color, marker='o', label='Solo minutesPlayed')
ax1.tick_params(axis='y', labelcolor=color)
ax1.tick_params(axis='x', rotation=45)

# Create a second y-axis for 'Solo top1'
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Solo top1', color=color)
ax2.plot(top_players['Player'], top_players['Solo top1'], color=color, marker='x', linestyle='--', label='Solo top1')
ax2.tick_params(axis='y', labelcolor=color)

# Title and layout
plt.title('Solo Minutes Played vs Solo Top 1 (Top 20 Players)')
plt.tight_layout()

# Save the plot
plt.savefig('solo_stats_line_chart.png')
