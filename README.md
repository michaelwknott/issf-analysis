# issf-analysis

![issf-analysis-streamlit](https://user-images.githubusercontent.com/17526532/227800485-ea79e23e-aba2-4449-811a-c5b96036f769.png)

## About the Project

A streamlit app to analysis individual athlete's ISSF results.

## Built With

+ [Pandas](https://pandas.pydata.org/)
+ [Streamlit](https://streamlit.io/)

## Getting Started

### Prerequisites

+ Python >= 3.10.0

### Installation

1. Clone the repo
   ```bash
   git clone git@github.com:michaelwknott/issf-analysis.git
   ```
1. Create a virtual environment
   ```bassh
   python -m venv .venv --prompt .
   ```
1. Activate the virtual environment
   ```bash
    source .venv/bin/activate
    ```
1. Install dependencies
    ```bash
    python -m pip install -r requirements.txt
    ```
1. Run the Streamlit app
    ```bash
    streamlit run app.py
    ```

### License

Distrubuted under the MIT License. See `LICENSE` for more information.


### Additional Information

The current data source includes results from 1896-2022. For 2022, the following events are included in the data source:
+ World Cup, LONATO, 2022
+ World Cup, LIMA, 2022
+ World Cup, CAIRO, 2022
+ World Cup, NICOSIA, 2022
+ World Cup, RIO DE JANEIRO, 2022
+ World Cup, CHANGWON, 2022
+ World Cup, BAKU, 2022
+ European Championships, HAMAR, 2022
