from django.contrib import admin

from account_user.models import User


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'is_active')
