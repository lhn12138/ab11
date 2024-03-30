import pandas as pd

# 从CSV文件读取数据
df = pd.read_csv('cleaned_data5.csv')

# 将年份转换为日期格式
df['years'] = pd.to_datetime(df['years'], format='%Y-%m')

# 计算年销量
df['year'] = df['years'].dt.year
annual_sales = df.groupby('year')['sales'].sum()

# 计算同比变化
annual_growth = annual_sales.pct_change() * 100
annual_growth = annual_growth.round(2)

# 将年销量和同比变化合并到一个DataFrame中
result = pd.concat([annual_sales, annual_growth], axis=1)
result.columns = ['annual_sales', 'annual_growth']

# 保存结果到新的CSV文件
result.to_csv('cleaned_data4.csv', index_label='year')

print("数据处理完成,结果已保存到 'cleaned_data4.csv' 文件中。")