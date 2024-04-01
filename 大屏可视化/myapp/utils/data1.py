import os
import pandas as pd
from 大屏可视化.settings import BASE_DIR

cleaned_data3 = pd.read_csv(os.path.join(BASE_DIR, 'cleaned_data3.csv'))


def read_csv_data1():
    data1 = []
    for index, row in cleaned_data3.iterrows():
        row_data = {
            'years': row['years'],
            'rank': row['rank'],
            'logo': row['logo'],
            'country': row['country'],
            'brand': row['brand'],
            'sales': row['sales']
        }
        data1.append(row_data)

    return data1
