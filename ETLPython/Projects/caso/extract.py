# Libraries
import yfinance as yf
import pandas as pd

tickers = ['NVDA', 'TSLA', 'MSFT', 'AMZN', 'AMD', 'INTC']
raw_dfs = {}

# NASDAQ's Data
for ticker in tickers:
    tk = yf.Ticker(ticker)
    raw_df = pd.DataFrame(tk.history(period='1d'))
    raw_df.columns = raw_df.columns.str.lower()
    raw_df = raw_df[['open', 'high', 'low', 'close']]

    raw_dfs[ticker] = raw_df

print(raw_dfs)