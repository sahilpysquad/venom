from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, TemplateView

from account_user.forms import UserForm
from account_user.models import User


class HomePage(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


class UserRegistration(CreateView):
    model = User
    form_class = UserForm
    template_name = 'account_user/user_registration_form.html'
    success_url = 'login/'


class VerifyUserEmail(View):
    template_name = 'email/confirm_user_email.html'

    def get(self, request):
        token = request.GET.get('token')
        if not token:
            messages.error(request, 'Token not found..!')
            return render(request, template_name=self.template_name)
        user_obj = User.objects.filter(email_token=token).first()
        if not user_obj:
            messages.error(request, 'Invalid Link')
            return render(request, template_name=self.template_name)
        user_obj.is_active, user_obj.is_email_verified = True, True
        user_obj.save()
        return render(request, template_name=self.template_name, context={'user': user_obj})


class UserLoginView(LoginView):
    template_name = 'account_user/user_login.html'
