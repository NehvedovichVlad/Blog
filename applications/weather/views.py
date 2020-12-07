from django.shortcuts import render
import requests

from applications.weather.models import City


def find_weather(request):
    appid = '1547f56cb0f7d14c2d8fee4263efc7a6'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

    all_cities = []
    cities = City.objects.all()

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"]
        }
        all_cities.append(city_info)


    image = {
        'Tokyo': 'Tokyo',
        'Osaka': 'Osaka',
        'Nara': 'Nara',
        'Nagano': 'Nagano',
        'Sapporo': 'Sapporo',
        'Nagasaki': 'Nagasaki',
        'Kanazawa': 'Kanazawa',
        'Nikko': 'Nikko',
        'Hiroshima': 'Hiroshima',
        'Takayama': 'Takayama'
    }

    context = {
        'all_info': all_cities,
    }
    return render(request, "weather/weather.html", context)
