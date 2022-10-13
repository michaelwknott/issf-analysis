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

with st.form(key="issf_filters"):

    championship = st.multiselect(
        "Select the championship(s):",
        options = df["championship_name"].unique(),
        default = df["championship_name"].unique(),
    )

    championship_years = (df["championship_year"].sort_values().unique())
    years = st.select_slider("Select year range:",
        options = championship_years,
        value = (min(championship_years), max(championship_years)),

    )

    event = st.multiselect(
        "Select the event:",
        options = df["championship_event"].unique(),
        default = df["championship_event"].unique(),
    )

    athlete = st.selectbox(
        "Select athlete:",
        options = df["name"].unique(),
    )

    submit_button = st.form_submit_button(label="Submit filters")

    if submit_button:
        st.dataframe(
            df[
                (df["championship_event"].isin(championship))
                & (df["championship_year"] >= years[0])
                & (df["championship_year"] >= years[1])
                & (df["championship_event"].isin(event))
                & (df["name"] == athlete)
            ]
        )
