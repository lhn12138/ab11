import os
import pandas as pd
from 大屏可视化.settings import BASE_DIR

cleaned_data5 = pd.read_csv(os.path.join(BASE_DIR, 'cleaned_data5.csv'))

def read_csv_data3():
    data3 = []
    for index, row in cleaned_data5.iterrows():
        row_data = {
            'years': row['years'],
            'rank': row['rank'],
            'manufacturer': row['manufacturer'],
            'sales': row['sales']
        }
        data3.append(row_data)

    # 按年月和排名进行排序
    data3 = sorted(data3, key=lambda x: (x['years'], int(x['rank'])))

    # 获取每月排名前 30 的数据
    result = []
    current_year_month = None
    current_rank = 1
    for row in data3:
        if row['years'] != current_year_month:
            current_year_month = row['years']
            current_rank = 1
        if current_rank <= 30:
            result.append(row)
        current_rank += 1

    return result

data = read_csv_data3()
for item in data:
    print(item)