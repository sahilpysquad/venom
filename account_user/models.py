from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(verbose_name=_('Email Address'), blank=True, null=True)
    phone = models.CharField(verbose_name=_('Phone'), max_length=15, null=True)
    email_token = models.CharField(verbose_name=_('Email Token'), max_length=30, null=True,)
    phone_otp = models.IntegerField(verbose_name=_('Phone OTP'), null=True)
    is_email_verified = models.BooleanField(verbose_name=_('Is Email Verified'), default=False)
    is_phone_verified = models.BooleanField(verbose_name=_('Is Phone Verified'), default=False)

    def __str__(self):
        return self.username


class UserDetails(models.Model):
    user = models.OneToOneField(verbose_name=_('User'), to=User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(verbose_name=_('Profile Picture'), null=True, blank=True)
    history = models.JSONField(verbose_name=_('History'), null=True, blank=True)

    def __str__(self):
        return self.user.username
