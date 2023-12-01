import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go


#Pvt_NumDead = pd.read_csv('./Data_graph/Pvt_NumDead.csv',index_col='Country name')

def Display_Deaddisaster(Data,name_country='World'):
  data = Data.loc[name_country]
  fig = px.bar(data,y=data.values , hover_data=None)
  fig.update_traces(hovertemplate='{}: %{{y}}'.format(name_country),showlegend=True,name=name_country)
  fig.update_layout(
    xaxis_title='',
    yaxis_title='',
    plot_bgcolor= 'white',
  )
  fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='lightgray', griddash='dot',tickfont=dict(color='gray'))
  fig.update_xaxes(tickfont=dict(color='gray'))
  st.plotly_chart(fig)
  
def Display_sharedead(Data,NameCountry='World'):
  data2 = Data.loc[NameCountry]
  fig2 = px.line(data2, x=data2.index, y=data2.values,color_discrete_sequence=['#ff084a'])
  scatter_trace = go.Scatter(x=data2.index, y=data2.values, mode='markers', marker=dict(size=6, color='#ff084a'), name='Markers',showlegend=False)
  fig2.add_trace(scatter_trace)
  fig2.update_traces(hovertemplate='{}: %{{y}}'.format(NameCountry))
  fig2.update_layout(
      #title_font = dict(size=20,color='#5b5b5b',family="Liberation Serif"),
      xaxis_title='',
      yaxis_title='',
      plot_bgcolor= 'white',
      #yaxis=dict(gridcolor='lightgray', gridwidth=0.5)
  )
  fig2.update_yaxes(griddash='dot',showgrid=True,gridwidth=0.5,tickfont=dict(color='gray'),gridcolor='lightgray',ticksuffix='%')
  fig2.update_xaxes(tickfont=dict(color='gray'))
  st.plotly_chart(fig2)
  

def Display_EventDead(Data,Names='World'):
  #EventDead_graph = Data.reset_index()
  fig = px.bar(Data[Data['Country name']==Names], x='Year', y=[
      'Number of deaths from drought',
      'Number of deaths from earthquakes',
      'Number of deaths from volcanic activity',
      'Number of deaths from floods',
      'Number of deaths from mass movements',
      'Number of deaths from storms',
      'Number of deaths from landslides',
      'Number of deaths from fog',
      'Number of deaths from wildfires',
      'Number of deaths from extreme temperatures',
      'Number of deaths from glacial lake outbursts'
  ],color_discrete_sequence=["#f37736","#9e3d64","#ee4035","#0392cf","#8d5524","#2c1847","#aa7c6b","#9edbf9","#d60000","#003877","#eea990"],
               )

  for trace_name in Data[Data['Country name']==Names].columns[2:]:
    fig.update_traces(showlegend=True, name=trace_name[22:],selector=dict(name=trace_name),hovertemplate='%{y}')

  fig.update_yaxes(showgrid=True, griddash='dot',gridcolor='#dfe3ee',gridwidth=0.5, tickfont=dict(color='gray'),)
  fig.update_xaxes(tickfont=dict(color='gray'))
  fig.update_layout(
      barmode='stack',
      xaxis_title='',
      yaxis_title='',
      title='Decadal average: Number of deaths from natural disasters World',
      title_font = dict(size=25,color='#5b5b5b',family="Liberation Serif"),
      legend_title=None,
      plot_bgcolor='white'
  )

  st.plotly_chart(fig)
  

