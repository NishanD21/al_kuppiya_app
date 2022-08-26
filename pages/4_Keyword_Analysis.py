#..............................UI design of Keyword Analysis.....................................

#Importing necessary Libraries

import pandas as pd # for Dataframes manipulation
import numpy as np # for arrays manipulation
import seaborn as sns # foe data visualization
import plotly.express as px # for data visualization
import matplotlib.pyplot as plt # for data visualization
from PIL import Image # to import images to User Interface (UI)
import requests # to assist importing images to User Interface (UI)
from io import BytesIO # to assist importing images to User Interface (UI)
from requests_html import HTMLSession # to extract the words from YouTube channel
from rake_nltk import Rake # to extract keywords
from fuzzywuzzy import fuzz #for hashtag rating
import streamlit as st # for UI design

#Importing Images to user interface (UI)

url0 = "https://raw.githubusercontent.com/NishanD21/SNA/main/Images/Keyword%20Analysis.png"
url1 = "https://raw.githubusercontent.com/NishanD21/SNA/main/Images/FB1.png"
url2 = "https://raw.githubusercontent.com/NishanD21/SNA/d4d282cba51f29e11e4cb91c61fe4431ef88f7fd/Images/YT1.png"
url3 = "https://raw.githubusercontent.com/NishanD21/SNA/main/Images/Insta.png"
url00 = "https://raw.githubusercontent.com/NishanD21/SNA/main/Images/Sidebar/SM%20Logos.png"

response0 = requests.get(url0)
response1 = requests.get(url1)
response2 = requests.get(url2)
response3 = requests.get(url3)
response00 = requests.get(url00)

img0 = Image.open(BytesIO(response0.content))
img1 = Image.open(BytesIO(response1.content))
img2 = Image.open(BytesIO(response2.content))
img3 = Image.open(BytesIO(response3.content))
img00 = Image.open(BytesIO(response00.content))

st.image(img0)
st.image(img2)

st.sidebar.markdown("<h2 style='text-align: center;'> </h2>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='text-align: center;'> </h2>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='text-align: center;'> </h2>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='text-align: center;'> </h2>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='text-align: center;'> </h2>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='text-align: center;'> </h2>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='text-align: center;'> </h2>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='text-align: center;'> </h2>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='text-align: center;'> </h2>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='text-align: center;'> </h2>", unsafe_allow_html=True)

st.sidebar.image(img00)
st.sidebar.markdown("<h6 style='text-align: center;'>Developed by: </h6>", unsafe_allow_html=True)
st.sidebar.markdown("<h6 style='text-align: center;'>Nishan Obeyesekera(Cardiff Met ID :20228183) </h6>", unsafe_allow_html=True)

#.................... Hashtag Analysis of YouTube............................

#text extraction from YouTube page

def extract_text_yt():
    s_yt = HTMLSession()
    url_yt = 'https://www.youtube.com/c/ALKuppiya'
    response_yt = s_yt.get(url_yt)
    return response_yt.html.find(first=True).text

# Separating keywords 

df_yt = pd.read_json("https://raw.githubusercontent.com/NishanD21/SNA/main/3.%20Keyword%20Behaviour%20-%20Copy/yt_keywords.json")

#Finding the Fuzzywuzzy rating for Hashtags

hashtags_yt = ['#advancelevel','#youtube','#alkuppiya','#subscribe','#liveclasses','#new','#studymotivations','#elearning','#exam','#trailer']
rating_yt = []

for words_yt in hashtags_yt:
    ratio_yt = fuzz.WRatio(words_yt,df_yt['1970-01-01'])
    rating_yt.append(ratio_yt)

df_com_yt = pd.DataFrame({'Hashtags':hashtags_yt,
                     'Fuzzywuzzy Rating':rating_yt })  

# Visualization rating for top 10 YouTube Hashtags

