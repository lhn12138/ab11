from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render
from .utils import getPublicData
# Create your views here.

def predict1(request):
    if request.method == 'GET':
#         # sumCar, highVolume, topCar, mostModel, mostBrand, averagePrice = getCenterData.getBaseData()
#         # lastSortList = getCenterData.getRollData()
#         # oilRate, electricRate, mixRate = getCenterData.getTypeRate()
        return JsonResponse({
#             # 'sumCar': sumCar,
#             # 'highVolume': highVolume,
#             # 'topCar': topCar,
#             # 'mostModel': mostModel,
#             # 'mostBrand': mostBrand,
#             # 'averagePrice': averagePrice,
#             # 'lastSortList': lastSortList,
#             # 'oilRate': oilRate,
#             # 'electricRate': electricRate,
#             # 'mixRate': mixRate
        })