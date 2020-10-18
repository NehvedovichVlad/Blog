from django.apps import AppConfig


class NewsConfig(AppConfig):
    label = 'news'
    name = f"applications.{label}"
    verbose_name = 'Новости'
