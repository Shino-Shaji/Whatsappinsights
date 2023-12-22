import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Sample data for demonstration
data = {'Emoji': ['😊', '😄', '😅', '😂', '😆'],
        'Count': [20, 15, 12, 10, 8]}
edf = pd.DataFrame(data)

labels = edf['Emoji'].head(5)
sizes = edf['Count'].head(5)
sizes = sizes.reset_index(drop=True)
colors = ['#99e6ff', '#00ccff', '#00ffff', '#33ccff', '#66ccff']
explode = (0.1, 0, 0, 0, 0)

fig, ax = plt.subplots()
wedges, _ = ax.pie(
    sizes,
    explode=explode,
    labels=labels,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    wedgeprops={'edgecolor': 'none'},  # Remove lines surrounding the wedges
    textprops=dict(size=10),
)

ax.axis('equal')

st.pyplot(fig)
