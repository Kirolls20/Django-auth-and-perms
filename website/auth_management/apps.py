from django.apps import AppConfig
from django.conf import settings




class AuthManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auth_management'


    def ready(self):
        import auth_management.signals

