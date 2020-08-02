import pandas as pd
import numpy as np


def encode(data, col, max_val):
    data[col + '_sin'] = np.sin(2 * np.pi * data[col] / max_val)
    data[col + '_cos'] = np.cos(2 * np.pi * data[col] / max_val)
    return data


anchor_data = pd.read_csv('datasets/anchor-weed.csv', parse_dates=True, squeeze=True)
anchor_data = anchor_data.drop('Unnamed: 0', axis=1)
anchor_prices = anchor_data['price']
anchor_prices_lag = pd.concat([anchor_prices.shift(1), anchor_prices], axis=1)
anchor_prices_lag.columns = ['price', 'price+1']

date = anchor_data['date'].to_series()
month = pd.DatetimeIndex(date).month
day = date.dt.dayofweek
print('Hello')
