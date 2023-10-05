from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from api_auth.models import CustomUser


class CustomAuthBackend():
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(username=username)
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return None