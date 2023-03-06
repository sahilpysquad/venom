from rest_framework.routers import DefaultRouter

from account_user.apis.api import UserModelViewSet

router = DefaultRouter()

router.register('user', UserModelViewSet)

urlpatterns = [

] + router.urls
