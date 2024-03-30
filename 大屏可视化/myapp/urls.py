from django.urls import path

from myapp import views

urlpatterns = [
    path("center/", views.center, name='center'),
    path("centerLeft/", views.centerLeft, name='centerLeft'),
    path("bottomLeft/", views.bottomLeft, name='bottomLeft'),
    path("centerRight/", views.centerRight, name='centerRight'),
    path("centerRightChange/<int:energyType>", views.centerRightChange, name='centerRightChange'),
    path("bottomRight/", views.bottomRight, name='bottomRight'),
    path("predict2/", views.predict2, name='predict2'),
    path("predict22/", views.predict22, name='predict22'),
    path("data3/", views.data3, name='data3'),
    path("data2/", views.data2, name='data2'),
    path("data1/", views.data1, name='data1'),
    path("getData/", views.getData, name='getData'),

]
