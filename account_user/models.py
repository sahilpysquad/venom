from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    PHONE_NUMBER_REGEX = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )

    email = models.EmailField(verbose_name=_('Email Address'), unique=True, null=False)
    phone = models.CharField(
        verbose_name=_('Phone'), max_length=17, unique=True, validators=[PHONE_NUMBER_REGEX], null=False
    )
    email_token = models.CharField(verbose_name=_('Email Token'), max_length=30, null=True, )
    phone_otp = models.IntegerField(verbose_name=_('Phone OTP'), null=True)
    is_email_verified = models.BooleanField(verbose_name=_('Is Email Verified'), default=False)
    is_phone_verified = models.BooleanField(verbose_name=_('Is Phone Verified'), default=False)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username

    def get_basic_details(self):
        return {
            'id': self.id,
            'username': self.username,
            'full_name': self.full_name,
            'email': self.email,
            'phone': self.phone,
            'is_active': self.is_active
        }

    @property
    def full_name(self):
        return self.get_full_name()


class UserDetails(models.Model):
    user = models.OneToOneField(verbose_name=_('User'), to=User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(verbose_name=_('Profile Picture'), null=True, blank=True)
    history = models.JSONField(verbose_name=_('History'), null=True, blank=True)

    class Meta:
        verbose_name = 'User Detail'
        verbose_name_plural = 'User Details'

    def __str__(self):
        return self.user.username
