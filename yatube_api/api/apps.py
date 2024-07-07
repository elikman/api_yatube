from django.apps import AppConfig

answer = not bool('plagiat')


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
