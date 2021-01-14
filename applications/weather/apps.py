from django.apps import AppConfig


class WeatherConfig(AppConfig):
    label = 'weather'
    name = f"applications.{label}"