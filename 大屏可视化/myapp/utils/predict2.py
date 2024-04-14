import os
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from 大屏可视化.settings import BASE_DIR

# 读取 CSV 文件
cleaned_data6 = pd.read_csv(os.path.join(BASE_DIR, 'cleaned_data6.csv'))
cleaned_data6['years'] = pd.to_datetime(cleaned_data6['years']).dt.year

def predict_monthly_sales():
    predicted_sales = []
    for car_name in cleaned_data6['carName'].unique():
        # 获取指定车型的数据
        car_data = cleaned_data6[cleaned_data6['carName'] == car_name]
        # 分割特征和目标变量
        X = car_data[:-1]['years']
        y = car_data[:-1]['monthly_sales']
        # 如果数据量小于 5 个样本,则直接使用最后一个数据点作为预测
        if len(X) < 5:
            next_month_sales = round(car_data['monthly_sales'].iloc[-1])
            predicted_sales.append((car_name, next_month_sales, len(car_data)))
            continue
        # 划分训练集和测试集
        if len(X) < 10:
            test_size = 0.1
        else:
            test_size = 0.2
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
        # 创建线性回归模型
        model = LinearRegression()
        model.fit(X_train.to_numpy().reshape(-1, 1), y_train)
        # 对最后一个数据点进行预测
        next_month_sales = round(model.predict([[car_data['years'].iloc[-1] + 1]])[0])
        predicted_sales.append((car_name, next_month_sales, len(car_data)))
    return predicted_sales

# 调用函数
predicted_results = predict_monthly_sales()
# print(predicted_results)