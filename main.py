# import os
# os.system("pip install -r requirements.txt")

import streamlit as st
import folium
# from streamlit_folium import folium_static
import urllib.parse
import pandas as pd
# from map_format import add_legends_popup
# from core_data import get_data
from PIL import Image
from streamlit_option_menu import option_menu
import webbrowser


# st.set_page_config(page_title=None, page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)

# col2, col3 = st.columns([6,1])
# image = Image.open('image/log_regtangular.png')
#
# with col2:
#     st.image(image, width=700)

# with col3:
#     st.write("")

# st.image(image, width=500)



with st.sidebar:
    selected = option_menu("Team Hi", ["Home", "Historical Data",'Github'],
        icons=['house','clipboard-data', 'github'], menu_icon="emoji-laughing", default_index=0)
    st.subheader("About:")
    st.write("hi, this is a random project")

github_url = "https://github.com/gridsusc/mindspark-9-team-winner"
if selected == 'GitHub':
    webbrowser.open_new_tab(github_url)

elif selected == 'Historical Data':
    st.header("Lead Your Life")
    st.markdown("#### Historical Data ")

    time = st.select_slider(
         'See Historical Lead Poisoning Data in: ',
         options=['1999', '2000', '2001', '2002', '2003', '2004', '2005','2006', '2007', '2008', '2009'
                  '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017','2018', '2019', '2020', '2021'])

    options = st.multiselect(
         'What counties you would like to see?',
         ['Rogers Park','Norwood Park','Jefferson Park','Forest Glen','North Park','Albany Park','Portage Park','Irving Park',
        'Dunning', 'Montclare', 'Belmont Cragin','West Ridge','Hermosa','Avondale','Logan Square','Humboldt Park','West Town',
        'Austin','West Garfield Park','East Garfield Park','Near West Side','North Lawndale','Uptown','South Lawndale',
        'Lower West Side','Loop','Near South Side','Armour Square','Douglas','Oakland','Fuller Park','Grand Boulevard',
        'Kenwood','Lincoln Square','Washington Park','Hyde Park','Woodlawn','South Shore','Chatham','Avalon Park',
    'South Chicago',
    'Burnside',
    'Calumet Heights',
    'Roseland',
    'North Center',
    'Pullman',
    'South Deering',
    'East Side',
    'West Pullman',
    'Riverdale',
    'Hegewisch',
    'Garfield Ridge',
    'Archer Heights',
    'Brighton Park',
    'McKinley Park',
    'Lake View',
    'Bridgeport',
    'New City',
    'West Elsdon',
    'Gage Park',
    'Clearing',
    'West Lawn',
    'Chicago Lawn',
    'West Englewood',
    'Englewood',
    'Greater Grand Crossing',
    'Lincoln Park',
    'Ashburn',
    'Auburn Gresham',
    'Beverly',
    'Washington Heights',
    'Mount Greenwood',
    'Morgan Park',
    "O'Hare",
    'Edgewater',
    'Near North Side',
    'Edison Park'])

    @st.cache
    def convert_df():
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        df = pd.read_csv("data.csv")
        return df.to_csv().encode('utf-8')

    csv = convert_df()

    st.download_button(
        label="Download data as CSV",
        data= csv,
        file_name='Lead_All_Data.csv',
        mime='text/csv',
    )

elif selected == 'Home':
    st.header("Lead Your Life")
    st.markdown("#### Predictive Analysis to Prevent Childhood Lead Poisoning in Chicago")

    time = st.select_slider(
        'Select what year you want to predict: ',
        options=['2022', '2023', '2024'])


    ########map ###############
    def load_data():
        data = pd.read_csv(
            "",
            nrows=100000,  # approx. 10% of data
            names=[
                "date/time",
                "lat",
                "lon",
            ],  # specify names directly since they don't change
            skiprows=1,  # don't read header since names specified directly
            usecols=[0, 1, 2],  # doesn't load last column, constant value "B02512"
            parse_dates=[
                "date/time"
            ],  # set as datetime instead of converting after the fact
        )

        return data
# radius = st.slider('Select Radius (miles): ', 0.0, 5.0, 1.0)

# space_type = st.radio(
#      "Select Space Type",
#      ('Single-Space', 'Multi-Space'))


def empty_map():
    folium_map = folium.Map(location=[34.0522, -118.2437], zoom_start=12)
    return folium_map


# if st.button('Find Parking Space'):
#     data, lat, long = get_data(location, radius, time, space_type)
#     print(location, radius, time, space_type)
#     if len(data) == 0:
#         st.write("Woops... No spots found. Maybe try another radius?")
#     else:
#         st.write("We found " + str(len(data)) + " spots for you!")
#     if 3 <= radius <= 5:
#         zoom_start = 12
#     else:
#         zoom_start = 15
#     folium_map = add_legends_popup(data, folium.Map(zoom_start=zoom_start, location=[lat, long]), lat, long)
# else:
#      folium_map = empty_map()
#
#
# # folium_map = generate_map("700 W 9th St")
# folium_static(folium_map)f