def Display_AffectTotal(Data, selected_countries=['United States', 'Haiti', 'Bangladesh', 'Japan', 'Fiji']):
    # Filter the data based on selected countries
    datas = [Data.loc[country] for country in selected_countries]

    Aff_graph = pd.DataFrame({country: data.values for country, data in zip(selected_countries, datas)}, index=datas[0].index)
    colors = ["#ee4035", "#f37736", "#9e3d64", "#7bc043", "#0392cf"]
    fig3 = px.line(Aff_graph, x=Aff_graph.index, y=Aff_graph.columns,
                   labels={'index': 'Date', 'value': 'Total Affected'},
                   color_discrete_sequence=colors)
    fig3.update_traces(hovertemplate='%{x}')

    for i, cols in enumerate(Aff_graph.columns):
        goscatter = go.Scatter(x=Aff_graph.index, y=Aff_graph[cols], mode='markers',
                              marker=dict(size=6, color=colors[i]), showlegend=False)
        fig3.add_trace(goscatter)

    fig3.update_yaxes(showgrid=True, gridcolor='#dfe3ee', gridwidth=0.5, griddash='dot', tickfont=dict(color='gray'))
    fig3.update_xaxes(tickfont=dict(color='gray'))
    fig3.update_layout(
        title='Total Affected by Country',
        title_font=dict(size=25, color='#5b5b5b', family="Liberation Serif"),
        xaxis_title='',
        yaxis_title='',
        legend_title=None,
        plot_bgcolor='white'
    )
    st.plotly_chart(fig3)
    
    

def Display_DeadEarthquake(Data,Names='World'):
  datas1 = Data.loc[Names]
  datas1['Number of deaths from earthquakes']
  fig4 = px.bar(datas1['Number of deaths from earthquakes'], x=datas1['Number of deaths from earthquakes'].index, y=datas1['Number of deaths from earthquakes'].values)
  fig4.update_traces(hovertemplate='%{y}',showlegend=True,name=Names)
  fig4.update_layout(
      title = 'Deaths from earthquakes 1900 to 2020',
      xaxis_title=None,
      yaxis_title=None,
      title_font = dict(size=25,color='#5b5b5b',family="Liberation Serif"),
      plot_bgcolor='white'
  )
  fig4.update_yaxes(showgrid=True, gridcolor='lightgray', gridwidth=0.5, griddash='dot', tickfont=dict(color='gray'))
  fig4.update_xaxes( tickfont=dict(color='gray'))
  st.plotly_chart(fig4)
  
  

def display_EventEath(Data,Names='World'):
  EventEarthquake = Data.reset_index()
  fig5 = px.bar(EventEarthquake[EventEarthquake['Country name']==Names],x='Year',y=['Number of people injured from earthquakes',
                                                              'Number of people affected by earthquakes',
                                                              'Number of people left homeless from earthquakes'],color_discrete_sequence=["#9e3d64","#f6db5f","#ffb554"])
  for trace_name in EventEarthquake[EventEarthquake['Country name']==Names].columns[2:]:
    fig5.update_traces(hovertemplate='%{y}',name=trace_name[16:],selector=dict(name=trace_name))
  fig5.update_layout(
      barmode='stack',
      xaxis_title='',
      yaxis_title='',
      plot_bgcolor='white',
      legend_title=None
  )
  fig5.update_yaxes(showgrid=True, gridcolor='lightgray', gridwidth=0.5, griddash='dot', tickfont=dict(color='gray'))
  fig5.update_xaxes( tickfont=dict(color='gray'))
  st.plotly_chart(fig5)
  
def Display_DeadVocal(Data,Names='World'):
  datas = Data.loc[Names]
  fig = px.line(datas, datas.index, datas['Volcanic eruption deaths (NGDC/NOAA)'],color_discrete_sequence=['#cf0000'])
  goscatter = go.Scatter(x=datas.index, y=datas['Volcanic eruption deaths (NGDC/NOAA)'],mode='markers',marker=dict(size=4,color='#cf0000'),showlegend=False)
  fig.add_traces(goscatter)
  fig.update_traces(hovertemplate='%{y}')
  fig.update_layout(
      xaxis_title=None,
      yaxis_title=None,
      plot_bgcolor='white',
      legend_title=None
  )
  fig.update_yaxes(showgrid=True, gridcolor='lightgray', gridwidth=0.5, griddash='dot', tickfont=dict(color='gray'))
  fig.update_xaxes( tickfont=dict(color='gray'))
  st.plotly_chart(fig)
  
