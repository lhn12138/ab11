from myapp.models import *

def getAllCars():
    return CarInfo.objects.all()
