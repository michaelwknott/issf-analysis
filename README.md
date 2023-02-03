# issf-analysis
A streamlit app to analysis individual athlete's ISSF results.

## Results Data
The current data source includes results from 1896-2022. For 2022, the following events are included in the data source:
+ World Cup,LONATO,2022
+ World Cup,LIMA,2022
+ World Cup,CAIRO,2022
+ World Cup,NICOSIA,2022
+ World Cup,RIO DE JANEIRO,2022
+ World Cup,CHANGWON,2022
+ World Cup,BAKU,2022
+ European Championships,HAMAR,2022

## Instructions
To run the app locally, utilse the following steps.

Clone to repo:

`git@github.com:michaelwknott/issf-analysis.git`

Change into the issf-analysis directory:

`cd issf-analysis`

Create a virtual environment:

`python -m venv .venv --prompt .`

Activate the virtual environment:

`source .venv/bin/activate`

Install dependencies:

`python -m pip install -r requirements.txt`

Run the Streamlit app:

`streamlit run app.py`
