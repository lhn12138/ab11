import json
import re
import time
from .getPublicData import *


def getPriceSortData():
    cars = list(getAllCars())
    priceSortList = {'0-5w': 0, '5-10w': 0, '10-15w': 0, '15-20w': 0, '20-30w': 0, '30w以上': 0}
    for i in cars:
        s = [json.loads(i.min_price)][0]
        if s < 5:
            priceSortList['0-5w'] += 1
        elif s >= 5 and s < 10:
            priceSortList['5-10w'] += 1
        elif s >= 10 and s < 15:
            priceSortList['10-15w'] += 1
        elif s >= 15 and s < 20:
            priceSortList['15-20w'] += 1
        elif s >= 20 and s < 30:
            priceSortList['20-30w'] += 1
        else:
            priceSortList['30w以上'] += 1
    # print(priceSortList
    realData=[]
    for k,v in priceSortList.items():
        realData.append({
            'name':k,
            'value':v
        })
    return realData

