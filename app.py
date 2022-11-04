import os
import sqlite3

import pandas as pd
import plotly.express as px
import streamlit as st
from dotenv import load_dotenv

load_dotenv()


DEFAULT_CHAMPIONSHIP = 4
DEFAULT_EVENT = 5 #25m Rapid Fire Pistol Men

st.set_page_config(
    page_title = "Rapid Fire Pistol Analysis",
    page_icon=":dart:",
    layout="wide"
)


@st.cache
def load_data_from_csv():
    return pd.read_csv("data/issf_results.csv")


df = load_data_from_csv()

st.sidebar.title("Filters:")
championship_names = sorted((
    df["championship_name"]
    .unique()
))

championship = st.sidebar.selectbox(
    "Select the championship(s):",
    options = championship_names,
    index = DEFAULT_CHAMPIONSHIP,
)

championship_years = sorted((
    df["championship_year"]
    .loc[df["championship_name"] == championship]
    .unique()
))

years = st.sidebar.select_slider("Select year range:",
    options = championship_years,
    value = (min(championship_years), max(championship_years)),
)

championship_events = sorted((
    df["championship_event"]
    .loc[
        (df["championship_name"] == championship)
        & (df["championship_year"] >= years[0])
        & (df["championship_year"] <= years[1])
    ]
    .unique()
))

event = st.sidebar.selectbox(
    "Select the event:",
    options = championship_events,
    index = DEFAULT_EVENT,
)

athletes = sorted((
    df["name"]
    .loc[
        (df["championship_name"] == championship)
        & (df["championship_year"] >= years[0])
        & (df["championship_year"] <= years[1])
        & (df["championship_event"] == event)
    ]
    .unique()
))

athlete = st.sidebar.selectbox(
    "Select athlete:",
    options = athletes,
)

df_filtered = df[
       (df["championship_name"] == championship)
        & (df["championship_year"] >= years[0])
        & (df["championship_year"] <= years[1])
        & (df["championship_event"] == event)
        & (df["name"] == athlete)
    ]


# Mainpage
st.title(":dart: ISSF Results Analysis")

number_of_competitions = df_filtered["championship_name"].count()

st.write("")
st.header(athlete)
st.subheader(f"{championship}: {event}")
st.write("")

col3, col4, col5, col6, col7 = st.columns(5)
with col3:
    st.metric(label="# Comps", value=number_of_competitions)

with col4:
    st.metric(label="Avg Rank", value=int(df_filtered["rank"].mean()))

with col5:
    st.metric(label="Avg Qual Score", value=int(df_filtered["qualification_score"].mean()))

with col6:
    st.metric(label="Max Qual Score", value=int(df_filtered["qualification_score"].max()))

with col7:
    st.metric(label="Min Qual Score", value=int(df_filtered["qualification_score"].min()))


col8, col9, col10, col11, col12 = st.columns(5)
number_of_finals = df_filtered["final_score"].count()
conversion_rate = number_of_finals / number_of_competitions *100

with col8:
    st.metric(label="# Finals", value=number_of_finals)

with col9:
    st.metric(label="Conversion Rate", value=f"{conversion_rate:.0f} %")

with col10:
    st.metric(label="# Gold 🥇", value=len(df_filtered[df_filtered["rank"] == 1]))

with col11:
    st.metric(label="# Silver 🥈", value=len(df_filtered[df_filtered["rank"] == 2]))

with col12:
    st.metric(label="# Bronze 🥉", value=len(df_filtered[df_filtered["rank"] == 3]))

st.write("")
st.subheader("Qualification Score Summary per Year")
fig1 = px.box(
        df_filtered,
        x="championship_year",
        y="qualification_score",
        #title=f"Qualification Score Summary per Championship"
        ).update_traces(marker=dict(color='red'))

fig1.update_layout(
        title_x=0.8,
        title_xanchor="center",
        xaxis_title="",
        yaxis_title="Qualification Score",
        height=800,
        font=dict(
            size=18
        )
)

st.plotly_chart(fig1, use_container_width=True)

hide_st_style = """
            <style>
            main menu {visiablity: hidden;}
            footer {visability: hidden;}
            header {visability: hidden;}
            </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)
