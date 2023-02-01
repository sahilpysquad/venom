from django.urls import path

from account_user.views import UserRegistration

urlpatterns = [
    path('registration/', UserRegistration.as_view(), name='user_registration'),
]
