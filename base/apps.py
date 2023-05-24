from django.apps import AppConfig
from django.db.models import signals


class BaseConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "base"

    def ready(self):
        import base.signals as app_signals
        from .models import SpecialRequest
        signals.post_save.connect(
            app_signals.revert_extension_requested, sender=SpecialRequest)
