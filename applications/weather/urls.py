from django.urls import path

from .views import *

urlpatterns = [
    path("weather/", find_weather, name='weather'),
    path("weather/delete/<city_name>/", delete_city, name='delete_city'),

]