def Display_IndexDrought(Data):
  fig = px.line(Data, x=Data.index, y=Data.columns,color_discrete_sequence=['#ff0065','#398564'])
  colors = ['#ff0065','#398564']
  for i,cols in enumerate(Data.columns):
      goscatter = go.Scatter(x=Data.index, y=Data[cols], mode='markers', marker=dict(size=5, color=colors[i]),showlegend=False)
      fig.add_trace(goscatter)

  fig.update_traces(showlegend=True, name='9-year average',selector=dict(name='Palmer Drought Severity Index (9-year avg) (NOAA)'))
  fig.update_traces(showlegend=True, name='Annual drought severity index',selector=dict(name='Palmer Drought Severity Index (annual) (NOAA)'))
  fig.update_layout(
      xaxis_title = None,
      yaxis_title = None,
      plot_bgcolor='white',
      legend_title=None
  )
  fig.update_yaxes(showgrid=True, gridcolor='lightgray', gridwidth=0.5, griddash='dot', tickfont=dict(color='gray'),zeroline=True, zerolinecolor='#999999')
  fig.update_xaxes( tickfont=dict(color='gray'))
  st.plotly_chart(fig)
  

def Display_WeatherEx(Data):
  fig = px.line(Data, x=Data.index, y=Data.Lightning)
  colors=['#a26e1a','#a44383','#38761d','#7c059f','#0776ca','#ef8308','#ff0065','#274e13','#afba0c']

  for i,cols in enumerate(Data.columns):
    new_data = Data[Data[cols] != 0]
    if not new_data.empty:
      fig.add_trace(go.Scatter(x=new_data.index, y=new_data[cols],mode='lines',name=cols,line=dict(color=colors[i])))
      goScatter = go.Scatter(x=new_data.index, y=new_data[cols],mode='markers', marker=dict(size=4,color=colors[i]),showlegend=False)
      fig.add_trace(goScatter)

  fig.update_layout(
        xaxis_title = None,
        yaxis_title = None,
      plot_bgcolor='white',
      legend_title=None)
  fig.update_yaxes(showgrid=True, gridcolor='lightgray', gridwidth=0.5, griddash='dot', tickfont=dict(color='gray'))
  fig.update_xaxes( tickfont=dict(color='gray'))
  st.plotly_chart(fig)
  
def Display_FloodEx(Data):
  fig = px.line(Data, x=Data.Year, y=Data['Global precipitation anomaly'],color_discrete_sequence=['#ff0065'])
  goscatter = go.Scatter(x = Data.Year, y=Data['Global precipitation anomaly'],mode='markers',marker=dict(size=6,color='#ff0065'),showlegend=False)
  fig.add_trace(goscatter)
  #fig.add_trace(go.Scatter(x=extreme_flood.Year, y=extreme_flood.Zero, mode='lines',line=dict(color='#777777')))
  fig.update_layout(
          xaxis_title = None,
          yaxis_title = None,
      plot_bgcolor='white',
      legend_title=None)
  fig.update_yaxes(showgrid=True, gridcolor='lightgray', gridwidth=0.5, griddash='dot', tickfont=dict(color='gray'),zeroline=True,   zerolinecolor='#999999',ticksuffix=' mm')
  fig.update_xaxes( tickfont=dict(color='gray'))
  st.plotly_chart(fig)
  
  
