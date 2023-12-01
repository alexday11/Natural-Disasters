import streamlit as st
import pandas as pd
from graph import (Display_Deaddisaster,Display_sharedead,Display_EventDead,Display_AffectTotal,Display_DeadEarthquake,
                   display_EventEath,Display_DeadVocal,Display_IndexDrought,Display_WeatherEx,Display_FloodEx,Display_Precipita,
                   Display_HeatWave,Display_HighTemp,Display_LowTemp,Display_Wildfire,Display_Top10Wildfire,
                   Display_NumberWildfire,Display_Acrec,Display_DamageOfGDP,Display_NewsCoverage,Display_ReceiveNews,
                   Display_Continent_NewsCoverage,Display_Continent_ReceiveNews,Display_ReportDisaster)


st.set_page_config(
    page_title= 'Natural Disasters',
    page_icon= '🌎',
)
# data
Pvt_NumDead = pd.read_csv('./Data_graph/Pvt_NumDead.csv',index_col='Country name')
Pvt_ShareDead = pd.read_csv('./Data_graph/Pvt_ShareDead.csv',index_col='Entity')
EventDead = pd.read_csv('./Data_graph/EventDead.csv')
Pvt_TotalAff = pd.read_csv('./Data_graph/Pvt_TotalAff.csv',index_col='Country name')
Pvt_Earthquake = pd.read_csv('./Data_graph/Pvt_Earthquake.csv',index_col=['Country name','Year'])
Pvt_DeadVocal = pd.read_csv('./Data_graph/Pvt_DeadVocal.csv',index_col=['Entity','Year'])
drought_affect = pd.read_csv('./Data_graph/drought_affect.csv',index_col='Year')
WeatherAff = pd.read_csv('./Data_graph/WeatherAff.csv',index_col='Year')
extreme_flood = pd.read_csv('./Data_graph/global-precipitation-anomaly.csv')
Precip_usa = pd.read_csv('./Data_graph/unusually-high-precipitation-usa.csv')
Heat_wave = pd.read_csv('./Data_graph/heat-wave-index-usa.csv')
High_Temp = pd.read_csv('./Data_graph/high-summer-temp-usa.csv')
Low_Temp = pd.read_csv('./Data_graph/low-winter-temps-usa.csv')
Pvt_wildfire = pd.read_csv('./Data_graph/Pvt_wildfire.csv',index_col=['Country name','Year'])
TopWildfire  = pd.read_csv('./Data_graph/TopWildfire.csv',index_col='Country name')
Wildfire_num = pd.read_csv('./Data_graph/wildfire-numbers-usa.csv')
Acres_num = pd.read_csv('./Data_graph/acres-burned-usa.csv')
economic_group = pd.read_csv('./Data_graph//economic_group.csv',index_col=['Country name','Year'])
NewsCover_group = pd.read_csv('./Data_graph/NewsCover_group.csv',index_col='Entity')
Receive_news_group = pd.read_csv('./Data_graph/Receive_news_group.csv',index_col='Entity')
continent_new = pd.read_csv('./Data_graph/continent_new.csv',index_col='Entity')
receive_continent_new = pd.read_csv('./Data_graph/receive_continent_new.csv',index_col='Entity')
Pvt_natural = pd.read_csv('./Data_graph/Pvt_natural.csv',index_col='Year')

st.title('Natural Disasters')
st.markdown(''' Natural disasters – from earthquakes and floods to storms and droughts – affect millions of people every year. However, we are not defenseless against them, and the global death toll, especially from droughts and floods, has been reduced.

While natural disasters account for a small fraction of all deaths globally, they can have a large impact, especially on vulnerable populations in low-to-middle-income countries with insufficient infrastructure to protect and respond effectively​. Understanding the frequency, intensity, and impact of natural disasters is crucial if we want to be better prepared and protect people’s lives and livelihoods.

On this page, you will find our complete collection of data, charts, and research on natural disasters and their human and economic costs.''')


