import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from predict.utils.getPublicData import *
import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'predict.settings')
django.setup()

if not settings.configured:
    settings.configure(INSTALLED_APPS=['predict'])

def predict_monthly_sales():
    # 从数据库中获取所有车型
    cars = list(getAllCars())

    predicted_sales = []

    for car in cars:
        # 获取指定车型的数据
        car_df = pd.DataFrame(list(Predict.objects.filter(carName=car.carName).values()))

        # 将 'years' 列转换为数值
        car_df['years'] = pd.to_datetime(car_df['years']).dt.year

        # 分割特征和目标变量
        X = car_df[:-1]['years']
        y = car_df[:-1]['monthly_sales']

        # 如果数据量小于 5 个样本,则直接使用最后一个数据点作为预测
        if len(X) < 5:
            next_month_sales = round(car_df['monthly_sales'].iloc[-1])
            predicted_sales.append((car.carName, next_month_sales, len(car_df)))
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
        next_month_sales = round(model.predict([[car_df['years'].iloc[-1] + 1]])[0])
        predicted_sales.append((car.carName, next_month_sales, len(car_df)))

    print(predicted_sales)


