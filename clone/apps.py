from django.apps import AppConfig


class CloneConfig(AppConfig):
    name = 'clone'

    def ready(self):
        import clone.signals