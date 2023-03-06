from rest_framework.viewsets import ModelViewSet

from account_user.apis.serializers import UserModelSerializer
from account_user.models import User


class UserModelViewSet(ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = User.objects.filter(is_active=True)
