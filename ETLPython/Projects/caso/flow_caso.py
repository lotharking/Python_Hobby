# Import libraries

import pandas as pd
import numpy as np
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
        raw_df.index = pd.to_datetime(raw_df.index, format='%m/%d/%Y').strftime('%Y-%m-%d')

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
@task
def transform(raw_dfs, tickers):
    # Feature engineering
    
    for ticker in tickers:
        df = raw_dfs[ticker]
        
        df['dif_open_close'] = df['open'] - df['close']
        df['range_day'] = df['high'] - df['low']
        df['signe_day'] = np.where(df['dif_open_close'] > 0.0, "+", np.where(df['dif_open_close'] < 0.0, "-", "0"))

        df = df[["close", "dif_open_close", "range_day", "signe_day"]]
        df.columns = map(lambda x: ticker + '_' + x, df.columns.to_list())

        raw_dfs[ticker] = df

    # Add
    dfs_list = raw_dfs.values()
    tablon = pd.concat(dfs_list, axis=1)

    return tablon

# Load
@task
def load():
    pass

# Flow
with Flow("ETL caso") as flow:
    # Enviroment variables
    tickers = ['NVDA', 'TSLA', 'MSFT', 'AMZN', 'AMD', 'INTC']
    today = date.today()
    today = today.strftime("%Y-%m-%d")

    raw_dfs = extract(tickers=tickers, today=today)
    transform(raw_dfs, tickers)
    # load(tablon)

flow.run()