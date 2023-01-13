from pandas_datareader import data as pdr
from datetime import date
import yfinance as yf
yf.pdr_override()
import pandas as pd

# Tickers list
# We can add and delete any ticker from the list to get desired ticker live data
ticker_list=['DOW', 'CVX', 'TSLA', 'AAPL']

today = date.today()

# We can get data by our choice by giving days bracket
start_date= '2023-01-01'
end_date= '2023-01-13'

files=[]
def getData(ticker):
    data = pdr.get_data_yahoo(ticker, start=start_date, end=today)
    dataname= ticker+'_'+str(today)
    files.append(dataname)
    SaveData(data, dataname)
    print(ticker)
    print(data)

def SaveData(df, filename):
    df.to_csv('./data/'+filename+'.csv')

for tik in ticker_list:
    getData(tik)
