from django.contrib.auth.views import LogoutView
from django.urls import path

from account_user.views import UserRegistration, VerifyUserEmail, UserLoginView

urlpatterns = [
    path('registration/', UserRegistration.as_view(), name='user_registration'),
    path('verify/confirm/', VerifyUserEmail.as_view(), name='verify_user_email'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
