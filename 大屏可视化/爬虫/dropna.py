import pandas as pd

# 读取CSV文件并删除最后一行
df = pd.read_csv('./car_sales_data1.csv')
df = df.iloc[:-1]

# 定义要删除的列
cols_to_clean = ['月销量(辆)', '当月销量排名', '占厂商份额', '在厂商排名']

# 遍历要清理的列
for col in cols_to_clean:
    # 删除包含'-'或'--'的行
    df = df[~df[col].isin(['-', '--'])]

# 保存清理后的数据到新的CSV文件
df.to_csv('cleaned/cleaned_data6.csv', index=False)
