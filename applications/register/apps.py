from django.apps import AppConfig


class RegisterConfig(AppConfig):
    label = 'register'
    name = f"applications.{label}"

    def ready(self):
        import applications.register.signals
