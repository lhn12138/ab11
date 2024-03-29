import csv

# 读取原始CSV文件,指定编码方式为'utf-8'
with open('./cleaned/cleaned_data7.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    data = list(reader)

# 选择需要保留的列
keep_columns = ['brand', 'saleVolume', 'min_price', 'max_price', 'carModel', 'energyType']

# 创建新的数据列表,只保留需要的列
new_data = [{k: row[k] for k in keep_columns} for row in data]

# 写入新的CSV文件,指定编码方式为'utf-8'
with open('output.csv', 'w', newline='', encoding='utf-8') as file:
    fieldnames = keep_columns
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(new_data)

print("数据清洗完成,新的CSV文件已保存。")
