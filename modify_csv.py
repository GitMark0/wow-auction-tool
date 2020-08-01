import pandas as pd
import math

vos_tbl = pd.read_csv('VoS_2019-2020.csv')

rows_list = []
for index, row in vos_tbl.iterrows():
    for i in range(1, 32):
        suffix = f'0{i}' if i < 10 else str(i)
        row_date = str(int(row['Year'])) + '-' + str(int(row['monthVal'])) + '-' + str(i)
        row_quantity = 0 if math.isnan(row['qty' + suffix]) else int(row['qty' + suffix])
        row_price = 0 if math.isnan(row['mktslvr' + suffix]) else int(row['mktslvr' + suffix])
        rows_list.append({'date': row_date, 'quantity': row_quantity, 'price': row_price})

vos_modified = pd.DataFrame(rows_list)
vos_modified.to_csv('VoS-m_2019-2020.csv')
print('Hello')
