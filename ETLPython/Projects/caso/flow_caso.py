# Import libraries

import pandas as pd
import numpy as nd
import yfinance as yf
from datetime import date
import requests

from prefect import task, Flow

# Extract of data
@task
def extract(tickers, today):
    raw_dfs = {}

    # NASDAQ's Data
    for ticker in tickers:
        tk = yf.Ticker(ticker)
        raw_df = pd.DataFrame(tk.history(period='1d'))
        raw_df.columns = raw_df.columns.str.lower()
        raw_df = raw_df[['open', 'high', 'low', 'close']]

        raw_dfs[ticker] = raw_df

    # Data BTC
    reponse = requests.get('https://api.coinbase.com/v2/prices/spot?currency=USD')
    btc_raw = reponse.json()
    btc_raw = float(btc_raw['data']['amount'])

    btc_index = pd.to_datetime([today])
    btc_raw = pd.DataFrame({'btc_usd': btc_raw}, index=btc_index)

    raw_dfs['btc_usd'] = btc_raw
    
    return raw_dfs

# Transform
def transform(raw_dfs):
    pass

# Load
def load():
    pass

# Flow
with Flow("ETL caso") as flow:
    # Enviroment variables
    tickers = ['NVDA', 'TSLA', 'MSFT', 'AMZN', 'AMD', 'INTC']
    today = date.today()
    today = today.strftime("%Y-%m-%d")

    raw_dfs = extract(tickers, today)
    # tablon = transform(raw_dfs)
    # load(tablon)

flow.run()