from django import forms
from .models import info_form

class info_form_form(forms.ModelForm):
    class Meta:
        model = info_form
        fields = ['full_name','Reg','email', 'cc_myself']
