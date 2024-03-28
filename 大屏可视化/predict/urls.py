from django.urls import path
from . import views


urlpatterns = [
    path("predict1", views.predict1 ,name='predict1'),


]
