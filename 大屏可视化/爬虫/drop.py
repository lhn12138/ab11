import pandas as pd

# 读取CSV文件并删除最后一行
df = pd.read_csv('temp33.csv')
df = df.drop('占品牌份额', axis=1)
df.to_csv('cleaned_data3.csv', index=False)

