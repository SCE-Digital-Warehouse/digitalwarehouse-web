from django.apps import AppConfig
from django.db.models import signals



class BaseConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "base"

    def ready(self):
        from .models import User
        import base.signals as app_signals

        signals.pre_delete.connect(
            app_signals.user_pre_delete_handler, sender=User)
