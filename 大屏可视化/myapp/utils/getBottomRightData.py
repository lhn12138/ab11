import json
import re
import time
from myapp.utils.getPublicData import getAllCars

def getRankData():
    cars = list(getAllCars())
    carData =[]
    for car in cars:
        car.price = car.min_price +'-'+car.max_price
        carData.append({
            'brand':car.brand,
            'rank':car.rank,
            'carName':car.carName,
            'carImg':car.carImg,
            'manufacturer':car.manufacturer,
            'carModel':car.carModel,
            'price':car.price,
            'saleVolume':car.saleVolume,
            'marketTime':car.marketTime,
            'over_score':car.over_score


        })
    return carData