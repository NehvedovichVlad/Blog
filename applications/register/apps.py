from django.apps import AppConfig


class RegisterConfig(AppConfig):
    label = 'register'
    name = f"applications.{label}"