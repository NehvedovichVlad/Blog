from django.shortcuts import render
import requests

from .forms import CityForm
from .models import City


def find_weather(request):
    appid = '1547f56cb0f7d14c2d8fee4263efc7a6'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()
    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"]
        }
        all_cities.append(city_info)

    context = {
        'all_info': all_cities,
        'form': form
    }
    return render(request, "weather/weather.html", context)


    # image = {
    #     'Tokyo': 'Tokyo',
    #     'Osaka': 'Osaka',
    #     'Nara': 'Nara',
    #     'Nagano': 'Nagano',
    #     'Sapporo': 'Sapporo',
    #     'Nagasaki': 'Nagasaki',
    #     'Kanazawa': 'Kanazawa',
    #     'Nikko': 'Nikko',
    #     'Hiroshima': 'Hiroshima',
    #     'Takayama': 'Takayama'
    # }