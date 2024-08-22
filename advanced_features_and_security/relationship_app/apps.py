from django.apps import AppConfig


class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'

class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self) -> None:
        import accounts.signals
