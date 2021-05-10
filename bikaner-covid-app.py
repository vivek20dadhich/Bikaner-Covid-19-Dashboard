import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

df = pd.read_csv('Bikaner-covid-cases-data.csv')

st.title("Covid-19 Dashboard For Bikaner")
st.markdown('This dashboard visualizes the Covid-19 Per Day Cases and Recoveries in Bikaner')
left_column, right_column = st.beta_columns(2)
# You can use a column just like st.sidebar:
left_column.button('Current Active Cases - 9135')

st.sidebar.header('Last updated on 9th May at 11pm')
st.sidebar.markdown('Per day cases data is from 02/Apr/2021 Recoveries data is from 30/Apr/2021')
#st.sidebar.markdown()

COLORS_MAPPER = {
    "Cases": "#38BEC9",
    "Recoveries": "#D64545"
}

layout = go.Layout(
    title="Per Day Cases",
    plot_bgcolor="#FFF",  # Sets background color to white
    hovermode="x",
    hoverdistance=100, # Distance to show hover label of data point
    spikedistance=1000, # Distance to show spike
    xaxis=dict(
        title="Date",
        linecolor="black",  # Sets color of X-axis line
        showgrid=False,  # Removes X-axis grid lines
        showspikes=True, # Show spike line for X-axis
        # Format spike
        spikethickness=2,
        spikedash="dot",
        spikecolor="#999999",
        spikemode="across",
    ),
    yaxis=dict(
        title="Cases/Recover",  
        linecolor="black",  # Sets color of Y-axis line
        showgrid=False,  # Removes Y-axis grid lines    
    )
)

fig = go.Figure(layout=layout)
fig.add_trace(go.Scatter(x=df['Date'], y=df['Cases'], mode='lines',name='+ve cases',
                         marker=dict(color='rgb(255, 56, 56)',size=9),line=dict(color='RoyalBlue',width=3)))
fig.add_trace(go.Scatter(x=df['Date'], y=df['Recoveries'],mode='lines',name='Recover',
                         marker=dict(color='rgb(0, 77, 0)',size=9),line=dict(color='rgb(134, 179, 0)',width=3,dash='dot')))

st.plotly_chart(fig)
