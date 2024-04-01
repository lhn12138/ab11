import os
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from 大屏可视化.settings import BASE_DIR

df = pd.read_csv(os.path.join(BASE_DIR, 'cleaned_data1.csv'))


def predict_sales():
    df['min_price'] = df['min_price'].astype(float)
    df['max_price'] = df['max_price'].astype(float)

    # 创建价格区间列
    bins = [0, 5, 10, 15, 20, 30, float('inf')]
    labels = ['0-5w', '5-10w', '10-15w', '15-20w', '20-30w', '30w以上']
    df['price_range'] = pd.cut(df['min_price'], bins=bins, labels=labels)

    # 创建特征和目标变量
    X = df[['carModel', 'energyType', 'price_range']].copy()
    y = df['saleVolume']

    # 将特征变量转换为数值
    car_model_map = {model: i for i, model in enumerate(df['carModel'].unique())}
    energy_type_map = {type: i for i, type in enumerate(df['energyType'].unique())}
    price_range_map = {range: i for i, range in enumerate(df['price_range'].unique())}

    X['carModel'] = X['carModel'].map(car_model_map)
    X['energyType'] = X['energyType'].map(energy_type_map)
    X['price_range'] = X['price_range'].map(price_range_map)

    # 划分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 训练线性回归模型
    model = LinearRegression()
    model.fit(X_train, y_train)

    # 获取所有品牌
    brands = df['brand'].unique()

    # 存储预测结果的数组
    results = []

    # 遍历所有品牌
    for brand in brands:
        # 获取该品牌下的车型和能源类型
        brand_df = df[df['brand'] == brand]
        car_models = brand_df['carModel'].unique()
        energy_types = brand_df['energyType'].unique()

        # 遍历该品牌下的车型和能源类型组合
        for car_model in car_models:
            for energy_type in energy_types:
                # 获取该组合的数据
                data = brand_df[(brand_df['carModel'] == car_model) & (brand_df['energyType'] == energy_type)]
                if data.empty:
                    continue


                # 遍历价格区间并进行预测
                for price_range in df['price_range'].unique():
                    # 构建测试数据
                    test_data = pd.DataFrame({
                        'carModel': [car_model_map[car_model]],
                        'energyType': [energy_type_map[energy_type]],
                        'price_range': [price_range_map[price_range]]
                    }, index=[0])

                    # 进行预测
                    predicted_sales = int(model.predict(test_data)[0])

                    # 存储预测结果
                    results.append({"brand":brand, "car_model":car_model, "price_range":price_range, "energy_type":energy_type, "predicted_sales":predicted_sales})


    return results
