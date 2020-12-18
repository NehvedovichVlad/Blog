from django.shortcuts import render, redirect
import requests

from applications.weather.forms import CityForm
from applications.weather.models import City


def find_weather(request):
    appid = '1547f56cb0f7d14c2d8fee4263efc7a6'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

    err_msg =''
    message = ''
    message_class = ''

    if request.method == 'POST':
        form = CityForm(request.POST)

        if form.is_valid():
            new_city = form.cleaned_data['name']
            existing_city_count = City.objects.filter(name=new_city).count()

            if existing_city_count == 0:
                res = requests.get(url.format(new_city)).json()
                if res['cod'] == 200:
                    form.save()
                else:
                    err_msg = 'City does not exist in the world'
            else:
                err_msg = 'City already exists in the database!'
        if err_msg:
            message = err_msg
            message_class = 'is-danger'
        else:
            message = 'City added successfully'
            message_class = 'is-success'


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
        'form': form,
        'message': message,
        'message_class': message_class
    }
    return render(request, "weather/weather.html", context)

def delete_city(request, city_name):
    City.objects.get(name=city_name).delete()
    
    return  redirect('weather')

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