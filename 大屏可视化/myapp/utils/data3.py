import os
import pandas as pd
from 大屏可视化.settings import BASE_DIR

cleaned_data5 = pd.read_csv(os.path.join(BASE_DIR, 'cleaned_data4.csv'))


def read_csv_data3():
    data3 = []
    for index, row in cleaned_data5.iterrows():
        row_data = {
            'year': int(row['year']),
            'sales': int(row['sales']),
            'rate': row['rate'],
        }
        data3.append(row_data)

        yearList = []
        volumeList = []
        rateList = []

        for i in data3:
            yearList.append(i['year'])
            volumeList.append(i['sales'])
            rateList.append(i['rate'])

    return yearList, volumeList, rateList
