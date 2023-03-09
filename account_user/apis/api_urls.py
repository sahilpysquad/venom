from django.urls import path
from rest_framework.routers import DefaultRouter

from account_user.apis.api import UserModelViewSet, LoginAPIView

router = DefaultRouter()

router.register('user', UserModelViewSet)

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='token_obtain_pair'),
] + router.urls
