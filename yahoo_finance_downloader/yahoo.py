#%%
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
import json
from  datetime import date

today = date.today()

tickers = ["MSFT","GME"]
start="2021-06-03"
end="2021-06-08"
interval="1m"

yf.pdr_override()
for ticker in tickers:
    df2 = pdr.get_data_yahoo(ticker,start,end,interval)
    df2.index.name = 'Date'
    rpivot = df2.reset_index().melt('Date', var_name=['Attribute'])
    with open(f'{ticker}_{today}.json','w') as out:
            out.write((rpivot.to_json(indent=4)))
            out.close()


# %%
