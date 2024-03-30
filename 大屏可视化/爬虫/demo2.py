import pandas as pd

# 从CSV文件读取数据
df = pd.read_csv('cleaned_data5.csv')

# 将 'rate' 列中的百分号去掉,转换为浮点数
df['rate'] = df['rate'].str.replace('%', '').astype(float)

# 查看处理后的数据
print(df)

# 将处理后的数据保存到新的 CSV 文件
df.to_csv('cleaned_data5.csv', index=False)