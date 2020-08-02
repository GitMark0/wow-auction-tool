import pandas as pd
import numpy as np
from sklearn import preprocessing


# sin/cos encoding of feature
def encode(data, col, max_val):
    data[col + '_sin'] = np.sin(2 * np.pi * data[col] / max_val)
    data[col + '_cos'] = np.cos(2 * np.pi * data[col] / max_val)
    return data


scaler = preprocessing.MinMaxScaler()

anchor_data = pd.read_csv('datasets/anchor-weed.csv', parse_dates=True, squeeze=True)
anchor_data = anchor_data.drop('Unnamed: 0', axis=1)

# normalize price and quantity
anchor_data[['quantity', 'price']] = scaler.fit_transform(anchor_data[['quantity', 'price']])

# sine/cosine transform of dow and month
anchor_data['date'] = pd.to_datetime(anchor_data['date'])
anchor_data['month'] = pd.DatetimeIndex(anchor_data['date']).month
anchor_data['dow'] = anchor_data['date'].dt.dayofweek
anchor_data = encode(anchor_data, 'month', 12)
anchor_data = encode(anchor_data, 'dow', 6)

# lag feature from price
anchor_data = pd.concat([anchor_data, anchor_data['price'].shift(1)], axis=1)
anchor_data.columns = [*anchor_data.columns[:-1], 'price+1']

# drop redundant columns
anchor_data = anchor_data.drop(['date', 'month', 'dow'], axis=1)

# drop first 12 rows -> 0 values and save data
anchor_data = anchor_data.iloc[12:]
anchor_data.to_csv('datasets/anchor-weed_prepared.csv')

