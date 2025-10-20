from django.apps import AppConfig

class TallerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'taller'

    def ready(self):
        # Create admin user automatically after migrations/runserver if not exists.
        try:
            from django.contrib.auth import get_user_model
            User = get_user_model()
            if not User.objects.filter(username='admin').exists():
                User.objects.create_superuser('admin', email='', password='1234')
        except Exception:
            # During initial migrate this may fail; ignore silently.
            pass
