import pandas as pd
import matplotlib.pyplot as plt

monelite_tbl = pd.read_csv('monelite-ore-prices.csv')

date_time = pd.to_datetime(monelite_tbl['date'])
avg_price = monelite_tbl['priceavg']

price_time = pd.DataFrame()
price_time['price'] = avg_price
price_time = price_time.set_index(date_time)

fig, ax = plt.subplots()
plt.xticks(rotation=90)
plt.plot(price_time)
plt.show()
