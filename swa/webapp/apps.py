from django.apps import AppConfig

class WebAppConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'webapp'

    def ready(self):
        import webapp.signals 
    