### Dead Disaster ###
st.header('Natural disasters data explorer',divider='gray')
st.markdown("""
            The number of deaths from natural disasters can be highly variable from year-to-year; some years pass with very few deaths before a large disaster event claims many lives.If we look at the average over the past decade, approximately 45,000 people globally died from natural disasters each year. This represents around 0.1% of global deaths.

Low-frequency, high-impact events such as earthquakes and tsunamis are not preventable, but such high losses of human life are. We know from historical data that the world has seen a significant reduction in disaster deaths through earlier prediction, more resilient infrastructure, emergency preparedness, and response systems.Those at low incomes are often the most vulnerable to disaster events: improving living standards, infrastructure and response systems in these regions will be key to preventing deaths from natural disasters in the coming decades.
            """)
st.subheader(':gray[Decadal average: Annual number of deaths from disasters]')
st.markdown(''':gray[Disasters include all geophysical, meteorological and climate events including earthquakes, volcanic activity, landslides, drought, wildfires,
storms, and flooding. Decadal figures are measured as the annual average over the subsequent ten-year period.]
 ''')
default_index = Pvt_NumDead.index.get_loc('World') 
names1 = st.selectbox('Select countries and region', Pvt_NumDead.index, index=default_index)  
Display_Deaddisaster(Pvt_NumDead,names1)

### Disaster index ###
st.subheader(':gray[Deaths from natural disasters as a share of total deaths, 1990 to 2019]')
default_index2 = Pvt_ShareDead.index.get_loc('World')
names2 = st.selectbox('Select countries and region', Pvt_ShareDead.index, index=default_index2)  
Display_sharedead(Pvt_ShareDead,names2)

### Event Dead ###
st.header('Number of deaths by type of natural disaster',divider='gray')
st.markdown("""
            Number of deaths by type of natural disaster In this visualization I give a sense of how the global picture has evolved over the last century. It shows the estimated annual death toll – from all disasters at the top For most of us, it is hard to know whether any given year was a particularly deadly one in the context of previous years.

What we see is that in the 20th century, it was common to have years where the death toll was in the millions. This was usually the result of major droughts or floods
Improved food security, resilience to other disasters, and better national and international responses mean that the world has not experienced death tolls of this scale in many decades. Famines today are usually driven by civil war and political unrest.

In most years, the death toll from disasters is now in the range of 10,000 to 20,000 people. In the most fatal years – which tend to be those with major earthquakes or cyclones – this can reach tens to hundreds of thousands.

This trend does not mean that disasters have become less frequent, or less intense. It means the world today is much better at preventing deaths from disasters than in the past. This will become increasingly important in our response and adaptation to climate change.
            """)
country_names = EventDead['Country name'].unique()
country_names = ['World'] + list(country_names)
selected_country = st.selectbox('Select countries and region', country_names, index=0)

Display_EventDead(EventDead, selected_country)


### Injuries ###

st.header('Injuries and displacement from disasters',divider='gray')
st.markdown("""
            Human impacts from natural disasters are not fully captured in mortality rates. Injury, homelessness, and displacement can all have a significant impact on populations.

The visualisation below shows the number of people displaced internally from natural disasters.
            """)
st.markdown("""
            Injuries: number of people injured is defined as "People suffering from physical injuries, trauma or an illness requiring immediate medical assistance as a direct result of a disaster."
            """)
st.markdown("""
            Homelessness: number of people homeless is defined as "Number of people whose house is destroyed or heavily damaged and therefore need shelter after an event."            """)
st.markdown("""
            Affected: number of people affected is defined as "People requiring immediate assistance during a period of emergency, i.e. requiring basic survival needs such as food, water, shelter, sanitation and immediate medical assistance."            """)
st.markdown("""
            Total number affected: total number of people affected is defined as "the sum of the injured, affected and left homeless after a disaster."            """)


all_countries = Pvt_TotalAff.index.unique().tolist()

default_countries = ['United States', 'Haiti', 'Bangladesh', 'Japan', 'Fiji']

for country in default_countries:
    if country not in all_countries:
        default_countries = [all_countries[0]]

selected_countries = st.multiselect('Select countries to display', all_countries, default=default_countries)
Display_AffectTotal(Pvt_TotalAff, selected_countries)


### Natural disasters by type ###
st.header('Natural disasters by type',divider='gray')

st.subheader('Earthquake')
st.subheader('Deaths from earthquakes')
st.markdown("""
            Deaths from earthquakes At the global level we see that earthquake deaths have been a persistent human risk through time. Deaths from earthquakes, 1900 to 2020 Deaths from earthquakes includes direct deaths from the event plus those from secondary impacts (such as a tsunami triggered by an earthquake). Due to data availability, reporting and evidence, it's expected that more recent data will be more complete than the long historical record. A trend in reported estimates therefore doesn't necessarily reflect the true change over time.  """)


