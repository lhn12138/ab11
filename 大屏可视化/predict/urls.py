from django.urls import path

from predict import views
urlpatterns = [
    path("predict1/", views.predict1 ,name='predict1'),


]
