import os
import sqlite3

import pandas as pd
import plotly.express as px
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title = "Rapid Fire Pistol Analysis",
    page_icon=":dart:",
    layout="wide"
)


@st.cache
def load_data_from_database():
    db_url = os.environ["DATABASE_URL"]
    conn = sqlite3.connect(db_url)
    return pd.read_sql("SELECT * FROM competitionresult", conn)


df = load_data_from_database()

st.title(":dart: ISSF Results Analysis")

championship_names = sorted((
    df["championship_name"]
    .unique()
))

championship = st.multiselect(
    "Select the championship(s):",
    options = championship_names,
    default = championship_names,
)

championship_years = sorted((
    df["championship_year"]
    .loc[df["championship_name"].isin(championship)]
    .unique()
))

years = st.select_slider("Select year range:",
    options = championship_years,
    value = (min(championship_years), max(championship_years)),
)

championship_events = sorted((
    df["championship_event"]
    .loc[df["championship_year"].isin(years)]
    .unique()
))

events = st.multiselect(
    "Select the event:",
    options = championship_events,
    default = championship_events,
)

athletes = sorted((
    df["name"]
    .loc[df["championship_event"].isin(events)]
    .unique()
))

athlete = st.selectbox(
    "Select athlete:",
    options = athletes,
)

st.dataframe(
     df[
       (df["championship_name"].isin(championship))
        & (df["championship_year"] >= years[0])
        & (df["championship_year"] <= years[1])
        & (df["championship_event"].isin(events))
        & (df["name"] == athlete)
    ]
)
