import os
import pandas as pd
from 大屏可视化.settings import BASE_DIR

cleaned_data6 = pd.read_csv(os.path.join(BASE_DIR, 'cleaned_data6.csv'))
def read_csv_data4():

    data4 = []
    for index, row in cleaned_data6.iterrows():
        row_data = {
            'carName': row['carName'],
            'years': row['years'],
            'monthly_sales': row['monthly_sales'],

        }
        data4.append(row_data)

    return data4
