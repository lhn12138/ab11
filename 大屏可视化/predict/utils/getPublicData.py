import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "大屏可视化.settings")
import django
django.setup()
from predict.models import *
def getAllCars():
    print(Predict.objects.all())
