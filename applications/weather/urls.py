from django.urls import path

from .views import *

urlpatterns = [
    path("weather/", find_weather),

]