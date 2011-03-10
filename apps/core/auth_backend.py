from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import ImproperlyConfigured
from django.db.models import get_model

from lending.apps.core.models import CoreUser

class CoreUserModelBackend(object):
    def authenticate(self, username=None, password=None):
        try:
            user = CoreUser.objects.get(username=username)
            if user.check_password(password):
                return user
        except CoreUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        return CoreUser.objects.get(pk=user_id)