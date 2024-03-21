import json
import re
import time
from .getPublicData import *

def getSquareData():
    cars = list(getAllCars())
    carsVolume = {}
    for i in cars:
        if carsVolume.get(i.carName, -1) == -1:
            carsVolume[str(i.carName)] = int(i.saleVolume)
        else:
            carsVolume[str(i.carName)] += int(i.saleVolume)

    carSortVolume = sorted(carsVolume.items(),key=lambda x:x[1], reverse=True)[:15]
    brandList=[]
    volumeList=[]
    priceList=[]
    for i in carSortVolume:
        brandList.append(i[0])
        volumeList.append(i[1])
    for j in cars[:15]:
        j.price = j.min_price

        #正则表达式
        # j.price = re.findall('\d+\.\d+',j.min_price)

        priceList.append(float(j.price))
    return brandList,volumeList,priceList