def Display_Precipita(Data):
  fig = px.line(Data, x=Data.Year, y=['Share of land area experienced unusually high annual precipitation (NOAA)',
        'Share of land area experienced unusually high annual precipitation - 9yr avg (NOAA)'], color_discrete_sequence=['#264961','#ff0065'])
  colors=['#264961','#ff0065']
  for i, cols in enumerate(Data.iloc[:,3:].columns):
    goscatter = go.Scatter(x = Data.Year, y=Data[cols],mode='markers',marker=dict(size=5,color=colors[i]),showlegend=False)
    fig.add_trace(goscatter)
    fig.update_traces(showlegend=True, name='Annual trend',selector=dict(name='Share of land area experienced unusually high annual precipitation (NOAA)'))
    fig.update_traces(showlegend=True, name='9-year average',selector=dict(name='Share of land area experienced unusually high annual precipitation - 9yr avg (NOAA)'))
  fig.update_layout(
      xaxis_title = None,
      yaxis_title = None,
      plot_bgcolor='white',
      legend_title=None
      )
  fig.update_yaxes(showgrid=True, gridcolor='lightgray', gridwidth=0.5, griddash='dot', tickfont=dict(color='gray'),ticksuffix='%')
  fig.update_xaxes( tickfont=dict(color='gray'))
  st.plotly_chart(fig)
  
def Display_HeatWave(Data):
  fig = px.line(Data, x=Data.Year, y=Data['Heat Wave Index (NOAA)'], color_discrete_sequence=['#ff084a'])
  goscatter = go.Scatter(x=Data.Year, y=Data['Heat Wave Index (NOAA)'],mode='markers', marker=dict(size=5,color='#ff084a'),showlegend=False)
  fig.add_trace(goscatter)
  fig.update_layout(
      xaxis_title='',
      yaxis_title='',
      plot_bgcolor='white',
      legend_title=None
  )
  fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='lightgray', griddash='dot', tickfont=dict(color='gray'))
  fig.update_xaxes( tickfont=dict(color='gray'))
  st.plotly_chart(fig)
  
def Display_HighTemp(Data):
  fig = px.line(Data, x=Data.Year, y=['Hot Daily Highs (NOAA)','9-year average (Hot Daily Highs)'], color_discrete_sequence=['#ff6289','#548a4c'])
  colors = ['#ff6289','#548a4c']
  for i , cols in enumerate(Data.iloc[:,3:].columns):
    goscatter = go.Scatter(x=Data.Year, y=Data[cols],mode='markers', marker=dict(size=5,color=colors[i]),showlegend=False)
    fig.add_trace(goscatter)
    fig.update_traces(showlegend=True, name='Daily Highs', selector=dict(name='Hot Daily Highs (NOAA)'))
    fig.update_traces(showlegend=True, name='9-year average', selector=dict(name='9-year average (Hot Daily Highs)'))
  fig.update_layout(
        xaxis_title=None,
        yaxis_title=None,
      plot_bgcolor='white',
      legend_title=None
    )
  fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='lightgray', griddash='dot', tickfont=dict(color='gray'),ticksuffix='%')
  fig.update_xaxes( tickfont=dict(color='gray'))
  st.plotly_chart(fig)
  
  
def Display_LowTemp(Data):
  fig = px.line(Data, x=Data.Year, y=['Cold Daily Lows (NOAA)','9-year average (Cold Daily Lows)'], color_discrete_sequence=['#ff6289','#548a4c'])
  colors = ['#ff6289','#548a4c']
  for i, cols in enumerate(Data.iloc[:,3:].columns):
    goscatter = go.Scatter(x=Data.Year, y=Data[cols],mode='markers', marker=dict(size=5,color=colors[i]),showlegend=False)
    fig.add_trace(goscatter)
    fig.update_traces(showlegend=True, name='Daily Lows', selector=dict(name='Cold Daily Lows (NOAA)'))
    fig.update_traces(showlegend=True, name='9-year average', selector=dict(name='9-year average (Cold Daily Lows)'))
  fig.update_layout(
        xaxis_title='',
        yaxis_title=None,
      plot_bgcolor='white',
      legend_title=None
    )
  fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='lightgray', griddash='dot', tickfont=dict(color='gray'),ticksuffix='%')
  fig.update_xaxes( tickfont=dict(color='gray'))
  st.plotly_chart(fig)
  

