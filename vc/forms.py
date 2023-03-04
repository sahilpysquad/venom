from django import forms

from account_user.models import User
from vc.models import VC
from utils.helper_methods import send_mail


class VCModelForm(forms.ModelForm):
    class Meta:
        model = VC
        fields = ('name', 'organizer', 'emi_type', 'emi_amount', 'participant', 'interest')

    def save(self, commit=True):
        vc = super(VCModelForm, self).save(commit=commit)
        emails = list(vc.participant.values_list('email', flat=True))
        send_mail.apply_async(kwargs={
            'subject': 'PARTICIPATED IN VC',
            'to': emails,
            'html_template': 'email/participated_in_vc_email.html',
            'context': vc.get_basic_details()
        })
        return vc
