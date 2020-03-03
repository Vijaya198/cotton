from django.apps import AppConfig


class AccountLoginConfig(AppConfig):
    name = 'account_login'
    def ready(self):
        import demo_project.users.signals
