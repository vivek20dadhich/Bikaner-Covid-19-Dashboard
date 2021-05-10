import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

df = pd.read_csv('Bikaner-covid-cases-data.csv')
st.set_page_config(layout="wide")
st.title("Covid-19 Dashboard For Bikaner")
st.markdown('This dashboard visualizes the Covid-19 Per Day Cases and Recoveries in Bikaner')

#st.sidebar.header('Last updated on 10th May at 9pm')
st.sidebar.markdown('Per day cases data is from 02/Apr/2021 Recoveries data is from 30/Apr/2021')

col1,col2 = st.beta_columns([3,1])
with col1:
    
    COLORS_MAPPER = {
        "Cases": "#38BEC9",
        "Recoveries": "#D64545"
    }

    layout = go.Layout(
        #title="",
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
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Cases'],mode='markers+lines',name='+ve cases',
                             marker=dict(color='rgb(255, 56, 56)',size=4),line=dict(color='rgb(111, 231, 219)',width=2)))
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Recoveries'],mode='lines',name='Recover',
                             marker=dict(color='green',size=4),line=dict(color='rgb(211, 231, 119)',width=2)))

    st.plotly_chart(fig)
    
with col2:
    st.button("Current Active Cases - 8694")
    st.button("Samples taken today - 1155")
    my_expander = st.beta_expander("More")
    with my_expander:
        st.markdown("Last updated on 10th May at 9pm")
    