country_names2 = Pvt_Earthquake.index.get_level_values('Country name').unique()
country_names2 = ['World'] + list(country_names2)
names4 = st.selectbox('Select countries and region', country_names2, index=0 , key='selectbox1')  
Display_DeadEarthquake(Pvt_Earthquake, names4)

names5 = st.selectbox('Select countries and region', country_names2 , index=0, key='selectbox2')  
st.subheader(':gray[Number of people affected is defined as “the sum of the injured, affected and left homeless after a disaster]')
display_EventEath(Pvt_Earthquake, names5)


## Volcanic ##
st.subheader('Volcanoes')
st.markdown("""
            Deaths from volcanic eruptions
In the visualization we see the number of deaths from significant volcanic eruptions across the world. Using the timeline on the map we can see the frequency of volcanic activity deaths over time. If we look at deaths over the past century we see several high-impact events: the Nevado del Ruiz eruption in Colombia in 1985; the Mount Pelée eruption in Martinique in 1902; and 1883 eruption of Krakatoa in Indonesia.
            """)
st.subheader(':gray[Number of deaths from volcanic eruptions, 1570 to 2017]')
st.markdown("""
            :gray[Deaths from volcanic eruption events includes direct deaths from volcanic eruptions, in addition to secondary impacts (such
as a tsunami or earthquake triggered by an eruption)]
            """)
names6 = st.selectbox('Select countries and region',country_names2,index=0,key='selectboxes3')
Display_DeadVocal(Pvt_DeadVocal,names6)


## Drought ##

st.header('Famines & Droughts',divider='gray')
st.markdown("""
            In the visualization shown here we see trends in drought severity in the United States. Given is the annual data of drought severity, plus the 9-year average.This is measured by the The Palmer Drought Severity Index: the average moisture conditions observed between 1931 and 1990 at a given location is given an index value of zero. A positive value means conditions are wetter than average, while a negative value is drier than average. A value between -2 and -3 indicates moderate drought, -3 to -4 is severe drought, and -4 or below indicates extreme drought.
            """)
st.subheader(':gray[Drought severity index, United States]')
st.markdown("""
            :gray[The Palmer Drought Severity Index is the most widely used index to measure drought severity over time. An index value of
zero represents the average moisture conditions observed between 1931 and 1990. Positive values mean wetter than
average, negatives mean drier than average.]
            """)
Display_IndexDrought(drought_affect)

## Weather ###
st.header('Long-term trends in deaths from US weather events',divider='gray')
st.markdown('Trends in the US provide some of the most complete data on impacts and deaths from weather events over time.This chart shows death rates from lightning and other weather events in the United States over time. Death rates are given as the number of deaths per million individuals. Over this period, we see that on average each has seen a significant decline in death rates. This is primarily the result of improved infrastructure, predicted and response systems to disaster events.')

st.subheader(':gray[Fatality rates in the US due to weather events]')
st.markdown('Annual death rate from weather events, measured per million individuals.')
Display_WeatherEx(WeatherAff)


## precipitation and flooding
st.header('Extreme precipitation and flooding',divider='gray')
st.subheader('Precipitation anomalies')
st.markdown("""
            In the visualization shown we see the global precipitation anomaly each year.

This precipitation anomaly is measured relative to the century average from 1901 to 2000. Positive values indicate a wetter year than normal; negative values indicate a drier year.

Also shown is US-specific data on the share of land area which experiences unusually high precipitation in any given year.
            """)

st.subheader(':gray[Global precipitation anomaly]')
st.markdown("""
                :gray[This indicator shows annual anomalies compared with the average precipitation from 1901 to 2000 based on rainfall and
snowfall measurements from land-based weather stations worldwide.]
                """)
Display_FloodEx(extreme_flood)

st.subheader(':gray[Share of US land area with unusually high annual precipitation]')
st.markdown("""
                :gray[Share of land area in the United States which experienced unusually high annual precipitation in a given year. This compares
actual yearly precipitation totals with expected totals based on historical data.]
                """)
Display_Precipita(Precip_usa)


