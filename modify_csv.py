import pandas as pd
import math
import calendar

c = calendar.Calendar()

vos_tbl = pd.read_csv('anchor-weed18.csv')

rows_list = []
for index, row in vos_tbl.iterrows():
    year = int(row['Year'])
    month = int(row['monthVal'])
    for i in c.itermonthdays(year, month):
        if i == 0:
            continue
        suffix = f'0{i}' if i < 10 else str(i)
        row_date = f'{year}-{month}-{i}'
        row_quantity = 0 if math.isnan(row['qty' + suffix]) else int(row['qty' + suffix])
        row_price = 0 if math.isnan(row['mktslvr' + suffix]) else round(int(row['mktslvr' + suffix])/100, 2)
        rows_list.append({'date': row_date, 'quantity': row_quantity, 'price': row_price})

vos_modified = pd.DataFrame(rows_list)
vos_modified.to_csv('anchor-weed.csv')
