import json
import time
from .getPublicData import *


def getBaseData():
    cars = list(getAllCars())
    sumCar = 35091
    highVolume = cars[0].saleVolume
    topCar = cars[0].carName
    # 车型
    carModels = {}
    maxModel = 0
    mostModel = ''
    for i in cars:
        if carModels.get(i.carModel, -1) == -1:
            carModels[str(i.carModel)] = 1
        else:
            carModels[str(i.carModel)] += 1

    carModels = sorted(carModels.items(), key=lambda x: x[1], reverse=True)
    mostModel = carModels[0][0]
    # print(carModels[0][0])
    # 品牌
    carBrands = {}
    maxBrand = 0
    mostBrand = ''
    for i in cars:
        if carBrands.get(i.brand, -1) == -1:
            carBrands[str(i.brand)] = 1
        else:
            carBrands[str(i.brand)] += 1

    for k, v in carBrands.items():
        if v > maxBrand:
            maxBrand = v
            mostBrand = k
    # 价格
    carPrices = {}
    averagePrice = 0
    sumPrice = 0
    for i in cars:
        x = json.loads(i.min_price) + json.loads(i.max_price)
        sumPrice += x
    averagePrice = sumPrice / (sumCar * 2)
    averagePrice = 19.76

    return sumCar, highVolume, topCar, mostModel, mostBrand, averagePrice


def getRollData():
    cars = list(getAllCars())
    # 品牌
    carBrands = {}
    for i in cars:
        if carBrands.get(i.brand, -1) == -1:
            carBrands[str(i.brand)] = 1
        else:
            carBrands[str(i.brand)] += 1
    brandList = [(value, key) for key, value in carBrands.items()]
    brandList = sorted(brandList, reverse=True)[:10]
    sortDict = {i[1]: i[0] for i in brandList}
    lastSortList = []
    for key, value in sortDict.items():
        lastSortList.append({
            'name': key,
            'value': value
        })
    return lastSortList


def getTypeRate():
    cars = list(getAllCars())
    catTypes = {}
    for i in cars:
        if catTypes.get(i.energyType, -1) == -1:
            catTypes[str(i.energyType)] = 1
        else:
            catTypes[str(i.energyType)] += 1

    oilRate = round(catTypes['汽油'] / 525 * 100, 2)

    electricRate = round(catTypes['纯电动'] / 525 * 100, 2)

    mixRate = round(((525 - catTypes['汽油'] - catTypes['纯电动']) / 525 * 100),2)

    return oilRate, electricRate, mixRate
