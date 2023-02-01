from django.views.generic import CreateView, TemplateView

from account_user.forms import UserForm
from account_user.models import User


class HomePage(TemplateView):
    template_name = 'home.html'


class UserRegistration(CreateView):
    model = User
    form_class = UserForm
    template_name = 'account_user/user_registration_form.html'
    success_url = '/'