# Extreme Temperature (Heat & Cold)
st.header('Extreme Temperature (Heat & Cold)',divider='gray')
st.markdown('Extreme temperature risks to human health and mortality can result from both exposure to extreme heat and cold.')

st.subheader('Heatwaves and high temperatures')
st.markdown("""
            In the visualizations shown here we see long-term data on heatwaves and unusually high temperatures in the United States.

Overall we see there is significant year-to-year variability in the extent of heatwave events. What stands out over the past century of data was the 1936 North American heatwave – one of the most extreme heat wave events in modern history, which coincided with the Great Depression and Dust Bowl of the 1930s.

When we look at the trajectory of unusually high summer temperatures over time (defined as 'unusually high' in the context of historical records) we see an upward trend in recent decades
            """)
st.subheader(':gray[Annual Heat Wave Index in the United States]')
st.markdown("""
            :gray[This index defines a heat wave as a period lasting at least four days with an average temperature that would only be
expected to occur once every 10 years, based on the historical record. The index value for a given year depends on how
often heat waves occur and how widespread they are.]
            """)
Display_HeatWave(Heat_wave)


st.subheader(':gray[Share of US land area with unusually high summer temperatures]')
st.markdown("""
            :gray[Unusually hot summers are defined based on daily maximum temperatures. At each station, the recorded highs are
compared with the full set of historical records. After averaging over a particular month or season of interest, the warmest 10
percent of years are defined as “unusually hot.”]
            """)
Display_HighTemp(High_Temp)


st.subheader('Cold temperatures')
st.markdown("""
            Whilst we often focus on heatwave and warm temperatures in relation to weather extremes, extremely low temperatures can often have a high toll on human health and mortality. In the visualization here we show trends in the share of US land area experiencing unusually low winter temperatures. In recent years there appears to have been a declining trend in the extent of the US experiencing particularly cold winters.
            """)
st.subheader(':gray[Share of US land area with unusually low winter temperatures]')
st.markdown("""
            :gray[Unusually cold winter temperatures are measured based on daily minimum temperatures. At each station, the recorded lows
are compared with the full set of historical records. After averaging over a particular month or season of interest, the coldest
10 percent of years are defined as “unusually cold.”]
            """)
Display_LowTemp(Low_Temp)

# Wildfire #

st.header('Wildfires',divider='gray')
names7 = st.selectbox('Select countries and region',country_names2,index=0, key='select_box4')
Display_Wildfire(Pvt_wildfire,names7)
#Top wildfire
Display_Top10Wildfire(TopWildfire)


st.subheader('US Wildfires')
st.markdown("""
            How are the frequency and extent of wildfires in the United States changing over time?

In the charts below we provide three overviews: the number of wildfires, the total acres burned, and the average acres burned per wildfire. This data is shown from 1983 onwards, when comparable data recording began.

Over the past 30-35 years we notice three general trends in the charts below (although there is significant year-to-year variability):

on average, the annual number of wildfires has not changed much;
on average, the total acres burned has increased from the 1980s and 1990s into the 21st century;
the combination of these two factors suggest that the average acres burned per wildfire has increased.
There has been significant media coverage of the long-run statistics of US wildfires reported by the National Interagency Fire Center (NIFC). The original statistics are available back to the year 1926. When we look at this long-term series it suggests there has been a significant decline in acres burned over the past century. However, the NIFC explicitly state:

Prior to 1983, sources of these figures are not known, or cannot be confirmed, and were not derived from the current situation reporting process. As a result the figures prior to 1983 should not be compared to later data.

Representatives from the NIFC have again confirmed (see the Carbon Brief's coverage here) that these historic statistics are not comparable to those since 1983. The lack of reliable methods of measurement and reporting mean some historic statistics may in fact be double or triple-counted in national statistics.

This means we cannot compare the recent data below with old, historic records. But it also doesn't confirm that acres burned today are higher than the first half of the 20th century. Historically, fires were an often-used method of clearing land for agriculture, for example. It's not implausible to expect that wildfires of the past may have been larger than today but the available data is not reliable enough to confirm this.
            """)

st.subheader(':gray[Number of wildfires in the United States]')
st.markdown(""":gray[The number of wildfire events in the United States. Data is shown from 1983 onwards, when comparable data records
began.]""")
Display_NumberWildfire(Wildfire_num)

