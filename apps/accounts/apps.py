from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'apps.accounts'

    def ready(self):
        import apps.accounts.signals