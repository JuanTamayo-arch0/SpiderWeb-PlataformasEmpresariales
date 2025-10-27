from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'  # Ajusta si el nombre de tu app es otro

    def ready(self):
        import users.signals  # Ajusta si tu app se llama distinto

