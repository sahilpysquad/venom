from django import forms

from vc.models import VC


class VCModelForm(forms.ModelForm):
    class Meta:
        model = VC
        fields = ('name', 'organizer', 'emi_type', 'total_amount', 'participant')
