import pandas as pd

# 读取原始的 CSV 文件
df = pd.read_csv('cleaned/cleaned_data6.csv')

# 创建一个新的 ID 列
id_column = range(1, len(df) + 1)

# 将 ID 列插入到 DataFrame 的首列
df.insert(0, 'id', id_column)

# 保存修改后的 CSV 文件
df.to_csv('cleaned/cleaned_data7.csv', index=False)