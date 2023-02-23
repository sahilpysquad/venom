from django import forms

from account_user.models import User
from utils.helper_methods import send_mail, generate_token


class UserForm(forms.ModelForm):
    password2 = forms.CharField(label='Password2', widget=forms.PasswordInput, max_length=150, required=True)
    password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, max_length=150, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'password', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields.get('first_name').required = True
        self.fields.get('last_name').required = True

    def clean(self):
        data = super(UserForm, self).clean()
        password = data.get('password')
        password2 = data.get('password2')
        if not password == password2:
            self.add_error('password', 'Password and Confirm Password does not match..!')
        return data

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=commit)
        user.set_password(user.password)
        user.is_active = False
        if user.email:
            token = generate_token()
            user.email_token = token
            send_mail.apply_async(kwargs={
                'subject': 'VERIFY YOUR EMAIL',
                'to': (user.email,),
                'html_template': 'email/email_verification_mail.html',
                'context': {'url': f'http://localhost:8000/vc/account/verify/confirm/?token={token}'}
            })
        user.save()
        return user
