from django.shortcuts import render
import requests


def find_weather(request):
    appid = '1547f56cb0f7d14c2d8fee4263efc7a6'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

    city = 'Tokyo'
    res = requests.get(url.format(city)).json()

    city_info = {
        'city': city,
        'temp': res["main"]["temp"],
        'icon': res["weather"][0]["icon"]
    }
    context = {
        'info': city_info
    }
    return render(request, "weather/weather.html", context)
