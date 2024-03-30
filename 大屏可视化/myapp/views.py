from django.http import JsonResponse

from .utils import getBottomLeftData
from .utils import getBottomRightData
from .utils import getCenterChangeData
from .utils import getCenterData
from .utils import getCenterLeftData
from .utils import getCenterRightData
from .utils.predict22 import predict_sales
from .utils.predict2 import predict_monthly_sales
from .utils.data3 import read_csv_data3
from .utils.data2 import read_csv_data2
from .utils.getData import read_csv_data
from .utils.data1 import read_csv_data1


# Create your views here.

def center(request):
    if request.method == 'GET':
        sumCar, highVolume, topCar, mostModel, mostBrand, averagePrice = getCenterData.getBaseData()
        lastSortList = getCenterData.getRollData()
        oilRate, electricRate, mixRate = getCenterData.getTypeRate()
        return JsonResponse({
            'sumCar': sumCar,
            'highVolume': highVolume,
            'topCar': topCar,
            'mostModel': mostModel,
            'mostBrand': mostBrand,
            'averagePrice': averagePrice,
            'lastSortList': lastSortList,
            'oilRate': oilRate,
            'electricRate': electricRate,
            'mixRate': mixRate
        })


def centerLeft(request):
    if request.method == 'GET':
        lastPieList = getCenterLeftData.getPieBrandData()
        return JsonResponse({
            'lastPieList': lastPieList,

        })


def bottomLeft(request):
    if request.method == 'GET':
        brandList, volumeList, priceList = getBottomLeftData.getSquareData()
        return JsonResponse({
            'brandList': brandList,
            'volumeList': volumeList,
            'priceList': priceList,

        })


def centerRight(request):
    if request.method == 'GET':
        realData = getCenterRightData.getPriceSortData()
        return JsonResponse({
            'realData': realData,

        })


def centerRightChange(request, energyType):
    if request.method == 'GET':
        oilData, electricData = getCenterChangeData.getCircleData()
        realData = []
        if energyType == 1:
            realData = oilData
        else:
            realData = electricData
        return JsonResponse({
            'realData': realData

        })


def bottomRight(request):
    if request.method == 'GET':
        carData = getBottomRightData.getRankData()
        return JsonResponse({
            'carData': carData

        })


def predict2(request):
    if request.method == 'GET':
        List = predict_monthly_sales()
        return JsonResponse({
            'List': List,
        })


def predict22(request):
    if request.method == 'GET':
        List1 = predict_sales()
        return JsonResponse({
            'List1': List1,
        })

def data3(request):
    if request.method == 'GET':
        yearList, volumeList, rateList = read_csv_data3()
        return JsonResponse({
            'yearList': yearList,
            'volumeList': volumeList,
            'rateList': rateList,
        })

def data2(request):
    if request.method == 'GET':
        yearsList, volumeList, rateList = read_csv_data2()
        return JsonResponse({
            'yearsList': yearsList,
            'volumeList': volumeList,
            'rateList': rateList,
        })

def getData(request):
    if request.method == 'GET':
        carData1 = read_csv_data()
        return JsonResponse({
            'carData1': carData1

        })

def data1(request):
    if request.method == 'GET':
        carData2 = read_csv_data1()
        return JsonResponse({
            'carData2': carData2

        })