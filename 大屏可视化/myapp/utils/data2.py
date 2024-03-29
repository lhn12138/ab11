import os
import pandas as pd
from 大屏可视化.settings import BASE_DIR

cleaned_data4 = pd.read_csv(os.path.join(BASE_DIR, 'cleaned_data4.csv'))
def read_csv_data2():

    data2 = []
    for index, row in cleaned_data4.iterrows():
        row_data = {
            'year': row['year'],
            'rank': row['rank'],
            'logo': row['logo'],
            'manufacturer': row['manufacturer'],
            'sales': row['sales']
        }
        data2.append(row_data)

    return data2

d = read_csv_data2()
for item in d:
    print(item)