hashtags_chart_yt = df_com_yt.groupby(by=["Hashtags"]).sum()[["Fuzzywuzzy Rating"]]
fig_keyword_yt= px.bar(
    hashtags_chart_yt,
    x=hashtags_chart_yt.index,
    y="Fuzzywuzzy Rating",
    title="<b>YouTube channel Hashtag Rating for top 10 Hashtags</b>",
    color_discrete_sequence=["#d62728"] * len(hashtags_chart_yt),
    template="plotly_dark",
    text_auto=True,
    #color="Fuzzywuzzy Rating"
)

st.plotly_chart(fig_keyword_yt,use_container_width=True)

#.................... Hashtag Analysis of Facebook............................

st.image(img1) # Separator

#text extraction from Facebook page

def extract_text_fb():
    s_fb = HTMLSession()
    url_fb = 'https://www.facebook.com/Alkuppiya'
    response_fb = s_fb.get(url_fb)
    return response_fb.html.find(first=True).text

# Separating keywords 

df_fb = pd.read_json("https://raw.githubusercontent.com/NishanD21/SNA/main/3.%20Keyword%20Behaviour%20-%20Copy/fb_keywords.json")

#Finding the Fuzzywuzzy rating for Hashtags

hashtags_fb = ['#alkuppiya','#onlineclasses','#liveclasses','#advancelevel','#videolessons','#tutorials','#elearning','#exam','#syllabus','#facebook']
rating_fb = []

for words_fb in hashtags_fb:
    ratio_fb = fuzz.WRatio(words_fb,df_fb['1970-01-01'])
    rating_fb.append(ratio_fb)

df_com_fb = pd.DataFrame({'Hashtags':hashtags_fb,
                     'Fuzzywuzzy Rating':rating_fb})  


hashtags_chart_fb = df_com_fb.groupby(by=["Hashtags"]).sum()[["Fuzzywuzzy Rating"]]
fig_keyword_fb= px.bar(
    hashtags_chart_fb,
    x=hashtags_chart_fb.index,
    y="Fuzzywuzzy Rating",
    title="<b>Facebook page Hashtag Rating for top 10 Hashtags</b>",
    color_discrete_sequence=["#0083B8"] * len(hashtags_chart_fb),
    template="plotly_dark",
    text_auto=True,
    #color="Fuzzywuzzy Rating"
)

st.plotly_chart(fig_keyword_fb,use_container_width=True)

#.................... Hashtag Analysis of Instagram............................

st.image(img3) # Separator

#text extraction from Instagram page

def extract_text_in():
    s_in = HTMLSession()
    url_in = 'https://www.instagram.com/al_kuppiya/'
    response_in = s_in.get(url_in)
    return response_in.html.find(first=True).text

# Separating keywords 

df_in = pd.read_json("https://raw.githubusercontent.com/NishanD21/SNA/main/3.%20Keyword%20Behaviour%20-%20Copy/insta_keywords.json")

#Finding the Fuzzywuzzy rating for Hashtags

hashtags_in = ['#videolessons','#studymotivations','#advancelevel','#alkuppiya','#onlineclasses','#liveclasses','#elearning','#exam','#subscribe','#instagram']
rating_in = []

for words_in in hashtags_in:
    ratio_in = fuzz.WRatio(words_in,df_in['1970-01-01'])
    rating_in.append(ratio_in)

df_com_in = pd.DataFrame({'Hashtags':hashtags_in,
                     'Fuzzywuzzy Rating':rating_in})  


hashtags_chart_in = df_com_in.groupby(by=["Hashtags"]).sum()[["Fuzzywuzzy Rating"]]
fig_keyword_in= px.bar(
    hashtags_chart_in,
    x=hashtags_chart_in.index,
    y="Fuzzywuzzy Rating",
    title="<b>Instagram page Hashtag Rating for top 10 Hashtags</b>",
    color_discrete_sequence=["#9467bd"] * len(hashtags_chart_in),
    template="plotly_dark",
    text_auto=True,
    #color="Fuzzywuzzy Rating"
)

st.plotly_chart(fig_keyword_in,use_container_width=True)


hide_stremlit_style = """
<style>
#MainMenu{visibility:hidden}
footer{visibility:hidden}
</style>

"""
st.markdown(hide_stremlit_style,unsafe_allow_html=True)
