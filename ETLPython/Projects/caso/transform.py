from extract import raw_dfs, tickers, today

import pandas as pd
import numpy as np

# Feature engineering
## To create: dif_open_close / range_day / signe_day

raw_dfs = raw_dfs.copy()
tickers = tickers.copy()

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