def Display_Wildfire(Data,Names='World'):
  datas = Data.loc[Names]
  fig = px.bar(datas, x=datas.index, y=datas['Number of deaths from wildfires'], color_discrete_sequence=['#4C6A9C'])
  fig.update_traces(hovertemplate='%{y}', showlegend=True, name=Names)
  fig.update_layout(
      title = 'Number of deaths from wildfires',
      xaxis_title = None,
      yaxis_title = None,
      title_font = dict(size=25,color='#5b5b5b',family="Liberation Serif"),
      plot_bgcolor='white',
      legend_title=None
  )
  fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='lightgray', griddash='dot', tickfont=dict(color='gray'))
  fig.update_xaxes( tickfont=dict(color='gray'))
  st.plotly_chart(fig)
  
  
def Display_Top10Wildfire(Data):
  fig = px.bar(Data, x=Data.index, y=Data['Number of deaths from wildfires'], color_discrete_sequence=['darkcyan'])
  fig.update_layout(
      xaxis_title = None,
      yaxis_title = None,
      title = 'Top 10 Country Average Death from WildFire',
      title_font = dict(size=25,color='#5b5b5b',family="Liberation Serif"),
      plot_bgcolor='white',
      legend_title=None
  )
  fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='lightgray', griddash='dot', tickfont=dict(color='gray'))
  fig.update_xaxes( tickfont=dict(color='gray'))
  st.plotly_chart(fig)
  
def Display_NumberWildfire(Data):
  fig = px.bar(Data, x=Data.Year, y=Data['Number of wildfires - comparable data (NIFC)'], color_discrete_sequence=['#ee4035'])
  fig.update_traces(hovertemplate='United States: %{y}')
  fig.update_layout(
    xaxis_title = None,
    yaxis_title = None,
    plot_bgcolor='white',
    legend_title=None
    )
  fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='lightgray', griddash='dot', tickfont=dict(color='gray'))
  fig.update_xaxes( tickfont=dict(color='gray'))
  st.plotly_chart(fig)
  
def Display_Acrec(Data):
  fig = px.bar(Data, x=Data.Year, y=Data['Acres burned - comparable data (NIFC)'], color_discrete_sequence=['#4C6A9C'])
  fig.update_traces(hovertemplate='United States: %{y}  acres')
  fig.update_layout(
    xaxis_title = None,
    yaxis_title = None,
    plot_bgcolor='white',
    legend_title=None
    )
  fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='lightgray', griddash='dot', tickfont=dict(color='gray'),ticksuffix='illion acres')
  fig.update_xaxes( tickfont=dict(color='gray'))
  st.plotly_chart(fig)
  
  
def Display_DamageOfGDP(Data,Names='World'):
  datas = Data.loc[Names]
  new_data = datas[datas['Total economic damages from disasters as a share of GDP'] != 0]
  if not  new_data.empty:
    fig = px.bar(new_data, x=new_data.index, y=new_data['Total economic damages from disasters as a share of GDP'])
  fig.update_traces(hovertemplate = '{}: %{{y}} %'.format(Names),showlegend=True, name=Names)
  fig.update_layout(
        xaxis_title=None,
        yaxis_title=None,
    plot_bgcolor='white',
    legend_title=None
    )
  fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='lightgray', griddash='dot', tickfont=dict(color='gray'),ticksuffix='%')
  fig.update_xaxes( tickfont=dict(color='gray'))
  st.plotly_chart(fig)
  
  