st.subheader(':gray[Wildfire acres burned in the United States]')
st.markdown(""":gray[Number of acres of wildfire burned in a given year in the United States. This is shown from 1983 onwards, when consistent
reporting began.]""")
Display_Acrec(Acres_num)

st.header('Economic costs',divider='gray')
st.subheader('Global disaster costs')
st.markdown("""
            Natural disasters not only have devastating impacts in terms of the loss of human life, but can also cause severe destruction with economic costs.When we look at global economic costs over time in absolute terms we tend to see rising costs. But, importantly, the world – and most countries – have also gotten richer. Global gross domestic product has increased more than four-fold since 1970. We might therefore expect that for any given disaster, the absolute economic costs could be higher than in the past.

A more appropriate metric to compare economic costs over time is to look at them in relation to GDP. This is the indicator adopted by all countries as part of the UN Sustainable Development Goals to monitor progress on resilience to disaster costs.

In the chart, we see global direct disaster losses given as a share of GDP.
            """)
names8 = st.selectbox('Select countries and region',country_names2,index=0,key='selectbox6')
Display_DamageOfGDP(economic_group,names8)


st.header('Not all deaths are equal: How many deaths make a natural disaster newsworthy?',divider='gray')
st.subheader('The type of disaster matters')
st.markdown("""
            In other words, the type of disaster matters to how newsworthy networks find it to be. The visualizations show the extent of this observed "news effect". The chart shows the proportion of each type of disaster that receives news coverage, and the second shows the "casualties ratio", which tells us—all else equal—how many casualties would make media coverage equally likely for each type of disaster.
            """)
st.subheader(':gray[News coverage of disasters]')
st.markdown("""
            :gray[The data considers disasters occurring between 1968-2002 and their corresponding coverage in major US networks. It is
evident that "spectacular" disasters receive more coverage.]
            """)
Display_NewsCoverage(NewsCover_group)

st.subheader(':gray[How many deaths does it take for a disaster to receive news coverage?]')
st.markdown("""
            :gray[Disaster occurrence and news coverage data is used to compute the casualties ratio. The casualties ratio indicates how
many casualties would make media coverage (in major US networks) equally likely, all else equal.]
            """)
Display_ReceiveNews(Receive_news_group)

st.subheader('And the location of the disaster matters too')
st.markdown("""
            There are other biases, too. Eisensee and Strömberg found that while television networks cover more than 15% of the disasters in Europe and South Central America, they show less than 5% of the disasters in Africa and the Pacific. Disasters in Africa tend to get less coverage than ones in Asia because they are less "spectacular", with more droughts and food shortages occurring there relative to Asia.

However, after controlling for disaster type, along with other factors such as the number killed and the timing of the news, there is no significant difference between coverage of African and Asian disasters. Instead, a huge difference emerges between coverage of Africa, Asia, and the Pacific on the one hand, and Europe and South and Central America, on the other.

According to the researchers’ estimates, 45 times as many people would have to die in an African disaster for it to garner the same media attention as a European one. The two visualizations show the extent of this bias.

ABC News’s slogan is “See the whole picture” and CNN’s is “Go there”, but good follow-up questions might be: what exactly, and where?
            """)
st.subheader(':gray[News coverage of disasters, by continent]')
st.markdown("""
            :gray[The data considers disasters occurring between 1968-2002 and their corresponding coverage in major US networks.
]
            """)
Display_Continent_NewsCoverage(continent_new)

st.subheader(""" :gray[How many deaths does it take for a disaster in different continents toreceive news coverage?] """)
st.markdown("""
            :gray[Disaster occurrence and news coverage data is used to compute the casualties ratio. The casualties ratio indicates how many casualties
would make media coverage (in major US networks) equally likely, all else equal.]
            """)
Display_Continent_ReceiveNews(receive_continent_new)

st.header('Number of reported disasters by type',divider='gray')
st.markdown('This same data is shown here as the number of reported disaster events by type. Again, the incompleteness of historical data can lead to significant underreporting in the past. The increase over time is therefore not directly reflective of the actual trend in disaster events.')

st.subheader(':gray[Global reported natural disasters by type, 1970 to 2023]')
st.markdown("""
            :gray[The annual reported number of natural disasters, categorised by type. The number of global reported natural disaster events
in any given year. Note that this largely reflects increases in data reporting, and should not be used to assess the total
number of events.]
            """)
Display_ReportDisaster(Pvt_natural)