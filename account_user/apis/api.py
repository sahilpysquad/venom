from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from account_user.apis.permissions import IsOwnerOfObject
from account_user.apis.serializers import UserModelSerializer, CustomTokenObtainPairSerializer
from account_user.models import User


class LoginAPIView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserModelViewSet(ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = User.objects.filter(is_active=True)

    def get_permissions(self):
        if self.action in ('update', 'delete', 'retrieve'):
            return [IsAuthenticated(), IsOwnerOfObject()]
        elif self.action == 'list':
            return [IsAdminUser()]
        else:
            return [AllowAny()]
