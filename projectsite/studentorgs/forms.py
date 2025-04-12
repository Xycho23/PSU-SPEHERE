from django import forms
from .models import Organization
from .models import OrgMember

class OrganizationsForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'description']

class OrgMemberForm(forms.ModelForm):
    class Meta:
        model = OrgMember
        fields = '__all__'

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = '__all__'  # Or list specific fields like ['name', 'description', etc.]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
