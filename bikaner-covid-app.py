import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import os
import time
import stat

df = pd.read_csv('Bikaner-covid-cases-data.csv')
blankIndex=[''] * len(df)
df.index=blankIndex
st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align:left; color: stratos;'>Covid-19 Dashboard For Bikaner </h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:left; color: stratos;'>This dashboard visualizes the Covid-19 Per Day Cases and Recoveries in Bikaner</p>", unsafe_allow_html=True)

st.sidebar.info('Per day cases data is from 02/Apr/2021')
st.sidebar.info('Per day Recoveries data is from 30/Apr/2021')

def cases():
    st.markdown(int(df["Active Cases"].iloc[-1]))

def samp():
    st.table(pd.DataFrame({'Date':df["Date"].iloc[-3:], 'Samples Taken':df["Samples Taken"].iloc[-3:]}))

def update():
    #fileStatsObj = os.stat ("https://github.com/vivek20dadhich/Bikaner-Covid-19-Dashboard/blob/main/Bikaner-covid-cases-data.csv")
    #modificationTime = time.ctime(fileStatsObj[stat.ST_MTIME])
    st.markdown(pd.DataFrame({'':df["Date"].iloc[-1:] + '  at 21:00'}))

def data():
    st.markdown("Daily report released from CMHO office Bikaner")
    

def bar():
    #create trace1
    trace1 = go.Bar(
                    x = df['Date'],
                    y = df['Cases'],
                    name = "+ve Cases",
                    marker = dict(color = '#729ECE',
                                 line=dict(color='rgb(0,0,0)',width=1)))
    # create trace2 
    trace2 = go.Bar(
                    x = df['Date'],
                    y = df['Recoveries'],
                    name = "Recover",
                    marker = dict(color = '#98DF8A',
                                  line=dict(color='rgb(0,0,0)',width=1)))
    data4 = [trace1, trace2]
    layout = go.Layout(
                    plot_bgcolor="#F2F2FF",  # Sets background color to white
                    autosize=False,
                    width=950,
                    height=450,
                    hovermode="x",
                    barmode = "relative",
                    xaxis_tickangle=-90,
                    bargap=0.16, # gap between bars of adjacent location coordinates.
                    bargroupgap=0.3, # gap between bars of the same location coordinate.
                    hoverdistance=200, # Distance to show hover label of data point
            )
    #layout = go.Layout(barmode = "group")
    fig = go.Figure(data=data4, layout=layout)

    config={"displayModeBar": False, "showTips": False, 'scrollZoom': False}
    st.plotly_chart(fig,config=config)


def scat():
    layout = go.Layout(
                plot_bgcolor="#F2F2FF", 
                autosize=False,
                width=900,
                height=450,
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
                             marker=dict(color='#CE5C5C',size=4),line=dict(color='#729ECE',width=2.2)))
    
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Recoveries'],mode='markers+lines',name='Recover',
                             marker=dict(color='#008081',size=4,opacity=0.5),line=dict(color='#98DF8A',width=2.2)))
    
    st.plotly_chart(fig,config=config)




col1,col2 = st.beta_columns([6.5,2])

with col1:
    plot_type = st.radio("Select the type of plot",('Bar', 'Line and Scatter Plot'))

    if plot_type == 'Bar':
        bar()
    if plot_type == 'Line and Scatter Plot':
        scat()
        
with col2:
    if st.button('Current Active Cases'):
        cases()

    if st.button('Samples taken'):
        samp()

    my_expander = st.beta_expander("More")
    with my_expander:
        if st.caption('Last updated on - '):
            update()
        if st.caption('Data source - '):
            data()
        





        
    


