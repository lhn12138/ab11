import json
import re
import time
from myapp.utils.getPublicData import getAllCars


def getRankData():
    cars = list(getAllCars())
    carData = []
    for car in cars:
        carData.append({
            'rank': car.rank,
            'brand': car.brand,
            'carImg': car.carImg,
            'carName': car.carName,
            'manufacturer': car.manufacturer,
            'carModel': car.carModel,
            'min_price': car.min_price,
            'max_price': car.max_price,
            'saleVolume': car.saleVolume,
            'marketTime': car.marketTime,
            'over_score': car.over_score,
            'appearance_score': car.appearance_score,
            'interior_score': car.interior_score,
            'configure_score': car.configure_score,
            'spatial_score': car.spatial_score,
            'comfort_score': car.comfort_score,
            'manipulating_score': car.manipulating_score,
            'motivation_score': car.motivation_score,
            'comprehensive_evaluation': car.comprehensive_evaluation

        })
    return carData
