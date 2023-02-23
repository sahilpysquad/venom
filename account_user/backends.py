from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from account_user.models import User


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username) | Q(phone=username))
            if user.check_password(raw_password=password) is True:
                return user
        except User.DoesNotExist:
            pass
