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
            'country': row['country'],
            'brand': row['brand'],
            'sales': row['sales']
        }
        data1.append(row_data)

    # 按年月和排名进行排序
    data1 = sorted(data1, key=lambda x: (x['years'], int(x['rank'])))

    # 获取每月排名前 30 的数据
    result = []
    current_year_month = None
    current_rank = 1
    for row in data1:
        if row['years'] != current_year_month:
            current_year_month = row['years']
            current_rank = 1
        if current_rank <= 30:
            result.append(row)
        current_rank += 1

    return result

data = read_csv_data1()
for item in data:
    print(item)