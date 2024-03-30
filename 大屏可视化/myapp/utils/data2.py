import os
import pandas as pd
from 大屏可视化.settings import BASE_DIR

cleaned_data5 = pd.read_csv(os.path.join(BASE_DIR, 'cleaned_data5.csv'))


def read_csv_data2():
    data4 = []
    for index, row in cleaned_data5.iterrows():
        row_data = {
            'years': row['years'],
            'sales': int(row['sales']),
            'rate': row['rate'],
        }
        data4.append(row_data)

        yearsList = []
        volumeList = []
        rateList = []

        for i in data4:
            yearsList.append(i['years'])
            volumeList.append(i['sales'])
            rateList.append(i['rate'])

    return yearsList, volumeList, rateList
