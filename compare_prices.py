import pandas as pd
import math
import re
import requests
from generate_token_export_ah_data_CSV import retrieve_token
import numpy as np

vendor_sell_prices = pd.read_csv('export.csv')
ah_data = pd.read_csv('auction_house_items.csv')

ah_item_ids = ah_data['item'].tolist()
ah_item_ids = [int(re.findall(r'\d+', item)[0]) for item in ah_item_ids]

ah_data = ah_data.drop(['item'], axis=1)
ah_data.insert(1, 'item_id', ah_item_ids)
access_token = retrieve_token()['access_token']

total_profit = 0

for index, row in vendor_sell_prices.iterrows():
    if math.isnan(row['id']) or math.isnan(row['sell_price']):
        continue
    item_id = int(row['id'])
    vendor_sell_price = int(row['sell_price'])
    items_ah = ah_data.loc[ah_data['item_id'] == item_id]
    less_than_vendor = items_ah.loc[items_ah['unit_price'] < vendor_sell_price]
    if less_than_vendor.shape[0] > 0:
        item_info = requests.get(
            f'https://eu.api.blizzard.com/data/wow/item/{str(item_id)}?namespace=static-eu&locale=en_GB&access_token={access_token}').json()
        item_name = item_info['name']
        unit_price = less_than_vendor['unit_price'].to_numpy()
        quantity = less_than_vendor['quantity'].to_numpy()
        diff = (np.array(vendor_sell_price) - unit_price) * quantity
        profit = diff.sum()
        total_profit += profit
        print(f'\n{item_name}; Vendor sell price: {vendor_sell_price}; Profit: {profit} ')
        print(less_than_vendor)

print(f'\nTotal profit: {total_profit}')
