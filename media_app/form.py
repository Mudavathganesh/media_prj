from django import forms
from.models import Jobapplication
class Resume_form(forms.ModelForm):
    class Meta:
        model=Jobapplication
        fields='__all__'