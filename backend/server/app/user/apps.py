from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app.user"

    # https://docs.djangoproject.com/en/5.0/topics/signals/#connecting-receiver-functions
    def ready(self):
        # Implicitly connect signal handlers decorated with @receiver.
        from . import signals
        # import app.user.signals

        # Explicitly connect a signal handler.
        # request_finished.connect(signals.user_signed_up)
