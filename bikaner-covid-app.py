import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

df = pd.read_csv('Bikaner-covid-cases-data.csv')

st.set_page_config(layout="wide")

st.title("Covid-19 Dashboard For Bikaner")
st.write('This dashboard visualizes the Covid-19 Per Day Cases and Recoveries in Bikaner')

#st.sidebar.header('Last updated on 10th May at 9pm')
st.sidebar.info('Per day cases data is from 02/Apr/2021 Recoveries data is from 30/Apr/2021')

col1,col2 = st.beta_columns([4,1.5])
with col1:
    
    layout = go.Layout(
        #title="",
        plot_bgcolor="#F2F2FF",  # Sets background color to white
        autosize=False,
        width=850,
        height=500,
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
    
    config={"displayModeBar": False, "showTips": False, 'scrollZoom': False}
    
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Cases'],mode='markers+lines',name='+ve cases',
                             marker=dict(color='rgb(255, 56, 56)',size=4),line=dict(color='lightskyblue',width=2.5)))
    
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Recoveries'],mode='markers+lines',name='Recover',
                             marker=dict(color='green',size=4,opacity=0.5),line=dict(color='rgba(211, 231, 119,0.8)',width=2.5)))

    #fig.show(config={"displayModeBar": False, "showTips": False})# Remove floating menu and unnecesary dialog box
    
    st.plotly_chart(fig,config=config)
    
with col2:
    
    if st.button('Active Cases'):
        st.write("Current Active Cases - 5921")
    if st.button('Samples taken'):
        st.write("Samples taken on 18th May - 2606")
        st.write("Samples taken on 17th May - 1115")
        st.write("Samples taken on 16th May - 2380")
    if st.button('Percent positive'):
        st.write("Percent positive on 18th May - 22.98")
        st.write("Percent positive on 17th May - 20.98")
        st.write("Percent positive on 16th May - 24.74")
        
    my_expander = st.beta_expander("More")
    with my_expander:
        st.info("Last updated on 18th May at 8pm")
        st.info("Data source - Daily report released from CMHO office Bikaner")
    


