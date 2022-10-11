import os
import sqlite3

import pandas as pd
import plotly.express as px
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title = "Rapid FIre Pistol Analysis",
    page_icon=":dart:",
    layout="wide"
)


@st.cache
def load_data_from_database():
    db_url = os.environ["DATABASE_URL"]
    conn = sqlite3.connect(db_url)
    return pd.read_sql("SELECT * FROM competitionresult", conn)


df = load_data_from_database()

st.sidebar.header("Filter Data:")

championship = st.sidebar.multiselect(
    "Select the championship(s):",
    options = df["championship_name"].unique(),
    default = df["championship_name"].unique(),
)

championship_years = df["championship_year"].sort_values().unique()
years = st.sidebar.select_slider(
    "Select year range:",
    options = championship_years,
    value = (min(championship_years), max(championship_years)),
)

event = st.sidebar.selectbox(
    "Select the event:",
    options = df["championship_event"].unique(),
)

athlete =  st.sidebar.selectbox(
    "Select athlete:",
    options = df["name"].sort_values().unique(),
)


st.title(":dart: ISSF Results Analysis")

st.dataframe(df)

# TO DO add filter options to dataframe
