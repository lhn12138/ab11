import os
import pandas as pd
from 大屏可视化.settings import BASE_DIR

cleaned_data6 = pd.read_csv(os.path.join(BASE_DIR, 'cleaned_data2.csv'))
def read_csv_data():

    data = []
    for index, row in cleaned_data6.iterrows():
        row_data = {
            'year': row['year'],
            'rank': row['rank'],
            'logo': row['logo'],
            'country': row['country'],
            'brand': row['brand'],
            'sales': row['sales']
        }
        data.append(row_data)

    return data