def Display_NewsCoverage(Data):
  fig = px.bar(Data, x='Share in news (Eisensee and Strömberg 2007)', y=Data.index,orientation='h',color_discrete_sequence=['#289e89'])
  fig.update_layout(
          xaxis_title=None,
          yaxis_title=None,
      plot_bgcolor='white',
      legend_title=None
      )
  fig.update_xaxes(showgrid=True, gridwidth=0.5, gridcolor='lightgray', griddash='dot', tickfont=dict(color='gray'),showticklabels=False)
  fig.update_yaxes( tickfont=dict(color='#2e4045'),categoryorder='total ascending',showline=True, linewidth=2, linecolor='gray')
  fig.update_traces(text=Data['Share in news (Eisensee and Strömberg 2007)'], textposition='outside', texttemplate='%{text}%')
  st.plotly_chart(fig)
  
def Display_ReceiveNews(Data):
  fig = px.bar(Data, x='Equal coverage casualties ratio (Eisensee and Strömberg 2007)', y=Data.index,orientation='h',color_discrete_sequence=['#289e89'])
  fig.update_layout(
          xaxis_title=None,
          yaxis_title=None,
      plot_bgcolor='white',
      legend_title=None
      )
  fig.update_xaxes(showgrid=True, gridwidth=0.5, gridcolor='lightgray', griddash='dot', tickfont=dict(color='gray'),showticklabels=False)
  fig.update_yaxes( tickfont=dict(color='#2e4045'),categoryorder='total ascending',showline=True, linewidth=2, linecolor='gray')
  fig.update_traces(text=Data['Equal coverage casualties ratio (Eisensee and Strömberg 2007)'], textposition='outside', texttemplate='%{text}')
  st.plotly_chart(fig)
  
def Display_Continent_NewsCoverage(Data):
  fig = px.bar(Data, x='Share in news (Eisensee and Strömberg 2007)', y=Data.index,orientation='h',color_discrete_sequence=['#bf8bff'])
  fig.update_layout(
          xaxis_title=None,
          yaxis_title=None,
      plot_bgcolor='white',
      legend_title=None
      )
  fig.update_xaxes(showgrid=True, gridwidth=0.5, gridcolor='lightgray', griddash='dot', tickfont=dict(color='gray'),showticklabels=False)
  fig.update_yaxes( tickfont=dict(color='#2e4045'),categoryorder='total ascending',showline=True, linewidth=2, linecolor='gray')
  fig.update_traces(text=Data['Share in news (Eisensee and Strömberg 2007)'], textposition='outside', texttemplate='%{text}%')
  st.plotly_chart(fig)
  
def Display_Continent_ReceiveNews(Data):
  fig = px.bar(Data, x='Equal coverage casualties ratio (Eisensee and Strömberg 2007)', y=Data.index,orientation='h',color_discrete_sequence=['#bf8bff'])
  fig.update_layout(
          xaxis_title=None,
          yaxis_title=None,
      plot_bgcolor='white',
      legend_title=None
      )
  fig.update_xaxes(showgrid=True, gridwidth=0.5, gridcolor='lightgray', griddash='dot', tickfont=dict(color='gray'),showticklabels=False)
  fig.update_yaxes( tickfont=dict(color='#2e4045'),categoryorder='total ascending',showline=True, linewidth=2, linecolor='gray')
  fig.update_traces(text=Data['Equal coverage casualties ratio (Eisensee and Strömberg 2007)'], textposition='outside', texttemplate='%{text}')
  st.plotly_chart(fig)
  
  
def Display_ReportDisaster(Data):
  fig = px.bar(Data, x=Data.index, y=Data.iloc[:,1:].columns,color_discrete_sequence=['#fbbe5b','#202020','#4f372d','#eb6841',
                                                                                                           '#edc951','#00a0b0','#a7204c','#6a329f','#004c4c','#66b2b2','#9bd21d'])
  fig.update_layout(
      barmode='stack',
      xaxis_title='',
      yaxis_title='',
      plot_bgcolor='white',
      legend_title=None
  )
  fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='lightgray', griddash='dot', tickfont=dict(color='gray'))
  fig.update_xaxes( tickfont=dict(color='gray'))
  st.plotly_chart(fig)