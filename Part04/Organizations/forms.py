from django import forms
from .models import Organizations

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organizations
        fields = ['name', 'college', 'description']