import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import yfinance as yf

# Tickers list
# We can add and delete any ticker from the list to get desired ticker live data

#ticker_list=['DOW', 'CVX', 'TSLA', 'AAPL']

#today = date.today()

# We can get data by our choice by giving days bracket
start_date= '2022-01-13'
end_date= '2023-01-13'

dow = yf.download('PW',start_date,end_date)
cvx = yf.download('CVX',start_date,end_date)
tsla = yf.download('TSLA',start_date,end_date)


data = pd.concat([dow['Open'],cvx['Open'],tsla['Open']],axis = 1)
data.columns = ['dowOpen','cvxOpen','tslaOpen']
scatter_matrix(data, figsize = (8,8), hist_kwds= {'bins':250})
plt.show()


'''
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
'''
